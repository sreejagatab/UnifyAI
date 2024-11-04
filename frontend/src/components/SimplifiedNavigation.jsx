// SimplifiedNavigation.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import { useUserRole } from '../utils/auth';

function SimplifiedNavigation() {
  const role = useUserRole();

  return (
    <nav aria-label="Main Navigation">
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/dashboard">Dashboard</Link></li>
        {role === 'admin' && <li><Link to="/admin">Admin Panel</Link></li>}
        <li><Link to="/models">AI Models</Link></li>
        <li><Link to="/support">Support</Link></li>
      </ul>
    </nav>
  );
}

export default SimplifiedNavigation;
