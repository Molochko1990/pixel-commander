import heapq


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def heuristic(curr_position, end_position):
    return abs(curr_position[0] - end_position[0]) + abs(curr_position[1] - end_position[1])


def a_star_search(map_matrix, start, end):
    open_list = []
    closed_list = []

    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(map_matrix) - 1) or \
                    node_position[0] < 0 or \
                    node_position[1] > (len(map_matrix[len(map_matrix) - 1]) - 1) or \
                    node_position[1] < 0:
                continue

            if map_matrix[node_position[0]][node_position[1]] != 0:
                continue

            neighbor = Node(node_position, current_node)
            if neighbor in closed_list:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if any(open_node for open_node in open_list if neighbor == open_node and neighbor.g > open_node.g):
                continue

            heapq.heappush(open_list, neighbor)

    return None
