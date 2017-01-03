# LegalAdviceUserHistoryBot

Examining a stream of posts to /r/legaladvice to look at a user's history for activity.

The warning_subreddits list and political_subreddits list can be customized for whatever subs you would like.

To use this bot, you must create a config.py file in the following format:

user_agent = 'Your desired user agent'

client_id = 'Client ID from reddit'

client_secret = 'Client Secret from reddit'

If you don't have these details:

1) Log into your account on reddit, select "preferences", then select apps.

2) Create a new "personal use script app" and fill in your information (tip: use redirect URL http://localhost:8080)

3) Input information into config.py

