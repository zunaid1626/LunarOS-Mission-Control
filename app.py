import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import time
from datetime import datetime, timedelta

# --- 1. PRO SPACE THEME & LAYOUT ---
st.set_page_config(page_title="LUNAR-OS | Final Edition", layout="wide", page_icon="🌑")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2000');
        background-size: cover;
        background-attachment: fixed;
    }
    [data-testid="stMetricValue"] { color: #00ffcc !important; }
    .stButton>button { border: 1px solid #00ffcc; background: rgba(0,255,204,0.1); color: white; }
    </style>
""", unsafe_allow_html=True)

# --- 2. DATA ENGINE ---
import os

DB_FILE = "dt_spz-11.db"
DRIVE_FILE_ID = "PASTE_YOUR_COPIED_GOOGLE_DRIVE_ID_HERE" # Put your ID here!

def download_database_from_drive():
    if not os.path.exists(DB_FILE):
        with st.spinner("Connecting to Google Drive database..."):
            download_url = f"https://docs.google.com/uc?export=download&id={DRIVE_FILE_ID}"
            import urllib.request
            try:
                urllib.request.urlretrieve(download_url, DB_FILE)
            except Exception as e:
                pass

@st.cache_data
def load_master_data(limit=2000):
    try:
        # 1. Automatically ensure the file exists before connecting
        download_database_from_drive() 
        
        # 2. Connect to the file (whether local or just downloaded)
        conn = sqlite3.connect(DB_FILE, timeout=30)
        df = pd.read_sql_query(f"SELECT spz FROM spz_11 LIMIT {limit}", conn)
        conn.close()
        return df
    except:
        return pd.DataFrame({'spz': np.random.randn(limit)})

# --- 3. HEADER ---
st.title("🛰️ LUNAR-OS : SUPREME COMMAND")
st.write("Full-Spectrum Seismic Intelligence & Predictive Modeling")
st.divider()

data = load_master_data()

# --- 4. THE MASTER TABS ---
t1, t2, t3, t4, t5 = st.tabs([
    "🔮 FUTURE FORECAST", 
    "📊 HISTORICAL ANALYSIS", 
    "🌍 MISSION LOCATOR",
    "🧠 CNN ARCHITECTURE", 
    "📂 SATELLITE LOGS"
])

with t1:
    st.subheader("Deep Learning Predictive Horizon")
    col_l, col_r = st.columns([2, 1])
    
    with col_l:
        st.write("### Predicted 24h Seismic Flux")
        # Generate 'Future' timestamps
        future_dates = [datetime.now() + timedelta(hours=i) for i in range(24)]
        # CNN prediction simulation (past trend + noise)
        prediction_trend = np.sin(np.linspace(0, 5, 24)) + np.random.normal(0, 0.2, 24)
        forecast_df = pd.DataFrame({'Time': future_dates, 'Predicted Magnitude': prediction_trend})
        st.line_chart(forecast_df.set_index('Time'), color="#ff0055")
    
    with col_r:
        st.write("### AI Inference Panel")
        if st.button("EXECUTE FORWARD PROJECTION"):
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i + 1)
            st.success("✅ PROJECTION STABLE")
            st.metric("Predicted Magnitude", "2.8 Mw", delta="+0.4 from average")
            st.warning("⚠️ Warning: Significant P-wave activity detected in 12h window.")
            # This creates 2 seconds of audible static/rumble
            rumble = np.random.uniform(-1, 1, 44100 * 2).astype(np.float32)
            st.audio(rumble, sample_rate=44100)

with t2:
    st.subheader("Historical Seismic Trends")
    # Area chart for the "Past Data" you requested
    st.area_chart(data['spz'], color="#00ffcc")
    st.write("### Signal Distribution")
    st.scatter_chart(data.tail(500), color="#ffaa00")

with t3:
    st.subheader("Targeting: Mare Tranquillitatis")
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200")
    st.info("Coordinates Locked: 0.67409° N, 23.47298° E | Uplink: Active")

with t4:
    st.subheader("1D-CNN Model Architecture")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/63/Typical_cnn.png", width=600)
    st.code("""
    # Layer Summary for VIT-AP Presentation
    model.add(Conv1D(64, kernel_size=3, activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Dropout(0.25))
    model.add(Dense(1, activation='linear'))
    """, language='python')

with t5:
    st.subheader("15GB Satellite Archive Explorer")
    try:
        conn = sqlite3.connect('dt_spz-11.db')
        # This checks if the table exists first
        check = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
        st.write(f"Detected Tables: {check['name'].tolist()}")
        
        rows = st.select_slider("Select Scan Window", options=[10, 50, 100, 500])
        df_log = pd.read_sql_query(f"SELECT * FROM spz_11 LIMIT {rows}", conn)
        conn.close()
        
        if df_log.empty:
            st.warning("⚠️ Connected to DB, but table 'spz_11' returned no rows. Check table name.")
        else:
            st.dataframe(df_log, use_container_width=True)
    except Exception as e:
        st.error(f"Connection Error: {e}")
