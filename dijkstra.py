#----------------------------------------------------------
# Lab #6: Dijkstra's Shortest-Path Tree
#
# Date: 25-Nov-2026
# Authors:
#           A01754717 Nestor Daniel Huidobro Aguilar 
#           A01754754 Alexis Maximiliano Alva Martínez
#----------------------------------------------------------


type WeightedGraph = dict[str, set[tuple[str, float]]]

def dijkstra_spt(
            initial:str,
            graph:WeightedGraph) -> tuple[dict[str,float],WeightedGraph]:
      #Costo infinito para todos, 0 para el inicial

      costs:dict[str,float] = {v:float('inf') for v in graph}
      costs[initial] = 0

      #parent[v] = de quien llegue a v, peso de esa arista
      parent:dict[str, tuple[str,float]] = {}
      visited:set[str] = set()

      while len(visited) < len(graph):
            #No visitadods y alcanzables
            cannditates = [v for v in graph
                           if v not in visited and costs[v] != float('inf')]
            if not cannditates:
                  break
            #Menor costo;empate, el primero alfabeticamente
            current = min(cannditates, key=lambda v: (costs[v], v))
            visited.add(current)

            #Relajar aristas
            for neighbor, weight in graph[current]:
                  if neighbor in visited:
                        continue
                  new_cost = costs[current] + weight
                  if new_cost < costs[neighbor]:
                        costs[neighbor] = new_cost
                        parent[neighbor] = (current, weight)

            #Armar el arbol (no dirigido) con los padres
            tree:WeightedGraph = {v:set() for v in graph}
            for child, (father,weight) in parent.items():
                  tree[father].add((child,weight))
                  tree[child].add((father,weight))

      return costs, tree

if __name__ == '__main__':
    g: WeightedGraph = {'A': {('B', 5), ('C', 10), ('E', 6)},
                        'B': {('A', 5), ('D', 2)},
                        'C': {('A', 10), ('D', 1), ('E', 3)},
                        'D': {('B', 2), ('C', 1), ('E', 4)},
                        'E': {('A', 6), ('C', 3), ('D', 4)}}
    print(dijkstra_spt('A', g))