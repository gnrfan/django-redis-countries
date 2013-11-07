module_file = open("redis_countries/__init__.py").read()
long_description = open('README.md').read()

from setuptools import setup, find_packages

setup(
    name='django_redis_countries',
    description='IP to country middleware',
    packages=find_packages(),
    author='Ivo Sanchez Checa Crosato',
    author_email='ivoscc [at] gmail.com',
    install_requires=['redis', 'simplejson'],
    test_requires=['mock', 'nose'],
    url='http://github.com/muleros/django-redis-countries',
    license="MIT",
    zip_safe=False,
    keywords="redis, django, middleware, countries",
    long_description=long_description,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
    ]
)
