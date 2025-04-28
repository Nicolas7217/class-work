#1
sport = ["football", "basketball"]
favorite = input("What is your favorite sport: ")
sport += favorite
print(sport.append(favorite))
sport.sort()
print(sport)

#2
subjects = ["maths", "science", "history", "geography", "languages", "business"]
dislike = input("which subject do you dislike the most: ")
subjects.remove(dislike)
print(subjects)

#3
colors = ["red", "blue", "yellow", "green", "pink", "white", "black", "orange", "grey", "gold"]
num1 = int(input("Enter a number 1-4: "))
num2 = int(input("Enter a number 5-9: "))
print(colors[num1:num2])

#4
numbers = [123,
            456,
            789]
for row in numbers:
    print(row)
user = int(input("Enter a 3-digit number: "))
position = numbers.index(user)
if user in numbers:
    print(position)
else:
    print("that is not in the list")