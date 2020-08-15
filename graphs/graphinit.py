def initGraph():
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [6, 7],
        6: [5, 7],
        7: [5, 6],
        8: [9],
        9: [8, 10],
        10: [9, 11],
        11: [10, 12],
        12: [11]
    }

    return graph


def print_dfs(dfs_result):
    preorder = dfs_result[0]
    postorder = dfs_result[1]
    parent = dfs_result[2]
    print("===Preorder===\n")
    for v in preorder:
        print(v)
    print('\n')

    print("===Postorder===\n")
    for v in postorder:
        print(v)
    print('\n')

    print("===Parent===\n")
    print(parent)
    print('\n')

def print_bfs(bfs_result):
    parent = bfs_result[0]
    visited = bfs_result[1]
    print("===Parent===\n")
    print(parent)
    print('\n')

    print("===Visited===\n")
    for v in visited:
        print(v)

