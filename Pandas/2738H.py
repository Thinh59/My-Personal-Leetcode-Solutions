import pandas as pd
files = pd.DataFrame({"file_name" : ["draft1.txt", "draft2.txt", "draft3.txt"], "content" : ["The stock exchange predicts a bull market which would make many investors happy.", "The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market.", "The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market. As always predicting the future market is an uncertain game and all investors should follow their instincts and best practices."]})
def count_occurences(files: pd.DataFrame) -> pd.DataFrame:
    bull_count = files["content"].str.contains("bull", case = False).sum()
    bear_count = files["content"].str.contains("bear", case = False).sum()

    return pd.DataFrame({"word" : ["bull", "bear"], "count" : [bull_count, bear_count]})
print(count_occurences(files))