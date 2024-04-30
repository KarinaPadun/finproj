import axios from 'axios';

// Получить список пациентов
const getPatients = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/patients/');
    const patients = response.data;
    console.log(patients);
  } catch (error) {
    console.error(error);
  }
};

// Получить запись пациента по ID
const getPatient = async (id) => {
  try {
    const response = await axios.get(`http://localhost:8000/api/patients/${id}/`);
    const patient = response.data;
    console.log(patient);
  } catch (error) {
    console.error(error);
  }
};

// Создать новую запись пациента
const createPatient = async (patientData) => {
  try {
    const response = await axios.post('http://localhost:8000/api/patients/', patientData);
    const newPatient = response.data;
    console.log(newPatient);
  } catch (error) {
    console.error(error);
  }
};

// Обновить запись пациента
const updatePatient = async (id, patientData) => {
  try {
    const response = await axios.put(`http://localhost:8000/api/patients/${id}/`, patientData);
    const updatedPatient = response.data;
    console.log(updatedPatient);
  } catch (error) {
    console.error(error);
  }
};

// Удалить запись пациента
const deletePatient = async (id) => {
  try {
    await axios.delete(`http://localhost:8000/api/patients/${id}/`);
    console.log(`Patient with ID ${id} deleted`);
  } catch (error) {
    console.error(error);
  }
};


