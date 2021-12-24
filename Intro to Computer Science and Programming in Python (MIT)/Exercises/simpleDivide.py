def simple_divide(item, denom):
    try:
        for i in range(len(item)):
            item[i] /= denom
    except ZeroDivisionError:
        result = [0]*len(item)
        return result
    else:
        return item
  
print(simple_divide([2, 4, 8], 0))