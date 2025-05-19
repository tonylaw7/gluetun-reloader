Here’s a clean and concise README.md you can include at the root of your project:

⸻

🛑 Gluetun Stopper

A minimal Dockerized Python service that uses the Gluetun HTTP control server to periodically stop the WireGuard/OpenVPN tunnel every 2 hours (or a custom interval), using authenticated API requests.

⸻

📁 Project Structure

gluetun-stopper/
├── docker-compose.yml         # Combined Gluetun + Stopper services
├── Dockerfile                 # Image definition for Python API client
├── gluetun_stop.py            # Python script to stop Gluetun via HTTP API
├── requirements.txt           # Python dependency list
├── .env                       # Configurable environment variables
└── README.md


⸻

⚙️ Setup Instructions

1. Clone the project

git clone https://github.com/youruser/gluetun-stopper.git
cd gluetun-stopper

2. Configure environment

Edit .env:

GLUETUN_URL=http://gluetun:8000/v1/openvpn/status
USERNAME=myusername
PASSWORD=mypassword
INTERVAL_HOURS=2

# Optional WireGuard
WIREGUARD_PRIVATE_KEY=your_wireguard_key
WIREGUARD_ADDRESSES=10.2.0.2/32

🧠 The Gluetun control server must be enabled and configured with a proper config.toml authentication file.

3. Build and start containers

docker-compose up --build -d

The gluetun-stopper service will trigger PUT /v1/openvpn/status every 2 hours with {"status": "stopped"}.

⸻

🐍 Python Script Behavior
	•	Reads settings from environment variables
	•	Sends a PUT request with Basic Auth to stop the tunnel
	•	Repeats every INTERVAL_HOURS hours (default: 2)

You can customize the script to add start, update, or full restart logic.

⸻

🔐 Auth Config Example (Gluetun config.toml)

[[roles]]
name = "control"
routes = [
  "PUT /v1/openvpn/status"
]
auth = "basic"
username = "myusername"
password = "mypassword"

Mount it to /gluetun/auth/config.toml and specify via:

- HTTP_CONTROL_SERVER_AUTH_CONFIG_FILEPATH=/gluetun/auth/config.toml


⸻

🧪 Test API Call

curl -X PUT http://localhost:8000/v1/openvpn/status \
     -u "myusername:mypassword" \
     -H "Content-Type: application/json" \
     -d '{"status":"stopped"}'


⸻

✅ TODO / Extensions
	•	Add support for restart or start logic
	•	Trigger updater API between stop/start
	•	Convert to stop → update → start cycle

⸻

Let me know if you’d like to convert this into a GitHub template repo or add support for CLI params!