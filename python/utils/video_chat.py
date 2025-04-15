import cv2
import streamlit as st
from python.main.video_processor import VideoAnalyzer
from python.main.nlp_handler import VideoNLP

# Initialize with threading for smoother performance
analyzer = VideoAnalyzer()
nlp = VideoNLP(analyzer)

st.title("🎥 Video NLP Analyzer")
st.write("Ask questions about live video:")

# Video display
frame_placeholder = st.empty()
stop_button = st.button("Stop Analysis")

# Chat interface
query = st.text_input("Ask about the video (e.g., 'count people')")

# Process frames
cap = cv2.VideoCapture(0)
while not stop_button:
    ret, frame = cap.read()
    if not ret:
        st.error("Video source disconnected")
        break
    
    # Process frame
    _, results = next(analyzer.process_stream())
    frame_placeholder.image(frame, channels="BGR")
    
    # Handle queries
    if query:
        response = nlp.answer(query)
        st.text_area("Analysis Result", value=response, height=100)
        query = ""  # Clear after processing

cap.release()