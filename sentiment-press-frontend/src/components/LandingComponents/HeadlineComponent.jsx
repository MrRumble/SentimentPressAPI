import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import "./Headline.css";

const Headlines = () => {
  const [headlines, setHeadlines] = useState([]);
  const [currentHeadline, setCurrentHeadline] = useState(null);

  const getYesterdayDate = () => {
    const today = new Date();
    today.setDate(today.getDate() - 1);  
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return today.toLocaleDateString('en-US', options); 
  };

  useEffect(() => {
    const fetchHeadlines = async () => {
      try {
        const baseURL = process.env.REACT_APP_API_BASE_URL;
        const response = await fetch(`${baseURL}/api/get-headlines`, {
          method: 'GET', 
          headers: {
            'Content-Type': 'application/json',
          },
        });
        const data = await response.json();
        setHeadlines(data.headlines); 
      } catch (error) {
        console.error("Error fetching headlines:", error);
      }
    };

    fetchHeadlines();
  }, []);  

  useEffect(() => {
    const intervalId = setInterval(() => {
      if (headlines.length > 0) {
        const randomIndex = Math.floor(Math.random() * headlines.length);
        setCurrentHeadline(headlines[randomIndex]);
      }
    }, 6000); 

    return () => clearInterval(intervalId);
  }, [headlines]);  

  return (
    <div className="headline-container">
      <AnimatePresence>
        {currentHeadline && (
          <motion.div
            key={currentHeadline.main_headline}  
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.5 }} 
            className="headline"
          >
            <p><strong>Yesterday's Headlines:</strong> <i>{getYesterdayDate()}</i></p> 
            <h2 style={{ color: '#920089', fontSize: "2.5rem" }}><i>{currentHeadline.search_term}</i></h2> 
            <p><i>{currentHeadline.main_headline}</i></p> 
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default Headlines;
