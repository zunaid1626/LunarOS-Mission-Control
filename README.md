# 🛰️ LUNAR-OS : MISSION CONTROL
**Advanced 1D-CNN Lunar Seismic Detection & Telemetry Platform**

### 🚀 Project Overview
Developed for VIT-AP, LUNAR-OS is a state-of-the-art deep learning pipeline designed to process and analyze 15GB of historical Apollo seismic telemetry archives to predict and detect moonquakes.

### 🛠️ Core Features
- **Neural Inference (Deep Scan):** Real-time 1D-CNN sliding window anomaly detection.
- **Future Prediction Horizon:** 24-hour forward-projecting trend forecasting.
- **Seismic Sonification:** Numerical signal-to-audio waveform processing.
- **Multimodal Visualization:** Interactive high-fidelity energy flux area and scatter charts.

### 📦 Local Setup Instructions
1. Clone the repository logic.
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure the localized telemetry archive (`dt_spz-11.db`) is placed in the root directory.
4. Execute via Streamlit: `streamlit run app.py`
