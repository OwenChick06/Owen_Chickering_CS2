import random

origname = input("What is your name ")
name = origname.split(" ")
names = str(origname)

def firstname(name):
    return(name[0])   

def reversename(origname):
    stringlength=len(origname) 
    reversed_name=origname[stringlength::-1]
    return(reversed_name)

def middlename(name):
    num_names = len(name)
    if num_names >= 3:
        middle_name = name[1:-1]
        return middle_name

def lastname(name):
    length = len(name)
    return(name[length-1])

def scramble(name):
    random.shuffle(name)  
    newname = ''.join(name)
    random.shuffle(newname)
    return ''.join(newname)

def vowels(names):
    vowels = "aeiouAEIOU"
    count = len([char for char in names if char in vowels])
    return count

def consonant(origname):
    notallowed = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", " "] 
    chars = []
    for i in origname:
        if i not in notallowed:
            chars.append(i)
    newname = "".join(chars)
    iteration = {}
    for c in newname:
        if c in iteration:
            iteration[c] += 1
        else:
            iteration[c] = 1
    return iteration

def lowecase(origname):
    result_string = ''
    for char in origname:
        if 'A' <= char <= 'Z':
            result_string += chr(ord(char) + 32)
        else:
            result_string += char
    return result_string

def uppercase(origname):
    result = ''
    for char in origname:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def booleancheck(origname):
    if "-" in origname:
        result = True
    else:
        result = False
    return result

def shuffleword(origname):
    characters = list(origname)
    random.shuffle(characters)
    return ''.join(characters)

def initials(origname):
  intial = (origname)
  namelist = intial.split()
  initials = ""
  for letter in namelist:  
    initials += letter[0]
  return initials

def main():
    print(firstname(name))
    print(middlename(name))
    print(lastname(name))
    print(reversename(origname))
    print(vowels(names))
    print(consonant(origname))
    print(lowecase(origname))
    print(uppercase(origname))
    print(booleancheck(origname))
    print(shuffleword(origname))
    print(initials(origname))

main()

