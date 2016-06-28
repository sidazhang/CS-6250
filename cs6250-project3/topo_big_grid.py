# A --- B --- C --- D --- E
# |           |           |
# F           G           H
# |           |           |
# I --- J --- K --- L --- M
# |           |           |
# N           O           P
# |           |           |
# Q --- R --- S --- T --- U

topo = \
    {
        'A': ['B', 'F'],
        'B': ['A', 'C'],
        'C': ['B', 'D', 'G'],
        'D': ['C', 'E'],
        'E': ['D', 'H'],
        'F': ['A', 'I'],
        'G': ['C', 'K'],
        'H': ['E', 'M'],
        'I': ['F', 'J', 'N'],
        'J': ['I', 'K'],
        'K': ['G', 'J', 'L', 'O'],
        'L': ['K', 'M'],
        'M': ['H', 'L', 'P'],
        'N': ['I', 'Q'],
        'O': ['K', 'S'],
        'P': ['M', 'U'],
        'Q': ['N', 'R'],
        'R': ['Q', 'S'],
        'S': ['O', 'R', 'T'],
        'T': ['S', 'U'],
        'U': ['T', 'P']
    }
