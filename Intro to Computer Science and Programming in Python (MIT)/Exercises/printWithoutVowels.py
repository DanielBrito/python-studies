def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    result = ""
    vowels = "aeiou"
    
    for ch in s:
      if ch.lower() not in vowels or ch==' ':
        result += ch
    
    print(result)