from odoo import models, fields, api

class GradesEvaluation(models.Model):
    _name = 'grades.evaluation'
    _description = 'Grades Evaluation'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True)
    observations = fields.Text(string='Observations')
    course_id = fields.Many2one('grades.course', string='Course', ondelete='cascade')
    grade_ids = fields.One2many('grades.grade', 'evaluation_id', string='Grades')

    @api.model_create_multi
    def create(self, vals):
        result = super(GradesEvaluation, self).create(vals)
        for student in result.course_id.student_ids:
            if not self.env['grades.grade'].search([('student_id', '=', student.id), ('evaluation_id', '=', result.id)]):
                self.env['grades.grade'].create({
                    'student_id': student.id,
                    'value': 0,
                    'date': fields.Date.today(),
                    'evaluation_id': result.id,
                })
        return result