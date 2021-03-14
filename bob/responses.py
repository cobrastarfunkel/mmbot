
class BobResponse:
    def __init__(self, bus, channel_id, post):
        self.bus = bus
        self.channel_id = channel_id
        self.post = post

    def __post_msg(self, msg):
        return self.bus.posts.create_post(options={
            'channel_id': self.channel_id,
            'message': msg,
        })

    def parse_response(self):
        if 'hi' in self.post['message']:
            return self.__post_msg("Hello from Bobot")