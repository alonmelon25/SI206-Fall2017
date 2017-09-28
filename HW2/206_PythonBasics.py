import operator

# SI 206 Fall 2017

##COMMENT YOUR CODE WITH:
<<<<<<< HEAD
# Section Day/Time: Section 001 (2:30 - 4:00)
# People you worked with: Colleen
=======
# Section Day/Time: 
# People you worked with: 
>>>>>>> 9262dd73635b8feee19f15ccd3dbbfbd9f07fbfd

#########

# For each task, fill in the code for the function we describe.

## Our provided code will call the functions with a few different inputs, check the results, and print 'OK' when each function's output is correct.

## The starter code for each function includes a placeholder for your code. You need to fill in code for the function that returns the correct result as specified.


## Task 0. Background Information
## This function should print your name and your expected score.
def task0():
<<<<<<< HEAD
    print ("Aaron Cheng")
    print ("Expected Score: 60")
=======
    pass # Replace with your code!
>>>>>>> 9262dd73635b8feee19f15ccd3dbbfbd9f07fbfd



## Task A. String manipulation (function 'string_manip')
##   This function accepts any string as input. It should return a string that is manipulated in a variety of
##  ways defined in the specifications
def string_manip(s):
<<<<<<< HEAD
    s = s.strip().upper().replace(' ', '#').replace('UMSI', '')
    if len(s) == 1:
        return s
    s = s[::-1]
    return(s)
=======
    pass # Replace with your code!
>>>>>>> 9262dd73635b8feee19f15ccd3dbbfbd9f07fbfd



## Task B. Dictionaries and sorting (function 'name_counts')
## The function name_counts takes as input a list of strings. It should return a list of tuples, where each tuple contains a UNIQUE string from the list and the count of that string's occurrences in the list.

def name_counts(names):
<<<<<<< HEAD
    d = {}
    for name in names:
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1
    lst = list()
    for key, val in d.items():
        lst.append((key, val))

    lst = sorted(lst, key = operator.itemgetter(0))
    lst = sorted(lst, key = operator.itemgetter(1), reverse = True)

    return(lst)
=======
    pass # Replace with your code!
>>>>>>> 9262dd73635b8feee19f15ccd3dbbfbd9f07fbfd

## TASK C. Iteration and accumulation
## Complete the definition of the function build_acronym.
def build_acronym(ls):
<<<<<<< HEAD
    ac = ""
    for word in ls:
        ac = ac + word[0].upper()
    return(ac)
=======
    pass # Replace with your code!
>>>>>>> 9262dd73635b8feee19f15ccd3dbbfbd9f07fbfd


## TASK D. Python user-defined types
## Below we've provided a Python class definition representing a house. Add a method to the class called determine_size that returns a string determined by the size of the house.
class House(object):
    def __init__(self,color,street,number):
        self.house_color = color
        self.street_name = street
        self.address_number = number

    def __str__(self):
        return "This is a {} house, located at {} {}.".format(self.house_color,self.address_number,self.street_name)

    def determine_size(self):
<<<<<<< HEAD
        if self.house_color == 'blue':
            size = "big"
            return(size)
        elif self.house_color == 'red':
            size = "small"
            return(size)
        else:
            size = "medium"
            return(size)
=======
        pass # Replace with your code!


>>>>>>> 9262dd73635b8feee19f15ccd3dbbfbd9f07fbfd






################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected):
  score = 0;
  if got == expected:
    score = 3
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
    total = 0
    print()
    print ('Task 0: Info')
<<<<<<< HEAD
    task0()
=======
    task0)
>>>>>>> 9262dd73635b8feee19f15ccd3dbbfbd9f07fbfd
    print ('Task A: string manipulation'
    """\nEach OK is worth 3 points.""")
    total += test(string_manip(' Colleen van Lent'), 'TNEL#NAV#NEELLOC')
    total += test(string_manip('  276 876'), '678#672')
    total += test(string_manip('!UMSI!'), '!!')
    total += test(string_manip('UMSI'), '')
    total += test(string_manip(''), '')

    print("\n\n")
    print('Task B: name_counts'
    """ \nEach OK is worth 3 points.""")
    total += test(name_counts([]), [])
    total += test(name_counts(['Christopher']), [('Christopher', 1)])
    total += test(name_counts(['Christopher', 'Christopher', 'Christopher']), [('Christopher', 3)])
    total += test(name_counts(['Eddie', 'Bacon', 'Christopher', 'Christopher', 'Christopher', 'Bacon', 'Bacon']), [('Bacon', 3), ('Christopher', 3), ('Eddie', 1)])
    total += test(name_counts(['Bacon', 'Catherine', 'Eddie', 'Bacon', 'Becca', 'Christopher', 'Bacon', 'Eddie', 'Mike']), [('Bacon', 3), ('Eddie', 2), ('Becca', 1), ('Catherine', 1), ('Christopher', 1), ('Mike', 1)])
    total += test(name_counts(["Cai","Cai","Bette","Ferdinand","Ferdinand","Emmett","Bette","Cai","Bette","Emmett",]),[("Bette",3),("Cai",3),("Emmett",2),("Ferdinand",2)])

    print("\n\n")
    print('Task C: build_acronym'
    """ \nEach OK is worth 3 points.""")
    total += test(build_acronym(["thank","goodness","ice","freezes"]),"TGIF")
    total += test(build_acronym(["pretty","yurts","tumble","hard","on","northerly slopes"]),"PYTHON")
    total += test(build_acronym(["yay"]),"Y")
    total += test(build_acronym([]),"")
    total += test(build_acronym(["Hooray","Ice cream"]),"HI")

    print("\n\n")
    print('Task D: determine_size'
    """ \nEach OK is worth 3 points.""")
    nh = House("blue","State",206)
    nh2 = House("red","Main",506)
    nh3 = House("purple","Liberty",281)
    nh4 = House("brick","Kingsley",110)
<<<<<<< HEAD

=======
    
>>>>>>> 9262dd73635b8feee19f15ccd3dbbfbd9f07fbfd
    total += test(nh.determine_size(),"big")
    total += test(nh2.determine_size(),"small")
    total += test(nh3.determine_size(),"medium")
    total += test(nh4.determine_size(),"medium")

    print("\n\n")
    print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
