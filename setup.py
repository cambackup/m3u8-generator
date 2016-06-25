import setuptools

setuptools.setup(name='m3u8-generator',
                 version=1.0,
                 description='m3u8 playlist generator',
                 long_description=open('README.md').read().strip(),
                 author='cambackup.com',
                 author_email='info@cambackup.com',
                 url='https://github.com/cambackup/m3u8-generator',
                 py_modules=['m3u8_generator'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='m3u8 generaror',
                 )