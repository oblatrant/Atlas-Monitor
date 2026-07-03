from flask import Flask, render_template, request, jsonify
from mcstatus import JavaServer
import time
import random

app = Flask(__name__)

# -----------------------------
# HISTORY STORAGE

store = {}

MAX_HISTORY = 60


# -----------------------------
# CORE DATA ENGINE (RESTORED FEEL)

def get_data(ip):

    if not ip:
        return {
            "success": False,
            "message": "No IP provided"
        }

    try:
        server = JavaServer.lookup(ip)
        status = server.status()

        # -----------------------------
        # RAW MC DATA

        latency = round(status.latency, 2)
        players = status.players.online
        maxp = status.players.max

        # -----------------------------
        # RESTORED "DASHBOARD FEEL LAYER"
        load = round(
            (latency * 0.35) +
            (players * 2.2) +
            random.uniform(-3, 3),
            2
        )

        cpu = round(min(100, (load / 1.4) + random.uniform(-2, 2)), 2)

        memory = round(
            min(100, (players / max(maxp, 1)) * 100 + random.uniform(2, 8)),
            2
        )

        network = round(latency + random.uniform(-2, 2), 2)

        uptime = round(99.2 + random.random() * 0.7, 2)

        # -----------------------------
        # HISTORY SYSTEM (60 POINTS)
        if ip not in store:
            store[ip] = []

        store[ip].append({
            "t": time.strftime("%H:%M:%S"),
            "latency": latency,
            "players": players,
            "load": load,
            "cpu": cpu,
            "network": network
        })

        store[ip] = store[ip][-MAX_HISTORY:]

        # -----------------------------
        # RESPONSE
        return {
            "success": True,
            "online": True,

            "ip": ip,

            "players": players,
            "max": maxp,

            "latency": latency,
            "load": load,
            "cpu": cpu,
            "memory": memory,
            "network": network,
            "uptime": uptime,

            "history": store[ip]
        }

    except Exception as e:

        return {
            "success": False,
            "online": False,

            "ip": ip,

            "players": 0,
            "max": 0,
            "latency": 0,
            "load": 0,
            "cpu": 0,
            "memory": 0,
            "network": 0,
            "uptime": 0,

            "history": [],
            "error": str(e)
        }


# -----------------------------
# FRONTEND PAGE
@app.route("/")
def index():
    return render_template("index.html")


# -----------------------------
# MAIN API (FIXED NAME)
@app.route("/api/server")
def api_server():

    ip = request.args.get("ip")
    return jsonify(get_data(ip))


# -----------------------------
# RUN SERVER
if __name__ == "__main__":

    print("Atlas Monitor running on http://127.0.0.1:5000")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )