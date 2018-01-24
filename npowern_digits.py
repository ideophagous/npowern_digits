#get the index of the element in "my_list" equal to "value"
#if no such element exists, return -1
def get_equal_value_index(my_list,value):
    for i in range(len(my_list)):
        if value==my_list[i]:
            return i
    return -1

#get the list of congruences of powers of n modulo 100,
#as well as the index in the congruence list where the 
#cycle breaks, and the index where the cycle starts
def conguence_of_powers(n):
    value = n%100
    my_list = [1,value]
    i = 2
    while i<100:
        value = (value*n)%100
        j = get_equal_value_index(my_list,value)
        if j==-1:
            my_list.append(value)
        else:
            break
        i+=1
    cycle_end = i
    cycle_beginning = j
    return cycle_end,cycle_beginning,my_list

#adjust digits to the right by adding 0, to ensure
#we always have two digits
def adjust_digits(k):
    return str(k).rjust(2,'0')


#get the last two digits of n^n
def get_npowern_digits(n):
    cycle_end,cycle_beginning,congruences = conguence_of_powers(n)
    n_congruence = n%100
    if n<cycle_beginning:
        return adjust_digits((n_congruence)**n%100)
    else:
        actual_congruence_index = cycle_beginning+(n-cycle_beginning)%(cycle_end-cycle_beginning)
        return adjust_digits(congruences[actual_congruence_index])
    
if __name__ == '__main__':
    n = int(input())
    print(get_npowern_digits(n))
