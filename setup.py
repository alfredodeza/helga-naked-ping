from setuptools import setup, find_packages

version = '0.0.1'

setup(name="helga-ping",
      version=version,
      description=('annoy users who insist (or have no idea) on naked pings'),
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot ping',
      author='alfredo deza',
      author_email='alfredo [at] deza [dot] pe',
      url='https://github.com/alfredodeza/helga-ping',
      license='MIT',
      packages=find_packages(),
      entry_points = dict(
          helga_plugins = [
              'ping = ping:ping',
          ],
      ),
)
