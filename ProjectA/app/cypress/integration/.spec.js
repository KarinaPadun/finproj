// cypress/integration/appointment-scheduling.spec.js

describe('Appointment Scheduling', () => {
  it('should allow scheduling a new appointment', () => {
    cy.visit('/schedule-appointment');
    cy.get('#patientName').type('John Doe');
    cy.get('#patientEmail').type('johndoe@example.com');
    cy.get('#doctorSelect').select('Dr. Smith');
    cy.get('#appointmentDate').type('2024-05-10');
    cy.get('#appointmentTime').type('10:00');
    cy.get('#appointmentType').select('Video Call');
    cy.get('button[type="submit"]').click();
    cy.get('.success-message').should('contain', 'Appointment scheduled successfully');
  });
});
