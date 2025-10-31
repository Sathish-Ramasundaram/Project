import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Html from './pages/HTML';
import Css from './pages/CSS';
import Javascript from './pages/JavaScript';
import ReactPage from './pages/React';

function App() {
  return (
    <Router>
      <nav style={{ display: 'flex', gap: '1rem', padding: '1rem' }}>
        <Link to="/">Home</Link>
        <Link to="/html">HTML</Link>
        <Link to="/css">CSS</Link>
        <Link to="/javascript">JavaScript</Link>
        <Link to="/react">React</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/html" element={<Html />} />
        <Route path="/css" element={<Css />} />
        <Route path="/javascript" element={<Javascript />} />
        <Route path="/react" element={<ReactPage />} />
      </Routes>
    </Router>
  );
}

export default App;
