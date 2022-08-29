"""
обход в глубину
итеративный подход
"""

tree = [1,2,3,4, 5, [34, 55, [123, [1234]], 11, 245], [6,5,4,3,4,56], [1,2,234], 4,5,6]

while tree:
    res = tree.pop(0)
    if isinstance(res, int):
        print(res)
    elif isinstance(res, list):
        for item in reversed(res):
            tree.insert(0, item)



"""
обход в ширину
"""

while tree:
    res = tree.pop(0)
    if isinstance(res, int):
        print(res)
    elif isinstance(res, list):
        for item in res:
            tree.append(item)
            
