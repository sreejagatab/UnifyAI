// LandingPage.jsx
import React from 'react';
import { useHistory } from 'react-router-dom';

function LandingPage() {
  const history = useHistory();

  const handleGetStarted = () => {
    history.push('/signup');
  };

  return (
    <div>
      <header>
        <h1>Welcome to UnifyAI</h1>
        <p>Experience seamless AI-driven automation and real-time intelligence for all industries.</p>
      </header>
      <section>
        <h2>Key Features</h2>
        <ul>
          <li>Multi-LLM Integration for superior accuracy</li>
          <li>No-Code Workflow Builder for easy automation</li>
          <li>AI-Powered Recommendations and Analytics</li>
          <li>Real-Time Collaboration for team efficiency</li>
        </ul>
      </section>
      <button onClick={handleGetStarted}>Get Started</button>
    </div>
  );
}

export default LandingPage;
