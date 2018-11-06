# Usage:
$ python h1b_counting.py

# about code
There are two functions in h1b_counting.py for counting occupation and state separately. The algorithm of the two function are similar. 

## algorithm
1. input csv file as array. (the only place I used numpy libraray function)
2. find the indexes of specified header name(e.g. "STATUS" and "SOC_NAME").
3. use these indexes to get the target column. 
4. counting, if the statement is true(e.g. if value in STATUS == "Certified")
5. calculate the percentage.
6. sort the counting result. 
7. output the top10 result as text format.

## further improvement 
1. Since the column name is slitely different between 2014 and others, I set if statement to contatin two of them. However, the statement may change in future. If want to find this similar column automatically, it is better to input regex libaray and use wildcard. 
2. Input csv file with your own filename. I write the I/O statement and comment it out in line 5-7. If you want to test your own file, just comment out line 8 and use line 5-7. It will print prompt. However, in this case, there are fixed directory structure, it is not neccessary to use prompt. 
3. If csv file is too big to run into "out of memory error", it is necessary to split the csv file first and read them separately.
4. Though python is helpful, sometimes, shell is more convenient to handle table file such like this case. 
