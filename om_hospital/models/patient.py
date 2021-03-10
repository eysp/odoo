from odoo import models, fields, api



class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient records'

    patient_name = fields.Char(string='Name' required='True')
    patient_age = fields.Integer('age')
