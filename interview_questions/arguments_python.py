#default argument
def my_function(name = "friend"): #parameter
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function() #no argement given : answer: Hello friend
my_function("Linus")
print()
#keyword argument
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy") #keyword argument
print()

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
print()

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")
print()

def fun(**kwargs):
  for k, val in kwargs.items():
    print("%s == %s" % (k, val))


# Driver code
fun(s1='Geeks', s2='for', s3='Geeks')