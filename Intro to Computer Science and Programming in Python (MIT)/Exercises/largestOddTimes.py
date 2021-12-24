def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    
    odd_count= []

    for i in L:
        if (L.count(i))&1:
            odd_count.append(i)

    if len(odd_count)>0:
        return max(odd_count)
    else:
        return None