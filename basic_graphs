# undirected
from typing import Tuple

adjacency_list_1 = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["B", "D", "E"],
    "D": ["B", "C"],
    "E": ["C"]
}

# undirected
adjacency_matrix_1 = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

# directed
adjacency_list_2 = {
    "A": ["B", "D"],
    "B": ["F"],
    "C": ["D", "B", "F", "E"],
    "D": ["B", "E"],
    "E": [],
    "F": ["E"]
}

adjacency_list_3 = {
    "A": ["B", "D"],
    "B": ["A", "D", "C", "F"],
    "C": ["D", "B", "F", "E"],
    "D": ["A", "B", "E"],
    "E": ["D", "C", "F"],
    "F": ["B", "C", "E"]
}

"""
Sometimes, for undirected graphs you get a list of edges. 
You can easily change this list into an adjacency list with
the following function. 
"""

edges_1 = [("A", "B"), ("B", "D"), ("B", "C"), ("D", "C"), ("C", "E")]


def convert_edges_to_adj_list(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    adj_matrix = {}
    for edge in edges:
        if edge[0] not in adj_matrix.keys():
            adj_matrix[edge[0]] = [edge[1]]
        else:
            adj_matrix[edge[0]].append(edge[1])
        if edge[1] not in adj_matrix.keys():
            adj_matrix[edge[1]] = [edge[0]]
        else:
            adj_matrix[edge[1]].append(edge[0])
    return adj_matrix


"""
As an exercice I will try to convert an adjacency list 
representation to an adjacency matrix one. 
"""


def convert_adj_list_to_adj_matrix():
    pass


"""Keep in mind the difference between visiting a node and 
exploring a node. Exploring a node implies visiting all its
neighbor."""


def dfs(start: str, adj_list: dict[str, list[str]]) -> list[str]:
    """
    IMPORTANT: If the graph contains a cycle, will run in an infinite loop.
        Another condition is the existence of a reachable dead end. Otherwise,
        we will also run in an infinite loop.
    The general idea behind the dfs is to go in one direction until there are
    no more neighbors in that direction. Then start anew with the last unexplored
    neighbor."""
    stack = [start]  # LIFO
    path = []
    while stack:
        current = stack.pop()
        path.append(current)
        for neighbor in adj_list[current]:
            stack.append(neighbor)
    return path


adj_list_with_no_cycle = {
    "A": ["B"],
    "B": ["C"],
    "C": [],
    "D": ["C"]
}


def dfs_for_graph_with_cycles(start: str, adj_list: dict[str, list[str]]) -> list[str]:
    visited = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            for neighbor in adj_list[current]:
                stack.append(neighbor)
            visited.append(current)
    return visited


dfs_visited = []


def dfs_recursive(start: str, adj_list: dict[str, list[str]]) -> None:
    """Because we check that the neighbor hasn't already been visited, it works with cyclical
     graphs too."""
    dfs_visited.append(start)

    for neighbor in adj_list[start]:
        if neighbor not in dfs_visited:
            dfs_recursive(neighbor, adj_list)


def bfs(start: str, adj_list: dict[str, list[str]]) -> None:
    """The general idea is that we explore a node before visiting its neighbors."""
    bfs_visited = []
    queue = [start]    # FIFO
    while queue:
        current = queue.pop(0)
        if current not in bfs_visited:
            for neighbor in adj_list[current]:
                queue.append(neighbor)
            bfs_visited.append(current)
    print(bfs_visited)


def has_path(start: str, end: str, adj_list: dict[str, list[str]]) -> bool:
    queue = [start]
    has_path_visited = []
    while queue:
        current = queue.pop(0)
        if current == end:
            return True
        if current not in has_path_visited:
            queue.extend(adj_list[current])
            has_path_visited.append(current)
    print(has_path_visited)
    return False


# connected components

"""
I will be given a forrest. I need to count the number of connected 
components. I need two functions. One that makes a traversal and 
return the last visited node. The other one that iteratively calls
the first function, counts the number of calls and keeps a count of
already visited nodes. 
First, lets restrict input to forrest of undirected trees. Otherwise
matters will get much harder. 
"""

forrest_1 = {
    "A": ["B", "C", "D", "E"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A"],
    "E": ["B"],
    "F": ["B", "C"],
    "G": ["I", "H"],
    "H": ["G", "I"],
    "I": ["G", "H"],
    "K": ["L"],
    "L": ["K"],
    "J": []
}


def count_connected_components(forrest: dict[str, list[str]]):
    """General idea is to start a traversal. When the traversal ends, we
    jump to the next unvisited node in the list of nodes. When all nodes
    in the forrest are visited, we end the loop. Each time we need to make
    a jump, we update the count. We return the value of count."""
    count = 0
    bfs_visited = []
    nodes = list(forrest.keys())
    queue = [nodes[0]]
    while len(bfs_visited) != len(nodes):
        while queue:
            current = queue.pop(0)
            if current not in bfs_visited:
                for neighbor in forrest[current]:
                    queue.append(neighbor)
                bfs_visited.append(current)
        # queue is empty, thus we make a jump.
        count += 1
        # we start a new traversal from the last visited node.
        for node in nodes:
            if node not in bfs_visited:
                queue = [node]
                break
    print(count)

# EXERCICE : identify the largest component.


def explore_component(start, forrest):
    visited = []
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            for neighbor in forrest[current]:
                queue.append(neighbor)
            visited.append(current)
    return len(visited), visited


def largest_component(forrest: dict[str, list[str]], names: bool = False):
    """We are going to need a variation of the breadth first traversal that
    returns the number of nodes in the component. Before each jump, we check
    if the number of nodes in the current component is bigger than in the
    previous component. If it's the case, we update the var."""
    largest_component_number = 0
    largest_component_names = []

    bfs_visited = []
    nodes = list(forrest.keys())
    for node in nodes:
        if node not in bfs_visited:
            number_of_nodes_in_component, visited = explore_component(node, forrest)
            if number_of_nodes_in_component > largest_component_number:
                largest_component_number = number_of_nodes_in_component
                largest_component_names = visited
            # we only want to add the newly visited nodes, meaning the ones that weren't
            # visited in any of the previous traversals
            newly_visited = [n for n in visited if n not in bfs_visited]
            bfs_visited.extend(newly_visited)
    if names:
        print(largest_component_names)
    else:
        print(largest_component_number)


#largest_component(forrest_1, True)
#count_connected_components(forrest_1)


def shortest_path_bfs(start: str, adj_list: dict[str, list[str]], end: str) -> int:
    """The general idea is that we should make a BFS while also
     counting the distance. Here, we define distance by the number
     of edges traversed, NOT the number of nodes visited."""
    visited = []
    queue = [(0, start)]
    while queue:
        path_count, node = queue.pop(0)
        if node == end:
            return path_count
        if node not in visited:
            visited.append(node)
            for neighbor in adj_list[node]:
                queue.append((path_count+1, neighbor))
    return -1


adjacency_list_4_directed = {
    "A": ["D", "F"],
    "B": ["D"],
    "C": ["B", "E", "G"],
    "D": ["G"],
    "E": ["B"],
    "F": ["C"],
    "G": []
}



# island count
# W represents water, L represents land.
four_islands = [
    ["W", "W", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L", "L"],
    ["W", "W", "W", "W", "L", "L"],
    ["W", "W", "L", "W", "L", "L"],
    ["W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "L"]
]


# my solution
def get_neighbors(position: tuple[int, int], matrix: list[list[str]]) -> list[tuple[int, int]]:
    """Return a list of existent neighbors on land."""
    max = len(matrix) - 1
    row, col = position
    # all four possible neighbors.
    neighbors = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]
    # let's filter the non-existent neighbors
    neighbors_on_land = []
    for p in neighbors:
        r, c = p
        if r > max or c > max:
            continue
        elif r < 0 or c < 0:
            continue
        elif matrix[r][c] != "L":
            continue
        else:
            neighbors_on_land.append(p)
    print(f"in get_neighbors, neighbors: {neighbors_on_land}")
    return neighbors_on_land


def explore_island(start: tuple[int, int], matrix: list[list[str]]):
    visited: list[tuple[int, int]] = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            neighbors = get_neighbors(current, matrix)
            stack.extend(neighbors)
        print(f"explore_island, stack:{stack}")
    return visited


def count_islands_trial(matrix: list[list[str]]):
    """Two pieces of lands are part of the same island if and only if
    piece A is either at the top, the bottom, the left or the right
    of piece B. The reason why piece A (x, y) is a neighbor
    of piece B is NEVER that piece B is at (x+1, y+1) i.e positioned
    diagonally.
    The main idea is while going through the matrix, start traversals onlu
    when we are on unvisited land. Each time we start a traversal,
    we should increment the count. We should mark those pieces of lands
    as visited so we do not count the same island multiple times."""
    count = 0
    visited: list[tuple[int, int]] = []
    row_nr = -1    # the first position in matrix is (0,0)
    for row in matrix:
        row_nr += 1
        print(f"row number: {row_nr}")
        col_nr = -1    # the first position in matrix is (0,0)
        for piece_of_earth in row:
            col_nr += 1
            print(f"col number: {col_nr}")
            if piece_of_earth == "L":
                piece_of_earth_position: tuple[int, int] = row_nr, col_nr
                if piece_of_earth_position not in visited:
                    count += 1
                    visited_updated = explore_island(piece_of_earth_position, matrix)
                    visited.extend(visited_updated)
    print(count)


#count_island(four_islands)

""" Time and space complexity of island_count shouldn't be superior to O(rc)."""


# cleaner solution
def count_islands_clean(matrix: list[list[str]]):
    """The main improvements compared to my solution is that all checks are done
     in a central place. In my solution, the checking is done across 3 functions."""
    count = 0
    visited = []
    row_nr = -1
    for row in matrix:
        print(visited)
        row_nr += 1
        col_nr = -1
        for col in row:
            col_nr += 1
            if explore(matrix, row_nr, col_nr, visited):
                count += 1
    print(count)


def explore(matrix: list[list[str]],
            row_nr: int,
            col_nr: int,
            visited: list[tuple[int, int]]) -> bool:
    boundary = len(matrix) - 1  # we assume matrix is square

    # all checks done in a single place.
    if row_nr > boundary or col_nr > boundary:
        return False
    if row_nr < 0 or col_nr < 0:
        return False
    if (row_nr, col_nr) in visited:
        return False
    if matrix[row_nr][col_nr] == "W":
        return False

    visited.append((row_nr, col_nr))

    explore(matrix, row_nr, col_nr+1, visited)
    explore(matrix, row_nr, col_nr-1, visited)
    explore(matrix, row_nr+1, col_nr, visited)
    explore(matrix, row_nr-1, col_nr, visited)

    return True


#count_islands_clean(four_islands)


# min island

def min_island(matrix: list[list[str]]) -> int:
    """We have a matrix. The efficiency constraint is that all checks need
    to happen in a single place. The strategy is to start counting only if
    the matrix is on land. I will use a BFS and a get_neighbor. However, no
    checks are going to be done in the get_neighbor. To measure the area we
    will subtract the len of visited before the bfs_traversal, and after
    the traversal. Given that the same piece of land cannot be in two separate
    islands, we don't have to worry about forgetting to count one piece of land."""

    visited: list[tuple[int, int]] = []
    # we suppose that the matrix is square, otherwise we would have to multiply length
    # by width to get the biggest land possible.
    current_min_island = len(matrix)**2
    row_nr = -1
    for row in matrix:
        row_nr += 1
        col_nr = -1
        for col in row:
            col_nr += 1
            area = measure_area(matrix, row_nr, col_nr, visited)
            if area != -1 and area < current_min_island:
                current_min_island = area


def measure_area(matrix: list[list[str]],
                 row_nr: int,
                 col_nr: int,
                 visited: list[tuple[int, int]]) -> int:

    before = len(visited)

    if not existent_pos(row_nr, col_nr, matrix, visited):
        return -1
    pos = row_nr, col_nr
    queue: list[tuple[int, int]] = [pos]

    while queue:
        pos = queue.pop(0)
        for possible_near_land in get_possible_near_land(*pos):
            near_row_nr, near_col_nr = possible_near_land
            if not existent_pos(near_row_nr, near_col_nr, matrix, visited):
                continue
            queue.append((near_col_nr, near_col_nr))
        visited.append(pos)
    possible_min_island = len(visited) - before
    return possible_min_island


def get_possible_near_land(row_nr, col_nr):
    return [(row_nr, col_nr + 1),
            (row_nr, col_nr - 1),
            (row_nr+1, col_nr),
            (row_nr-1, col_nr)]


def existent_pos(row_nr: int, col_nr: int,
                 matrix: list[list[str]],
                 visited: list[tuple[int, int]]) -> bool:
    pos = row_nr, col_nr
    boundaries = range(len(matrix))
    if pos in visited:
        return False
    elif row_nr not in boundaries or col_nr not in boundaries:
        return False
    elif matrix[row_nr][col_nr] != "L":
        return False
    return True


three_islands = [
    ["L", "L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L", "W"],
    ["L", "W", "W", "W", "W", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "L", "L", "L", "L", "W"]
]

r = min_island(three_islands)   # should return 3
print(r)


# coloring problem
def brute_force():
    pass


def backtracking():
    pass


def greedy_algorithm():
    pass


