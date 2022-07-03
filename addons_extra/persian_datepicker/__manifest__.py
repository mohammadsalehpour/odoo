{
    'name': 'Persian Datepicker',
    'version': "1.0.0",
    'category': 'DameDast',
    'summary':
        """
            Persian Datepicker Support.
        """,
    'author': 'Mohammad Salehpour',
    'license': 'AGPL-3',
    'images': [],
    'depends': ['web'],
    'data': [
        'views/templates.xml',
        'views/UserPreferences_Views.xml',
    ],
    'demo': [],
    'test': [],
    'assets': {
        'web.assets_common': [
            (
                "after",
                "/web/static/lib/moment/moment.js",
                "/persian_datepicker/static/src/js/moment-jalaali.js",
            ),
            (
                "after",
                "/web/static/src/legacy/js/core/time.js",
                "/persian_datepicker/static/src/js/mytime.js",
            ),
            (
                "replace",
                "/web/static/lib/tempusdominus/tempusdominus.js",
                "/persian_datepicker/static/src/js/tempusdominus_fixed.js",
            ),
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
