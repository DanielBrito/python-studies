def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
        
    result_dict = {}
    result_str = ""
    i = 0
    
    for item in map_from:
        result_dict[item] = map_to[i]
        i += 1
    
    for element in code:
        result_str += result_dict[element]
    
    return (result_dict, result_str)