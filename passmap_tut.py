import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns

df = pd.read_csv('messibetis.csv')

<<<<<<< HEAD
df['x'] = df['x'] * 1.2
df['y'] = df['y'] * 0.8
df['endX'] = df['endX'] * 1.2
df['endY'] = df['endY'] * 0.8

fig, ax = plt.subplots(figsize=(13.5, 8))
=======
df['x'] = df['x']*1.2
df['y'] = df['y']*0.8
df['endX'] = df['endX']*1.2
df['endY'] = df['endY']*0.8

fig,ax = plt.subplots(figsize=(13.5,8))
>>>>>>> 4c379b5711fe8a4387c49bbb57f7cba8e41c0b02
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

pitch = Pitch(pitch_type='statsbomb',
              pitch_color='#22312b',
              line_color='#c7d5cc')
pitch.draw(ax=ax)
plt.gca().invert_yaxis()

<<<<<<< HEAD
=======

>>>>>>> 4c379b5711fe8a4387c49bbb57f7cba8e41c0b02
for x in range(len(df['x'])):
    s_X, e_X, s_Y, e_Y = df['x'][x], df['endX'][x], df['y'][x], df['endY'][x]
    if df['outcome'][x] == "Successful":
        plt.plot((s_X, e_X), (s_Y, e_Y), color='g')
<<<<<<< HEAD
        plt.scatter(s_X, s_Y, color='g')
=======
        plt.scatter(s_X,s_Y, color='g')
>>>>>>> 4c379b5711fe8a4387c49bbb57f7cba8e41c0b02
    if df['outcome'][x] == "Unsuccessful":
        plt.plot((s_X, e_X), (s_Y, e_Y), color='r')
        plt.scatter(s_X, s_Y, color='r')

plt.title('Messi Pass Map vs Real Betis', color='w', size=20)
<<<<<<< HEAD
plt.show()
=======
plt.show()
>>>>>>> 4c379b5711fe8a4387c49bbb57f7cba8e41c0b02
