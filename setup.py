import setuptools

with open('README.md') as f:
    readme = f.read()

PACKAGES = [
            'vk2telegraph',
            'vk2telegraph.vk', 
            'vk2telegraph.vk.backends', 
            'vk2telegraph.vk.backends.requests_html_backend',
            'vk2telegraph.tgph',
            'vk2telegraph.tgph.backends'
            ]

setuptools.setup(
    name='vk2telegraph',
    version='0.0.1',
    author='Kristaller',
    description='This script translate VK articles to Telegra.ph posts',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/kristaller486/vk2telegraph',
    packages = PACKAGES,
    keywords=['vk', 'telegraph', 'vk posts', 'telegra.ph'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=[
        'fake-useragent',
        'fire',
        'telegraph',
        'requests',
        'beautifulsoup4'
    ]
)