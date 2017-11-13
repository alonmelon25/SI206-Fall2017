import requests
import facebook  #pip install facebook-sdk
import json

access_token = None
if access_token is None:
    access_token = input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")


graph = facebook.GraphAPI(access_token)
posts = graph.get_connections('me','posts') 

while True:
	try:
		with open('my_posts.json','a') as f:
			for post in posts['data']:
				f.write(json.dumps(post)+"\n")
			posts = requests.get(posts['paging']['next']).json()
	except KeyError:
		#ran out of posts
		break