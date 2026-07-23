from typing import Any

class GraphItem:
    def __init__(self, vertexLabel: str, metadata: dict[str, Any], labels: dict[str, Any]):
        self.vertexLabel = vertexLabel
        self.metadata = metadata
        self.labels = labels
    
    def __repr__(self):
        return f'metadata:{self.metadata} \t labels:{self.labels}'