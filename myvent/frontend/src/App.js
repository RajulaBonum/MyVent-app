// src/App.js
import React from 'react';
import { Routes, Route, NavLink } from 'react-router-dom'; // Using NavLink for active styling
import LandingPage from './components/LandingPage';
import EventList from './components/EventList';
import EventDetail from './components/EventDetail';
import RSVPManagement from './components/RSVPManagement';
import Profile from './components/Profile';
import Contact from './components/Contact';
import About from './components/About';
import EventAnalytics from './components/EventAnalytics';

const App = () => {
    return (
        <div>
            {/* Bootstrap Navigation Bar */}
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container-fluid">
                    <NavLink className="navbar-brand" to="/">MyVent</NavLink>
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarNav"
                        aria-controls="navbarNav"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/">Home</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/events">Events</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/profile">Profile</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/rsvp-management">RSVP Management</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/contact">Contact</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/about">About</NavLink>
                            </li>
                            <li className="nav-item">
                                <NavLink className="nav-link" to="/analytics">Analytics</NavLink>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            {/* Route Definitions */}
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/events" element={<EventList />} />
                <Route path="/event/:id" element={<EventDetail />} />
                <Route path="/profile" element={<Profile />} />
                <Route path="/rsvp-management" element={<RSVPManagement />} />
                <Route path="/contact" element={<Contact />} />
                <Route path="/about" element={<About />} />
                <Route path="/analytics" element={<EventAnalytics />} />
            </Routes>
        </div>
    );
};

export default App;
