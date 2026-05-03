import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


#costanti
G = 1
M0 = 0.01
c = 1


st.set_page_config(layout="centered")

st.title("Schwarszchild spacetime 2d embedding")

M = st.slider(
    "Mass (fixed)",
    min_value=float(M0),
    max_value=20.0,
    value=float(M0),
)

show_er = st.checkbox("Show Einstein-Rosen")
viewer = st.checkbox("Front view")
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

def update(M):

    ax.clear()
    #graphic settings
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    ax.set_title(
        "Schwarszchild spacetime 2d embedding",
        color="white"
    )
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    Rs = 2*G*M/c**2
    r = np.linspace(Rs, 100, 200)
    phi = np.linspace(0, 2*np.pi, 200)
    r, phi = np.meshgrid(r, phi)
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    z = 2*np.sqrt(Rs*(r-Rs))
    r2 = np.linspace(Rs, 100, 200)
    phi2 = np.linspace(0, 2*np.pi, 200)
    x2 = r2*np.cos(phi2)
    y2 = r2*np.sin(phi2)
    z2 = 2*np.sqrt(Rs*(r2-Rs))
    planet, = ax.plot([],[],[], marker = "o", color = "cyan",markersize = 5)   
    def animation(i):  
        planet.set_data([x2[i]] ,[y2[i]])
        planet.set_3d_properties([z2[i]])
        return planet
    ani = FuncAnimation(fig, animation, frames = 300, interval = 10)
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_zlim(0, 80)
    if not viewer:
        ax.view_init(60,45)
    if show_er:
        ax.plot_surface(x, y, z, cmap="inferno")
        ax.plot_surface(x, y, -z, cmap="inferno")
    else:
        ax.plot_surface(x, y, z, cmap="inferno")
update(M)

st.pyplot(fig)
