from bobs_bus import bus
import asyncio
import json

bus.login()
bus.posts.create_post(options={
    'channel_id': 'y9tmz5hzrb8b3nghjpyw5f6xyr',
    'message': "Im a test message from Bob",
})

my_id = bus.users.get_user(user_id='me')['id']

async def my_event_handler(message):
    msg = json.loads(message)
    if 'event' in msg and msg['event'] == 'posted' and 'mentions' in msg['data'] and my_id in msg['data']['mentions']:
        post = json.loads(msg['data']['post'])
        if 'hi' in post['message']:
            bus.posts.create_post(options={
                'channel_id': 'y9tmz5hzrb8b3nghjpyw5f6xyr',
                'message': "Hi! Im a test message from Bob",
            })
    else:
        print(json.dumps(json.loads(message)))


bus.init_websocket(my_event_handler)