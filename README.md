# Visual Language Model (VLM) for Video Analysis

A real-time video analysis system that allows natural language interaction to extract insights from live or recorded video streams.

## ✨ Features

- **Natural Language Video Queries**
  - "Count all cars in the last minute"
  - "Show me people moving west"
  - "Find parked delivery trucks"
- **Multi-Source Video Input**
  - Webcam
  - Video files (MP4, AVI)
  - RTSP streams (CCTV cameras)
- **Advanced Object Tracking**
  - Persistent ID tracking
  - 60-second rolling history
  - Movement analysis
- **Interactive Dashboard**
  - Real-time video display
  - Query history
  - Visualization tools

## 🛠️ Technology Stack

| Component          | Technology Used           | Purpose                          |
|--------------------|---------------------------|----------------------------------|
| Computer Vision    | YOLOv8 (Ultralytics)      | Object detection and tracking    |
| NLP Engine         | Custom rule-based parser  | Natural language understanding   |
| Video Processing   | OpenCV 4.7               | Frame capture and processing     |
| User Interface     | Streamlit                | Interactive web dashboard        |
| Hardware Interface | Arduino Uno              | Physical trigger integration     |

## 📦 Installation

### Prerequisites
- Python 3.9+
- NVIDIA GPU (recommended) with CUDA 11.7
- Arduino IDE (for hardware integration)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Large_Visualization_Model.git
cd Large_Visualization_Model
```

2. Create and activate virtual environment:

```bash 
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Download YOLOv8 model:

```bash
wget https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt -O data/models/yolov8n.pt
```

## 🚀 Usage
### Running the System
1. Start the Streamlit dashboard:

```bash
streamlit run python/utils/video_chat.py
```
2. Access the interface at http://localhost:8501

### Example Queries
```bash
"Count all vehicles in the left lane"
"Highlight people wearing safety vests"
"Alert if any object stays >30 seconds"
"Show movement heatmap of last 5 minutes"
```

### Hardware Integration
1. Upload Arduino sketch:
```
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(2) == LOW) {
    Serial.println("TRIGGER_AI");
    delay(1000);
  }
}
```
2. Connect to system via USB

## 📂 Project Structure
```
Large_Visualization_Model/
├── data/
│   ├── models/               # ML model weights
│   ├── videos/               # Sample videos
│   └── detections/           # Output storage
├── docs/                     # Documentation
├── python/
│   ├── main/                 # Core application
│   ├── utils/                # Helper functions
│   └── tests/                # Unit tests
├── arduino/                  # Hardware code
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```
## 🤝 Contributing
1. Fork the project

2. Create your feature branch:

```bash
git checkout -b feature/new-analysis-module
```
3. Commit your changes:
```bash
git commit -m 'Add new movement analysis feature'
```
4. Push to the branch:
```bash
git push origin feature/new-analysis-module
```
5. Open a pull request

## 📧 Contact
For questions or support:

* Email: anish.fc0094@gmail.com

* GitHub Issues: Open New Issue
