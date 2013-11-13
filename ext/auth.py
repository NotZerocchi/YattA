from twython import Twython 
import requests
import webbrowser

APP_KEY = 'scMhZpaXu5dJ8T6zak3Q'
APP_SECRET = 'ykMQ49YB8Mk5lTs6AN0UWiUALFKdpuN0pECMgeDaOkg'

twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens(callback_url='oob')

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

webbrowser.open(auth['auth_url'])

oauth_verifier = raw_input("Enter PIN: ")

twitter = Twython(APP_KEY, APP_SECRET, 
		  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authentication_tokens(oauth_verifier)

OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']