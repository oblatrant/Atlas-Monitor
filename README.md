<h1 align="center"> Atlas Monitor </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Early%20Development-3b82f6?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/JavaServer-MCStatus-00AA55?style=for-the-badge">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Charts-Chart.js-FF6384?style=for-the-badge">
</p>

<p align="center">
A modern Minecraft server monitoring dashboard built with Flask, MCStatus, and Chart.js.
</p>

---

<img width="1920" height="1039" alt="Screenshot_2026-07-02_15-46-50" src="https://github.com/user-attachments/assets/f02abf72-7e53-4b59-9fe8-48c1ffc9af04" />

---

# Features

- Monitor any Java Minecraft server
- Live latency graph
- Performance dashboard
- Real-time server polling
- Beautiful glassmorphism interface
- Server status monitoring
- Memory usage indicators
- CPU usage indicators
- Network statistics
- Connected server table
- Live activity feed
- Historical chart data

---

# Early Development Notice

> **Atlas Monitor is currently in early development.**

This repository is an early public release intended to showcase the project and its current direction.

### Current limitations

- The sidebar pages (Servers, Analytics, Performance, Activity, Alerts, Settings) are **not functional yet**.
- Several analytics currently use placeholder or simulated values while backend functionality is being developed.
- Additional APIs and monitoring features are planned for future releases.

More functionality is coming in future updates.

---

# Code Notes

To keep the repository clean and easier to browse:

- All developer comments have been removed from the source code.
- Future releases may include a fully commented version for educational purposes.

---

# Project Structure

```
AtlasMonitor/
│
├── app.py
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── app.js
│
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/oblatrant/Atlas-Monitor.git
```

---

## 2. Enter the project

```bash
cd Atlas-Monitor
```

---

## 3. Install dependencies

```bash
pip install flask mcstatus
```

or

```bash
pip install -r requirements.txt
```

---

## 4. Start the server

```bash
python app.py
```

or on Linux

```bash
python3 app.py
```

---

## 5. Open your browser

Visit

```
http://127.0.0.1:5000
```

---

# How To Use

## Step 1

Launch the Flask application.

```
python3 app.py
```

---

## Step 2

Open your browser and navigate to

```
http://127.0.0.1:5000
```

---

## Step 3

Enter any Java Minecraft server IP.

Example:

```
mc.hypixel.net
```

or

```
play.cubecraft.net
```

---

## Step 4

Press **Connect**

---

## Step 5

Atlas Monitor will begin polling the server and display live statistics including:

- Player count
- Latency
- Memory
- CPU
- Network
- Uptime
- Performance graph
- Activity feed

---

# Built With

- Python
- Flask
- MCStatus
- HTML5
- CSS3
- JavaScript
- Chart.js

---

# Planned Features

- [ ] Multiple server monitoring
- [ ] Working sidebar navigation
- [ ] Server history database
- [ ] Better analytics
- [ ] Server icons
- [ ] Ping heatmaps
- [ ] Export reports
- [ ] Dark/Light themes
- [ ] Authentication
- [ ] Docker support
- [ ] Plugin support
- [ ] Notifications
- [ ] Better uptime tracking
- [ ] Mobile responsiveness

---

# Contributing

Pull requests, ideas, and feature suggestions are always welcome.

If you discover a bug or have an improvement, feel free to open an issue.

---
