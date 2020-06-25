from setuptools import setup

setup(name='pbixrefresher',
      version='0.2.0',
      description='Script for refreshing and publishing Power BI workbooks',
      url='https://github.com/dubravcik/pbixrefresher-python',
      author='Michal Dubravcik, Barnabás Nagy',
      author_email='michal.dubravcik@gmail.com, otapi@protonmail.ch',
      license='MIT',
      packages=['pbixrefresher'],
      install_requires=[
          'pywinauto',
          'psutil'
      ],
	  entry_points = {
        "console_scripts": ['pbixrefresher = pbixrefresher.pbixrefresher:main']
        },
      zip_safe=False)