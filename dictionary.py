list=[1,6,9,'a', 'c']
for item in list:
    if str(item).isnumeric() and item>6:
        print(item)