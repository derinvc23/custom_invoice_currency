{
    'name': 'Custom Invoice Currency',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Accounting',
    'summary': 'Set BOB as default currency on invoice lines',
    'description': """
        This module ensures that the currency on invoice lines is always BOB, 
        regardless of the journal selected.
    """,
    'depends': ['account'],
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}