import { useEffect, useState } from "react";

const API = "";
const ROOT = "/storage/emulated/0";

export default function Cloud() {
  const [path, setPath] = useState(ROOT);
  const [folders, setFolders] = useState([]);
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadFiles = async (targetPath) => {
    setLoading(true);
    setError("");

    try {
      const response = await fetch(
        `${API}/files/?path=${encodeURIComponent(targetPath)}`
      );

      if (!response.ok) {
        throw new Error("Unable to load files");
      }

      const data = await response.json();

      if (data.error) {
        throw new Error(data.error);
      }

      setPath(targetPath);
      setFolders(data.folders || []);
      setFiles(data.files || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadFiles(ROOT);
  }, []);

  const openFolder = (name) => {
    loadFiles(`${path}/${name}`);
  };

  const goBack = () => {
    if (path === ROOT) return;

    const parent = path.substring(0, path.lastIndexOf("/"));

    if (parent.startsWith(ROOT)) {
      loadFiles(parent);
    } else {
      loadFiles(ROOT);
    }
  };

  const downloadFile = (name) => {
    const fullPath = `${path}/${name}`;

    window.location.href =
      `${API}/download/?path=${encodeURIComponent(fullPath)}`;
  };

  return (
    <div className="cloud-page">

      <div className="cloud-header">
        <div>
          <p className="eyebrow">GALAXY M12 STORAGE</p>
          <h1>ZEK CLOUD</h1>
          <p className="subtitle">
            Access files stored on your personal server.
          </p>
        </div>
      </div>

      <div className="cloud-toolbar">
        <button
          onClick={goBack}
          disabled={path === ROOT}
        >
          ← Back
        </button>

        <span>{path.replace(ROOT, "My Storage")}</span>
      </div>

      {loading && (
        <div className="cloud-message">
          Loading storage...
        </div>
      )}

      {error && (
        <div className="cloud-message">
          {error}
        </div>
      )}

      {!loading && !error && (
        <div className="cloud-list">

          {folders.map((folder) => (
            <button
              className="cloud-item"
              key={`folder-${folder}`}
              onClick={() => openFolder(folder)}
            >
              <span className="cloud-icon">📁</span>

              <div>
                <strong>{folder}</strong>
                <small>Folder</small>
              </div>

              <span>›</span>
            </button>
          ))}

          {files.map((file) => (
            <div
              className="cloud-item"
              key={`file-${file}`}
            >
              <span className="cloud-icon">📄</span>

              <div className="cloud-file-name">
                <strong>{file}</strong>
                <small>File</small>
              </div>

              <button
                className="download-button"
                onClick={() => downloadFile(file)}
              >
                ↓
              </button>
            </div>
          ))}

          {folders.length === 0 && files.length === 0 && (
            <div className="cloud-message">
              This folder is empty.
            </div>
          )}

        </div>
      )}

    </div>
  );
}
