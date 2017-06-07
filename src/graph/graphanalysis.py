
if __name__ == '__main__':
    pass    
else:   
    from .graphinfo import GraphInfo
    from ..containers import Matrix, Table
    
    
import networkx as nx
    
class GraphAnalysis:
    def __init__(self):
        pass
    
    def GetAllConnectedComponent(self, graphInfo):
        A = graphInfo.GetWeightMatrixRef().dat
        G=nx.from_numpy_matrix(A)
        return nx.connected_components(G)
   
    def GetOptimalPathsFrom(self, graphInfo, node):
        A = graphInfo.GetWeightMatrixRef().dat
        G=nx.from_numpy_matrix(A)
        return nx.single_source_dijkstra_path(G,node)
        