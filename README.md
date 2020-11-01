# fleetwood-slack

Prerequisites:
- A Slack workspace you want to add the bot to
- Install Python3
- Install ngrok: https://ngrok.com/download

Creating the Slack app:
1. Go to https://api.slack.com/apps and click Create New App
2. Name it and choose a workspace
3. Add Scopes
    1. Go to OAuth & Permissions
    2. Under Bot Token Scopes, add permissions. For this app, we at least need app_mentions:read, which allows our app to view messages that directly mention our bot
4. Scroll to the top of the OAuth & Permissions page and click Install App to Workspace

## Set up ngrok and events:
1. Run ngrok: ngrok http 3000
2. On Event Subscriptions page, enable events (if not already enabled)
3. In request URL, put ngrok URL plus /slack/events, e.g. https://8eb44499712a.ngrok.io/slack/events
4. Click Subscribe to Bot Events
5. Add the Bot User Event app_mention, which will subscribe to message events that mention our bot

## Set up the Bolt project:
1. Clone the Github repo: git clone https://github.com/helloleah/fleetwood-slack.git
2. cd fleetwood-slack
3. python3 -m venv .venv
4. source .venv/bin/activate
5. pip install -r requirements.txt
6. export SLACK_SIGNING_SECRET=*** (from Basic Information page)
7. export SLACK_BOT_TOKEN=xoxb-*** (from OAuth & Permissions page)
8. FLASK_APP=app.py FLASK_ENV=development flask run -p 3000
