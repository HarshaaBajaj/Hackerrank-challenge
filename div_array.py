def div_arr(a):
    '''
        Description : split array into two such that sum of elements in both is equal
        Input : array
        Output : splitable index
    '''
    total = sum(a) - a[0] # whole sum - first element to begin with
    seen = a[0] # already seen element total
    for i in range(len(a)-1): # repeat for all elements 
        #print(a[i],total,seen) # to debug
        if total != seen : # if equal sums are not yet found
            total -= a[i+1] # subtract this element from total
            seen += a[i+1] # add this element to seen total
        else : # if they are equal we can split
            return i + 1

if __name__ == '__main__':
	a = input('Please enter the list \n') or '2,7,9'
    a = [int(x) for x in a.split()]
    res = div_arr(a)
    if res != None: # if we found a split index
        print('Array splitable \n',[a[0:res],a[res:]]) # return list of the two new arrays
    else: print('Unable to split\n',a) # if not found return the original array
    
# example input:
# a=[1,2,3,4,5,5] ; b=[5,5,1,2,3,4]; c = [3,4]
# expected output :
# Array splitable : [[1, 2, 3, 4], [5, 5]]
# Array splitable : [[5, 5], [1, 2, 3, 4]] 
# Unable to split : [3,4]
