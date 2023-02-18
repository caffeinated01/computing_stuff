# Example usage of enumerate
"""
Enumerate takes in two args
1) Iterable - a sequence, an iterator, or objects that support iteration
2) Start - (optional) the number of which enumerate starts counting from. If omitted, 0 is taken as start
Enumerate adds counter to an iterable and returns it. The returned object is an enumerate object.
"""

a = ["JJC", "NYJC", "TJC", "CJC", "HCI", "RJC", "YIJC"]
for i, v in enumerate(a):
    print(i, v)  # i refers to index, while v refers to value
