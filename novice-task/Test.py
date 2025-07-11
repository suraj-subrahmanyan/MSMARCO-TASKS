import jsonlines

items = [
    {1: 'one', 2: 'two'} # Key is an integer, not a string
]
filename = "jimmmyl"
with jsonlines.open("jimmy", 'w') as writer:
    writer.write_all(items)

help(jsonlines.open)

