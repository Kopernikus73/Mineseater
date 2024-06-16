# Mineseater

## What is it?
Mineseater is similar to Minesweeper and the concept is almost the same. You check fields for bombs and hope they won't reveal a bomb that ends the game.

## How to play?
Playing Mineseater is very simple.

### Select a grid size
The grid size you can select is a number between 2 and 9. The grid will be (grid_size x grid_size) so for example (3x3). It's recommended to choose a smaller number at first.

### Set the amount of bombs
The selected amount of bombs can reach from 1 to the amount of spots - 1. So for a 3x3 grid, there are 9 spots so you can can set the amount of bombs to 1,2,3,4,5,6,7 or 8.

### Play the game
After you set everything up, you will see something similar to this:

![Mineseater_Example1](https://github.com/Kopernikus73/Mineseater/assets/128999240/5e959406-f042-40df-99f7-8f71d96a8957)

The numbers at the top are the columns and the numbers on the left are the rows.

The ">" is simply the indicator for you that you can type something. 

For checking a field for a bomb, use the format (column|row) for example 01 would be the field in column 0 and in row 1. Then press enter.


You will see something similar to this:

![Mineseater_Example2](https://github.com/Kopernikus73/Mineseater/assets/128999240/620efffa-b3f7-486e-b548-873916a29582)

The 1 in field 01 shows the number of adjacent bombs. Adjacent means direct neighboring. So 00, 11 and 02 are adjacent to 01.

### How to win the game?
To win the game, you have to check every field that has no bombs on it for a bomb.
