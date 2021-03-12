# Stubs for networkx.classes.graphviews (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from networkx.classes import DiGraph, Graph, MultiDiGraph, MultiGraph
from networkx.classes.coreviews import ReadOnlyGraph
from typing import Any

class SubGraph(ReadOnlyGraph, Graph):
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph, filter_node: Any = ..., filter_edge: Any = ...) -> None: ...

class SubDiGraph(ReadOnlyGraph, DiGraph):
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph, filter_node: Any = ..., filter_edge: Any = ...) -> None: ...

class SubMultiGraph(ReadOnlyGraph, MultiGraph):
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph, filter_node: Any = ..., filter_edge: Any = ...) -> None: ...

class SubMultiDiGraph(ReadOnlyGraph, MultiDiGraph):
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph, filter_node: Any = ..., filter_edge: Any = ...) -> None: ...

class ReverseView(ReadOnlyGraph, DiGraph):
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph) -> None: ...

class MultiReverseView(ReadOnlyGraph, MultiDiGraph):
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph) -> None: ...

class DiGraphView(ReadOnlyGraph, DiGraph):
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph) -> None: ...

class MultiDiGraphView(ReadOnlyGraph, MultiDiGraph):
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph) -> None: ...

class GraphView(ReadOnlyGraph, Graph):
    UnionAdj: Any = ...
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph) -> None: ...

class MultiGraphView(ReadOnlyGraph, MultiGraph):
    UnionAdj: Any = ...
    root_graph: Any = ...
    graph: Any = ...
    def __init__(self, graph) -> None: ...