🚨 AI Emergency Response System

An intelligent emergency response platform that uses Machine Learning and AI-based decision-making to assist in emergency situations. The system predicts emergency severity, assigns the appropriate response vehicle, estimates arrival time based on traffic conditions, and visualizes the emergency location on an interactive map.

📌 Project Overview

The AI Emergency Response System helps emergency services respond faster by:

Predicting emergency severity using Machine Learning
Assigning suitable emergency vehicles automatically
Estimating response time based on traffic conditions
Displaying emergency locations on an interactive map
Supporting Medical, Fire, and Police emergencies

This project demonstrates the integration of:

Artificial Intelligence
Machine Learning
Streamlit
Geospatial Mapping
Decision Support Systems
🎯 Features
🚑 Smart Vehicle Assignment

Automatically assigns:

ICU Ambulance
Ambulance
Fire Truck
Police Vehicle

based on emergency type and severity level.

🤖 ML-Based Severity Prediction

Uses a trained Machine Learning model to predict emergency severity using traffic conditions.

🚦 Traffic-Aware Response

Considers:

Morning Traffic
Afternoon Traffic
Night Traffic

to estimate emergency response time.

📍 Interactive Map Visualization

Displays:

Emergency Location
Nearby Hospital
Route between locations

using Folium Maps.

⚡ Real-Time Emergency Request

Users can submit emergency requests through a simple interface.

🏗️ System Architecture

User Request
↓
Traffic Analysis
↓
ML Severity Prediction
↓
Vehicle Assignment Agent
↓
ETA Calculation
↓
Map Visualization

📂 Project Structure
ai-main/
│
├── app.py                     # Main Streamlit Application
│
├── agents/
│   └── dispatcher.py          # Vehicle Assignment Logic
│
├── ml/
│   ├── train.py               # Model Training
│   └── predict.py             # Severity Prediction
│
├── models/
│   └── model.pkl              # Trained ML Model
│
├── maps/
│   └── routing.py             # Route Calculation
│
├── utils/
│   └── traffic.py             # Traffic Simulation
│
├── data/
│   └── emergency_data.csv     # Training Dataset
│
└── requirements.txt
🛠️ Technologies Used
Technology	Purpose
Python	Core Development
Streamlit	Web Application
Scikit-Learn	Machine Learning
Joblib	Model Serialization
Folium	Interactive Maps
Geopy	Location Services
OSMnx	Route Optimization
Pandas	Data Processing
🚀 Installation
Clone Repository
git clone https://github.com/yourusername/AI-Emergency-Response-System.git

cd AI-Emergency-Response-System
Install Dependencies
pip install -r requirements.txt
Train Model
python ml/train.py
Run Application
streamlit run app.py
📸 Demo Workflow
Select Emergency Location
Choose Emergency Type
Medical
Fire
Police
Select Time of Day
Click Request Help
System:
Predicts Severity
Assigns Vehicle
Calculates ETA
Displays Route on Map
📊 Sample Output

Emergency Type: Medical

Traffic Level: High

Predicted Severity: 92

Assigned Vehicle: ICU Ambulance

Estimated Arrival Time: 20 Minutes

🔮 Future Enhancements
Live GPS Tracking
Real-Time Traffic API Integration
Hospital Availability Monitoring
Multi-Agent Emergency Coordination
SMS and Email Alerts
AI Route Optimization
Disaster Management Dashboard
Emergency Chatbot Assistant

python -m pip install -r requirements.txt
python ml/train.py
streamlit run app.py
python -m streamlit run app.py
