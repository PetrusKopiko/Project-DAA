import json
import networkx as nx
import timeit
import matplotlib.pyplot as plt

dataset_path = "test.json"
with open(dataset_path, "r") as f:
    graph_data = json.load(f)

def run_dijkstra(graph, source=0):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(int(node), int(neighbor), weight=weight)
    nx.single_source_dijkstra(G, source)

node_counts = []
edge_counts = []
runtimes = []

for graph_key, graph_info in graph_data.items():
    nodes = graph_info["nodes"]
    edges = graph_info["edges"]
    adjacency_list = graph_info["adjacency_list"]
    
    start_time = timeit.default_timer()
    run_dijkstra(adjacency_list)
    end_time = timeit.default_timer()
    
    runtime = end_time - start_time
    
    node_counts.append(nodes)
    edge_counts.append(edges)   
    runtimes.append(runtime)

plt.figure(figsize=(10, 6))
plt.plot(node_counts, runtimes, marker='o', label="Runtime by Nodes")
plt.xlabel("Number of Nodes")
plt.ylabel("Time (seconds)")
plt.title("Dijkstra's Algorithm Runtime Analysis")
plt.grid()
plt.legend()
plt.show()
