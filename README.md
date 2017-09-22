# RNG_AppAmplify

                               Script Name : RNG.py

Python Version : 3.3 or above 


Short Description : The script takes a positive integer(N) from stdin and returns
                    a number within the range from 1 to N.The program is designed 
                    in such a way that the output is 73% biased to higher values, 
                    where higher mean numbers greater N/2.

I/P Format : A single integer 'a' where (1 < a < 1000000)
             NOTE : For values greater than 1000000 performance could get slow
                     depending upon the system's memory and CPU.

O/P Format : A single integer 'b' where (0 < 1 <= 'a')


Method Used :  Counting the number of 'high' and 'low' values produced and based  
               on it producing a value which brings the total number of high values
               closer to 73% of overall produced values for a given number.

Suggested Improvements : Instead of storing 'high' and 'low' values in lists, it can
                         be stored in tree which could reduce the access time for
                         element from O(n) to O(logn).
                         if possible, avoide storing the complete list of values to
                         save memory.
