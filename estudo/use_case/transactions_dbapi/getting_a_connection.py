from sqlite3 import connect

from sqlalchemy.orm import Session, session

from estudo.connection import engine

from sqlalchemy import text

# with engine.connect() as conn:
#     query = text("select 'hello world'")
#     result = conn.execute(query)
#     print(result.all())

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
#     conn.commit()

# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
#     )

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM some_table"))
#     for x, y in result:
#         print(f'x:{x}, y:{y}')]


# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM some_table WHERE y > :y"),
#                           {"y": 2})
#     for x, y in result:
#         print(x,y)

# with engine.connect() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x,y) VALUES (:x, :y)"),
#         [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
#     )
#     conn.commit()

stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(stmt, {'y': 6})
    for x, y in result:
        print(f'x:{x}, y:{y}')
