from mattermostdriver import Driver
import os
import sys
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s', datefmt='"%d-%b-%Y %H:%M:%S"')
handler.setFormatter(formatter)
logger.addHandler(handler)

bus = Driver({
    'url': 'mattermost-docker_web_1',
    'token': os.environ['BOB_TOKEN'],
    'scheme': 'http',
    'port': 80,
    'verify': False,
    #'debug': True
})

bus.login()
bobs_id = bus.users.get_user(user_id='me')['id']
