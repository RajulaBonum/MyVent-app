// src/components/Contact.js
import React from 'react';
import './Contact.css';

const Contact = () => {
    return (
        <div className="contact-page">
            <h2>Contact Us</h2>
            <form className="contact-form">
                <input type="text" placeholder="Your Name" className="form-control" />
                <input type="email" placeholder="Your Email" className="form-control" />
                <textarea placeholder="Your Message" className="form-control"></textarea>
                <button type="submit" className="btn-primary">Send Message</button>
            </form>
        </div>
    );
};

export default Contact;
