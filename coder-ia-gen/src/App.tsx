import { useState, useEffect } from 'react';

function App() {
  const [count, setCount] = useState<number | null>(null);

  const fetchCount = async () => {
    const res = await fetch('http://localhost:8000/count');
    const data = await res.json();
    setCount(data.count);
  };

  const resetCount = async () => {
    const res = await fetch('http://localhost:8000/count/reset', { method: 'POST' });
    const data = await res.json();
    setCount(data.count);
  };

  const incrementCount = async () => {
    const res = await fetch('http://localhost:8000/count/increment', { method: 'POST' });
    const data = await res.json();
    setCount(data.count);
  };

  useEffect(() => {
    fetchCount();
  }, []);

  return (
    <div>
      <h1>Compteur : {count !== null ? count : 'Chargement...'}</h1>
  <button onClick={incrementCount}>Incrémenter</button>
  <button onClick={resetCount}>Remettre à zéro</button>
    </div>
  );
}

export default App;