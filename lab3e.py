#!/usr/bin/env python3

# Create the list called "my_list" here, not within any function defined below.
# That makes it a global object. We'll talk about that in another lab.
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Returns all of items in the global object my_list unchanged
    return my_list

def give_first_item():
    # Returns the first item in the global object my_list as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Returns a list that includes the first and last items in the global object my_list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Returns a list that includes the second and third items in the global object my_list
    return [my_list[1], my_list[2]]

if __name__ == '__main__':  # This section also referred to as a "main block"
    print(give_list())                # Should print the whole list: [100, 200, 300, 'six hundred']
    print(give_first_item())          # Should print the first item: '100'
    print(give_first_and_last_item()) # Should print the first and last item: [100, 'six hundred']
    print(give_second_and_third_item())  # Should print the second and third items: [200, 300]
