import json

class BobResponse:
    def __init__(self, bus, channel_id, post):
        self.bus = bus
        self.channel_id = channel_id
        self.post = post
        self.teams = {}
        self.set_teams()

    def __post_msg(self, msg):
        return self.bus.posts.create_post(options={
            'channel_id': self.channel_id,
            'message': msg,
        })

    def parse_response(self):
        if 'hi' in self.post['message']:
            return self.__post_msg("Hello from Babot")
    
    def set_teams(self):
        all_teams = self.bus.teams.get_teams()
        for team in all_teams:
            self.teams[team['name']] = team['id']

    def get_teams(self):
        return json.dumps(self.teams, indent=2)
    
    def get_post(self):
        return json.dumps(self.post, indent=2)

    def __str__(self):
        return f"Channel id: {self.channel_id}\nPost: {self.get_post()}\nTeams: {self.get_teams()}"