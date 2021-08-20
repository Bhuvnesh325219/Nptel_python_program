

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer



nltk.downloader.download('vader_lexicon')
file='data_file.xlsx'
xl=pd.ExcelFile(file)



dfs=xl.parse(xl.sheet_names[0])
print(dfs)
