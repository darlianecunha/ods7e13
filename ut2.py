import numpy as np
import matplotlib.pyplot as plt

def plot_radar_chart(scores):
    categories = [f"7.{i+1}" for i in range(len(scores))]
    values = scores + scores[:1]  # Repeat the first value to close the circle
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='teal', alpha=0.25)
    ax.plot(angles, values, color='teal', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    return fig

