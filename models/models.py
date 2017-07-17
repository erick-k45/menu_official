# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Empleados(models.Model):
    _inherit = 'hr.employee'

class Departamentos(models.Model):
    _inherit = 'hr.department'

class Skill(models.Model):
    _inherit = 'hr.skill'

class Encuestas(models.Model):
    _inherit = 'survey.survey'

class Orientation(models.Model):
    _inherit = 'employee.orientation'

class Knowledge(models.Model):
    _inherit = 'document.page'

class company(models.Model):
    _inherit = 'company_profile.profile'

class Rep(models.Model):
    _name = 'menu.r'
