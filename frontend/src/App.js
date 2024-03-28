import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';
import {Deploy} from './Component/Deploy/Deploy';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = () => {
    fetch('/api')
      .then(response => {
        if (response.status === 200) {
          return response.json();
        }
        throw new Error('Request failed.');
      })
      .then(data => {
        setData(data);
      })
      .catch(error => {
        console.error(error);
      });
  };



  return (
    <div>
      <h1>React Flask App</h1>
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
}

export default App;
