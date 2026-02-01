# 🚀 Network AI Monitor

Network AI Monitor is a real-time network traffic monitoring and bandwidth analysis tool built using Python and AI-based logic.

It helps users monitor internet usage, detect abnormal traffic, and track upload/download speed of all network interfaces automatically.

This tool is useful for:
• Network Monitoring  
• Bandwidth Analysis  
• Suspicious Traffic Detection  
• Cybersecurity Projects  
• Live Dashboard Visualization  

---

## 📌 Why This Project is Important?

Today, networks face many issues like:
- Unknown bandwidth usage
- Slow internet speed
- Malware traffic
- Suspicious background downloads
- Network abuse

Network AI Monitor solves these problems by:
✔ Tracking real-time bandwidth  
✔ Logging data into CSV  
✔ Detecting abnormal traffic  
✔ Showing live monitoring dashboard  
✔ Helping in cybersecurity analysis  

---

## ⚙️ Features

✅ Real-time bandwidth monitoring  
✅ Upload & Download speed tracking  
✅ Per-interface monitoring (WiFi/Ethernet)  
✅ CSV data logging  
✅ AI-based anomaly detection  
✅ Simple dashboard interface  
✅ Standalone EXE (no Python required)  

---

## 🛠️ Technologies Used

- Python
- psutil
- PySide6 (GUI)
- PyInstaller (EXE build)
- CSV logging
- Basic AI logic

---

## 📂 Project Structure

network-ai-monitor/
│
├── dashboard_main.py
├── monitor.py
├── requirements.txt
├── dist/
 └── dashboard_main.exe


---

## ▶️ How to Run (For Normal Users)

### Step 1
Download the project ZIP from GitHub.

### Step 2
Extract the ZIP file.

### Step 3
Open:


### Step 4
Double click **dashboard_main.exe**

### Step 5
Wait 1–2 minutes ⏳

Monitoring will start automatically and live bandwidth data will appear.

---

## 💻 How to Run (For Developers)

If you want to run using Python:

### Install dependencies
````bash
pip install -r requirements.txt

python dashboard_main.py

pyinstaller --onedir dashboard_main.py



