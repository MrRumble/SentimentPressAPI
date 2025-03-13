import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Homepage from './pages/Home';
import LandingPage from './pages/Landing';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/home" element={<Homepage />} /> 
          <Route path='/' element={<LandingPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;