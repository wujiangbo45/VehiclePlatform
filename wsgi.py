# -*- coding: utf-8 -*-
import sys
from django.core.management import execute_from_command_line
from gevent import monkey
# monkey.patch_all()
import os
# 设置 Django 项目配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import leancloud
from gevent.pywsgi import WSGIServer
from cloud import engine
APP_ID = os.environ['LC_APP_ID']
APP_KEY = os.environ['LC_APP_KEY']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])
leancloud.init(APP_ID, master_key=MASTER_KEY)
#

execute_from_command_line(['', 'makemigrations', 'ManageApp'])
execute_from_command_line(['', 'migrate'])


from django.contrib.auth.models import User
try:
    User.objects.get(username='admin')
except:
    User.objects.create_superuser('admin', 'emailname@demon.com','woshi123')
application = engine
if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    server = WSGIServer(('localhost', PORT), application)
    server.serve_forever()
