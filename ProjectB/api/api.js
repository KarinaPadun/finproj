import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

export const getPatients = () => {
  return api.get('/patients/')
    .then(response => response.data)
    .catch(error => console.error(error));
};

export const createPatient = (patientData) => {
  return api.post('/patients/', patientData)
    .then(response => response.data)
    .catch(error => console.error(error));
};
