import sys
import time
import itertools

# Fungsi untuk menghitung shortest path menggunakan algoritma TSP
def tsp(graph, start):
    all_nodes = set(graph.keys())
    all_nodes.remove(start)
    min_distance = sys.maxsize
    shortest_path = []

    # Generate semua kemungkinan permutasi jalur
    permutations = list(itertools.permutations(all_nodes))
    total_permutations = len(permutations)

    # Iterasi melalui setiap permutasi jalur
    for i, permutation in enumerate(permutations):
        current_path = [start] + list(permutation) + [start]
        current_distance = 0

        # Menghitung jarak total pada jalur saat ini
        for j in range(len(current_path) - 1):
            src = current_path[j]
            dest = current_path[j + 1]
            if src in graph and dest in graph[src]:
                current_distance += graph[src][dest]
            else:
                current_distance = sys.maxsize
                break

        # Memperbarui shortest path jika ditemukan jarak yang lebih pendek
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = current_path

        # Menampilkan hasil setiap iterasi
        print(f"Iterasi {i+1}/{total_permutations}: Path = {current_path}, Distance = {current_distance}")

    return shortest_path, min_distance
# Fungsi untuk menghitung shortest path menggunakan algoritma Dijkstra
def dijkstra(graph, start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_node = None
        min_distance = sys.maxsize

        # Memilih node dengan jarak terpendek yang belum dikunjungi
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_node = node
                min_distance = distances[node]

        visited.add(min_node)

        # Memperbarui jarak minimum ke node-nodes tetangga
        for neighbor in graph[min_node]:
            new_distance = distances[min_node] + graph[min_node][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        # Menampilkan hasil setiap iterasi
        print(f"Visited: {visited}, Distances: {distances}")

    return distances


# Fungsi untuk menjalankan program
def main():
    # Graph berdasarkan informasi yang diberikan
    graph = {
        'a': {'b': 12, 'c': 10, 'g': 12},
        'b': {'a': 12, 'c': 8, 'd': 12},
        'c': {'b': 8, 'a': 10, 'd': 11, 'e': 3},
        'd': {'b': 12, 'c': 11, 'e': 11},
        'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
        'f': {'e': 6, 'g': 9},
        'g': {'a': 12, 'e': 7, 'f': 9}
    }
    print("Shortest Path Calculation")
    print("1. TSP (Travelling Salesman Problem)")
    print("2. Dijkstra")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        start_node = input("Enter the starting node: ")
        start_time = time.time()
        shortest_path, min_distance = tsp(graph, start_node)
        end_time = time.time()
        print("\nMunawir_F55121017_A")
        print("Shortest Path")
        print("Path:", shortest_path)
        print("Distance:", min_distance)
        print("Time taken:", end_time - start_time, "seconds")
    elif choice == 2:
        start_node = input("Enter the starting node: ")
        start_time = time.time()
        distances = dijkstra(graph, start_node)
        end_time = time.time()
        print("\nMunawir_F55121017_A")
        print("Shortest Distances")
        for node, distance in distances.items():
            print(f"Node: {node}, Distance: {distance}")
        print("Time taken:", end_time - start_time, "seconds")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()