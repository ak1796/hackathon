import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AeroGuard AI",
    page_icon="🌫️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f6f8fb;
}
.metric-card {
    background-color: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}
.card-title {
    font-size: 14px;
    color: #6b7280;
}
.card-value {
    font-size: 28px;
    font-weight: 700;
}
.badge {
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
}
.badge-orange { background:#fff7ed; color:#c2410c; }
.badge-green { background:#ecfdf5; color:#047857; }
.badge-red { background:#fef2f2; color:#b91c1c; }
.section-box {
    background:white;
    padding:20px;
    border-radius:16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌍 AeroGuard AI")
st.sidebar.caption("Hyper-Local AQI Intelligence")

location = st.sidebar.selectbox(
    "📍 Location",
    ["Downtown Mumbai", "Andheri East", "Bandra West", "Kurla"]
)

persona = st.sidebar.selectbox(
    "👤 Persona",
    ["Children / Elderly", "Outdoor Workers", "General Public"]
)

st.sidebar.markdown("---")
st.sidebar.info("Prototype UI – dummy data only")

# ---------------- HEADER ----------------
st.markdown(f"### {location}")
st.caption("Live AQI Dashboard · 6-Hour Forecast")

# ---------------- KPI CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

aqi = 105
pm25 = 72
dominant = "PM2.5"
risk = "Sensitive Groups"

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="card-title">Current AQI</div>
        <div class="card-value">{aqi}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="card-title">PM2.5 (µg/m³)</div>
        <div class="card-value">{pm25}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="card-title">Dominant Pollutant</div>
        <div class="card-value">{dominant}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="card-title">Health Advisory</div>
        <span class="badge badge-orange">{risk}</span>
    </div>
    """, unsafe_allow_html=True)

# ---------------- TREND + INSIGHTS ----------------
left, right = st.columns([2.2, 1])

# ----- AQI TREND -----
with left:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.subheader("📈 AQI 6-Hour Trend")

    times = [datetime.now() + timedelta(hours=i) for i in range(6)]
    values = np.random.randint(80, 160, 6)

    df = pd.DataFrame({"Time": times, "AQI": values})

    fig = px.line(df, x="Time", y="AQI", markers=True)
    fig.update_layout(height=320, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ----- HEALTH INSIGHTS -----
with right:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.subheader("🩺 Personalized Health Insights")

    st.markdown("""
    **Risk Level:** Moderate  
    **Persona:** {}
    
    **Recommendations:**
    - Reduce prolonged outdoor exposure  
    - Wear N95 mask if outdoors  
    - Avoid intense physical activity
    """.format(persona))

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EXPLAINABILITY ----------------
st.markdown("<div class='section-box'>", unsafe_allow_html=True)
st.subheader("🧠 Forecast Explanation")

st.write("""
• AQI is rising due to **evening traffic congestion**  
• **Low wind speed** is trapping pollutants  
• PM₂.₅ remains elevated from sustained emissions  
• This spike is expected to **subside overnight**
""")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- HEATMAP ----------------
st.markdown("<div class='section-box'>", unsafe_allow_html=True)
st.subheader("🗺️ City AQI Heatmap (Dummy)")

map_df = pd.DataFrame({
    "lat": 19.07 + np.random.randn(40) * 0.02,
    "lon": 72.87 + np.random.randn(40) * 0.02,
    "AQI": np.random.randint(60, 200, 40)
})

st.map(map_df)
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.caption("AeroGuard AI · Streamlit Prototype · PS02")
st.caption("© 2026 AeroGuard Technologies")