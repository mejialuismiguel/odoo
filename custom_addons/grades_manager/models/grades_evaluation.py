from odoo import models, fields

class GradesEvaluation(models.Model):
    _name = 'grades.evaluation'
    _description = 'Grades Evaluation'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True)
    observations = fields.Text(string='Observations')
    course_id = fields.Many2one('grades.course', string='Course', ondelete='cascade')
    grade_ids = fields.One2many('grades.grade', 'evaluation_id', string='Grades')