import re

# All (alphanumeric) strings

pattern1 = re.compile(r"^[\w]+$")
print(pattern1.match("sdlf204hg024").group())

# All strings ending with b

pattern2 = re.compile(r"^[\w]+b$")
print(pattern2.match("asdfasdfj23r0b").group())

# All strings of a,b such that each a follows a b

pattern3=re.compile(r"^b(ba?)+b$")
print(pattern3.match("bbbbbbbbabababab").group())

# All strings with consecutive repeated words

pattern4 = re.compile(r"^(\w+)\s+\1$")
print(pattern4.match("asldkf  asldkf").group())

# All strings that start with an integer, end with a word

pattern5 = re.compile(r"^\d+.*[a-zA-Z]+")
print(pattern5.match("123412.353fj342k0jflkjsd").group())

# All strings that have grotto and raven

pattern6 = re.compile(r"(^.*\bgrotto\b.*\braven\b.*$|^.*\braven\b.*\bgrotto\b.*$)")
print(pattern6.match("aslfdj raven sfd grotto sdlkfjdskj").group())

# Register first word of a sentence

pattern7 = re.compile(r"(^|^.*\.)\s*([a-zA-Z]+\b).*$")
print(pattern7.match("21f$h. word thingie ").group(2))





