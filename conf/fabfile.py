import datetime

from fabric.api import env, puts, cd
from fabric.contrib.project import rsync_project 
from fabric.colors import _wrap_with  
from fabric.operations import run

env.project = 'philratcliffe.co.uk'

_green_bg = _wrap_with('42')
_red_bg = _wrap_with('41') 

RSYNC_EXCLUDE = ('.git', 'logs', '*.pyc')

def server():
    # path to the cc directory on the remote server. 
    env.rk_remote_path = '/home/redkestrel/projects/philratcliffe.co.uk/' 

    # path to the cc directory on the local server. 
    env.rk_local_path = '~/projects/philratcliffe.co.uk/'

    env.hosts = ['seneca']
    env.user = 'redkestrel'

def sync():
    """
    Synchronize project with webserver
    """

    puts(_green_bg('Synching philratcliffe.co.uk'))
    start_time = datetime.datetime.now()

    rsync_project(
                remote_dir=env.rk_remote_path, \
                local_dir=env.rk_local_path, 
                delete=True,
                exclude=RSYNC_EXCLUDE)

    end_time = datetime.datetime.now()
    finish_message = 'Correctly finished synching in %i seconds' % \
        (end_time - start_time).seconds        
    puts(_green_bg(finish_message))


