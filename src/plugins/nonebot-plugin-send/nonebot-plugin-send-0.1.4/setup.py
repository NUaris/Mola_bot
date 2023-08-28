
# -*- coding: utf-8 -*-
from setuptools import setup

import codecs

with codecs.open('README.md', encoding="utf-8") as fp:
    long_description = fp.read()
INSTALL_REQUIRES = [
    'nonebot-adapter-onebot>=2.1.3',
    'nonebot2>=2.0.0b4',
]

setup_kwargs = {
    'name': 'nonebot-plugin-send',
    'version': '0.1.4',
    'description': '一个基于nonebot的反馈通知插件',
    'long_description': long_description,
    'license': 'MIT',
    'author': '',
    'author_email': 'sena-nana <851183156@qq.com>',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': [
        'nonebot_plugin_send',
        'nonebot_plugin_send.utils',
    ],
    'package_data': {'': ['*']},
    'long_description_content_type': 'text/markdown',
    'install_requires': INSTALL_REQUIRES,
    'python_requires': '>=3.8',

}


setup(**setup_kwargs)
