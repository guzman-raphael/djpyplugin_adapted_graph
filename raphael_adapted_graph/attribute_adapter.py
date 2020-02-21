import datajoint as dj
import networkx as nx


class GraphAdapter(dj.AttributeAdapter):

    attribute_type = 'longblob'  # this is how the attribute will be declared

    @staticmethod
    def get(obj):
        # convert edge list into a graph
        return nx.Graph(obj)

    @staticmethod
    def put(obj):
        # convert graph object into an edge list
        assert isinstance(obj, nx.Graph)
        return list(obj.edges)


graph = GraphAdapter()
