# -*- coding: utf-8 -*-
{
    'name': "Meeting Room",

    'summary': """Manage create meeting room""",

    'description': """
        Meeting Room module for Rrinity Roots:
            - Subject for meetings.
            - Book a meeting room.
            - Choose a room for a meeting.
            - Choose the time and date for the meeting.
            - Meeting attendees.
            - Cancellation confirmation status.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm'],

    # always loaded
    'data': [
        'view/create.xml',
        'view/meeting_room1.xml',
        'view/form_room_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}