portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports, y):
    # Write your recursive code here
    if y == len(portnames):
        return
    print(' '.join([portnames[i] for i in range(y, route)]))
    if route == len(portnames):
       y+= 1
       return permutations(y, ports, y)
    else:
        return permutations(route + 1, ports, y)
    
    # Print the port names in route when the recursion terminates

y = 0

# This will start the recursion with 0 ("PAN") as the first stop
permutations(0, list(range(1, len(portnames))), y)