import React, { useState } from "react";
import { Button, Form, Modal } from "react-bootstrap";
import { BsCash } from "react-icons/bs";
import { useUser } from "../../../UserContext";
import axios from "axios";

const MakeTransaction = ({ setSuccessMessage, setShowOverlay }) => {
  const [show, setShow] = useState(false);
  const {username} = useUser();
  const [payeeName, setPayeeName] = useState('');
  const [amountPayed, setAmountPayed] = useState('');

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const makeTransaction = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/make_transaction/', {
        username,
        payeeName,
        amountPayed
      });
      if (response.data.success) {
        setSuccessMessage("Transferred Succesfully")
      } else {
        setSuccessMessage("Transfer Failed")
      }
    } catch (error) {
      console.error('Transaction Failed: Server-Side Error:', error);
    }
    setShowOverlay(true);
    setTimeout(() => setShowOverlay(false), 10000);
  };

  return (
    <>
      <Button variant="outline-info" onClick={handleShow}>
        <BsCash className="icon"></BsCash>
        Make Transaction
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Make Transaction</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={makeTransaction}>
            <Form.Group className="mb-3">
              <Form.Label>Transfer To:</Form.Label>
              <Form.Control 
                type="text"
                value={payeeName}
                onChange={e => setPayeeName(e.target.value)}
              />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Transfer Amount:</Form.Label>
              <Form.Control 
                type="text"
                value={amountPayed}
                onChange={e => setAmountPayed(e.target.value)}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="primary" type="submit" onClick={handleClose}>
            Submit
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default MakeTransaction;
