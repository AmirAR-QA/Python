word1 = input("Please enter a word: ")
word2 = input("Please enter the word you'd like to compare against: ")

list1 = word1
list2 = word2

a = list(list1)
b = list(list2)

d = a.copy()

for i in b:
    try:
        d.remove(i)
    except ValueError:
        pass

if len(d) == 1:
    print("If you take away the letter", d ,"from", word1 ,"then you'll be able to make the word", word2)
else:
    print("You can't make", word2 , "by taking a single letter away from", word1,"!")
