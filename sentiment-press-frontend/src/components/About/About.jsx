import React from 'react';

const About = () => {
  return (
    <div style={{ textAlign: 'left', fontSize: '18px', maxWidth: '700px', margin: 'auto' }}>
      <h2>Stay Informed with Sentiment Analysis</h2>
      <p>
        Want to understand the news sentiment around a topic? Our platform analyzes 
        <strong> 100 news articles from yesterday</strong>, processes the data, and generates a 
        <strong> sentiment score</strong> to reveal the overall tone.
      </p>

      <p><strong>🔍 Search any term to discover:</strong></p>
      <ul style={{ textAlign: 'left', display: 'inline-block' }}>
        <li>📌 A smart summary of yesterday’s news coverage</li>
        <li>📊 The <strong>top 3</strong> and <strong>bottom 3</strong> articles ranked by sentiment</li>
        <li>📈 A trend chart tracking sentiment over time</li>
        <li>📊 Side-by-side comparisons of multiple search terms</li>
      </ul>

      <p><strong>Stay ahead with real-time sentiment insights!</strong></p>

      <p>
        Explore the <a 
          href="https://github.com/MrRumble/SentimentPressV2" 
          target="_blank" 
          rel="noopener noreferrer" 
          style={{ color: 'purple', fontWeight: 'bold', fontStyle: 'italic' }}
        >
          SentimentPress GitHub Repository
        </a> for a comprehensive technical rundown of the project, including a full explanation of the development process. It's a great showcase of my work and how I tackled various challenges throughout the project.
      </p>

      <p style={{ marginTop: '0px', fontSize: '14px' }}>
        Created by <a 
          href="https://github.com/MrRumble" 
          target="_blank" 
          rel="noopener noreferrer" 
          style={{ color: 'purple', fontWeight: 'bold' }}
        >
          James Rumble
        </a>
      </p>
    </div>
  );
};

export default About;
