# Enhanced-Conway-s-Game-of-Life
Implementation and analysis of Conway's Game of Life when extended with features such as Variation in Population, Weight of Nodes and Age of Nodes.

## Conway's Game of Life
### Initialisation
1. A grid of certain width (w) and height (h) is initialised as the arena.
2. Based on the initial population count, some cells are initialised (x, y) at random, such that 0 <= x <= w-1 and 0 <= y <= h-1.
3. No. of iterations (i.e. no. of generations) is decided before execution.

### Rules
1. If a cell is alive, and no. of neighbours is less than 2, then the cell dies due to loneliness.
2. If a cell is alive, and no. of neighbours is more than 3, then the cell dies due to over-crowding.
3. If a cell is alive, and no. of neighbours is 2 or 3, then the cell lives.
4. If a cell is not alive, and no. of neighbours is exactly 3, then the cell takes birth and becomes live.

5. Rules (1-4) followed for every iteration.
