"""
Flask-WP
-------------

Flask-WP is a backend for wordpress database.
You can use wordpress admin panel for your blog and use flask-wp to customize your website's front or api or etc.
"""
from setuptools import setup


setup(
    name='Flask-WP',
    version='1.0',
    url='https://github.com/RevengeComing/flaskwp',
    license='BSD',
    author='Sepehr Hamzehlouy',
    author_email='s.hamzelooy@gmail.com',
    description='A Backend for wordpress database',
    long_description=__doc__,
    py_modules=['flask_wp'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        "Flask-sqlalchemy"
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)