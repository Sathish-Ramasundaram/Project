import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import HTMLPage from './pages/HTMLPage';
import CSSPage from './pages/CSSPage';
import JavaScriptPage from './pages/JavaScriptPage';
import ReactPage from './pages/ReactPage';

function App() {
  return (
    <Router>
      <nav style={{ padding: '1rem', background: '#eee' }}>
        <Link to="/" style={{ marginRight: '1rem' }}>Home</Link>
        <Link to="/html" style={{ marginRight: '1rem' }}>HTML</Link>
        <Link to="/css" style={{ marginRight: '1rem' }}>CSS</Link>
        <Link to="/javascript" style={{ marginRight: '1rem' }}>JavaScript</Link>
        <Link to="/react" style={{ marginRight: '1rem' }}>React</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/html" element={<HTMLPage />} />
        <Route path="/css" element={<CSSPage />} />
        <Route path="/javascript" element={<JavaScriptPage />} />
        <Route path="/react" element={<ReactPage />} />
      </Routes>
    </Router>
  );
}

export default App;
