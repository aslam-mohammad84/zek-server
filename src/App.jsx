import { useEffect, useState } from "react";
import "./App.css";
import Cloud from "./Cloud";
import Chat from "./Chat";
function App() {
  const [page, setPage] = useState("dashboard");

  const [data, setData] = useState(null);
  const [error, setError] = useState(false);

  const fetchStatus = async () => {
    try {
      const response = await fetch("/api/status");
      if (!response.ok) {
        throw new Error("API request failed");
      }

      const result = await response.json();

      setData(result);
      setError(false);
    } catch (err) {
      console.error("Failed to fetch server status:", err);
      setError(true);
    }
  };

  useEffect(() => {
    fetchStatus();

    const interval = setInterval(fetchStatus, 5000);

    return () => clearInterval(interval);
  }, []);

  const formatUptime = (seconds = 0) => {
    const days = Math.floor(seconds / 86400);
    const hours = Math.floor((seconds % 86400) / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);

    return `${days}d ${hours}h ${minutes}m`;
  };

  if (!data) {
    return (
      <div className="loading-screen">
        <div className="loader"></div>

        <h2>ZEK SERVER OS</h2>

        <p>
          {error
            ? "Waiting for FastAPI server..."
            : "Connecting to Samsung Galaxy M12..."}
        </p>
      </div>
    );
  }

  return (
    <div className="dashboard">
<nav className="zek-nav">
  <button
    onClick={() => setPage("dashboard")}
    className={page === "dashboard" ? "active" : ""}
  >
    Dashboard
  </button>

  <button
    onClick={() => setPage("cloud")}
    className={page === "cloud" ? "active" : ""}
  >
    Cloud
  </button>
<button
  onClick={() => setPage("chat")}
  className={page === "chat" ? "active" : ""}
>
  ZEK AI
</button>
</nav>

{page === "cloud" && <Cloud />}
{page === "chat" && <Chat />}
<div style={{ display: page === "dashboard" ? "contents" : "none" }}>

      <header className="header">
        <div>
          <p className="eyebrow">SAMSUNG GALAXY M12</p>

          <h1>ZEK SERVER OS</h1>

          <p className="subtitle">
            Personal AI Home Server
          </p>
        </div>

        <div
          className={`status ${
            data.server?.status === "online"
              ? "online"
              : "offline"
          }`}
        >
          <span className="status-dot"></span>

          {data.server?.status || "unknown"}
        </div>
      </header>


      <section className="hero">

        <div>
          <p className="hero-label">
            SYSTEM OVERVIEW
          </p>

          <h2>
            Your server is{" "}
            <span>
              {data.server?.status === "online"
                ? "online."
                : "offline."}
            </span>
          </h2>

          <p>
            Live system telemetry from your Galaxy M12.
            Automatically refreshed every 5 seconds.
          </p>
        </div>

      </section>


      <section className="metrics">

        <MetricCard
          title="CPU"
          value={`${data.cpu?.cpu_percent ?? 0}%`}
          percent={data.cpu?.cpu_percent ?? 0}
          description="Processor utilization"
        />

        <MetricCard
          title="MEMORY"
          value={`${data.memory?.percent ?? 0}%`}
          percent={data.memory?.percent ?? 0}
          description={`${data.memory?.used_mb ?? 0} MB used`}
        />

        <MetricCard
          title="STORAGE"
          value={`${data.storage?.used_gb ?? 0} GB`}
          percent={data.storage?.used_percent ?? 0}
          description={`${data.storage?.free_gb ?? 0} GB available`}
        />

        <MetricCard
          title="UPTIME"
          value={formatUptime(
            data.uptime?.uptime_seconds
          )}
          description="Continuous runtime"
        />
       <MetricCard
  title="BATTERY"
  value={`${data.battery?.percentage ?? 0}%`}
  percent={data.battery?.percentage ?? 0}
  description={
    data.battery?.status === "CHARGING"
      ? "Charging"
      : data.battery?.status === "FULL"
      ? "Fully charged"
      : "On battery"
  }
/>

<MetricCard
  title="TEMPERATURE"
  value={
    data.battery?.temperature != null
      ? `${data.battery.temperature}°C`
      : "N/A"
  }
  description={`Battery health: ${
    data.battery?.health ?? "Unknown"
  }`}
/>
      </section>


      <section className="bottom-grid">

        <div className="panel">

          <div className="panel-header">
            <div>
              <p className="panel-label">
                SERVER
              </p>

              <h3>System Details</h3>
            </div>
          </div>

          <div className="detail-row">
            <span>Device</span>
            <strong>Samsung Galaxy M12</strong>
          </div>

          <div className="detail-row">
            <span>Server</span>
            <strong>
              {data.server?.message ||
                "Server is running."}
            </strong>
          </div>

          <div className="detail-row">
            <span>Total RAM</span>
            <strong>
              {data.memory?.total_mb ?? 0} MB
            </strong>
          </div>

          <div className="detail-row">
            <span>Total Storage</span>
            <strong>
              {data.storage?.total_gb ?? 0} GB
            </strong>
          </div>

        </div>


        <div className="panel">

          <div className="panel-header">

            <div>
              <p className="panel-label">
                NETWORK
              </p>

              <h3>Connectivity</h3>
            </div>

            <span
              className={
                data.internet?.internet
                  ? "network-good"
                  : "network-bad"
              }
            >
              {data.internet?.internet
                ? "CONNECTED"
                : "OFFLINE"}
            </span>

          </div>


          <div className="network-display">

            <div className="network-icon">
              ◉
            </div>

            <div>
              <h2>
                {data.internet?.internet
                  ? "Internet Online"
                  : "No Internet"}
              </h2>

              <p>
                Galaxy M12 network connection
              </p>
            </div>

          </div>

        </div>

      </section>


      <footer>
        <span>ZEK SERVER OS</span>

        <span>
          LIVE TELEMETRY • 5 SEC REFRESH
        </span>
      </footer>
 </div> 
    </div>
  );
}


function MetricCard({
  title,
  value,
 percent,
  description,
}) {
  return (
    <div className="metric-card">

      <div className="metric-top">
        <span>{title}</span>

        <span className="live-dot"></span>
      </div>

      <h2>{value}</h2>

      <p>{description}</p>

      {percent !== undefined && (
        <div className="progress">

          <div
            className="progress-bar"
            style={{
              width: `${Math.min(
                Math.max(percent, 0),
                100
              )}%`,
            }}
          ></div>

        </div>
      )}

    </div>
  );
}

export default App;

