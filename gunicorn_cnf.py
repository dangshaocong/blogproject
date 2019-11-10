import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing
if not os.path.exists('log'):
    os.mkdir('log')
bind = '0.0.0.0:8000'  # 绑定ip和端口号
backlog = 512  # 监听队列
timeout = 30  # 超时
worker_class = 'gevent'

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2  # 指定每个进程开启的线程数
loglevel = 'debug'  # 日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'
errorlog = 'log/error.log'
accesslog = 'log/access.log'
