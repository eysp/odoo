from odoo import models, fields, api



class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient records'

    patient_name = feilds.Char(string='Patient Name')
