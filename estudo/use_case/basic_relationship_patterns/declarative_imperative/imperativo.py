from sqlalchemy.orm import properties, registry, relationship

from estudo.use_case.basic_relationship_patterns.declarative_imperative.declarativo import Child, Parent


# registry.map_imperatively(
#     Parent,
#     parent_table,
#     properties={"children": relationship("Child", back_populates="parent")}
# )

# registry.map_imperatively(
#     Child,
#     child_table,
#     properties={"parent": relationship("Parent", back_populates="children")}
# )
