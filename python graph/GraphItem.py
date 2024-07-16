class GraphItem:
    def __init__(self, metadata: dict, labels: set[str]):
        self.metadata = metadata
        self.labels = labels
    
    def __repr__(self):
        return f'metadata:{self.metadata} \t labels:{self.labels}'