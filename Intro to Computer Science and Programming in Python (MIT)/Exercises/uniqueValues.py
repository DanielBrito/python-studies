def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    fullList = []
    uniList = []
    keyList = []
    tracker = 0
    
    for value in aDict.values():
      fullList.append(value)
    
    for i in range(len(fullList)):
      tracker = fullList.count(fullList[i])
      if tracker == 1:
        uniList.append(fullList[i])
    
    for key, value in aDict.items():
      if value in uniList:
        keyList.append(key)
    
    keyList.sort()
    
    return keyList