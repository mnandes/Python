## Q1
	a - True
	b - 1
	c - 1.0
## Q2
	false
## Q3
	a - 'e'
    b - 'o'
    c - 'o'
    d - 'ell'
## Q4
	continue - skip to next iteration of the loop
	break - exit the loop
	else - executes this branch of code in case loop succeeds normally, without “breaking”

## Q5
	thistuple = ("apple",)
## Q6
	string = ''.join('X' for i in range(78))

## Q7
    l = [[0] * size for _ in range(size)] #with size = 100
## Q8
    Mutable -> List
    Immutable -> String, Tuple, Dictionary Key
## Q9
Prevent division by 0 returning a 0 (Possible error return value)

    z = y / x if x!=0 else 0

OR

    try: 
        z = y / x
    except ZeroDivisionError:
        print("Error! x is 0")
## Q10
For both Python 2.6 and 3.6:

    8.0 / 5 = 1.6
    8 / 5 = 1.6
    8 // 5 = 1
    8 % 5 = 3
    2 ** 3 = 8
    round(0.5) = 0
## Q11
Returns value `None`

## Q12
Variable x becomes a "pointer" to the method f.

By executing x(), we obtain the value of f.

## Q13
Both output `None` as the print calls for `Test.var`, therefore returning the default value of the variable.

Value would be 1 if called `a.var` in the print function.

## Q14

    from lib import xxx.py

## Q15

    [[1, 2, 3], (1, 2)]

## Q16

    True
    False

xy is in the first string, so the output is True.
In the second example, xy is not in every string of the array, therefore, the output is False.

## Q17

    [4,2]

## Q18

    x, y = y, x

## Q19

    {'c': 5, 'd': 6}

## Q20

    1,3,5

## Q21

    if __name__ == '__main__':

Where `__name__` is either set to the module name or to `__main__` when executed as a script.

## Q22

    50

## Q23

    I got decorated
    I am ordinary

## Q24

    if address > start and address < end:

## Q25

    A generator function 

## Q26
If no list is ever provided, the elements will still continue to stack up.

    add_to_list(3)
    add_to_list(4)
    print(add_to_list(5))

Will produce a result of `[3,4,5]`, but

    li=add_to_list(2,[1])
    print(li)
    li=add_to_list(3)
    print(li)
    li=add_to_list(4,[7])
    print(li)
    li=add_to_list(5)
    print(li)

Will produce a result of 

    [1, 2]
    [3]
    [7, 4]
    [3, 5]

Meaning that not specifying the list in the last add_to_list makes it start with a default list of [3] instead of [].






***
## Bonus

    import operator

    d = {}
    file = open('a.txt', 'r')
    lines = file.read().splitlines()

    for line in lines:
        if line not in d:
            d[line] = '1'
        else:
            d[line] = str(int(d[line]) + 1)

    sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    
    for key in sorted_d:
        print(sorted_d[key] + " " + key)



