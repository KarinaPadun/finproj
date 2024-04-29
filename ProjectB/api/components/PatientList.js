import React from 'react';
import { getPatients } from './api';

const PatientList = () => {
  const [patients, setPatients] = React.useState([]);

  React.useEffect(() => {
    getPatients()
      .then(data => setPatients(data));
  }, []);

  const patientList = patients.map(patient => (
    <li key={patient.id}>{patient.name}</li>
  ));

  return (
    <ul>{patientList}</ul>
  );
};

export default PatientList;
