# <img width="251" height="77" alt="logo" src="https://github.com/user-attachments/assets/7faff230-df03-45c9-afd1-71eb12d0f35a" />
 GroundTruth CX Agent: Hyper-Local Experience Automation
> **Track:** H-002 | Customer Experience & Conversational AI  
> **Status:** 🟢 Production Ready | **Privacy Level:** 🛡️ Enterprise (GDPR Compliant)

![Banner](https://capsule-render.vercel.app/api?type=waving&color=10b981&height=220&section=header&text=GroundTruth%20CX%20Agent&fontSize=50&fontAlign=50&animation=fadeIn&fontColor=ffffff&desc=Location%20Intelligence%20x%20Generative%20AI&descAlign=50)

## 📖 Context & Vision
Retail customers expect instant, context-aware answers. Standard chatbots fail because they treat every user the same—ignoring **where** they are and **who** they are.

**The Solution:** An intelligent orchestration agent that combines **Real-Time Location Signals**, **Live Inventory Data**, and **User History** to drive foot traffic. It doesn't just answer questions; it drives business results (e.g., *"You are 50m away, come in for a coffee!"*).

---

## 🚀 Key Features (Why This Wins)

### 1. 🌍 Hyper-Local Awareness (Location Intelligence)
* **The Problem:** Bots don't know if a user is at home or in the parking lot.
* **Our Solution:** The agent detects the user's telemetry (e.g., "Parking Lot - 50m away") and adapts the sales pitch.
* **Impact:** Converts nearby traffic into Store Visits instantly using **Geo-Conquesting logic**.

### 2. 🛡️ Enterprise Privacy Shield (PII Redaction)
* **The Problem:** Sending customer phone numbers to public LLMs violates privacy laws.
* **Our Solution:** A Regex-based **Pre-Processing Layer** intercepts messages *before* they hit the AI.
    * Detects Phone Numbers & Emails.
    * Redacts them to `[PHONE_REDACTED]`.
    * **Result:** Zero PII leakage to Google Gemini.

### 3. 🧠 RAG-Based Inventory Engine
* **The Problem:** AI Hallucinations (promising items that are out of stock).
* **Our Solution:** The bot connects to a live mock database (`store_inventory.csv`) with **100+ items**.
    * If user asks for "Umbrellas", it checks the *Live Stock*.
    * If Stock = 0, it apologizes and offers a substitute.

### 4. 🎨 "Mission Control" Dashboard
* **Dynamic UI:** Features a **Mint/Teal Theme** aligned with GroundTruth branding.
* **Live Telemetry:** Top-bar metrics update in real-time (Proximity, Signal Strength, Active Offers).
* **Map Visualization:** A toggleable geospatial view to visualize user location relative to the store.

---

## 🛠️ Tech Stack
| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | **Streamlit** | Responsive, mobile-first UI with Custom CSS. |
| **AI Brain** | **Google Gemini 1.5** | Self-healing connection logic (Auto-detects best model). |
| **Orchestrator** | **Python 3.9+** | Managing prompt templates and context injection. |
| **Data Layer** | **Pandas** | ETL processing for Inventory & User Profiles. |
| **Security** | **Regex** | Local-side PII scrubbing. |

---

## 📸 Visual Proof

| **1. The "Revenue" Win** | **2. The Privacy Shield** |
| :---: | :---: |
| ![Location Demo](<img width="1917" height="1031" alt="ouput-1" src="https://github.com/user-attachments/assets/b8c05514-7c7a-4a00-9e7d-113f2091a27b" />
) | ![Privacy Demo](<img width="1913" height="915" alt="privacy-shield-3" src="https://github.com/user-attachments/assets/0e0aaa38-16de-462a-8d84-09b46181db4a" />
) |
| *Bot detects user is 50m away in the snow and drives a sale.* | *System detects PII and redacts it before API call.* |

---

## 🧪 Quality Assurance & Test Cases

We rigorously tested the agent against **10 unique edge cases** to ensure enterprise reliability.

| ID | Scenario | Sidebar Context | User Input | Expected AI Behavior | Business Value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | **The "Hook"** | **Loc:** Parking Lot (50m)<br>**Weather:** Snowing | *"I'm freezing!"* | Invites user inside (50m) for Hot Cocoa + mentions Gold Coupon. | **Drive Foot Traffic** |
| **02** | **Privacy Shield** | **Loc:** Any | *"Call 987-654-3210"* | **🔴 Red Alert** appears. Number redacted from AI prompt. | **GDPR Compliance** |
| **03** | **Inventory Crisis** | **Loc:** Inside Store | *"Do you have umbrellas?"* | Checks CSV. Sees "Out of Stock". Apologizes. | **Prevent Hallucinations** |
| **04** | **Competitor Win-Back** | **Loc:** Competitor Store | *"I'm at Starbucks."* | *"We are just 1km away! Come to GroundTruth for better prices."* | **Geo-Conquesting** |
| **05** | **In-Store Navigation** | **Loc:** Inside Store | *"Where are the jackets?"* | *"Winter Jackets are in **Aisle 3** (Low Stock!)."* | **Customer Service** |
| **06** | **Scarcity Tactic** | **Loc:** Any | *"I want a jacket."* | *"Hurry! We only have **2 left** in stock."* | **Conversion Rate** |
| **07** | **Weather Cross-Sell** | **Loc:** Home<br>**Weather:** Sunny | *"I'm thirsty."* | Suggests **Iced Lemonade** (Hot Weather Item) instead of Cocoa. | **Contextual Sales** |
| **08** | **VIP Recognition** | **Loc:** Counter | *"Hi there!"* | *"Welcome back **Dhruv**! Thank you for being a **Gold Member**."* | **Loyalty Retention** |
| **09** | **Remote Delivery** | **Loc:** Home (5km away) | *"I want coffee."* | *"Since you are 5km away, shall we deliver to your home address?"* | **Omnichannel Support** |
| **10** | **Map Visualization** | **Loc:** Parking Lot | *Toggle Map ON* | Displays dynamic map showing user location relative to geofence. | **Geospatial UI** |

---

## 💻 Installation & Setup


git clone [https://github.com/dhruv4685/Groundtruth-Hackathon-2025-dhruvkimothi.git](https://github.com/dhruv4685/Groundtruth-Hackathon-2025-dhruvkimothi.git)
cd Groundtruth-Hackathon-2025-dhruvkimothi

## 2. Install Dependencies

pip install -r requirements.txt

## 3. Generate Enterprise Data
(Run this script to generate 100+ mock inventory items and User Profiles)

python setup_data.py

## 4. Launch the Agent

streamlit run app.py

📂 Project Structure
Bash

├── Output/
│   └── Sample_Execution_Log.pdf  # PDF Transcript of a successful run
├── Screenshots/
│   ├── demo_location.png         # Screenshot of Location Logic
│   └── demo_privacy.png          # Screenshot of PII Redaction
├── app.py                        # Main Application (Mint Theme + Logic)
├── setup_data.py                 # Data Generator (Creates Mock Enterprise DB)
├── store_inventory.csv           # Generated Inventory Database (RAG Source)
├── user_profile.json             # User Persona Data
├── logo.png                      # GroundTruth Branding Asset
├── README.md                     # Documentation
└── requirements.txt              # Dependencies
