import os

with open('create-users.input') as f:
    for line in f:
        user = line.strip()
        os.system(f'useradd {user}')
