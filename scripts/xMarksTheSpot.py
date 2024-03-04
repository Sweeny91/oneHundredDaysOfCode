line1 = ["__","️__","️__"]
line2 = ["__","__","️__"]
line3 = ["__","__","__"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where on the grid do you want to bury the treasure? (A1-C3) ") # Where do you want to put the treasure?


# Solution 1: Nested if-statements
# if position[1] == '1':
#   if position[0] == 'A':
#     line1 = ["X","️⬜️","️⬜️"]
#   elif position[0] == 'B':
#     line1 = ["⬜️","️X","️⬜️"]
#   elif position[0] == 'C':
#     line1 = ["⬜️","️⬜️","️X"]
# elif position[1] == '2':
#   if position[0] == 'A':
#     line2 = ["X","️⬜️","️⬜️"]
#   elif position[0] == 'B':
#     line2 = ["⬜️","️X","️⬜️"]
#   elif position[0] == 'C':
#     line2 = ["⬜️","️⬜️","️X"]  
# elif position[1] == '3':
#   if position[0] == 'A':
#     line3 = ["X","️⬜️","️⬜️"]
#   elif position[0] == 'B':
#     line3 = ["⬜️","️X","️⬜️"]
#   elif position[0] == 'C':
#     line3 = ["⬜️","️⬜️","️X"]  

# Solution 2: Indices
# grab the letter on the grid and cast to lower case
letter = position[0].lower()
# create list grid letters for comparison
abc = ["a", "b", "c"]
# create a varaible for the index of the letter on the grid for map reference
letter_index = abc.index(letter)
# create a variable for the index of the number on the grid for map reference
number_index = int(position[1]) - 1
# Change the array value at the given gridmark using a nested list reference
map[number_index][letter_index] = "X"

# Print where the treasure is buried back to the user
#print(f"{line1}\n{line2}\n{line3}")
print(map)