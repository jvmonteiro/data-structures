from graphinit import initGraph
import graphutils

print("Creating graph...")
graph = initGraph()

dfs_result = graphutils.dfs(graph)
graphutils.print_dfs(dfs_result)

bfs_result_1 = graphutils.bfs(graph, 1)
graphutils.print_bfs(bfs_result_1)

bfs_result_2 = graphutils.bfs(graph, 8)
graphutils.print_bfs(bfs_result_2)