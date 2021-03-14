from test_settings import bus

bus.login()

def post_msg():
    bus.posts.create_post(options={
        'channel_id': 'ujajuuyc8t8mpqpwoibe76etrr',
        'message': '@bobbybot hi',
    })

post_msg() 
