import React, { useState, useEffect } from 'react';
import './Home.css';
import GlobeComponent from '../components/Globe/Globe';
import QueryComponent from '../components/QueryComponent/QueryComponent';
import SentimentChart from '../components/SentimentChart/SentimentChart';
import { useRefresh } from './RefreshContext';
import { useLocation } from 'react-router-dom';

const Homepage = () => {
  const location = useLocation();
  const [searchTerm, setSearchTerm] = useState('');
  const [isInitialLoad, setIsInitialLoad] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');
  const { triggerRefresh } = useRefresh();

  useEffect(() => {
    // Extract search term from URL on initial load
    const searchParams = new URLSearchParams(location.search);
    const urlSearchTerm = searchParams.get('search');
    
    if (urlSearchTerm) {
      setSearchTerm(urlSearchTerm);
      setIsInitialLoad(false);
    }
  }, [location.search]);

  const handleSearch = (term) => {
    // Validate the search term
    if (term.trim()) {
      setSearchTerm(term);
      setErrorMessage(''); // Clear any previous errors
      triggerRefresh();
    } else {
      setErrorMessage('Query cannot be empty!');
    }
    setIsInitialLoad(false);
  };

  return (
    <div className="homepage">
      <div className="right-column">
        <div className="top-row">
          <div className="spinning-globe">
            <GlobeComponent position={[0, 0, 0]} scale={[2, 2, 2]} />
          </div>
          <div className="website-name">
            Sentiment Press
          </div>
        </div>
        <div className="bottom-row">
          <SentimentChart searchTerm={searchTerm} />
        </div>
        <div className="third-row">

        </div>
      </div>

      <div className="left-column">
        <QueryComponent 
          onSearch={handleSearch} 
          query={searchTerm} 
          errorMessage={errorMessage}  
        />
      </div>
    </div>
  );
};

export default Homepage;
