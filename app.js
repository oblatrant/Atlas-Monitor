let currentIP = null;
let chart = null;


// INIT CHART


function initChart() {

    const ctx = document.getElementById("performanceChart").getContext("2d");

    chart = new Chart(ctx, {

        type: "line",

        data: {
            labels: [],
            datasets: [{
                label: "Latency",
                data: [],
                borderWidth: 2,
                tension: 0.4
            }]
        },

        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: { x: { display: false } }
        }

    });

}


// FETCH SERVER DATA


async function fetchServer() {

    if (!currentIP) return;

    const res = await fetch(`/api/server?ip=${currentIP}`);
    const data = await res.json();

    if (!data.success) return;

    // KPI updates
    document.getElementById("players").innerText =
        `${data.players} / ${data.max_players}`;
    document.getElementById("latency").innerText = data.latency + " ms";
    document.getElementById("version").innerText = data.version;
    document.getElementById("memory").innerText = data.memory + "%";
    document.getElementById("cpu").innerText = data.cpu + "%";
    document.getElementById("network").innerText = data.network;
    document.getElementById("uptime").innerText = data.uptime;

    document.getElementById("overviewPlayers").innerText = data.players;
    document.getElementById("overviewVersion").innerText = data.version;

    document.getElementById("statusText").innerText = "Online";
    document.getElementById("serverIP").innerText = data.ip;

    document.querySelector(".status-dot").style.background = "#22c55e";

    // Chart update
    chart.data.labels.push("");
    chart.data.datasets[0].data.push(data.latency);

    if (chart.data.labels.length > 20) {
        chart.data.labels.shift();
        chart.data.datasets[0].data.shift();
    }

    chart.update();

}


// FETCH EVENTS


async function fetchEvents() {

    const res = await fetch("/api/events");
    const data = await res.json();

    const feed = document.getElementById("activityFeed");
    feed.innerHTML = "";

    data.forEach(ev => {

        const div = document.createElement("div");

        div.className = "activity-item";

        div.innerHTML = `
            <div class="dot"></div>
            <div>
                <p>${ev.message}</p>
                <span>${ev.time}</span>
            </div>
        `;

        feed.appendChild(div);

    });

}


// CONNECT BUTTON

document.getElementById("connectButton").addEventListener("click", () => {

    const ip = document.getElementById("serverInput").value;

    if (!ip) return;

    currentIP = ip;

    document.getElementById("connectionStatus").innerText = "Connected";

    initChart();

    fetchServer();
    fetchEvents();

    setInterval(fetchServer, 3000);
    setInterval(fetchEvents, 5000);

});