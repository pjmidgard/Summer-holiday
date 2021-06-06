#Author: Jurijus Pacalovas
#Author: Jurijus Pacalovas
import collections
import pause

from random import shuffle

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

d=Deck()
F=FrenchDeck()
print("Deck created")

print("\n \nShuffling the deck")
x=d.shuffle()
for i in x:
    print(i)
a=int(input("\n \nEnter 1 to deal the cards \n"))
WON=int(input("You have won!!!"))

while(a==1):
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
    
    print()
    print(WON)
print(d.shuffle())
pause.minutes(1)
#out put data
