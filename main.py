#There are five trees in Jack's front yard.
#He checks each tree to find out how tall it is in 
 #iches and writes the height on a sheet of paper. 
 #Jack's list: 98, 94, 41, 96, and 11. What is the
  #average height of a tree in Jack's front yard

tree_height_1 = int(input("enter tree height:"))
tree_height_2 = int(input("enter tree height:"))
tree_height_3 = int(input("enter tree height:"))
tree_height_4 = int(input("enter tree height:"))
tree_height_5 = int(input("enter tree height:"))

avg = (tree_height_1+tree_height_2+tree_height_3+tree_height_4+tree_height_5) / 5
print(f"The average height of the your trees is:{avg}")