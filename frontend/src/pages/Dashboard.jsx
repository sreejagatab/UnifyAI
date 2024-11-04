// Dashboard.jsx
import React from 'react';
import { Link } from 'react-router-dom';

function Dashboard() {
  return (
    <div>
      <h2>Dashboard</h2>
      <p>Access your models, workflows, and analytics in one place.</p>
      <ul>
        <li><Link to="/models">Manage AI Models</Link></li>
        <li><Link to="/usage">Track API Usage</Link></li>
        <li><Link to="/workflows">Create Workflow</Link></li>
        <li><Link to="/analytics">View Analytics</Link></li>
      </ul>
    </div>
  );
}

export default Dashboard;
