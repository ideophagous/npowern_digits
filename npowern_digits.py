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
def conguence_of_powers(n,m):
    value = n%(10**m)
    my_list = [1,value]
    i = 2
    while i<(10**m):
        value = (value*n)%(10**m)
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
def adjust_digits(k,m):
    return str(k).rjust(m,'0')


#get the last m digits of n^n
def get_npowern_digits(n,m):
    cycle_end,cycle_beginning,congruences = conguence_of_powers(n,m)
    n_congruence = n%(10**m)
    if n<cycle_beginning:
        return adjust_digits((n_congruence)**n%(10**m),m)
    else:
        actual_congruence_index = cycle_beginning+(n-cycle_beginning)%(cycle_end-cycle_beginning)
        return adjust_digits(congruences[actual_congruence_index],m)
    
if __name__ == '__main__':
    number = int(input("Enter n: "))
    digits_count = int(input("Enter the number of digits: "))
    print(get_npowern_digits(number,digits_count))
