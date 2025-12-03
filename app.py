import streamlit as st
import pandas as pd
import json
import re
import google.generativeai as genai
from PIL import Image

# --- 1. CONFIGURATION & BRANDING ---
# Try to load the local logo for the favicon, fallback to emoji if missing
try:
    favicon = Image.open("logo.png")
except:
    favicon = "📍"

st.set_page_config(
    page_title="GroundTruth AI | CX Automator", 
    layout="wide", 
    page_icon=favicon,
    initial_sidebar_state="expanded"
)

# --- 2. GROUNDTRUTH "MINT" THEME CSS ---
st.markdown("""
<style>
    /* GroundTruth Mint Background */
    .stApp {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        color: #0f172a;
    }
    
    /* Sidebar - Clean White */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Header - GroundTruth Style */
    .main-header {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        color: #0f172a;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border-left: 10px solid #10b981;
    }
    
    /* Metric Cards */
    .metric-card {
        background: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .metric-value {
        font-size: 26px;
        font-weight: 800;
        color: #059669;
    }
    .metric-label {
        font-size: 13px;
        color: #64748b;
        text-transform: uppercase;
        font-weight: 600;
    }
    
    /* PII Alert Box */
    .pii-alert {
        background-color: #fef2f2;
        border: 1px solid #fca5a5;
        padding: 15px;
        border-radius: 8px;
        color: #991b1b;
        font-weight: bold;
        margin: 10px 0;
    }

    /* Chat Styling */
    .user-msg { 
        background-color: #eff6ff; 
        padding: 15px; 
        border-radius: 15px 15px 0 15px; 
        text-align: right; 
        border: 1px solid #bfdbfe; 
        margin-bottom: 12px;
        color: #1e3a8a;
    }
    .bot-msg { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 15px 15px 15px 0; 
        border: 1px solid #e5e7eb; 
        margin-bottom: 12px;
        color: #334155;
    }
    
    .stTextInput > div > div > input {
        background-color: #f8fafc;
        color: #334155;
        border: 1px solid #cbd5e1;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. DATA & LOGIC LAYERS ---
@st.cache_data
def load_context():
    try:
        inventory = pd.read_csv("store_inventory.csv")
        with open("user_profile.json", "r") as f:
            profiles = json.load(f)
        return inventory, profiles
    except:
        return pd.DataFrame(), {}

inventory_df, user_profiles = load_context()
current_user = user_profiles.get("user_dhruv", {})

def mask_pii(text):
    redacted = False
    clean_text = text
    # Phone regex
    if re.search(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b|\b\d{10}\b', text):
        clean_text = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b|\b\d{10}\b', '[PHONE_REDACTED]', clean_text)
        redacted = True
    # Email regex
    if re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text):
        clean_text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[EMAIL_REDACTED]', clean_text)
        redacted = True
    return clean_text, redacted

def find_valid_model():
    """Auto-detects the best available Gemini model."""
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                return m.name
    except:
        return None
    return "models/gemini-pro"

# --- 4. SIDEBAR (CONTROL CENTER) ---
with st.sidebar:
    # --- LOGO DISPLAY (Robust Check) ---
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.header("📍 GroundTruth")

    st.markdown("### ⚙️ Signal Controls")
    api_key = st.text_input("🔑 Gemini API Key", type="password")
    
    st.divider()
    
    st.markdown("### 📡 Live Context Simulator")
    user_location = st.selectbox("📍 User Location", 
        ["Parking Lot (50m away)", "Inside Store (Aisle 3)", "Home (Remote)", "Competitor Store"])
    weather = st.radio("☁️ Local Weather", ["Sunny ☀️", "Snowing/Freezing ❄️", "Raining 🌧️"])
    
    st.divider()
    
    # Toggle Map
    show_map = st.toggle("🗺️ Show Live Map", value=True)
    
    st.divider()
    st.markdown("### 👤 Active Profile")
    st.info(f"ID: {current_user.get('name')}\nTier: {current_user.get('tier')}")

# --- 5. MAIN DASHBOARD UI ---

st.markdown("""
<div class="main-header">
    <h1 style="color: #0f172a; margin:0;">CX Experience Automation</h1>
    <p style="color: #64748b; margin:0; font-size: 1.1em;">Hyper-Local Intelligence Platform | 🟢 System Online</p>
</div>
""", unsafe_allow_html=True)

# Telemetry Deck
col1, col2, col3, col4 = st.columns(4)
distance = "0m"
if "Parking" in user_location: distance = "50m"
elif "Home" in user_location: distance = "5.2km"
elif "Competitor" in user_location: distance = "1.1km"

with col1: st.markdown(f"""<div class="metric-card"><div class="metric-label">Proximity</div><div class="metric-value">{distance}</div></div>""", unsafe_allow_html=True)
with col2: st.markdown(f"""<div class="metric-card"><div class="metric-label">Weather</div><div class="metric-value">{weather.split()[0]}</div></div>""", unsafe_allow_html=True)
with col3: st.markdown(f"""<div class="metric-card"><div class="metric-label">Active Offers</div><div class="metric-value">{len(inventory_df[inventory_df['Offer'] != 'None'])} Live</div></div>""", unsafe_allow_html=True)
with col4: st.markdown(f"""<div class="metric-card"><div class="metric-label">Signal</div><div class="metric-value" style="color: #10b981;">● Strong</div></div>""", unsafe_allow_html=True)

st.markdown("---")

# --- C. Map Visualization ---
if show_map:
    if "Parking" in user_location or "Inside" in user_location:
        map_data = pd.DataFrame({'lat': [19.0760], 'lon': [72.8777]})
        st.map(map_data, zoom=16, use_container_width=True)
else:
    st.caption("Map visualization hidden (Maximizing Chat View)")

# --- 6. CHAT INTERFACE ---
if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.history.append({"role": "model", "content": f"👋 Hello {current_user.get('name')}! My sensors detect you at **{user_location}**. I'm ready to assist."})

for msg in st.session_state.history:
    role_class = "user-msg" if msg["role"] == "user" else "bot-msg"
    icon = "👤" if msg["role"] == "user" else "🤖"
    st.markdown(f"<div class='{role_class}'><b>{icon}</b> {msg['content']}</div>", unsafe_allow_html=True)

# --- 7. AI LOGIC CORE ---
if user_input := st.chat_input("Ask about stock, offers, or store info..."):
    if not api_key:
        st.error("⚠️ System Offline: Please enter API Key in sidebar.")
        st.stop()
        
    st.session_state.history.append({"role": "user", "content": user_input})
    st.rerun()

if st.session_state.history and st.session_state.history[-1]["role"] == "user":
    last_msg = st.session_state.history[-1]["content"]
    safe_input, was_redacted = mask_pii(last_msg)
    
    if was_redacted:
        st.markdown(f"""<div class='pii-alert'>🛡️ <b>PRIVACY SHIELD ACTIVATED</b><br>Sensitive PII detected. Data redacted before transmission to Neural Engine.</div>""", unsafe_allow_html=True)

    inventory_context = inventory_df.head(15).to_string(index=False)
    
    prompt = f"""
    Act as a GroundTruth Retail AI Assistant.
    CONTEXT SIGNALS: Location: {user_location} (Distance: {distance}), Weather: {weather}, User: {current_user.get('name')} (Tier: {current_user.get('tier')})
    LIVE INVENTORY: {inventory_context}
    INSTRUCTIONS: Use the location! If close (50m), invite inside. If snowing/raining, suggest warm/dry items. Be brief.
    USER MESSAGE: {safe_input}
    """
    
    with st.spinner("⚡ Neural Engine Analyzing Signals..."):
        try:
            genai.configure(api_key=api_key)
            model_name = find_valid_model()
            if model_name:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                st.session_state.history.append({"role": "model", "content": response.text})
            else:
                st.error("Connection Error: No valid AI models found.")
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")