import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ev_report(data):
    prompt = f"""
You are an assistant that summarizes Electric Vehicle (EV) health based on telemetry data.

Vehicle Stats:
- Battery level: {data['battery_level']}%
- Charge cycles: {data['charge_cycles']}
- Distance driven: {data['distance_driven']} km
- Temperature: {data['temp']}°C

Write a friendly 3-4 line report about the vehicle's battery health and suggestions if needed.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Error: {e}"
