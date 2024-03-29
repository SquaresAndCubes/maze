#Pthon maze explorer
#Brent Vaalburg CSCI280
#Davenport University 3/18/2018
#Week 2 Assignment
#Dependencies:
#Python 3.6 w/ standard library

#******************************************#
#RUN WITH -h to see more options***********#
#******************************************#

#import double ended queue function
from collections import deque
import argparse


#maze from fig 2.37 in class text book converted to 0's and 1's
#0 for path 1 for wall

maze_a = [[1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
[1,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
[1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
[1,0,1,0,1,0,1,0,0,0,0,0,1,0,1],
[1,0,1,0,1,0,1,1,1,1,1,0,1,0,1],
[1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
[1,1,1,0,1,1,1,1,1,1,1,1,1,0,1],
[1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
[1,0,1,1,1,0,1,0,1,1,1,1,1,1,1],
[1,0,1,0,1,0,1,0,0,0,0,0,0,0,1],
[1,0,1,0,1,0,1,1,1,1,1,1,1,0,1],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[1,1,1,1,1,0,1,0,1,0,1,0,1,0,1],
[1,0,0,0,1,0,1,0,1,0,1,0,1,0,1],
[1,0,1,1,1,0,1,1,1,0,1,0,1,0,1],
[1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
[1,1,1,1,1,1,1,1,1,0,1,1,1,1,1]]



#function to Convert maze to a searchable tree

def mazetree(maze):
    #Define maze dimensions(so code doesnt run rampant)
    h = len(maze)
    w = len(maze[0]) if h else 0
    #define input for the tree
    tree = {(i, j): [] for j in range(w) for i in range(h) if not maze[i][j]}
    #take input and create a dictionary graph of keys which represent nodes adjacenies
    for r, c in tree.keys():
        if r < h - 1 and not maze[r + 1][c]:
            #Down
            tree[(r, c)].append(("D", (r + 1, c)))
            #Up
            tree[(r + 1, c)].append(("U", (r, c)))
        if c < w - 1 and not maze[r][c + 1]:
            #Right
            tree[(r, c)].append(("R", (r, c + 1)))
            #Left
            tree[(r, c + 1)].append(("L", (r, c)))
    #return the tree so the dfs_search function can use it
    return tree

#function for performing the dfs search on the tree that was created

def dfs_search(maze, top, steps):
    #define the entrace and exit of the maze by 2d array coord
    enter, exit = (16, 9), (0, 7)

    if top == True:
        enter, exit = (0, 7), (16,9)
    #create double ended queue for storing nodes to be explored
    dbl_end_queue = deque([("", enter)])
    #unordered collection for positions already seen or visited
    seen = set()
    #run the mazetree function to give dfs search the tree data
    tree = mazetree(maze)
    #while loop for exploring nodes in the queue
    while dbl_end_queue:
        path, curr_loc = dbl_end_queue.pop()
        #check to see if it has found the end yet
        if curr_loc == exit:
            print(path)
            return path#output of directions for path
        #or if the location has already been visited it continues
        if curr_loc in seen:
            continue
        #add location already visited to seen collection
        seen.add(curr_loc)
        #appends the queue with the path traveled already and adds last direction move made, and queues the next location
        for dir, adj in tree[curr_loc]:
            dbl_end_queue.append((path + dir, adj))
        if steps == True:
            print(path)

    print('There is no Path!')

#pretty display of maze
def print_maze():
    print('FIGURE 2.37 MAZE\n')
    chars = [' ', '*']
    for row in maze_a:
        for item in row:
            print(chars[item], end=' ')
        print()
    print('\n')

####################COMMAND LINE ARGUMENTS w/ Argparse############################

parser = argparse.ArgumentParser(description='Display more information.')
parser.add_argument('--tree', action='store_true', help='Displays maze tree.')
parser.add_argument('--top', action='store_true', help='Solve maze from top.')
parser.add_argument('--steps', action='store_true', help='Show steps taken.')
args = parser.parse_args()

#Main loop with options from command
def main():
    #Tree Switch
    if args.tree:
        print(mazetree(maze_a))
    #Solve from top of maze
    elif args.top:
        print_maze()
        print('Solved from top entrance:\n')
        dfs_search(maze_a, top=True, steps=False)
    elif args.steps:
        print_maze()
        print('Solved from bottom entrance:\n')
        dfs_search(maze_a, top=False, steps=True)
    #Default
    else:
        print_maze()
        print('Solved from bottom entrance:\n')
        dfs_search(maze_a, top=False, steps=False)

main()


