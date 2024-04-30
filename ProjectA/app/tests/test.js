// PatientForm.test.js

import React from 'react';
import { render, screen } from '@testing-library/react';
import PatientForm from './PatientForm';

test('PatientForm renders correctly', () => {
  render(<PatientForm />);
  const nameInput = screen.getByLabelText('Name');
  const emailInput = screen.getByLabelText('Email');
  expect(nameInput).toBeInTheDocument();
  expect(emailInput).toBeInTheDocument();
});

test('PatientForm handles name input change', () => {
  const { getByLabelText } = render(<PatientForm />);
  const nameInput = getByLabelText('Name');
  fireEvent.change(nameInput, { target: { value: 'John Doe' } });
  expect(nameInput.value).toBe('John Doe');
});
