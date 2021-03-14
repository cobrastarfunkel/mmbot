from test_settings import bus, logger
import logging, json

import unittest

logger.setLevel(logging.INFO)

class TestPostReplies(unittest.TestCase):
    def setUp(self):
        bus.login()
        self.my_id = bus.users.get_user(user_id='me')['id']

    def test_bobs_reply(self):
        """
        Test @bobbybot hi
        Should make a post to Townsquare
        """
        res = bus.posts.create_post(options={
            'channel_id': 'ujajuuyc8t8mpqpwoibe76etrr',
            'message': '@bobbybot hi',
        })
        logger.info(f"{json.dumps(res, indent=2)}")
        self.assertTrue('user_id' in res and res['user_id'] == self.my_id)

if __name__ == '__main__':
    unittest.main()
