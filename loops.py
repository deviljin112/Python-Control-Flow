################
# Control Flow #
################

# FOR Loop
# Used to iterate through data
# Syntax: for <variable> in <statement>:

## Looping through a list
shopping_list = ["eggs", "milk", "supermalt"]

for item in shopping_list:
    if item == "milk":
        print(item)

## Looping through a dict
sample_dict = {
    "name": "dev",
    "age": 99,
    "course": "DevOps",
    "hobbies": ["Coding", "Gaming", "Sleeping"],
}

for k, v in sample_dict.items():
    if isinstance(v, list):
        print(f"Key: {k}")
        for i in v:
            print(f"List Value: {i}")
    else:
        print(f"Key: {k}, Value: {v}")

for k in sample_dict.keys():
    print(f"Key: {k}")

for v in sample_dict.values():
    if isinstance(v, list):
        for i in v:
            print(f"List Value: {i}")
    else:
        print(f"Value: {v}")


# WHILE Loop
# Used to loop through a code block until a specific condition is met
# Syntax: while <condition> operator <condition>:

## While looping through a list
sample_list = ["foo", "bar", "dev", "ops"]

found = False
while not found:
    if "python" in sample_list:
        found = True
    else:
        sample_list.append("python")
