#finished chapter 1 of fluent python
#need to read more on difference between __repr__ and __str__ to really understand it
#plan on reading the "data model" chapter the book talks about for "further reading"


#The Python Data Model
#Guido’s sense of the aesthetics of language design is amazing. I’ve met many fine language
#designers who could build theoretically beautiful languages that no one would ever use,
#but Guido is one of those rare people who can build a language that is just slightly less
#theoretically beautiful but thereby is a joy to write programs in1.
#— Jim Hugunin
#creator of Jython, co-creator of AspectJ, architect of the .Net DLR
#One of the best qualities of Python is its consistency. After working with Python for a
#while, you are able to start making informed, correct guesses about features that are
#new to you.
#However, if you learned another object oriented language before Python, you may have
#found it strange to spell len(collection) instead of collection.len(). This apparent
#oddity is the tip of an iceberg which, when properly understood, is the key to everything
#we call Pythonic. The iceberg is called the Python Data Model, and it describes the API
#that you can use to make your own objects play well with the most idiomatic language
#features.
#You can think of the Data Model as a description of Python as a framework. It formalizes
#the interfaces of the building blocks of the language itself, such as sequences, iterators,
#functions, classes, context managers and so on.
#While coding with any framework, you spend a lot of time implementing methods that
#are called by the framework. The same happens when you leverage the Python Data
#Model. The Python interpreter invokes special methods to perform basic object operations,
#often triggered by special syntax. The special method names are always spelled
#with leading and trailing double underscores, i.e. __getitem__. For example, the syntax


#@Author: Jurijus Pacalovas



from math import hypot

class Vector:
    def __new__(cls, x, y):
         print("__new__ was invoked")
         instance = object.__new__(cls)
         return instance
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __str__(self):
        return f"{self.x}x + {self.y}y"



    
    
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    def __mul__(self, mult):
        return Vector(self.x * mult, self.y * mult)

class Point (object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Point(%s, %s)' %(self.x, self.y)
    def __add__(self, other):
        return [self.x + other.x, self.y + other.y]
    def __sub__(self, other):
        return [self.x - other.x, self.y - other.y]    


def a_s_results(point1, point2):
    addition = point1.__add__(point2) # > [5, 3]
    subtraction = point1.__sub__(point2) # > [-3, 1]

point1 = Point(1, 2)
point2 = Point(4, 1)
a_s_results(point1, point2)

print(Vector(1,2) + Vector(3,4))
print(Vector(1,2) * 3)
print(abs(Vector(2,3)))


u = Vector(0,1)
v = Vector(1,0)
w = Vector(1,1)
a = u + v
print (a)

print (abs(u))

print (w)

u == v
print(u)

u != v
print(u)






import collections
from typing import NamedTuple

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Card(NamedTuple):
    rank: str
    suit: str
beer_card = Card('7', 'diamonds')
beer_card

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

#obj[key] is supported by the __getitem__ special method. To evaluate my_collec
#tion[key], the interpreter calls my_collection.__getitem__(key).
#The special method names allow your objects to implement, support and interact with
#basic language constructs such as:
#• iteration;
#• collections;
#• attribute access;
#• operator overloading;
#• function and method invocation;
#• object creation and destruction;
#• string representation and formatting;
#• managed contexts (i.e. with blocks);
    

deck = FrenchDeck()
len(deck)
deck[0]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)



def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * suit_values[card.suit]
    return rank_value * len(suit_values) + suit_values[card.suit]


#Magic and dunder
#The term magic method is slang for special method, but when talking
#about a specific method like __getitem__, some Python developers
#take the shortcut of saying “under-under-getitem” which is
#ambiguous, since the syntax __x has another special meaning2. But
#being precise and pronouncing “under-under-getitem-underunder”
#is tiresome, so I follow the lead of author and teacher Steve
#Holden and say “dunder-getitem”. All experienced Pythonistas understand
#that shortcut. As a result, the special methods are also known
#as dunder methods 3.
#A Pythonic Card Deck
#The following is a very simple example, but it demonstrates the power of implementing
#just two special methods, __getitem__ and __len__.

zero = Card('4', 'clubs')
spades_high(zero)

for card in sorted(deck, key=spades_high):
    print(card)

#The first thing to note is the use of collections.namedtuple to construct a simple class
#to represent individual cards. Since Python 2.6, namedtuple can be used to build classes
#of objects that are just bundles of attributes with no custom methods, like a database
#record. In the example we use it to provide a nice representation for the cards in the
#deck, as shown in the console session:
##>>> beer_card = Card('7', 'diamonds')
#>>> beer_card
#Card(rank='7', suit='diamonds')
#But the point of this example is the FrenchDeck class. It’s short, but it packs a punch.
#First, like any standard Python collection, a deck responds to the len() function by
#returning the number of cards in it.
#>>> deck = FrenchDeck()
#>>> len(deck)
#52
#Reading specific cards from the deck, say, the first or the last, should be as easy as deck[0]
#or deck[-1], and this is what the __getitem__ method provides.
#>>> deck[0]
#Card(rank='2', suit='spades')
#>>> deck[-1]
#Card(rank='A', suit='hearts')
#Should we create a method to pick a random card? No need. Python already has a
#function to get a random item from a sequence: random.choice. We can just use it on
#a deck instance:
#from random import choice
#choice(deck)


#Card(rank='3', suit='hearts')
#>>> choice(deck)
#Card(rank='K', suit='spades')
#>>> choice(deck)
#Card(rank='2', suit='clubs')
#We’ve just seen two advantages of using special methods to leverage the Python Data
#Model:
#1. The users of your classes don’t have to memorize arbitrary method names for standard
#operations (“How to get the number of items? Is it .size() .length() or what?”)
#2. It’s easier to benefit from the rich Python standard library and avoid reinventing
#the wheel, like the random.choice function.
#But it gets better.
#Because our __getitem__ delegates to the [] operator of self._cards, our deck automatically
#supports slicing. Here’s how we look at the top three cards from a brand new
#deck, and then pick just the aces by starting on index 12 and skipping 13 cards at a time:
#>>> deck[:3]
#[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'),
#Card(rank='4', suit='spades')]
#>>> deck[12::13]
#[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'),
#Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
#Just by implementing the __getitem__ special method, our deck is also iterable:
#>>> for card in deck: # doctest: +ELLIPSIS
#... print(card)
#Card(rank='2', suit='spades')
#Card(rank='3', suit='spades')
#Card(rank='4', suit='spades')
#...
#The deck can also be iterated in reverse:
#>>> for card in reversed(deck): # doctest: +ELLIPSIS
#... print(card)
#Card(rank='A', suit='hearts')
#Card(rank='K', suit='hearts')
#Card(rank='Q', suit='hearts')



#dom.choice, reversed and sorted. Thanks to composition, the __len__ and __geti
#tem__ implementations can hand off all the work to a list object, self._cards.
##How about shuffling?
#As implemented so far, a FrenchDeck cannot be shuffled, because it
#is immutable: the cards and their positions cannot be changed, except
#by violating encapsulation and handling the _cards attribute
##directly. In Chapter 11 that will be fixed by adding a one-line __seti
#tem__ method.
#How special methods are used
#The first thing to know about special methods is that they are meant to be called by the
#Python interpreter, and not by you. You don’t write my_object.__len__(). You write
#len(my_object) and, if my_object is an instance of a user defined class, then Python
#calls the __len__ instance method you implemented.
#But for built-in types like list, str, bytearray etc., the interpreter takes a shortcut: the
#CPython implementation of len() actually returns the value of the ob_size field in the
#PyVarObject C struct that represents any variable-sized built-in object in memory. This
#is much faster than calling a method.
#More often than not, the special method call is implicit. For example, the statement for
#i in x: actually causes the invocation of iter(x) which in turn may call x.__iter__()
#if that is available.
#Normally, your code should not have many direct calls to special methods. Unless you
#are doing a lot of metaprogramming, you should be implementing special methods
#more often than invoking them explicitly. The only special method that is frequently
#called by user code directly is __init__, to invoke the initializer of the superclass in
#your own __init__ implementation.
##If you need to invoke a special method, it is usually better to call the related built-in
#function, such as len, iter, str etc. These built-ins call the corresponding special
#method, but often provide other services and — for built-in types — are faster than
#method calls. See for example “A closer look at the iter function” on page 438 in Chapter

#Avoid creating arbitrary, custom attributes with the __foo__ syntax because such names
#may acquire special meanings in the future, even if they are unused today.
#8 |


#Emulating numeric types
#Several special methods allow user objects to respond to operators such as +. We will
#cover that in more detail in Chapter 13, but here our goal is to further illustrate the use
#of special methods through another simple example.
##We will implement a class to represent 2-dimensional vectors, i.e. Euclidean vectors like
#those used in math and physics (see Figure 1-1).
#Figure


#We will start by designing the API for such a class by writing a simulated console session
#which we can use later as doctest. The following snippet tests the vector addition pictured
#in Figure 1-1:
#>>> v1 = Vector(2, 4)
#>>> v2 = Vector(2, 1)
#>>> v1 + v2
#Vector(4, 5)
#Note how the + operator produces a Vector result which is displayed in a friendly manner
#in the console.
#How

#caller of most special methods. In the next sections we discuss the code for each special
#method.
#String representation
#The __repr__ special method is called by the repr built-in to get string representation
#of the object for inspection. If we did not implement __repr__, vector instances would
###be shown in the console like <Vector object at 0x10e100070>.
#The interactive console and debugger call repr on the results of the expressions evaluated,
#as does the '%r' place holder in classic formatting with % operator, and the !r
#conversion field in the new Format String Syntax used in the str.format method5.
#Note that in our __repr__ implementation we used %r to obtain the standard representation
#of the attributes to be displayed. This is good practice, as it shows the crucial
##difference between Vector(1, 2) and Vector('1', '2') — the latter would not work
#in the context of this example, because the constructors arguments must be numbers,
#not str.
#The string returned by __repr__ should be unambiguous and, if possible, match the
#source code necessary to recreate the object being represented. That is why our chosen
#representation looks like calling the constructor of the class, e.g. Vector(3, 4).
#Contrast __repr__ with with __str__, which is called by the str() constructor and
#implicitly used by the print function. __str__ should return a string suitable for display
#to end-users.
#If you only implement one of these special methods, choose __repr__, because when
#no custom __str__ is available, Python will call __repr__ as a fallback.
#Difference between __str__ and __repr__ in Python is a
#StackOverflow question with excellent contributions from
#Pythonistas Alex Martelli and Martijn Pieters.
##Arithmetic operators
#Example 1-2 implements two operators: + and *, to show basic usage of __add__ and
#__mul__. Note that in both cases, the methods create and return a new instance of

#Vector, and do not modify either operand — self or other are merely read. This is the
#expected behavior of infix operators: to create new objects and not touch their operands.
#I will have a lot more to say about that in Chapter 13.
#As implemented, Example 1-2 allows multiplying a Vector by a
#number, but not a number by a Vector, which violates the commutative
##property of multiplication. We will fix that with the special
#method __rmul__ in Chapter 13.
#Boolean value of a custom type
#Although Python has a bool type, it accepts any object in a boolean context, such as the
#expression controlling an if or while statement, or as operands to and, or and not. To
#determine whether a value x is truthy or falsy, Python applies bool(x), which always
#returns True or False.
##By default, instances of user-defined classes are considered truthy, unless either
#__bool__ or __len__ is implemented. Basically, bool(x) calls x.__bool__() and uses
#the result. If __bool__ is not implemented, Python tries to invoke x.__len__(), and if
##that returns zero, bool returns False. Otherwise bool returns True.
#Our implementation of __bool__ is conceptually simple: it returns False if the magnitude
#of the vector is zero, True otherwise. We convert the magnitude to a boolean
##using bool(abs(self)) because __bool__ is expected to return a boolean.
#Note how the special method __bool__ allows your objects to be consistent with the
#truth value testing rules defined in the Built-in Types chapter of the Python Standard
#Library documentation.
#A faster implementation of Vector.__bool__ is this:
#def __bool__(self):
#return bool(self.x or self.y)
#This is harder to read, but avoids the trip through abs, __abs__, the
#squares and square root. The explicit conversion to bool is needed
#because __bool__ must return a boolean and or returns either
#operand as is: x or y evaluates to x if that is truthy, otherwise the
#result is y, whatever that is.
#Overview of special methods
#The Data Model page of the Python Language Reference lists 83 special method names,
#47 of which are used to implement arithmetic, bitwise and comparison operators.
#12 | Chapter 1: The Python Data Model

#subject of Chapter 2, and implementing your own sequence will be covered in Chapter
#10 we will create a multi-dimensional extension of the Vector class.
#Thanks to operator overloading, Python offers a rich selection of numeric types, from
#the built-ins to decimal.Decimal and fractions.Fraction, all supporting infix arithmetic
#operators. Implementing operators, including reversed operators and augmented
#assignment will be shown in Chapter 13 via enhancements of the Vector example.
#The use and implementation of the majority of the remaining special methods of the
#Python Data Model is covered throughout this book.
#Further reading
#The Data Model chapter of the Python Language Reference is the canonical source for
#the subject of this chapter and much of this book.
#Python in a Nutshell, 2nd Edition, by Alex Martelli, has excellent coverage of the Data
#Model. As I write this, the most recent edition of the Nutshell book is from 2006 and
##focuses on Python 2.5, but there were very few changes in the Data Model since then,
#and Martelli’s description of the mechanics of attribute access is the most authoritative
#I’ve seen apart from the actual C source code of CPython. Martelli is also a prolific
##contributor to Stack Overflow, with more than 5000 answers posted. See his user profile
#at http://stackoverflow.com/users/95810/alex-martelli.
#David Beazley has two books covering the Data Model in detail in the context of Python
#3: Python Essential Reference, 4th Edition, and Python Cookbook, 3rd Edition, coauthored
#with Brian K. Jones.
#The Art of the Metaobject Protocol (AMOP), by Gregor Kiczales, Jim des Rivieres, and
#Daniel G. Bobrow explains the concept of a MOP (Meta Object Protocol), of which the
#Python Data Model is one example.
#Soapbox
#Data Model or Object Model?
##What the Python documentation calls the “Python Data Model”, most authors would
#say is the “Python Object Model”. Alex Martelli’s Python in a Nutshell 2e and David
##Beazley’s Python Essential Reference 4e are the best books covering the “Python Data
#Model”, but they always refer to it as the “object model”. In the English language Wikipedia,
#the first definition of Object Model is “The properties of objects in general in a
#specific computer programming language.” This is what the “Python Data Model” is
#about. In this book I will use “Data Model” because that is how the Python object model
#is called in the documentation, and is the title of the chapter of the Python Language
#Reference most relevant to our discussions.



#Magic methods
#The Ruby community calls their equivalent of the special methods magic methods. Many
#in the Python community adopt that term as well. I believe the special methods are
#actually the opposite of magic. Python and Ruby are the same in this regard: both empower
#their users with a rich metaobject protocol which is not magic, but enables users
#to leverage the same tools available to core developers.
#In contrast, consider JavaScript. Objects in that language have features that are magic,
#in the sense that you cannot emulate them in your own user-defined objects. For example,
##before JavaScript 1.8.5 you could not define read-only attributes in your Java‐
#Script objects, but some built-in objects always had read-only attributes. In JavaScript,
#read-only attributes were “magic”, requiring supernatural powers that a user of the language
#did not have until ECMAScript 5.1 came out in 2009. The metaobject protocol
##of JavaScript is evolving, but historically it has been more limited than those of Python
#and Ruby.
#Metaobjects
#The Art of The Metaobject Procotol (AMOP) is my favorite computer book title. Less
##subjectively, the term metaobject protocol is useful to think about the Python Data Model
#and similar features in other languages. The metaobject part refers to the objects that
#are the building blocks of the language itself. In this context, prococol is a synonym of
#interface. So a metaobject protocol is a fancy synonym for object model: an API for core
#language constructs.
#A rich metaobject protocol enables extending a language to support new programming
##paradigms. Gregor Kiczales, the first author of the AMOP book, later became a pioneer
#in aspect-oriented programming and the initial author of AspectJ, an extension of Java
##implementing that paradigm. Aspect-oriented programming is much easier to implement
#in a dynamic language like Python, and several frameworks do it, but the most
##important is zope.interface, which is briefly discussed in the Further reading section

import collections
import pause

import subprocess

p = subprocess.call('pytest morakot_support/tests', shell=True)
print(p)
from random import shuffle

from pynput.keyboard import Key, Listener

#Python code in one module gains access to the code in another module by the process of importing it.
#The import statement is the most common way of invoking the import machinery, but it is not the only way. modules ), only the import statement performs a name binding operation.

#Collections in Python are containers that are used to store collections of data, for example, list, dict, set, tuple etc. These are built-in collections. Several modules have been
#developed that provide additional data structures to store collections of data.



Card = collections.namedtuple('Card', ['rank', 'suit'])
#One of the best qualities of Python is its consistency. After working with Python for a
#while, you are able to start making informed, correct guesses about features that are
#new to you.
#However, if you learned another object oriented language before Python, you may have
#found it strange to spell len(collection) instead of collection.len(). This apparent
#oddity is the tip of an iceberg which, when properly understood, is the key to everything
#we call Pythonic. The iceberg is called the Python Data Model, and it describes the API
#that you can use to make your own objects play well with the most idiomatic language
#features.'JQKA'
#You can think of the Data Model as a description of Python as a framework. It formalizes
#the interfaces of the building blocks of the language itself, such as sequences, iterators,
#functions, classes, context managers and so on.
#While coding with any framework, you spend a lot of time implementing methods that
#are called by the framework. The same happens when you leverage the Python Data
#Model. The Python interpreter invokes special methods to perform basic object operations,
#often triggered by special syntax. The special method names are always spelled
#with leading and trailing double underscores, i.e. __getitem__. For example, the syntax

#obj[key] is supported by the __getitem__ special method. To evaluate my_collec
#tion[key], the interpreter calls my_collection.__getitem__(key).
#The special method names allow your objects to implement, support and interact with
#basic language constructs such as:
#• iteration;
#• collections;
#• attribute access;
#• operator overloading;
#• function and method invocation;
#• object creation and destruction;
#• string representation and formatting;
#• managed contexts (i.e. with blocks);




class FrenchDeck:
    #Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made.
    #Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.
    
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')#[] (index operator)
    #The str() function returns the string version of the given object. ... a \uNNNN espace sequence instead of unencodable Unicode; namereplace - inserts a \N{.
    #A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
#The range() function
#defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
    #
#2
#3
#4
#5
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
#2
#5
#8
#11
#14
#17
#20
#23
#26
#29
    
    #Each element or value that is inside
    #of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ] 
    suits = 'spades diamonds clubs hearts'.split()#Definition. The split()
    #method splits a string into a list using a user specified separator. When a separator isn't defined, whitespace(” “) is used.

    def __init__(self):
        #self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class
        #in python. It binds the attributes with the given arguments. The reason you need to use self. is because Python does not use the @ syntax to refer to instance attributes.
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]


        

        #For example, a card is a combination of suit and rank. 

        #Inside __str__, we can use SUITS and RANKS to map the numerical values of suit and rank to strings. For example,
        #the expression Card.SUITS[self.suit] means use the attribute suit from the object self as an index into the class attribute named SUITS, and select the appropriate string.

        #__init__ method
#"__init__" is a reseved method in python classes. It is called as a constructor in
#object oriented terminology. This method is called when an object is created from a
#class and it allows the class to initialize the attributes of the class.

    def __len__(self):
        return len(self._cards)
    # len() function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.

   # The len() function will use the __len__ method if present to query your object for it's length.
   # The normal API people expect to use is the len() method, using a . len attribute instead would deviate
   # from that norm. If the length of self. ... __len__() return that attribute.

    def __getitem__(self, position):

        #A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your
        #application and a high degree of code reusing.

#As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions. These functions are called user-defined functions.

#Defining a Function
#You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

#Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).

#Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.

#The first statement of a function can be an optional statement - the documentation string of the function or docstring.

#The code block within every function starts with a colon (:) and is indented.

#The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.
        
        return self._cards[position]

    #The Python return statement is a special statement that you can use inside a function or method to send the function's result back to the caller.
    #A return statement consists of the return keyword followed by an optional return value. The return value of a Python function can be any Python object.

    #By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.

    
    #The magic method __getitem__ is basically used for accessing list items, dictionary entries, array elements etc. ...
    #The __getitem__ method is written in a way that one can access the indexed instance attributes, such as first or last name, day, month or year of the dob, etc.

    #implements two operators: + and *, to show basic usage of __add__ and __mul__. Note that in both cases, the methods create and return a new instance
    #of Vector, and do not modify either operand—self or other are merely read.
    #This is the expected behavior of infix operators: to create new objects and not touch their operands. I will have a lot more to say about that.


    #Magic and dunder
#The term magic method is slang for special method, but when talking
#about a specific method like __getitem__, some Python developers
#take the shortcut of saying “under-under-getitem” which is
#ambiguous, since the syntax __x has another special meaning2. But
#being precise and pronouncing “under-under-getitem-underunder”
#is tiresome, so I follow the lead of author and teacher Steve
#Holden and say “dunder-getitem”. All experienced Pythonistas understand
#that shortcut. As a result, the special methods are also known
#as dunder methods 3.
#
#A Pythonic Card Deck
#The following is a very simple example, but it demonstrates the power of implementing
#just two special methods, __getitem__ and __len__.


#The first thing to note is the use of collections.namedtuple to construct a simple class
#to represent individual cards. Since Python 2.6, namedtuple can be used to build classes
#of objects that are just bundles of attributes with no custom methods, like a database
#record. In the example we use it to provide a nice representation for the cards in the
#deck, as shown in the console session:


    class Card:
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value




#One of the best qualities of Python is its consistency. After working with Python for a
#while, you are able to start making informed, correct guesses about features that are
#new to you.
#However, if you learned another object oriented language before Python, you may have
#found it strange to spell len(collection) instead of collection.len(). This apparent
#oddity is the tip of an iceberg which, when properly understood, is the key to everything
#we call Pythonic. The iceberg is called the Python Data Model, and it describes the API
#that you can use to make your own objects play well with the most idiomatic language
#features.'JQKA'
#You can think of the Data Model as a description of Python as a framework. It formalizes
#the interfaces of the building blocks of the language itself, such as sequences, iterators,
#functions, classes, context managers and so on.
#While coding with any framework, you spend a lot of time implementing methods that
#are called by the framework. The same happens when you leverage the Python Data
#Model. The Python interpreter invokes special methods to perform basic object operations,
#often triggered by special syntax. The special method names are always spelled
#with leading and trailing double underscores, i.e. __getitem__. For example, the syntax

#obj[key] is supported by the __getitem__ special method. To evaluate my_collec
#tion[key], the interpreter calls my_collection.__getitem__(key).
#The special method names allow your objects to implement, support and interact with
#basic language constructs such as:
#• iteration;
#• collections;
#• attribute access;
#• operator overloading;
#• function and method invocation;
#• object creation and destruction;
#• string representation and formatting;
#• managed contexts (i.e. with blocks);

#Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made.
    #Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

            


def __repr__(self):
        return "(%s,%s)" %(self.value, self.suit)


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'JQKA']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        for i in self.cards:
            print(i)

    def __repr__(self):
        return "Cards remaining in deck: {}".format(len(self.cards))
    
    def shuffle(self):
        if len(self.cards) == 56:
            shuffle(self.cards)
            return self.cards
        else:
            return("Only full decks can be shuffled")

    def deal(self):
        if len(self.cards) != 0:
            return self.cards.pop()
        else:
            return("All cards have been dealt")

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

    
  

  
def show(key):
    
    if key == Key.tab:
        print("good")
          
    if key != Key.tab:
        print("try again")
          
    # by pressing 'delete' button 
    # you can terminate the loop 
    if key == Key.delete: 
        return False
  
# Collect all event until released


d=Deck()
F=FrenchDeck()
print("Deck created")

print("\n \nShuffling the deck")
x=d.shuffle()
for i in x:
    print(i)
a=int(input("\n \nEnter 1 to deal the cards \n"))



 
# or #
 



for i in x:
    print(i)
b=int(input("\n\nSEcond player, Please enter any number !!!\n"))
while(a==1 and b==1):
    print(d.deal())
    print()
    print(d)
    print()
    print(f.deal())
    print()
    print(f)
    print()
    print(a)
    print()
    a=int(input("Enter 1 to deal the cards (or) any key to discontinue \n"))
   

    b=int(input("Enter 2 to deal the cards (or) any key to discontinue \n"))
   

    
    print()
    print(b)
    pause.minutes(1)
    
    
    
    
print(d.shuffle())


#out put data

x = Vector(1,2)
print(x)

vector1 = Vector(12, 8)
print(vector1)

# before implementing __str__
print(vector1) #or print(repr(vector1)) 
# __str__ implemented
print(vector1)

v = Vector(2, 3)
print(v)
v2 = Vector(4, 5)
print(v+v2)
print(v+v2*2)
print(abs(v))

v3 = Vector(6, 5)
print(bool(v3))

FrenchDeckgame = FrenchDeck()
print(FrenchDeckgame)


"""
    The class "Ccy" can be used to define money values in various currencies. A Ccy instance has the string attributes 'unit' (e.g. 'CHF', 'CAD' od 'EUR' and the 'value' as a float. 
    A currency object consists of a value and the corresponding unit.
"""   

class Ccy:

    currencies =  {'CHF': 1.0821202355817312, 
                       'CAD': 1.488609845538393, 
                       'GBP': 0.8916546282920325, 
                       'JPY': 114.38826536281809, 
                       'EUR': 1.0, 
                       'USD': 1.11123458162018}
        
    def __init__(self, value, unit="EUR"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "{0:5.2f}".format(self.value) + " " + self.unit

    def __repr__(self):
        return 'Ccy(' + str(self.value) + ', "' + self.unit + '")'

    def changeTo(self, new_unit):
        """
            An Ccy object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Ccy.currencies[self.unit] * Ccy.currencies[new_unit])
        self.unit = new_unit
            
    def __add__(self, other):
        """
            Defines the '+' operator.
            If other is a CCy object the currency values 
            are added and the result will be the unit of 
            self. If other is an int or a float, other will
            be treated as a Euro value. 
        """
        if type(other) == int or type(other) == float:
                x = (other * Ccy.currencies[self.unit])
        else:
                x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit]) 
        return Ccy(x + self.value, self.unit)


    def __iadd__(self, other):
        """
            Similar to __add__
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit])
            self.value += x
        return self

    def __radd__(self, other):
        res = self + other
        if self.unit != "EUR":
            res.changeTo("EUR")
        return res
        
        # __sub__, __isub__ and __rsub__ can be defined analogue
        

    def __mul__(self, other):
        """
            Multiplication is only defined as a scalar multiplication, 
            i.e. a money value can be multiplied by an int or a float.
            It is not possible to multiply to money values
        """
        if type(other)==int or type(other)==float:
            return Ccy(self.value * other, self.unit)
        else:
            raise TypeError("unsupported operand type(s) for *: 'Ccy' and " + type(other).__name__)  
            
    def __rmul__(self, other):
        return self.__mul__(other)
        
    def __imul__(self, other):
        if type(other)==int or type(other)==float:
            self.value *= other
            return self
        else:
            raise TypeError("unsupported operand type(s) for *: 'Ccy' and " + type(other).__name__)



"""

    The class "Ccy" can be used to define money values in various currencies. A Ccy instance has the string attributes 'unit' (e.g. 'CHF', 'CAD' od 'EUR' and the 'value' as a float. 
    A currency object consists of a value and the corresponding unit.
    """

        

class Ccy:

    currencies =  {'CHF': 1.0821202355817312, 
                       'CAD': 1.488609845538393, 
                       'GBP': 0.8916546282920325, 
                       'JPY': 114.38826536281809, 
                       'EUR': 1.0, 
                       'USD': 1.11123458162018}
    
    def __init__(self, value, unit="EUR"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "{0:5.2f}".format(self.value) + " " + self.unit

    def changeTo(self, new_unit):
        """
            An Ccy object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Ccy.currencies[self.unit] * Ccy.currencies[new_unit])
        self.unit = new_unit
            
    def __add__(self, other):
        """
            Defines the '+' operator.
            If other is a CCy object the currency values 
            are added and the result will be the unit of 
            self. If other is an int or a float, other will
            be treated as a Euro value. 
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit]) 
        return Ccy(x + self.value, self.unit)


    def __iadd__(self, other):
        """
            Similar to __add__
        """
        if type(other) == int or type(other) == float:
            x = (other * Ccy.currencies[self.unit])
        else:
            x = (other.value / Ccy.currencies[other.unit] * Ccy.currencies[self.unit])
        self.value += x
        return self

    def __radd__(self, other):
        res = self + other
        if self.unit != "EUR":
            res.changeTo("EUR")
        return res

        # __sub__, __isub__ and __rsub__ can be defined analogue


from Chapeter1game import Ccy
x = Ccy(10.00, "EUR")
y = Ccy(10.00, "GBP")


print(x + y)

import random

BOB_player=random.randint(1, 56)


print(BOB_player)

if (a==b or a==BOB_player or b==BOB_player):
    print("wrong select card")


if (a<b and a>BOB_player):
    print("Second player has won")

    

if (a>b and a>BOB_player):
    print("First player has won")


if (b<BOB_player and a<BOB_player):
    print("BOB player has won")



with Listener(on_press = show) as listener:
    listener.join()



