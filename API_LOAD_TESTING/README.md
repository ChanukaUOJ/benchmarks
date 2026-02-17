
# Benchmarks
Benchmark reports for all services

## 📢 How to setup project

#### 1️⃣ Clone the project

```bash
  git clone https://github.com/LDFLK/benchmarks.git
```

#### 2️⃣ Go to the project directory

```bash
  cd benchmarks
```

#### 3️⃣ Open python environment

```bash
  #Create environment
  python -m venv .venv   
  
  #activate environment
  .venv/Scripts/Activate  #windows powershell
  source .venv/bin/activate   #linux
```

#### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

#### 5️⃣ Navigate to the relevant folder and start the server

```bash
  cd opengin/api/perf
  locust -f locust.py
```

#### 6️⃣ Access the web interface on
```bash
http://localhost:8089
````

## 🚀 Addtional Command-line Parameters

###### These parameters are optional when starting Locust from the command line. However, if you do not provide them via CLI, Locust will require you to enter them in the web UI before the test can start, since they are necessary to run the load test.

#### Example command
```bash
  locust -f locust.py --host <host_url> --users <number_of_users> --spawn-rate <rate>

  ex:
  locust -f locust.py --host="https://example.com" --users 100 --spawn-rate 10
```

#### 1️⃣ Test Configuration
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `--host` , `-H` | `string` | **Optional**. Service host url |
| `--users` , `-u` | `int` | **Optional**. Number of peak concurrency users |
| `--spawn-rate` , `-r` | `float` | **Optional**. Rate to spawn users (users per second) |
| `--run-time` , `-t` | `time string` | **Optional**. Stop after the specified amount of time, e.g. (300s, 20m, 3h, 1h30m, etc.). Only used together with --headless or --autostart.|

#### 2️⃣ Execusion Behaviour
| Parameter | Description                |
| :-------- |  :------------------------- |
| `--headless` |  **Optional**. Disable the web interface, and start the test immediately. |
| `--autostart`  |  **Optional**. Starts the test immediately (like --headless, but without disabling the web UI) |


