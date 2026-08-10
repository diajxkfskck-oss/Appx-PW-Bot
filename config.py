import os

api_id = int(os.environ.get("API_ID", 31280586))
api_hash = os.environ.get("API_HASH", "5f30188e8ff92b134ea343bb01eeaa90")
bot_token = os.environ.get("BOT_TOKEN", "8852786935:AAGwiBi2KF4LTOmq9GvyfYes0qW58jJBuYA")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "8847993242").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")
