import psutil as pst
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# graphic config
fig, ax = plt.subplots()
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_title('CPU and Memory use')
ax.set_xlabel('TIME')
ax.set_ylabel('USE (%)')
cpu_line, = ax.plot([], [], label='CPU', color='#836FFF')
mem_line, = ax.plot([], [], label='Memory', color='#00008B')
ax.legend()

# CPU AND MEMORY TEXT VALOR
cpu_text = ax.text(0.69, 0.3, '', transform=ax.transAxes)
mem_text = ax.text(0.69, 0.6, '', transform=ax.transAxes)

# Graphic Update Function
def update_chart(frame):

    # CPU Info
    cpu_percent = pst.cpu_percent()

    # Memory Info
    memory = pst.virtual_memory()
    memory_percent = memory.percent

    # Graphic Data
    cpu_line.set_data(list(range(frame)), [cpu_percent]*frame)
    mem_line.set_data(list(range(frame)), [memory_percent]*frame)

    # Update Text Valor CPU and Memory
    cpu_text.set_text(f'CPU: {cpu_percent:.1f}%')
    mem_text.set_text(f'Memory: {memory_percent:.1f}%')

    return cpu_line, mem_line, cpu_text, mem_text

# Graphic Animation
animation = FuncAnimation(fig, update_chart, frames=100, interval=1000, blit=True)

# Line Style
for line in [cpu_line, mem_line]:
    line.set_linewidth(2)
    line.set_marker('o')
    line.set_markersize(5)

# Background Style
ax.set_facecolor('#E0FFFF')

plt.show()

