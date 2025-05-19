# Gluetun Reloader

A simple Dockerized Python service that uses the [Gluetun HTTP control server](https://github.com/qdm12/gluetun/wiki/HTTP-control-server) to stop the WireGuard or OpenVPN tunnel every 2 hours (or at a custom interval), using authenticated API requests.

---

## Project Structure

```
gluetun-reloader/
├── docker-compose.yml         # Gluetun and Stopper services
├── Dockerfile                 # Python script container
├── gluetun_reload.py            # Python script to stop Gluetun
├── requirements.txt           # Python packages
├── .env                       # Environment configuration
└── README.md
```

---

## Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/youruser/gluetun-stopper.git
cd gluetun-stopper
```

### 2. Configure environment

Edit the `.env` file:

```ini
GLUETUN_URL=http://gluetun:8000/v1/openvpn/status
USERNAME=myusername
PASSWORD=mypassword
INTERVAL_HOURS=2

# Optional for WireGuard
WIREGUARD_PRIVATE_KEY=your_wireguard_key
WIREGUARD_ADDRESSES=10.2.0.2/32
```

Make sure the Gluetun control server is enabled and an auth config file is mounted properly.

### 3. Build and start the containers

```bash
docker-compose up --build -d
```

The `gluetun-stopper` service will send a `PUT` request to stop the VPN tunnel every 2 hours.

---

## Python Script Behavior

* Uses environment variables for settings
* Sends an authenticated HTTP PUT request to stop the VPN
* Waits and repeats every few hours based on configuration

You can extend the script to also start the tunnel or run the updater.

---

## Auth Config Example for Gluetun (`config.toml`)

```toml
[[roles]]
name = "control"
routes = [
  "PUT /v1/openvpn/status"
]
auth = "basic"
username = "myusername"
password = "mypassword"
```

Mount this file to `/gluetun/auth/config.toml` and reference it with:

```yaml
- HTTP_CONTROL_SERVER_AUTH_CONFIG_FILEPATH=/gluetun/auth/config.toml
```

---

## Test the API Manually

```bash
curl -X PUT http://localhost:8000/v1/openvpn/status \
     -u "myusername:mypassword" \
     -H "Content-Type: application/json" \
     -d '{"status":"stopped"}'
```

---

## ✅ TODO / Extensions

* Add support for restarting the VPN after a delay
* Trigger the server list updater
* Combine stop → update → start into one flow
