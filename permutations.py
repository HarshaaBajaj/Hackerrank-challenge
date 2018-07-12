def permutations(arr, sep=''):
    
    '''
    Description : Utility function to find possible permutations of input
    Approach : Divide and conquer implementation using recursion 
              For each element keep dividing the input until singleton except the element under consideration and return the permuted order 
    Input:
      arr -- input array
      sep -- desired separator between elements of each permutation
    Output:
      result -- list of str permutations
    '''
    
    global result
    if len(arr) == 0: result.extend([sep])
    else: [permutations(arr[:i] + arr[i+1:], sep+arr[i]) for i in range(len(arr))] # for each element find permuations excluding it
    return result

if __name__ == '__main__':
  result = []
  a = input('Enter the input separated by space\n') or '1 2 3'
  perms = permutations(list(map(str,a.split()) # create a list of str elements from (default)input
  print('Total possible permutations :',len(perms))
  print(perms)
  

