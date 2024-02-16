from . import hospital
from odoo import models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    # Otros campos del modelo
    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    birthday = fields.Date(string='Birthday')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Here you can find all appointment of the patient'
  
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor_id')
    patient_id = fields.Many2one('hospital.patient', string='Patient_id')
    appointment_state = fields.Selection([('pending', 'Pending',),('confirmed','Confirmed'),('cancelled','Cancelled',),('resolved','Resolved')], required=True, string='appointment_state')

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Here you can find all information about the doctors of the hospital'
  
    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name',required=True)
    specialty = fields.Char(string='Specualty', required=True)
   

