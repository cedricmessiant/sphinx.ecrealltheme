from setuptools import setup, find_packages

version = '1.0.dev0'

setup(name='sphinx.ecrealltheme',
      version=version,
      description=u"Theme for Ecréall sphinx documentation.",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
      ],
      keywords='sphinx theme',
      author='Cédric Messiant',
      author_email='cedric.messiant@gmail.com',
      url='https://github.com/collective/sphinx.ecrealltheme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sphinx'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'sphinxjp.themecore',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [sphinx_themes]
      path = sphinx.ecrealltheme:get_path
      """,
      )
