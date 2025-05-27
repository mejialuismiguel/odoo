from odoo import models, fields


class GradesCourse(models.Model):
    _name = 'grades.course'
    _description = 'Grades Course'
    _order = 'name'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    student_qty = fields.Integer(string='Student quantity')
    grades_averages = fields.Float(string='Grades averages')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Active', default=True)
    course_start = fields.Date(string='Course start')
    course_end = fields.Date(string='Course end')
    last_evaluation = fields.Datetime(string='Last evaluation')
    course_image = fields.Binary(string='Course icon')
    course_shift = fields.Selection([('day', 'Day'),('night', 'Night')], string='Course shift')