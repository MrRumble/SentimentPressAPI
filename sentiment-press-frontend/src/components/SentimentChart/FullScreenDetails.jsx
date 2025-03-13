import React from 'react';

const FullScreenDetails = ({ date, sentiment, summary, onClose }) => {
  const formattedDate = new Intl.DateTimeFormat("en-GB", {
    weekday: "short",
    year: "numeric",
    month: "short",
    day: "numeric",
  }).format(new Date(date));

  return (
    <div
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100vw',
        height: '100vh',
        background: 'rgba(0, 0, 0, 0.9)',
        color: 'white',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 2000,
        flexDirection: 'column',
        padding: '20px',
      }}
    >
      <h1>Sentiment Details</h1>
      <p><strong>Date:</strong> {formattedDate}</p>
      <p><strong>Sentiment Score:</strong> {sentiment}</p>
      <p><strong>Summary:</strong> {summary}</p>
      <button 
        onClick={onClose} 
        style={{
          marginTop: '20px',
          background: 'transparent',
          color: 'white',
          border: '1px solid white',
          padding: '10px',
          cursor: 'pointer',
        }}>
        Close
      </button>
    </div>
  );
};

export default FullScreenDetails;
