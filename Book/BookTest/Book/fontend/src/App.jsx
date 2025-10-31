import { useState, useEffect } from 'react';

function App() {
  const [pageId, setPageId] = useState(1);
  const [page, setPage] = useState({ title: '', content: '' });

  useEffect(() => {
    fetch(`http://localhost:5000/getPage?id=${pageId}`)
      .then(res => res.json())
      .then(data => setPage(data));
  }, [pageId]);

  return (
    <div style={{ whiteSpace: 'pre-line', padding: '20px'  }}>
      <h2>{page.title}</h2>
      <div>{page.content}</div>
      <button onClick={() => setPageId(p => Math.max(p - 1, 1))}>Previous</button>
      <button onClick={() => setPageId(p => p + 1)}>Next</button>
    </div>
  );
}

export default App;
