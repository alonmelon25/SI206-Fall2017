import facebook

access_token = 'EAACEdEose0cBAOpNxdqxGpzMG2RwXWcM6BMWnLmc6MUwSxBjQPlfGWYpVJ6MxxGF8BWkj4QngswwXLyRB1rbZCi66k3d0vFIgK4hUOzs1DMx6xmiXEj0FHUTs5g3Sk3ZCmzulwXpt0ZAoNYAqYWjesYmPz0KIcjGTOt9yqsEJ9NZCHttJkToKS2lzLCZCB5QBaXEyUGUdOgZDZD'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

friend_list = [friend['name'] for friend in friends['data']]

print (friend_list)
