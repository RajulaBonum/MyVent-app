// src/components/Login.js
import React from 'react';
import './Login.css';

const Login = () => {
    return (
        <div className="login-form">
            <h2>Login</h2>
            <form>
                <input type="email" placeholder="Email" className="form-control" />
                <input type="password" placeholder="Password" className="form-control" />
                <button type="submit" className="btn-primary">Login</button>
            </form>
        </div>
    );
};

export default Login;
