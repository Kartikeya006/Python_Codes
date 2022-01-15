home_distance = input()
home_distance = list(map(int, home_distance.split()))
tree_distance = input()
tree_distance = list(map(int, tree_distance.split()))
apple_oranges = input()
apple_oranges = list(map(int, apple_oranges.split()))
apple_co = input()
apple_co = list(map(int, apple_co.split()))
orange_co = input()
orange_co = list(map(int, orange_co.split()))
apple = 0
orange = 0
apple_range = abs(tree_distance[0]-home_distance[0])
orange_range = abs(tree_distance[1]-home_distance[1])
for i in list(apple_co):
    if apple_range > i and i> 0:
        apple = apple+1
    else:
        continue
for i in list(orange_co):
    if i < 0 and abs(i) > orange_range:
        orange = orange+1
    else:
        continue
print(apple)
print(orange)
