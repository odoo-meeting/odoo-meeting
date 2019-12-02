# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from datetime import timedelta
from openerp.exceptions import ValidationError
import logging


class meeting_room1(models.Model):
    _name = 'meeting.room1'

    name_id = fields.Many2one(
        'res.users',
        string='Meeting leader',
        required=True,
    )

    subject = fields.Char(
        string='Subject',
        required=True,
    )

    name_ids = fields.Many2many(
        'res.users',
        string='Attendee',
        required=True,
    )

    start_date = fields.Datetime(
        string = 'Start',
        required=True,

    )

    end_date = fields.Datetime(
        string = 'End',
        required=True,
    )

    number_room = fields.Many2one(
        'meeting.formroom',

        string='Room',
        required=True,
    )

    state = fields.Selection([
        ('draft', "Draft"),
        ('confirmed', "Confirm"),
        ('done', "Done"),
        ('cancel', 'Cancel'),
    ],
        default='draft'
    )

    @api.multi
    def draft(self):
        self.state = 'draft'

    @api.multi
    def confirm(self):
        self.onchange_end_date()
        return self.write({'state': 'confirmed'})

    @api.multi
    def done(self):
        self.state = 'done'

    @api.multi
    def cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        print(vals)
        session_obj = self.env['meeting.room1']
        session_id = session_obj.search([
            ('number_room', '=', vals.get('number_room')),
            ('start_date', '<', vals.get('end_date')),
            ('end_date', '>', vals.get('start_date')),
            ('state','=','done'),
        ])
        if session_id:
            raise ValidationError(_("ห้องไม่ว่าง หรือ เวลาตรงกัน"))
        rec = super(meeting_room1, self).create(vals)
        return rec

    @api.onchange('end_date')
    def onchange_end_date(self):
        if self.end_date < self.start_date:
            raise ValidationError(u'กรุณากรอกเวลาให้ถูกต้อง')

    @api.onchange('start_date')
    def onchange_start_date(self):
        if self.start_date < self.end_date:
            raise ValidationError(u'กรุณากรอกเวลาให้ถูกต้อง')

class meeting_formroom(models.Model):
    _name = 'meeting.formroom'

    name = fields.Char(
        string='Room',

    )



