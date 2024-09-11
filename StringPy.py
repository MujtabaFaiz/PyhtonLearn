#==========================================Strings
str = 'Hello Word'
#print(str)

#====================================== Quotes Inside Quotes
# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

#==================================== Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
#print(a)   can also use single ''''''

#==================================Strings are Arrays
a = 'Hello word'
#print(a[1])

#====================================loop with string
#for x in a:  when commnet under the loop statment getting error after writeb new line code
    #print(x)

#================================ String Length
st = 'string len'
#print(len(st) )

#===============================String Length

text = "The best things in life are free!"
#if "free" in text:
    #print("Yes")
#print("life" in text)

#==================================Check if NOT
text = "The best things in life are free!"
# if "free" not in text:
#     print("Yes")
# print("life" not in text)

#==================================Slicing string 
b = "Hello, World!"
#print(b[2:6])
 
#=================================Slice From the Start
b = "Hello, World!"
#print(b[:5])  #Hello

#================================Slice To the End
b = "Hello, World!"
#print(b[3:])  #lo, World!

#===================================Negative Indexing

b = "Hello, World!"
#print(b[-3:-2])  #lo, World!

#======================================Modify Strings

a = "Modify string"
#print(a.upper())  # Lower Case
#print(a.lower())  # Lower Case

#=====================================Remove Whitespace
a = " ABCDE               "
#print(a.strip()) #ABCDE

#====================================Replace String
#print(a.replace('B','Z'))
#print(a.replace('ABCDE','Z'))

#=================================Split String 
a = "Hello, World!"
b= a.split(",");
#print(a.split(","))
#print(b[0])

#=================================Concatenation String 
a ="H!"
b = "H@"
c= a+ " "+b;
#print(c)

#===================================String Format

age = 36
#txt = "My age is " + age
#print(txt) # Error  can only concatenate str (not "int") to str

#---------------------F-Strings
txt = f"My age is {age}"
#print(txt)

#--------------------Display the age with 2 decimals:

#txt = f"My age is {age:.2f}"
txt = f"The price is {10 * 10} dollars"
#print(txt)

#=====================================================Escape Character
#txt = "We are the so-called "Vikings" from the north." #  error
num = 56
txt = "We are the so-called \"Vikings\" from the north."  # show  duble Quote
#print(txt)
txt = "We are the so-called \'Vikings\' from the north." # show Single Quote
#print(txt)
txt = "We are the so-called \\ Vikings\\ from the north." # show Backslash
#print(txt)
txt = "We are the so-called \n Vikings from the north." # show New Line
#print(txt)
txt = "We are the so-called \r Vikings from the north." # Carriage Return --  Vikings from the north
#print(txt)
txt = "We are the so-called \t Vikings from the north." # tab
#print(txt)
txt = "We are the so-called \b Vikings from the north." # Backspace
#print(txt)

#======================================String Methods 
txt = "hello"
#print(txt.capitalize()) # Converts the first character to upper case
txt = "We are the so-calle AAAAAAAAAAAADDDDDDd from the north." 
#print(txt.casefold())# Converts string into lower case
txt = "We are the so-calle AAAAAAAAAAAADDDDDDd from the north." 
#print(txt.center()) # center expected at least 1 argument, got 0
txt = "We are the so-calle AAAAAAAAAAAADDDDDDd from the north"
#print(txt.center(1))
txt = "We are the"
#print(txt.count(""))
txt = "Hello"
#print(txt.encode(encoding="ascii"))
txt = "We are the"
#print(txt.endswith("h")) # return false id end latter is not match
txt = "H\te\tl\tl\to"
#print(txt.expandtabs(20)) # Set the tab size to 2 whitespaces:
txt = "We are the"
#print(txt.find("are"))  # Searches the string for a specified value and returns the position of where it was found
txt = "For only {price:.2f} dollars!" 
print(txt.format(price=50))
txt1 = "Format {fname} ".format(fname="MM", age = 30)
txt2 = "Format {0},  age {1}".format("MM",30)
txt3 = "Format {},  age {}".format("MM",30)
print(txt1,txt2,txt3)
