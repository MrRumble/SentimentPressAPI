import React, { useState, useEffect } from "react";

const SentimentDisplay = () => {
  const [highestSentiment, setHighestSentiment] = useState(null);
  const [lowestSentiment, setLowestSentiment] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Function to fetch sentiment data from the backend
  const fetchSentimentData = async () => {
    try {
      const baseURL = process.env.REACT_APP_API_BASE_URL;

      // Fetch the highest and lowest sentiment data in parallel
      const [highRes, lowRes] = await Promise.all([
        fetch(`${baseURL}/api/get-highest-sentiment-today`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }),
        fetch(`${baseURL}/api/get-lowest-sentiment-today`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }),
      ]);

      // Check if responses are okay
      if (!highRes.ok || !lowRes.ok) {
        throw new Error("Failed to fetch sentiment data");
      }

      // Parse the JSON responses
      const highestData = await highRes.json();
      const lowestData = await lowRes.json();
      console.log("Highest Sentiment Data:", highestData);
      console.log("Lowest Sentiment Data:", lowestData);

      // Set the sentiment state
      setHighestSentiment(highestData.term ? highestData : null);
      setLowestSentiment(lowestData.term ? lowestData : null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSentimentData();
  }, []);

  if (loading) return <p>Loading sentiment data...</p>;
  if (error) return <p style={{ color: "red" }}>Error: {error}</p>;

  return (
    <div style={{ display: "flex", justifyContent: "space-between", gap: "20px" }}>
      {/* Highest Sentiment Column */}
      <div style={{ flex: 1, padding: "20px", border: "1px solid #ccc", borderRadius: "10px" }}>
        <h3>Highest Sentiment Today</h3>
        {highestSentiment ? (
          <div>
            <p><strong>Term:</strong> {highestSentiment.term || "N/A"}</p>
            <p><strong>Score:</strong> {highestSentiment.sentiment_score || "N/A"}</p>
            <p><strong>Summary:</strong> {highestSentiment.summary || "N/A"}</p>
          </div>
        ) : (
          <p>No data available</p>
        )}
      </div>

      {/* Lowest Sentiment Column */}
      <div style={{ flex: 1, padding: "20px", border: "1px solid #ccc", borderRadius: "10px" }}>
        <h3>Lowest Sentiment Today</h3>
        {lowestSentiment ? (
          <div>
            <p><strong>Term:</strong> {lowestSentiment.term || "N/A"}</p>
            <p><strong>Score:</strong> {lowestSentiment.sentiment_score || "N/A"}</p>
            <p><strong>Summary:</strong> {lowestSentiment.summary || "N/A"}</p>
          </div>
        ) : (
          <p>No data available</p>
        )}
      </div>
    </div>
  );
};

export default SentimentDisplay;
