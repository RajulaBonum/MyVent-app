// src/App.js
import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
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
            {/* Navigation Menu */}
            <nav className="navbar">
                <Link to="/" className="nav-link">Home</Link>
                <Link to="/events" className="nav-link">Events</Link>
                <Link to="/profile" className="nav-link">Profile</Link>
                <Link to="/rsvp-management" className="nav-link">RSVP Management</Link>
                <Link to="/contact" className="nav-link">Contact</Link>
                <Link to="/about" className="nav-link">About</Link>
                <Link to="/analytics" className="nav-link">Analytics</Link>
            </nav>

            {/* Route Definitions */}
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/events" element={<EventList />} />
                <Route path="/event/:id" element={<EventDetail />} />  {/* Dynamic Route Example */}
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
