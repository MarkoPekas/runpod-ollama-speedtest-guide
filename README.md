# runpod-ollama-speedtest-guide
A guide to testing different runpod (and other linux VMs) configurations. Specifically the speed of LLM outputs

https://www.runpod.io/console/gpu-secure-cloud

| GPU       | T/S                | $/HR | T/$   |
|:--------- |:------------------ |:---- | ----- |
| RTX A6000 | 52.778275125799354 | 0.79 | 66.81 |
| A40       | 45.17065873434471  | 0.79 | 57.18 |
| L40       | 56.87802678475367  | 1.14 | 49.89 |
| A100 SXM  | 61.965978844301496 | 2.29 | 27.06 |
| RTX4090   | 12.613347074703317 | 0.74 | 17.05 |
| H100      | 43.002703448927555 | 4.69 | 9.17  |
| RTX A5000 | 1.5992600462735782 | 0.44 | 3.63  |

### Run

```bash
curl https://ollama.ai/install.sh | sh
```

```bash
ollama serve
```

then in a new terminal

```bash
ollama run mixtral:8x7b # choose whatever model you want to test
```

### Code for testing speed

```bash
apt-get update
apt-get install nano
nano speed.py
```

```python
import requests
import json

def send_request():
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mixtral:8x7b", # make sure to set the model here too
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
```

```bash
python speed.py
```
