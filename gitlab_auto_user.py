import requests
import gitlab

gl = gitlab.Gitlab('http://10.11.1.244', private_token='Frjba9fEARzscCurjYKv')

#r = requests.get(r"http://10.11.2.20/api/v4/users?private_token=xymQ6UasxZHzA-S-xc4_", verify=False).text
#users = gl.users.list()
#print(users)

users = [f'{course}{team}0{student}' for course in ['A', 'B'] \
         for team in range(1,4) for student in range(1,7)]
"""
r = requests.post(f'http://10.11.2.20//api//v4//users'\
                  f'?email=guy@bsmch.net&password=Bsmch@500K!'\
                  f'&username=guy&name=guy&skip_confirmation=true',\
                  headers={'Authorization': 'Bearer xymQ6UasxZHzA-S-xc4_'}, verify=False)

"""

for user in users:
    u = gl.users.create({'email': rf'{user.lower()}@bsmch.net', \
                         'password': 'Bsmch@500K!', \
                         'username': user, \
                         'name': user})                         
    u.activate() 
