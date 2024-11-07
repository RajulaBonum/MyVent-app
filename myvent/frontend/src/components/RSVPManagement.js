// src/components/RSVPManagement.js
import React, { useState } from 'react';
import './RSVPManagement.css';

const RSVPManagement = ({ rsvpList }) => {
    const [searchTerm, setSearchTerm] = useState('');

    const filteredRSVPs = rsvpList.filter(rsvp =>
        rsvp.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    return (
        <div className="rsvp-management">
            <h2>RSVP Management</h2>
            <input
                type="text"
                placeholder="Search RSVP"
                className="form-control search-input"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
            />
            <ul className="rsvp-list">
                {filteredRSVPs.map((rsvp, index) => (
                    <li key={index} className="rsvp-item">
                        <p><strong>Name:</strong> {rsvp.name}</p>
                        <p><strong>Event:</strong> {rsvp.event}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RSVPManagement;
