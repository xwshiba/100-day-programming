"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1: 
Input: graph = [[1, 2], [3], [3], []]
Output: [[0, 1, 3], [0, 2, 3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Example 3:
Input: graph = [[1],[]]
Output: [[0,1]]

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.
"""

# from collections import deque


# def shortestPath(graph):
#     search_queue = deque()
#     search_queue += graph[0]
#     searched = []
#     result = []
#     while search_queue:
#         current = search_queue.popleft()
#         path = [0]
#         if not current in searched:
#             if graph[current] == graph[len(graph)-2]:
#                 path.append(current)
#                 path.append(graph[current][0])
#                 result.append(path)
#             else:
#                 search_queue += graph[current]
#                 searched.append(current)
#     return result


# graph = [[1, 2], [3], [3], []]
# shortestPath(graph)

# graph = [[1], []]
# shortestPath(graph)

# graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
# shortestPath(graph)

graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7
graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 3
graph["d"] = {}
graph["d"]["fin"] = 1
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2

costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"

processed = []


def dijkstra_algo(graph, costs, parents):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs, parents


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
