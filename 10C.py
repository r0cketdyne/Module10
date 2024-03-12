def flota_combine_compar(flot1, flot2, flot3):
    smallest  = 0
    if flot1 < flot2:
        smallest = flot1
    else:
        smallest = flot2
    if (flot3 < smallest) :
        smallest = flot3
        
        
        
    return smallest

print("Testing")

print("Smallest:", flota_combine_compar(1, 3, 4))

#oddly, it seems like you can invoke a function at a print statement.