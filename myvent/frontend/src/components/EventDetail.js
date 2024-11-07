// src/components/EventDetail.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './EventDetail.css'; // Assuming this file contains styles for the component

const EventDetail = ({ events }) => {
    const { id } = useParams(); // Retrieve the dynamic parameter from the URL
    const [event, setEvent] = useState(null);

    // Find the event based on the ID (this assumes `events` is an array passed as a prop)
    useEffect(() => {
        if (events) {
            const foundEvent = events.find((e) => e.id === parseInt(id));
            setEvent(foundEvent);
        }
    }, [id, events]);

    if (!event) {
        return <p>Loading event details...</p>; // Display a loading message while fetching event data
    }

    return (
        <div className="event-detail">
            <h2>{event.title}</h2>
            <p><strong>Date:</strong> {event.date}</p>
            <p><strong>Location:</strong> {event.location}</p>
            <p>{event.description}</p>
            <button className="btn-primary">RSVP</button>
        </div>
    );
};

export default EventDetail;
