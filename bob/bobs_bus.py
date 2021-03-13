from mattermostdriver import Driver
import os

bus = Driver({
    'url': 'mattermost-docker_web_1',
    'token': os.environ['BOB_TOKEN'],
    'scheme': 'http',
    'port': 80,
    'verify': False,
    'debug': True
})