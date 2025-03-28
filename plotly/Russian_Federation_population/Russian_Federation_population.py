df = pd.read_csv(r"Распределение_по_возрастам.csv", delimiter=';')


def color(x):
    if x > 0:
        return 'Green'
    elif x < 0:
        return 'Red'
    else:
        return 'Black'


# Начальный график
fig = go.Figure(data=[go.Scatter(x=df['Unnamed: 0'], y=df['2019'], mode='markers',
                                 name='Численность населения РФ по возрастным группам',
                                 marker=dict(color=list((df['2019'] - df['2018']).apply(color)), size=20))],
                layout_yaxis_range=[0, np.max(df.drop('Unnamed: 0', axis=1)) + 1000])


frames = []
for i in range(1, len(df.columns)):
    frames.append(go.Frame(name=str(df.columns[i]),
                           data=[go.Scatter(x=df['Unnamed: 0'], y=df[df.columns[i]], mode='markers',
                                            name='Численность населения РФ по возрастным группам',
                                            marker=dict(color=list((df[df.columns[i]] - df[df.columns[i-1]] if i != 1 else pd.Series([0] * (len(df.columns) - 1))).apply(color)), size=20))]))

steps = []
for i in range(1, len(df.columns)):
    step = dict(label=str(df.columns[i]), method="animate", args=[[str(df.columns[i])]])
    steps.append(step)

sliders = [dict(currentvalue={"prefix": "", "font": {"size": 20}},
                len=0.9, x=0.1, pad={"b": 10, "t": 50}, steps=steps, active=len(df.columns) - 2)]

fig.update_layout(title='Численность населения РФ по возрастным группам',
                  xaxis_title="Возрастная группа",
                  yaxis_title="Численность населения",
                  updatemenus=[dict(direction="left",
                                    pad={"r": 10, "t": 80},
                                    x=0.1,
                                    xanchor="right",
                                    y=0,
                                    yanchor="top",
                                    showactive=False,
                                    type="buttons",
                                    buttons=[dict(label="►", method="animate", args=[None, {"fromcurrent": True}]),
                                             dict(label="❚❚", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False},
                                                                                               "mode": "immediate",
                                                                                               "transition": {"duration": 0}}])])])
fig.update_traces(hoverinfo="all", hovertemplate="Возрастная группа: %{x}<br>Численность группы: %{y}")
fig.layout.sliders = sliders
fig.frames = frames
fig.show()
