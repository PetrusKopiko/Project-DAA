import json
import random

# Function to create a random weighted graph
def create_random_graph(num_nodes, num_edges):
    adjacency_list = {str(i): [] for i in range(num_nodes)}
    edges_added = 0
    while edges_added < num_edges:
        # Randomly select two nodes and a weight
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        weight = random.randint(1, 10)
        # Avoid self-loops and duplicate edges
        if u != v and (v, weight) not in adjacency_list[str(u)]:
            adjacency_list[str(u)].append((str(v), weight))
            adjacency_list[str(v)].append((str(u), weight))
            edges_added += 1
    return {
        "nodes": num_nodes,
        "edges": num_edges,
        "adjacency_list": adjacency_list
    }

# Create a list of graphs with increasing sizes
graph_data = {}
sizes = [
    (10, 15), (10, 20), (20, 30), (20, 50), (30, 60), (30, 90), (40, 100),
    (50, 125), (50, 150), (60, 180), (70, 200), (80, 240), (90, 270),
    (100, 300), (200, 500), (300, 700), (400, 1000), (500, 1250),
    (600, 1500), (700, 1750), (800, 2000), (900, 2250), (1000, 2500),
    (2000, 5000), (3000, 7500), (4000, 10000), (5000, 12500),
    (10000, 20000), (20000, 50000), (30000, 70000), (50000, 100000),
    (70000, 150000), (100000, 200000), (150000, 300000), (200000, 400000),
    (250000, 500000), (300000, 600000), (350000, 700000), (400000, 800000),
    (450000, 900000), (500000, 1000000)
]

 # Format: (num_nodes, num_edges)

for i, (num_nodes, num_edges) in enumerate(sizes):
    graph_key = f"graph_{i+1}"
    graph_data[graph_key] = create_random_graph(num_nodes, num_edges)

# Save the dataset to a JSON file
with open("test.json", "w") as f:
    json.dump(graph_data, f, indent=4)

print("Dataset generated and saved to test.json")
