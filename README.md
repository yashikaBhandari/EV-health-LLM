# 🔋 EV Health Report Generator using LLM

This project uses **LLMs (Large Language Models)** to generate **battery health reports** for Electric Vehicles (EVs) based on real-time telemetry data.

Built using **Python**, **Streamlit**, and **OpenAI GPT**, this tool allows users to upload EV sensor data (`CSV file`) and receive smart, human-like summaries of each vehicle’s battery condition.

---

## 🚀 Demo Preview

> 👇 Upload your EV data CSV and instantly get insights like:
> - Is the battery in good health?
> - Are charge cycles too high?
> - Any warning signs based on temperature?


---

## 🧠 How It Works

1. User uploads a `.csv` file with EV sensor data
2. Each row (representing one vehicle) is passed to GPT with a structured prompt
3. GPT responds with a short, human-friendly battery report
4. Users can expand/collapse to view each vehicle's report

---

## 📦 Sample CSV Format

```csv
vehicle_id,battery_level,charge_cycles,distance_driven,temp
EV001,78,230,18000,37
EV002,62,150,9000,34
EV003,45,320,22000,40


```
## Features
✅ Upload EV sensor data in .csv format

✅ LLM (GPT) generates natural-language battery health reports

✅ Expandable sections for each EV

✅ Clean UI using Streamlit

✅ Modular code (separate OpenAI logic)


## 🔧 Tech Stack
Streamlit

OpenAI GPT-3.5 Turbo

Pandas



## Install Dependencies

<br>
pip install -r requirements.txt
<br>
Add Your OpenAI API Key
<br>
Temporarily set your OpenAI key in the terminal:

<br>

export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
<br>
## Run the App
<br>
streamlit run app.py
<br>
<br>
<h1><br>Project Structure <br></h1>

```
📁 ev-health-llm/
│
├── app.py                  # Main Streamlit UI
├── generate_report.py      # GPT-based report logic
├── requirements.txt        # Python dependencies
├── ev_data.csv             # Sample CSV
└── README.md               # You're reading this!
```

## Future Improvements
📊 Add visual charts (battery trends, heatmaps)

🧠 Integrate simple ML models to predict battery degradation

📤 Export health reports as PDF or Excel

☁️ Deploy online with Streamlit Cloud
