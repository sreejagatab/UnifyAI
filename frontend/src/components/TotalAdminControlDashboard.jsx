import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TotalAdminControlDashboard() {
  const [metrics, setMetrics] = useState({});

  useEffect(() => {
    axios.get('/api/admin_dashboard')
      .then(response => setMetrics(response.data))
      .catch(error => console.error('Error fetching admin data', error));
  }, []);

  return (
    <div>
      <h2>Total Admin Control Dashboard</h2>
      <div>
        <h3>Cloud Resource Usage</h3>
        <p>CPU Usage: {metrics.cloud_metrics?.cpu_usage}%</p>
        <p>Memory Usage: {metrics.cloud_metrics?.memory_usage}%</p>
        <p>Cloud Costs: ${metrics.cloud_metrics?.cloud_costs}</p>
      </div>
      <div>
        <h3>Error Logs</h3>
        <ul>
          {metrics.error_logs?.map((error, index) => (
            <li key={index}>{error}</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Audit Logs</h3>
        <ul>
          {metrics.audit_logs?.map((log, index) => (
            <li key={index}>{log}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default TotalAdminControlDashboard;
