import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { useUser } from '../UserContext';
import { Button } from 'react-bootstrap';

const LogoutButton = () => {    
  const navigate = useNavigate();
  const {user_logout, token, username} = useUser();

  const handleClick = async (e) => {
    e.preventDefault();
    // Create Request Form
    const formData = new FormData();
    formData.append('username', username);
    // Send Request Form
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/logout/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: token
          }
        }
      );
      // Handle Response
      if (response.data.success) {
        user_logout()
        navigate("/");
      } else {
        console.log("Logout failed: Server-Side Error")
      }
    } catch (error) {
      console.error('Transaction Failed: Server-Side Error:', error);
    }
  };

  return (
    <Button variant='danger' size='sm' onClick={handleClick}>Logout</Button>
  );
};

export default LogoutButton;