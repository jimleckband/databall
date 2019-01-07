import os
import pandas as pd
import numpy as np

import statsmodels.api as sm

os.chdir(.../...)

team_records = pd.read_csv('team_history_record.csv')
team_bat_stats = pd.read_csv('team_history_batting_stats.csv')

team_stats = pd.merge(team_records, team_bat_stats, left_on=['team_id','year'],right_on=['team_id','year'])

team_stats = team_stats[(team_stats['split_id'] == 0)]

X = team_stats['h']
y = team_stats['w']

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

model.summary()

X = team_stats[['k','h','d','t','hr','sb','cs','bb']]
