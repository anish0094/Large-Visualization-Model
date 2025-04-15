import streamlit as st
from datetime import datetime
import json
import os
import pandas as pd
from pathlib import Path
from python.utils.config import DETECTION_IMAGES_DIR, DETECTION_LOGS_DIR

# Dashboard Config
st.set_page_config(layout="wide")
st.title("🖥️ Real-Time Detection Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
date_filter = st.sidebar.date_input("Select Date")
min_confidence = st.sidebar.slider("Min Confidence", 0.0, 1.0, 0.5)

# Load Detection Data
def load_detections():
    detections = []
    for log_file in Path(DETECTION_LOGS_DIR).glob("*.json"):
        with open(log_file) as f:
            data = json.load(f)
            data["date"] = datetime.strptime(data["timestamp"], "%Y%m%d_%H%M%S").date()
            detections.append(data)
    return detections

# Main Dashboard
detections = load_detections()

# Metrics Row
col1, col2, col3 = st.columns(3)
col1.metric("Total Detections", len(detections))
col2.metric("Objects Today", sum(len(d["objects"]) for d in detections))
col3.metric("Avg Confidence", f"{sum(o['confidence'] for d in detections for o in d['objects'])/sum(len(d['objects']) for d in detections):.1%}")

# Recent Detections
st.subheader("📸 Latest Detections")
for detection in sorted(detections, key=lambda x: x["timestamp"], reverse=True)[:3]:
    img_path = os.path.join(DETECTION_IMAGES_DIR, f"{detection['timestamp']}.jpg")
    st.image(img_path, caption=f"Detected at {detection['timestamp']}", width=300)
    st.json(detection)  # Show raw metadata

# Object Analysis
st.subheader("📊 Object Statistics")
df = pd.DataFrame([obj for det in detections for obj in det["objects"]])
if not df.empty:
    st.bar_chart(df["type"].value_counts())
    st.dataframe(df[["type", "confidence", "track_id"]].sort_values("confidence", ascending=False))