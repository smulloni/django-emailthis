try:
    from setuptools import setup
except ImportError:
    from distutils import setup


setup(author="Jacob Smullyan",
      author_email='jsmullyan@gmail.com',
      description=description,
      long_description=long_description,
      license="BSD",
      platforms='OS Independent',
      name="django-emailthis",
      url="http://code.google.com/p/django-emailthis/",
      classifiers=["Development Status :: 3 - Alpha",
                   "Environment :: Web Environment",
                   "Environment :: Web Environment :: Django",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      version=VERSION,
      keywords="django email",
      packages=("emailthis",),
      package_dir={'' : '.'}
      )


