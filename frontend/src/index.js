import React from "react";
import ReactDOM from "react-dom/client";

function App() {
  return (
    <div style={{ fontFamily: "Arial", padding: "40px" }}>
      <h1>Plateforme React / Flask / PostgreSQL / Adminer</h1>
      <p>Frontend React déployé sur Render</p>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
