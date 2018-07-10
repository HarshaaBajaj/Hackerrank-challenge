def div_arr(a):
    '''
        Description : split array into two such that sum of elements in both is equal
        Input : array
        Output : list of two sub arrays
    '''
    index = [] # to save the split index
    total = sum(a) - a[0] # whole sum - first element to begin with
    seen = a[0] # already seen element total
    for i in range(len(a)-1): # repeat for all elements 
        #print(a[i],total,seen) # to debug
        if total != seen : # if equal sums are not yet found
            total -= a[i+1] # subtract this element from total
            seen += a[i+1] # add this element to seen total
        else : # if they are equal we can split
            index.append(i+1) # split index
            break # no need to search further
    if len(index)>0: # if we found a split index
        return([a[0:index[0]],a[index[0]:]]) # return list of the two new arrays
    else: return(a) # if not found return the original array

# example call:
# a=[1,2,3,4,5,5] ; b=[5,5,1,2,3,4]
# print(div_arr(a)) ; print(div_arr(b)) or list(map(div_arr,[a,b]))

# expected output :
# [[1, 2, 3, 4], [5, 5]]
# [[5, 5], [1, 2, 3, 4]] or
# [[[1, 2, 3, 4], [5, 5]], [[5, 5], [1, 2, 3, 4]]]
