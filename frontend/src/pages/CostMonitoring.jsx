// CostMonitoring.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CostMonitoring() {
  const [costData, setCostData] = useState([]);

  useEffect(() => {
    axios.get('/api/cost_data')
      .then(response => setCostData(response.data))
      .catch(error => console.error('Error fetching cost data:', error));
  }, []);

  return (
    <div>
      <h3>Cloud Cost Monitoring</h3>
      <table>
        <thead>
          <tr>
            <th>Month</th>
            <th>Cost ($)</th>
          </tr>
        </thead>
        <tbody>
          {costData.map((cost, index) => (
            <tr key={index}>
              <td>{cost.month}</td>
              <td>{cost.amount}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default CostMonitoring;
