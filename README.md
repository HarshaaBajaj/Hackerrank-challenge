# Miscellaneous simple programs/functions

### 1. getMovieTitles
## Given
A substring

## Objective
Produce an ascending ordered list for all movie titles containing the substring (non case sensitive) from given url database

## Description
The function getMovieTitles tries to retreive all the movie titles (could be over multiple pages) for the substring provided by user

### 2. Luggage
## Given
A string input of luggage ids

## Objective
Produce an string output of order of unloaded luggage

## Description
Loading :
  For the given input luggage each container can be filled with a maximum of three luggage bags
 Unloading :
  The containers are unloaded in LIFO and the bags are unloaded in FIFO fashion

### 3. div_array
## Given 
An array of integers

## Objective
Split the array into two arrays having the same sum of elements

## Description
-- The total sum of elements is calculated upfront
-- Each element in the array is added to a 'seen' total and subtracted from the 'total'  calculated in the previous step
-- The above step is repeated until either both the sums are equal in which case the index for the split is determined else the array can't be split and is returned as whole

