import os

bind = "0.0.0.0:5000"
workers = os.sysconf("SC_NPROCESSORS_ONLN") * 2
log_syslog = True
loglevel = "error"
reload = True if os.getenv('IP_TASK_SETTINGS', 'development') != 'production' else False
