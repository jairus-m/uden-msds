'''
COMP 4401
Homework 7 - Strings & Sets

General Homework Guidelines: 
- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing. 
- Use a consistent coding style. 
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs. 
- Every function must include a docstring for documentation (see: 
   https://realpython.com/documenting-python-code/). This docstring should include:
     - 1 or 2 lines describing what the function does
     - input parameters, their types and what they are for
     - return data type and what it is
- All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.
'''
#--------------------------------------------------------------------------#

###-----------------###
###-----Strings-----###
###-----------------###

# All functions must be able to handle edge cases like an empty string or list and 
# strings and lists with a single character.

from helper_functions import sortNumbers
import math
import unittest

# 1. Write a function, called checkPalindrome, that takes a string as an argument and 
# determines if the string is a palindrome. The function should return True if it is
# a palindrome, False otherwise.
# A palindrome is a string that is the same forward and backward like: level or noon.
# Make sure your function works on the string "rats live on no evil star"
# (10 points)

def checkPalindrome(word : str):
    """
    This function checks if a word is a palindrome which is a word
    that is the same when read forwards and backwards.
    Args:
        word (string) : word to check
    Returns:
        boolean : True or False
    """
    try:
        # check word argument validity
        if len(word) > 1 and type(word) == str:
            # make all letters lowercase, remove spaces and check if the same forwards/backwards
            if word.lower().replace(" ", '') == word[::-1].lower().replace(" ", ''):
                return True
            else:
                return False
        else:
            raise TypeError
    except:
        print('Please input a string with more than 1 character!')

# 2. Create a function, called sortStrings, that takes a list of strings and sorts the list 
# based on the length of string from lower to higher. Cannot use built-in sorting functions
# (10 points)


def sortStrings(words_list : list):
    """
    This function sorts a list of strings by length of string in ascending order.
    Args:
        words_list (list) : list of strings
    Returns
        list : list with strings in ascending order based on length of string
    """
    # make sure all elements in words_list is a string
    words = [str(word) for word in words_list]
    
    ordered_words = []
    
    # iterate through an ordered list len(word) in words
    for i in sortNumbers([len(word) for word in words]):
        # loop though each word a
        for word in words:
            # if the word has the same length as i, append to ordered_list (remove duplicate words as well in this process)
            if i == len(word) and word not in ordered_words:
                ordered_words.append(word)
    return ordered_words


# 3. Write a function, called mixedString, that takes a word string and computes a list of 
# all words generated by a single swap of letters in the word. 
# For example ‘swap’ should return [‘pwas’, ‘wsap’, ‘sawp’, swpa’] (notice that letters are 
# only swapped with their immediate neighbors only, i.e. you don’t have ‘waps’)
# (10 points)


def mixedString(word:str):
    """
    This function takes a word string and computes a list of 
    all words generated by a single swap of letters in the word. 
    Args:
        word : string
    """
    try:
        if type(word) != str or len(word) == 0:
            raise TypeError

        word = str(word)

        mixedWords = []

        # swapping first and last letter since for loop does not swap last index with first index
        word_to_swap = [letter for letter in word]

        # assigned this way so that the swap happens at the same time
        word_to_swap[0], word_to_swap[len(word)-1] = word_to_swap[len(word)-1], word_to_swap[0]
        new_word = ''.join(word_to_swap)
        if new_word not in mixedWords and new_word != word:
            mixedWords.append(new_word)

        # swapping all other letters
        for i in range(len(word) - 1):
            word_to_swap = list(word)  # Convert the word to a list to allow swapping
            word_to_swap[i], word_to_swap[i + 1] = word_to_swap[i + 1], word_to_swap[i]
            new_word = ''.join(word_to_swap)
            if new_word not in mixedWords and new_word != word:
                mixedWords.append(new_word)  # Convert the list back to a string and add to the list
        return mixedWords
    except:
        print('Please provide a valid string argument.')


# 4. Write a function, called reversePhrase, that takes a string of words and returns the 
# string with the words in reverse order. You cannot use any library methods or functions 
# like .split(). 
# For example if the sentence is: “I love python”, then the function returns: “python love 
# I”
# (10 points)


def reversePhrase(sentence : str):
    """
    This function takes a string of words and returns the 
    string with the words in reverse order.
    Args:
        sentence (string) : sentence to reverse
    Returns:
        reversed_sentence (string) : reverse sentence
    """
    try:
        # check validity of argument
        if type(sentence) != str or len(sentence) == 0:
            raise TypeError
        words = []

        while len(sentence) > 0:
            # find where the first space occurs
            space_index = sentence.find(" ")
            # if space not found at all, append string to words and break from loop
            if space_index == -1:
                words.append(sentence)
                break
            # use the space index to grab a word
            words.append(sentence[:space_index])
            # each time a word is grabbed and placed in words list, slice out that word from the sentence 
            # and iterate until len(sentence) == 0
            sentence = sentence[space_index + 1:]
        
        # construct the reverse phrase
        reversed_sentence = ' '.join(words[::-1])
        return reversed_sentence
    except TypeError:
        print('Please provide a valid string argument.')  

# 5. Write a function, called uniqueLetters, that takes a string as an argument and returns 
# a new string with no duplicated letters. 
# For example if the word is: “application” then the function returns “aplicton”
# (10 points)

def uniqueLetters(word : str):
    """
    Takes a word and returns the word without any duplicate letters.
    Args:
        word (string) 
    Returns:
       string : word without duplicate letters
    """
    try:
        if type(word) != str or len(word) == 0:
                raise TypeError
        unique_letters = []
        # list comprehension to append unique letters to unique_letters if not already in unique_letters
        [unique_letters.append(letter.lower()) for letter in word if letter not in unique_letters]
        return ''.join(unique_letters)
    except TypeError:
        print('Please input a valid string argument.')  



###--------------###
###-----Sets-----###
###--------------###

# 6. Create a function, called setComp, that uses Python set comprehension to generate a 
# set of pair tuples consisting of all of the integers between 1 and 10,000 and the square 
# of that number but only if the square is divisible by 3 and return that set. 
# For example (3, 9) would be in the set since 3^2 is 9 and 9 is divisible by 3.
# You should have 3333 tuples in your set.
# (10 points)

def setComp():
    """
    This function contains a set of tuples (x, x^2) if
    x^2 is divisible by 3.
    Args:
        None
    Returns
        set : set of tuples with the stated constraints
    """
    return {(i, i**2) for i in range(1,10000) if i**2 % 3 == 0}

# 7. Write a function, called minMaxSet, that takes a set of numbers and returns the 
# minimum and maximum value in the set as a tuple. Cannot use the built-in functions 
# min()/max(). Hint: You may want to use math.inf and -math.inf
# (10 points)

def minMaxSet(numbers : set):
    """
    Takes a set of numbers and returns the smallest element and the largest element as a tuple (smallest, largest).
    Args:
      numbers (set) : set of numbers 
    Returns:
      (tuple) : (minimum, maximum)
    """
    try:
        # if empty list, return []
        if len(numbers) == 0:
            return () 
        # go through each value in numbers and compare one by one to find minimum
        minimum = math.inf
        for num in numbers:
            if num < minimum:
                minimum = num
            else:
                pass
        # go through each value in numbers and compare one by one to find maximum
        maximum = -math.inf
        for num in numbers:
            if num > maximum:
                maximum = num
            else:
                pass
        return (minimum, maximum)
    except TypeError:
        print('Please input a set of numbers.')
        


# 8. Write a function, uniqueElems, that given a list of values, determines if all elements 
# are unique (no repeated values). If elements are unique return True and False otherwise. 
# You must use a set to perform this task.
# (10 points)

def uniqueElems(elements_list : list):
    """
    This function takes a list of elements and determines if all
    elements in the list are unique.
    Args:
        elements_list (list) : list of elements
    Returns:
        boolean : True or False (based on uniqueness of list of elements)
    """
    # make all elements strings so that integers and string numbers are seen as duplicates
    try:
        # this will error out the try block if len(elements_list) == 0 
        test_zero = 1 / len(elements_list)
            
        elements_list = [str(element) for element in elements_list]

        # compare length of the elements_list to the set of the elements_list to determine uniqueness
        if len(elements_list) == len(set(elements_list)):
            return True
        else:
            return False

    except:
        print('Please provide a list of elements.')
# 9. Write a function, called distinctElems, that takes two sets, A and B, and returns a new 
# frozen set containing elements that are in either A or B but NOT in the intersection of A 
# and B. 
# (10 points)

def distinctElems(a : set, b : set):
    """
    Takes two sets, a and b, and returns the elements and a and b that
    do not intersect with the other set.
    Args:
        a (set) : set of elements
        b (set) : set of elemets
    Returns:
        frozenset : set of non-intersecting values of set a and b
        
    """
     # if not a set, cannot perform set operations
    try:
        # c is the set 'a' without overlapping values of 'b'
        c = a-b
        # b-a is the set 'b' without overlapping values of 'a'
        # creating a new set of non-intersecting values of set 'a' and set 'b'
        for num in b-a:
            c.add(num)
        return frozenset(c)
    except TypeError:
        return 'Please input two non-empty sets as arguments.'


# 10. Write a function, called addsToK, that given an integer k and a list of n unordered 
# integers A, determines if there is a distinct pair of integers in A that add up to k. 
# Return True if a pair of integers add up to k, return False other.
# You must perform this task using sets. 
# (10 points)

def addsToK(k : int, nums : list):
    """
    This function takes an integer, k, and a list of unnordered intefers, nums, and determines if
    there is a distinct pair of integers in nums that can add up to k.
    Args:
      k (int) : integer value
    Return:
      boolean : True or False
    """
    try:
        # check validity of arguments
        [int(num) for num in nums]
        if type(k) != int or len(nums) == 0:
            raise TypeError
        # create x,y pairs based of unique values of nums
        x = set(nums)
        y = set(nums)

        # create all possible combinations of pairs based off numbers in nums
        pairs = []
        for num_x in x:
                for num_y in y:
                    # if x not equal to y and (x,y) not already in list, pair
                    if num_x != num_y and (num_x, num_y) not in pairs:
                        pairs.append((num_x, num_y))

        # create a list of sums based off the x,y pairs generated
        sums = []
        for pair in pairs:
            sums.append(pair[0] + pair[1])

        # create a set(sums) which contains all possible sums based of pairs created by the list, nums
        possible_sums = set(sums)

        # check if argument, k, is in the sums list
        if k in possible_sums:
            return True
        else:
            return False
    except:
        print("Please provide an integer argument for 'k' and a non-empty list of integers for 'nums'.")


class TestMain(unittest.TestCase):
    """This is a new class, TestMain, that is a subclass of the TestCase Class
    from the unittest package
    
    Tests:
    ----------------------------------------
        test_Palindrome: test for correct output
        test_sortStrings: test for correct output
        test_mixedString: test for correct output
        test_reversePhrase: test for correct output
        test_uniqueLetters: test for correct output
        test_setComp: test for correct output
        test_minMaxSet: test for correct output
        test_uniqueElems: test for correct output
        test_distinctElems: test for correct output
        test_addsToK: test for correct output
    """
    def test_Palindrome(self):
        """
        If a palindrome, expect True. Otherwise, False.
        """
        # Case 1: Non-palindrome
        self.assertEqual(False, checkPalindrome('Team Dream'))
        # Case 2: Palindrome with spaces
        self.assertEqual(True, checkPalindrome('rats live on no evil star'))
        # Case 3: Palindrome with capitalization 
        self.assertEqual(True, checkPalindrome('Too hot to hoot'))

    def sortStrings(self):
        """
        Expect the order of strings to be from smallest, 'a' to the largest, 'supercalifragilisticexpialidocious'.
        """
        self.assertEqual(['a', 'be', 'apple', 'jairusmartinez', 'supercalifragilisticexpialidocious'], sortStrings(['supercalifragilisticexpialidocious', 'apple', 'jairusmartinez', 'be', 'a']))

    def mixedString(self):
        """
        Expect all unique single, neighboring letter swaps in a word. Should not return the word itself or duplicates.
        """
        # Case 1: Class example.
        self.assertEqual(['pwas', 'wsap', 'sawp', 'swpa'], mixedString('swap'))
        # Case 2: 'doom' should return 3 words since 'doom' (switched o's) should be excluded
        self.assertEqual(['mood', 'odom', 'domo'], mixedString('doom'))
        # Case 3: Empty list of given a string with all same letters, 'aaa'
        self.assertEqual([], mixedString('aaa'))

    def reversePhrase(self):
         """
         Expect a sentence to be reversed.
         """
         self.assertEqual('Python love I', reversePhrase('I love Python'))

    def test_uniqueLetters(self):
        """
        Expect letters that appear more than once in a word to be eliminated. 
        """
        # Case 1: Class example + another example w/ capitilization difference.
        self.assertEqual('aplicton', uniqueLetters('Application'))
        self.assertEqual('teamdr', uniqueLetters('TeamDream'))

        # Case 2: 'supercalifragilisticexpialidocious'
        # Expect 13 unique letters
        self.assertEqual(len(set([x for x in 'supercalifragilisticexpialidocious'])), len(uniqueLetters('supercalifragilisticexpialidocious')))  
        # Unique letters should be the exact same 
        self.assertEqual(set([x for x in 'supercalifragilisticexpialidocious']), {x for x in uniqueLetters('supercalifragilisticexpialidocious')})    

    def test_setComp(self):
        """
        Expect a unique set with (i, i^2) where i = [1,10000] and i^2 divisible by 3.
        """
        # Case 1: Expect (3,9) to be in this set.
        self.assertEqual(True, (3,9) in setComp())

        # Case 2: Expect the length of the set to be 3333.
        self.assertEqual(3333, len(setComp()))

    def test_minMaxSet(self):
        """
        Expect (min integer, max integer) given a set of integers.
        """
        self.assertEqual((-15, 100), minMaxSet({-1, -15, 100, 68}))

    def test_uniqueElems(self):
        """
        Expect True if list contains all unique elements. False otherwise.
        """
        self.assertEqual(True, uniqueElems([1, 2, 'a', 'v', [1, 2]]))
        self.assertEqual(False, uniqueElems([1, 2, 'a', 'v', 1]))

    def test_distinctElems(self):
        """
        Expect a frozenset of elements in two different sets that DO NOT intersect.
        """
        # Case 1: Since using set operations, want to make sure that we handle list objects as arguments.
        self.assertEqual('Please input two non-empty sets as arguments.', distinctElems([1, 2, 3], [3, 4, 5]))
        # Case 2: Overlap of these two sets is 2 and 3 so expect forzenset({1, 4, 5})
        self.assertEqual(frozenset({1, 4, 5}), distinctElems({1, 2, 3}, {2, 3, 4, 5}))
        # Case 3: If two sets contain the same values, expect nothing to be reuturned. 
        self.assertEqual(frozenset(), distinctElems({1, 2, 3}, {1, 2, 3}))

    def test_addsToK(self):
        """
        If list, nums, contains two distinct elements (pairs without duplicates) that add up to integer k, return True. Otherwise, False.
        """
        self.assertEqual(False, addsToK(k=4, nums=[1, 2, 2, 2, 4]))
        self.assertEqual(False, addsToK(k=7, nums=[1, 2, 3, 7]))
        self.assertEqual(True, addsToK(k=7, nums=[1, 2, 3, 5, 7, 4]))


if __name__ == '__main__':
    unittest.main()