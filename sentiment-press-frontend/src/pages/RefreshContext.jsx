// RefreshContext.js
import React, { createContext, useState, useContext } from 'react';

const RefreshContext = createContext();

export const RefreshProvider = ({ children }) => {
  const [refreshKey, setRefreshKey] = useState(0);

  const triggerRefresh = () => {
    setRefreshKey(prev => prev + 1);
  };

  return (
    <RefreshContext.Provider value={{ refreshKey, triggerRefresh }}>
      {children}
    </RefreshContext.Provider>
  );
};

export const useRefresh = () => useContext(RefreshContext);