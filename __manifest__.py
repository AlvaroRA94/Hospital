

{
    'name': 'Hospital App',
    'version': '1.0.0.0.0',
    'author': 'Álvaro Roldán',
    'maintainer': 'Álvaro Roldán',
    'website': 'www.google.es',
    'license': 'AGPL-3',
    'category': 'Administration',
    'summary': 'Application oriented to administration of an hospitalarian service',
    'depends': ['base'],
    'security':['security/ir.model.access.csv',
                'security/patient_security.xml',
                'security/appointment_security.xml',
                'security/doctor_security.xml'],
    'data':['views/appointment_view.xml',
        'views/doctor_view.xml',
        'views/patient_view.xml'],
    'application' : True,
    'instalable' : True,
    'auto_install' : False,
    'images' : [
        'static/description/icon.png'
    ]               
}
