import ustruct   

def shortConverter (val):
    shortPackage = ustruct.pack('h',val)
    return shortPackage