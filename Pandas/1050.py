import pandas as pd

actor_director = pd.DataFrame({"actor_id" : [1, 1, 1, 1, 1, 2, 2], "director_id" : [1, 1, 1, 2, 2, 1, 1], "timestamp" : [0, 1, 2, 3, 4, 5, 6]})
print(actor_director)
def actors_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    res = actor_director.groupby(by = ["actor_id", "director_id"])["timestamp"].agg(len).reset_index()
    return res
print(actors_directors(actor_director))