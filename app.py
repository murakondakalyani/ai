import streamlit as st
import folium
from geopy.geocoders import Nominatim
from ml.predict import predict_severity
from agents.dispatcher import assign_vehicle

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Emergency System", layout="wide")

st.title("🚨 Real-Time AI Emergency Response System")

# =========================
# LOCATION INPUT (USER FRIENDLY)
# =========================
st.sidebar.header("📍 Emergency Request")

locations = {
    "Vijayawada Center": (16.5062, 80.6480),
    "Benz Circle": (16.5015, 80.6475),
    "Auto Nagar": (16.4930, 80.6720),
    "Gannavaram": (16.5400, 80.8000)
}

place = st.sidebar.selectbox("Select Location", list(locations.keys()))
lat, lon = locations[place]

# =========================
# EMERGENCY TYPE
# =========================
emergency = st.sidebar.selectbox(
    "🚨 Emergency Type",
    ["medical", "fire", "police"]
)

# =========================
# TIME BASED TRAFFIC
# =========================
time_of_day = st.sidebar.selectbox(
    "🕒 Time of Day",
    ["morning", "afternoon", "night"]
)

def get_traffic(time):
    if time == "morning":
        return "high"
    elif time == "afternoon":
        return "medium"
    else:
        return "low"

# =========================
# ETA CALCULATION
# =========================
def estimate_time(traffic):
    if traffic == "low":
        return "5 mins"
    elif traffic == "medium":
        return "10 mins"
    else:
        return "20 mins"

# =========================
# SOS BUTTON
# =========================
if st.sidebar.button("🔴 Request Help"):

    traffic = get_traffic(time_of_day)

    # ML Prediction
    severity = predict_severity(traffic)

    # Vehicle Assignment
    vehicle = assign_vehicle(emergency, severity)

    # ETA
    eta = estimate_time(traffic)

    # =========================
    # OUTPUT DISPLAY
    # =========================
    st.success(f"🚑 Assigned Vehicle: {vehicle}")
    st.warning(f"🚦 Traffic Level: {traffic}")
    st.error(f"🔥 Severity Score: {severity}")
    st.info(f"⏱ Estimated Arrival Time: {eta}")

    # =========================
    # MAP DISPLAY
    # =========================
    st.subheader("📍 Emergency Map")

    m = folium.Map(location=[lat, lon], zoom_start=13)

    # SOS location
    folium.Marker(
        [lat, lon],
        popup="🚨 Emergency Location",
        icon=folium.Icon(color="red")
    ).add_to(m)

    # Hospital location (fixed example)
    hospital_lat, hospital_lon = 16.5100, 80.6500

    folium.Marker(
        [hospital_lat, hospital_lon],
        popup="🏥 Hospital",
        icon=folium.Icon(color="green")
    ).add_to(m)

    # Route line
    folium.PolyLine(
        [(lat, lon), (hospital_lat, hospital_lon)],
        color="blue",
        weight=5
    ).add_to(m)

    st.components.v1.html(m._repr_html_(), height=500)