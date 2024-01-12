# runpod-ollama-speedtest-guide
A guide to testing different runpod (and other linux VMs) configurations. Specifically the speed of LLM outputs

https://www.runpod.io/console/gpu-secure-cloud

### Results

| GPU       | VRAM (GB) | SPEED (T/S) | PRICE ($/HR) | VALUE (T/$) | QUANT | MODEL                           |
| --------- | --------- | ----------- | ------------ | ----------- | ----- | ------------------------------- |
| RTX A6000 | 48        | 38.53       | 0.79         | 175,579.74  | 6     | mixtral:8x7b-instruct-v0.1-q6_K |
| A40       | 48        | 32.34       | 0.79         | 147,372.15  | 6     | mixtral:8x7b-instruct-v0.1-q6_K |
| L40       | 48        | 40.09       | 1.14         | 126,600.00  | 6     | mixtral:8x7b-instruct-v0.1-q6_K |

| GPU       | VRAM (GB) | SPEED (T/S) | PRICE ($/HR) | VALUE (T/$) | QUANT | MODEL                           |
| --------- | --------- | ----------- | ------------ | ----------- | ----- | ------------------------------- |
| RTX A6000 | 48        | 44.99       | 0.79         | 205,017.72  | 5     | mixtral:8x7b-instruct-v0.1-q5_1 |
| A40       | 48        | 38.12       | 0.79         | 173,711.39  | 5     | mixtral:8x7b-instruct-v0.1-q5_1 |
| L40       | 48        | 46.82       | 1.14         | 147,852.63  | 5     | mixtral:8x7b-instruct-v0.1-q5_1 |

| GPU          | VRAM (GB) | SPEED (T/S) | PRICE ($/HR) | VALUE (T/$) | QUANT | MODEL        |
|:------------ | --------- |:----------- |:------------ | ----------- | ----- | ------------ |
| RTX A6000    | 48        | 52.77       | 0.79         | 240,508.60  | 4     | mixtral:8x7b |
| RTX 6000 Ada | 48        | 68.05       | 1.14         | 214,894.17  | 4     | mixtral:8x7b |
| A40          | 48        | 45.17       | 0.79         | 205,840.98  | 4     | mixtral:8x7b |
| L40          | 48        | 56.87       | 1.14         | 179,614.82  | 4     | mixtral:8x7b |
| A100 SXM     | 80        | 61.96       | 2.29         | 97,413.77   | 4     | mixtral:8x7b |
| RTX4090      | 24        | 12.61       | 0.74         | 61,362.23   | 4     | mixtral:8x7b |
| H100         | 80        | 43.00       | 4.69         | 33,008.47   | 4     | mixtral:8x7b |
| RTX A5000    | 24        | 1.59        | 0.44         | 13,084.85   | 4     | mixtral:8x7b |

| GPU          | VRAM (GB) | SPEED (T/S) | PRICE ($/HR) | VALUE (T/$) | QUANT | MODEL                             |
| ------------ | --------- | ----------- | ------------ | ----------- | ----- | --------------------------------- |
| RTX4090      | 24        | 69.01       | 0.74         | 335,724.32  | 3     | mixtral:8x7b-instruct-v0.1-q3_K_S |
| A5000        | 24        | 38.25       | 0.44         | 312,954.55  | 3     | mixtral:8x7b-instruct-v0.1-q3_K_S |
| A40          | 48        | 41.21       | 0.79         | 187,792.41  | 3     | mixtral:8x7b-instruct-v0.1-q3_K_S |
| RTX 6000 Ada | 48        | 69.83       | 1.14         | 220,515.78  | 3     | mixtral:8x7b-instruct-v0.1-q3_K_S |
| A6000        | 48        | 45.6        | 0.79         | 207,797.47  | 3     | mixtral:8x7b-instruct-v0.1-q3_K_S |
| L40          | 48        | 56.71       | 1.14         | 179,084.21  | 3     | mixtral:8x7b-instruct-v0.1-q3_K_S |

| GPU          | VRAM (GB) | SPEED (T/S) | PRICE ($/HR) | VALUE (T/$) | QUANT | MODEL                           |
| ------------ | --------- | ----------- | ------------ | ----------- | ----- | ------------------------------- |
| RTX 4000 Ada | 20        | 46.75       | 0.39         | 431,538.46  | 2     | mixtral:8x7b-instruct-v0.1-q2_K |
| A5000        | 24        | 49.45       | 0.44         | 404,590.91  | 2     | mixtral:8x7b-instruct-v0.1-q2_K |
| RTX4090      | 24        | 75.88       | 0.74         | 369,145.95  | 2     | mixtral:8x7b-instruct-v0.1-q2_K |
| A6000        | 48        | 57.67       | 0.79         | 262,800     | 2     | mixtral:8x7b-instruct-v0.1-q2_K |
| RTX 6000 Ada | 48        | 80.12       | 1.14         | 253,010.52  | 2     | mixtral:8x7b-instruct-v0.1-q2_K |
| A40          | 48        | 51.05       | 0.79         | 232,632.91  | 2     | mixtral:8x7b-instruct-v0.1-q2_K |
| L40          | 48        | 65.55       | 1.14         | 207,000.00  | 2     | mixtral:8x7b-instruct-v0.1-q2_K |

*note: GPT-3.5 comes in about 500,000 tokens/$*

### Run

```bash
curl https://ollama.ai/install.sh | sh
```

```bash
ollama serve
```

then in a new terminal

```bash
ollama run mixtral:8x7b # note: use any model you would like
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
```

```bash
python speed.py
```
