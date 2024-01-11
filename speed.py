import requests
import json

MODEL_OLLAMA="mixtral:8x7b"

def send_request():
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": MODEL_OLLAMA,
        "prompt": "Why is the sky blue?",
        "stream": False  # Adjust this based on whether you want streaming or not
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

def calculate_speed(response_data):
    eval_count = response_data.get("eval_count", 0)
    eval_duration = response_data.get("eval_duration", 1)  # Prevent division by zero

    # Convert nanoseconds to seconds for eval_duration
    eval_duration_seconds = eval_duration / 1e9

    # Calculate tokens per second
    speed = eval_count / eval_duration_seconds
    return speed

def main():
    response_data = send_request()
    speed = calculate_speed(response_data)
    print(f"Speed: {speed} tokens/second")

if __name__ == "__main__":
    main()
