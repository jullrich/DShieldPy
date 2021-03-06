from distutils.core import setup
setup(
    name = "DShield",
    packages = ['DShield'],
    version = '0.1',
    license= 'gpl-3.0',
    description = 'Library to interact with DShield and the SANS Internet Storm Center. Also see isc.sans.edu/api',
    author = 'Johannes Ullrich',
    author_email = 'jullrich@sans.edu',
    url = 'https://github.com/jullrich/DShieldPy',
    download_url = 'https://github.com/jullrich/DShieldPy/dist/DShield-0.1.tar.gz',
    keywords = ['DShield','Security','Firewall','Logs','Intrusion Detection'],
    install_requires=[
        'base64',
        'configparser',
        'hashlib',
        'hmac',
        'json',
        'os',
        're',
        'requests',
        'socket',
        'struct',
        'sys',
        'syslog'
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intendend Audience :: Developers',
        'Topic :: Security',
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
    
