import React, { useState, useEffect } from "react";

const TopSearchTerm = () => {
  const [topSearch, setTopSearch] = useState({ term: "", count: 0 });

  useEffect(() => {
    const fetchTopSearch = async () => {
      try {
        const baseURL = process.env.REACT_APP_API_BASE_URL;
        const response = await fetch(`${baseURL}/api/get-todays-top-search`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        const data = await response.json();

        if (data.term) {
          setTopSearch({ term: data.term, count: data.count });
        } else {
          setTopSearch({ term: "No searches today", count: 0 });
        }
      } catch (error) {
        console.error("Error fetching top search term:", error);
      }
    };

    fetchTopSearch();

  }, []); 

  return (
    <div className="top-search-container">
      <h3 style={{ display: "inline", marginRight: "10px" }}>Today's Top Search:</h3>
      <span style={{ fontSize: "24px", fontWeight: "bold", marginRight: "10px", color: "purple" }}>
        <i>{topSearch.term.charAt(0).toUpperCase() + topSearch.term.slice(1)}</i>
      </span>
      <span style={{ fontSize: "18px" }}>
        - <strong>{topSearch.count} searches</strong>
      </span>
    </div>
  );
};

export default TopSearchTerm;
