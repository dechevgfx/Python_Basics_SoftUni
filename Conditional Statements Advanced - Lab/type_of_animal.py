animal = str(input())

if animal == "dog":
    print("mammal")
elif animal in 'snake, crocodile, tortoise':
    print("reptile")
else:
    print("unknown")
