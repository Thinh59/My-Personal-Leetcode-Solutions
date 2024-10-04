import pandas as pd

activity = pd.DataFrame({"player_id" : [1, 1, 2, 3, 3], "device_id" : [2, 2, 3, 1, 4], "event_date" : ["2016-03-01", "2016-05-02", "2017-06-25", "2016-03-02", "2018-07-03"], "games_played" : [5, 6, 1, 0, 5]})
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """res = activity.sort_values(by = "event_date")
    res = res.groupby(by = "player_id").head(1).reset_index()
    return res.sort_values(by = "player_id")[["player_id", "event_date"]].rename(columns = {"event_date" : "first_login"})"""
    return activity.groupby("player_id")["event_date"].min().reset_index(name = "first_login")
print(game_analysis(activity))