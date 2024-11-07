// src/components/EventList.js
import React from 'react';
import './EventList.css';

const EventList = ({ events }) => {
    return (
        <div className="event-list">
            <h2>Upcoming Events</h2>
            <div className="events-grid">
                {events.map(event => (
                    <div className="event-card" key={event.id}>
                        <h3>{event.title}</h3>
                        <p>{event.description}</p>
                        <button className="btn-primary">View Details</button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default EventList;
