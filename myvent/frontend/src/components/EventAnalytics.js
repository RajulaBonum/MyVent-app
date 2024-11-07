// src/components/EventAnalytics.js
import React from 'react';
import './EventAnalytics.css';

const EventAnalytics = () => {
    // Example data for demonstration purposes
    const analyticsData = [
        { event: 'Event A', attendees: 150 },
        { event: 'Event B', attendees: 200 },
        { event: 'Event C', attendees: 100 }
    ];

    return (
        <div className="analytics-page">
            <h2>Event Analytics</h2>
            <div className="analytics-grid">
                {analyticsData.map((data, index) => (
                    <div className="analytics-card" key={index}>
                        <p><strong>Event:</strong> {data.event}</p>
                        <p><strong>Attendees:</strong> {data.attendees}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default EventAnalytics;
