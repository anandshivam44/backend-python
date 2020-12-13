import json

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
t = {}
t['name'] = {}
t['name']['hey'] = 'Shivam'


# convert into JSON:
# y = json.dumps(x)

# the result is a JSON string:
print(t.get('name').get(1).get(2))
