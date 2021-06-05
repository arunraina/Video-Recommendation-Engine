 Recommender system
#recommendation based on scaled watch time ,Avg Watch Time, share, love & comments score

import pandas as pd
import numpy as np
K= pd.read_csv("github.csv")
K.head(2)

from sklearn import preprocessing
#The transformation is given by:
#X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
#X_scaled = X_std * (max - min) + min

#MinMaxScaler subtracts the minimum value in the feature and then divides by the range


min_max_scaler = preprocessing.MinMaxScaler()
videos5 = min_max_scaler.fit_transform(K[['Average_Watch_time','Share','Comment','Spammy_Views','Love']])

videos5_norm = pd.DataFrame(videos5, columns=['Average_Watch_time','Share','Comment','Spammy_Views','Love'])
videos5_norm.head(2)

#Getting the normalised data

K[['norm_Average_Watch_time','norm_Share','norm_Comment','norm_Spammy_Views','norm_Love']] = videos5_norm

#renaming the columns

K['score3'] = K['norm_Average_Watch_time'] * 0.6+ K['norm_Share']*0.1 + K['norm_Comment']*0.1 +K['norm_Love']*0.2 - K['norm_Spammy_Views']*0.1
videos5_scored = K.sort_values(['score3'], ascending= False)


#Alogirth of the Engine
videos5_scored[['Creator_Name', 'norm_Average_Watch_time', 'score3','norm_Share','norm_Love']]
videos5_scored.to_csv('RecommendationEng3=6New')
#Videos acording to the algorithm

scored3 = K.sort_values('score3', ascending=False)

plt.figure(figsize=(25,4))

ax = sns.barplot(x=scored3['Creator_Name'].head(10), y=scored3['score3'].head(10), data=scored3, palette='bright')

#plt.xlim(3.55, 5.25)
plt.title('Top Recommended Videos- RE3', weight='bold')
plt.xlabel('Name', weight='bold')
plt.ylabel('Scored3', weight='bold')
plt.savefig('scored8_videos.png')
print('scored8_videos')


#Plotting videos against the score
scored9.to_csv('RecommendationEng3New')
