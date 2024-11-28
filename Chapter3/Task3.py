import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([[1], [3]])
w1, w2 = np.array([[3], [5], [1]]), np.array([[0], [2], [2]])

points_1d = v1 @ np.random.normal(-4, 4, (1, 100))
plt.scatter(points_1d[0, :], points_1d[0, :])
plt.savefig("output_plot.png")


points_2d = w1 @ np.random.normal(-4, 4, (1, 100)) + w2 @ np.random.normal(-4, 4, (1, 100))
# points_2d_add = w1 @ np.random.normal(-4, 4, (1, 100)) + w1 * 0.5 @ np.random.normal(-4, 4, (1, 100))

# fig = go.Figure(data=[go.Scatter3d(
#     x=points_2d_add[0, :],
#     y=points_2d_add[1, :],
#     z=points_2d_add[2, :],
#     mode='markers')])
# fig.show()


fig = go.Figure( data=[go.Scatter3d(x=points_2d[0, :], y=points_2d[1, :], z=points_2d[2, :], 
                                    mode='markers', marker=dict(size=6,color='black') )])

fig.update_layout(margin=dict(l=0,r=0,b=0,t=0))
fig.show()