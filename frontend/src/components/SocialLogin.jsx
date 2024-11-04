// SocialLogin.jsx
import React from 'react';
import { useHistory } from 'react-router-dom';
import { loginWithProvider } from '../utils/auth';

function SocialLogin() {
  const history = useHistory();

  const handleLogin = async (provider) => {
    try {
      const redirectUrl = await loginWithProvider(provider);
      window.location.href = redirectUrl;
    } catch (error) {
      console.error("Login failed:", error);
      alert("Authentication failed, please try again.");
    }
  };

  return (
    <div>
      <button onClick={() => handleLogin('google')}>Login with Google</button>
      <button onClick={() => handleLogin('facebook')}>Login with Facebook</button>
      <button onClick={() => handleLogin('github')}>Login with GitHub</button>
    </div>
  );
}

export default SocialLogin;
