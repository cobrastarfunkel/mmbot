from mattermostdriver import Driver
import os
import sys, logging

logger = logging.getLogger("Test Logger")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('||%(name)s|| -> [%(asctime)s] [%(levelname)s] - %(message)s', datefmt='"%d-%b-%Y %H:%M:%S"')
handler.setFormatter(formatter)
logger.addHandler(handler)

bus = Driver({
    'url': 'mattermost-docker_web_1',
    'token': os.getenv('TEST_TOKEN'),
    'scheme': 'http',
    'port': 80,
    'verify': False,
})