import { useState } from "react";

function App() {
  const [message, setMessage] = useState("Hello, Sathish");

  return (
    <div>
      <p>{message}</p>
      <button onClick={() => setMessage("You clicked the button!")}>click me</button>
    </div>
  );
}

export default App;