people = []

people.append({
    "name": "bob"
    , "role": "one"
})
people.append({
    "name": "bob1"
    , "role": "one1"
})

for profile in people:
    print('''
    name: {}
    role: {}
    '''.format(profile['name'], profile['role']))
