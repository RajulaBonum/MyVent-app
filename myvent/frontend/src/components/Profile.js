// src/components/Profile.js
import React from 'react';
import './Profile.css';

const Profile = ({ user }) => {
    return (
        <div className="profile-page">
            <h2>User Profile</h2>
            <div className="profile-card">
                <p><strong>Name:</strong> {user.name}</p>
                <p><strong>Email:</strong> {user.email}</p>
                <button className="btn-primary">Edit Profile</button>
            </div>
        </div>
    );
};

export default Profile;
