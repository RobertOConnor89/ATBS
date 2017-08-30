def list_to_string(aList):
    aString = ''
    for x in aList:
        aString += x
        if aList.index(x)== (len(aList)-2):
            aString += ', and '
        elif aList.index(x) != (len(aList)-1):
            aString += ', '

    return aString
            
