// RealTimeDashboard.jsx

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function RealTimeDashboard() {
  const [data, setData] = useState({});

  useEffect(() => {
    axios.get('/api/admin_dashboard')
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => console.log('Error fetching data', error));
  }, []);

  return (
    <div>
      <h2>Real-Time Dashboard</h2>
      <div>
        <h3>Cloud Metrics</h3>
        <p>CPU: {data.cloud_metrics?.cpu_usage}%</p>
        <p>Memory: {data.cloud_metrics?.memory_usage}%</p>
      </div>
      <div>
        <h3>Errors</h3>
        <ul>
          {data.error_logs?.map((error, index) => (
            <li key={index}>{error}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default RealTimeDashboard;
