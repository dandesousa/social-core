"""
Discord OAuth2 backend, docs at:
    https://python-social-auth.readthedocs.io/en/latest/backends/discord.html
"""
from .oauth import BaseOAuth2


class DiscordOAuth2(BaseOAuth2):
    name = 'discord'
    AUTHORIZATION_URL = 'https://discordapp.com/api/oauth2/authorize'
    ACCESS_TOKEN_URL = 'https://discordapp.com/api/oauth2/token'
    REFRESH_TOKEN_URL = 'https://discordapp.com/api/oauth2/token'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    SCOPE_SEPARATOR = ' '
    EXTRA_DATA = [
        ('avatar', 'avatar'),
        ('bot', 'bot'),
        ('id', 'id'),
        ('email', 'email'),
        ('username', 'username'),
    ]

    def get_user_details(self, response):
        """Return user details from Disqus account"""
        rr = response.get('response', {})
        return {
            'username': rr.get('username', ''),
            'bot': rr.get('bot', ''),
            'id': response.get('id', ''),
            'email': rr.get('email', ''),
            'avatar': rr.get('avatar', ''),
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        key, secret = self.get_key_and_secret()
        return self.get_json(
            'https://discordapp.com/api/users/@me', headers={
                'Authorization': 'Bearer {0}'.format(access_token)
            }
        )
