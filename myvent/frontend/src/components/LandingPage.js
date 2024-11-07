// src/components/LandingPage.js
import React from 'react';
import './LandingPage.css';

const LandingPage = () => {
    return (
        <div className="landing-page">
            <header className="hero-section">
                <h1>Welcome to MyVent</h1>
                <p>Discover and manage amazing events!</p>
                <button className="btn-primary">Get Started</button>
            </header>
        </div>
    );
};

export default LandingPage;
