from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph(
    url="bolt://52.70.234.12:7687",
    username="neo4j",
    password="starts-carts-letter"
)

result = graph.query("""
MATCH (m) 
RETURN m
""")

print(result)