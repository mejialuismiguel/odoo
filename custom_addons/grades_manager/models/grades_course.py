from reportlab.graphics.shapes import String

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
    teacher_id = fields.Many2one('res.partner', string='Teacher', domain=[('is_teacher', '=', True)])
    evaluation_ids = fields.One2many('grades.evaluation', 'course_id', string='Evaluations')
    student_ids = fields.Many2many('res.partner','grades_course_students_rel', string='Students')
    state = fields.Selection([('register', 'Register'),('in_progress', 'In Progress'), ('finished', 'Finished')], String = 'State', default='register')