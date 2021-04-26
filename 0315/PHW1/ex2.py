# Ex-2. Dictionary Generation
# K : A tuple of unique subjects (keys)
# V : A tuple of numeric points (values)
# K and V have the same size
# Make a dictionary D of size with K and V

def makeDict(K, V):
    return dict(zip(K,V))   # Auto check whether redundant in key tuples

K = ('Korean', 'Mathematics', 'English')
V = (90.3, 85.5, 92.7)

if len(K) != len(V):
    print("K and V don't have the same size")
else:
    result = makeDict(K,V)
    print(type(result), result)