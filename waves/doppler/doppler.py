import numpy as np
import matplotlib.pyplot as plt


class Wavefront:
    """The wavefront class will hold the location and time that a
    wavefront was emitted

    """

    def __init__(self, x_emit, y_emit, w, t_emit):
        self.x_emit = x_emit
        self.y_emit = y_emit
        self.w = w           # wave propagation speed
        self.t_emit = t_emit

    def plot(self, t, ax=None, color="k"):

        if ax is None or self.t_emit > t:
            return

        r_front = self.w * (t - self.t_emit)

        # we will be drawing circles, so make an array with the polar angle
        theta = np.linspace(0.0, 2.0 * np.pi, 360, endpoint=True)

        # wavefronts are circles centered on their emitted coordinates
        x_front = self.x_emit + r_front * np.cos(theta)
        y_front = self.y_emit + r_front * np.sin(theta)

        ax.plot(x_front, y_front, color=color)


def doppler():

    # emitter velocity (in x-direction)
    vel = 1.0

    # emitter initial coords
    x_init = 0.0
    y_init = 0.0

    # wave velocity
    w = 2.0

    # wave frequency (# of peaks per second)
    f = 3.0

    # maximum time
    tmax = 10.0
    dt = 0.01

    # create a list of wavefront objects that we can refer to when we
    # want to plot things.  There are f wavefronts emitted per second,
    # so the total number of wavefronts is tmax*f
    t = 0

    wavefronts = []
    while t <= tmax:

        x_emit = x_init + vel * t
        y_emit = y_init

        wavefronts.append(Wavefront(x_emit, y_emit, w, t))

        t += 1/f

    xmax = x_init + vel * tmax

    # step forward in time (by dt) and draw any wavefronts that have
    # been emitted
    iframe = 0
    t = 0

    while t <= tmax:

        fig, ax = plt.subplots()

        x_source = x_init + vel * t
        y_source = y_init

        # plot the sources's path
        ax.plot([-1.2*xmax, 1.2*xmax], [y_init, y_init], color='k')

        # draw the source
        ax.scatter([x_source], [y_source], color='b')

        # loop over the wavefronts, and draw any that have been
        # emitted so far
        for wf in wavefronts:
            wf.plot(t, ax=ax, color="r")

        fig.subplots_adjust(left=0, right=1.0, bottom=0, top=1.0)

        ax.set_xlim(-1.2*xmax, 1.2*xmax)
        ax.set_ylim(-1.2*xmax, 1.2*xmax)
        ax.set_aspect("equal")
        ax.set_axis_off()

        fig.set_size_inches(12.8, 7.2)

        outfile = f"doppler_{iframe:04d}.png"
        fig.savefig(outfile)

        t += dt
        iframe += 1

        plt.close(fig)

if __name__ == "__main__":
    doppler()
