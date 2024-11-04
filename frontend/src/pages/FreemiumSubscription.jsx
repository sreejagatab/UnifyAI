// FreemiumSubscription.jsx
import React from 'react';
import { useHistory } from 'react-router-dom';

function FreemiumSubscription() {
  const history = useHistory();

  const handleUpgradeClick = () => {
    history.push('/pricing');
  };

  return (
    <div>
      <h2>Freemium Tier</h2>
      <p>
        Get started with our free features. Upgrade to unlock premium features like advanced API access, priority support, and exclusive AI models.
      </p>
      <ul>
        <li>✔ Basic Workflow Builder</li>
        <li>✔ Limited AI Model Access</li>
        <li>✔ Community Support</li>
        <li>❌ Priority Support</li>
        <li>❌ Advanced API Access</li>
      </ul>
      <button onClick={handleUpgradeClick}>Upgrade to Premium</button>
    </div>
  );
}

export default FreemiumSubscription;
