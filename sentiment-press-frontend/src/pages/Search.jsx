import React, { useState } from 'react';
import { IoSearchCircle } from "react-icons/io5";
import { FaChevronDown } from "react-icons/fa";

const SearchBar = ({ onSearch, errorMessage }) => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const [selectedTerm, setSelectedTerm] = useState('');

  const predefinedTerms = [
    "Trump", "Politics", "Business", "Science", "Sports",
    "Entertainment", "Education", "Environment", "UK", 
    "Finance", "Music", "Movies",
    'Technology', "Stock Market", "Weather", "Crime", "Starmer",
    "War", "AI", "Rugby", 'Gaza', 'Israel', 'Russia', 'Ukraine'
  ];

  const handleTermSelect = (term) => {
    setSelectedTerm(term);
    setIsDropdownOpen(false);
    onSearch(term);
  };

  return (
    <div style={{ position: 'relative', width: '100%' }}>
      <div style={{ 
        marginBottom: '10px', 
        display: 'flex', 
        alignItems: 'center', 
        position: 'relative',
        cursor: 'pointer'
      }}>
        <button
          type="button"
          onClick={() => setIsDropdownOpen(!isDropdownOpen)}
          style={{
            width: '100%',
            padding: '10px',
            fontSize: '16px',
            textAlign: 'left',
            background: 'white',
            border: '1px solid #ddd',
            borderRadius: '4px',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center'
          }}
        >
          {selectedTerm || 'Select a topic'}
          <FaChevronDown style={{ color: '#920089' }} />
        </button>
      </div>
      
      {isDropdownOpen && (
        <div style={{
          position: 'absolute',
          top: '100%',
          left: 0,
          width: '100%',
          maxHeight: '300px',
          overflowY: 'auto',
          backgroundColor: 'white',
          border: '1px solid #ddd',
          borderRadius: '4px',
          boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
          zIndex: 10,
        }}>
          {predefinedTerms.map((term, index) => (
            <div
              key={index}
              onClick={() => handleTermSelect(term)}
              style={{
                padding: '10px',
                cursor: 'pointer',
                color: 'black',
              }}
              onMouseEnter={(e) => e.target.style.backgroundColor = '#f0f0f0'}
              onMouseLeave={(e) => e.target.style.backgroundColor = 'white'}
            >
              {term}
            </div>
          ))}
        </div>
      )}

      {errorMessage && (
        <div style={{ color: 'red', fontSize: '14px', marginTop: '8px' }}>
          {errorMessage}
        </div>
      )}
    </div>
  );
};

export default SearchBar;
