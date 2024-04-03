# AVL Tree Visualization

![avl_tree_screenshot](https://github.com/wawelgreg/avl-tree-visualization/assets/141285799/a3e3dda2-b430-4831-90bd-4a0664737e4e)

Insertion and automatic balancing of AVL tree with live visualization on terminal screen.

## Info

- Meant to be run in shell/terminal.
- Uses Python [Curses](https://docs.python.org/3/howto/curses.html).

## Background

This program utilizes Python Curses to show live each phase of the AVL Tree after each insertion and rotation. This program can do both single and double rotations, as it's a requirement really, for an AVL Tree to actually function and balance properly. This project helped me finally understand how AVL Tree balancing functions.

## Usage

To run, call the executable python file *avl_tree.py* from the command line:

```
./avl_tree.py
```

The constants at the bottom of *avl_tree.py* can be modified as you please:
```
TIME, TIME_END = 1, 3
LEVEL_SPACER = 2
IN_LIST = [0,1,2,3,4,5,6,7,-1,-2,-99,-40,-20,8,9]
```

*TIME*: float: This number constant corresponds to the wait time between frame. Pretty much a tickrate of sorts. A higher value will result in slower progression of maze generation.
(1 = One second)

*TIME_END*: float: This number value corresponds to the duration of display of the final resulting generated AVL Tree before automatic closing of the curses wrapper() function and program closing.
(1 = One second)

*LEVEL_SPACER*: int: This integer value corresponds to the depth of spacing from the left for each branch in the AVL Tree matrix used for visualization and printing. The spacing left of the visualized node is calculated by multiplication of the depth of the AVL Tree traversal with the *LEVEL_SPACER* integer constant.
```
LEVEL_SPACER = 0
```
![image](https://github.com/wawelgreg/avl-tree-visualization/assets/141285799/d48ea42d-045b-4421-9d13-2d544fb2b75d)

```
LEVEL_SPACER = 1
```
![image](https://github.com/wawelgreg/avl-tree-visualization/assets/141285799/70a01f05-8968-4777-b32e-7839b3d59c34)

```
LEVEL_SPACER = 5
```
![image](https://github.com/wawelgreg/avl-tree-visualization/assets/141285799/28408835-a029-460e-ba49-ed9ccb17d7fc)

*IN_LIST*: list(float/int): This list of numbers is iterated and used to insert nodes into the AVL Tree with payload of corresponding value from list. 
