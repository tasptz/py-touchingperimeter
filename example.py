import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

from touchingperimeter import *

def main():
    #random.seed(0)
    bin = Rect(0, 0, 100, 100)
    fig = plt.figure()
    for i in range(2):
        ax = fig.add_subplot(1, 2, 1 + i, aspect='equal')
        ax.set_xlim(bin.x - 1, bin.w + 1)
        ax.set_ylim(bin.y - 1, bin.h + 1)
        ax.set_axis_off()

    def plot_rect(r, ax=0, idx=0, **kwargs):
        ax = fig.axes[ax]
        fill = kwargs.pop('fill', False)
        ec = kwargs.pop('ec', 'k')
        o = []
        if 'text' in kwargs:
            text = kwargs.pop('text')
            o.append(ax.text(r.x + r.w // 2, r.y + r.h // 2, text))
        o.append(ax.add_patch(patches.Rectangle((r.x, r.y), r.w, r.h, fill=fill, ec=ec, **kwargs)))
        return o

    boxes = []
    for i in range(100):
        w = random.randint(1, 10)
        fh = random.randint(2, 4)
        boxes.append(Box(w, w * fh))

    # sort rects by area
    boxes.sort(reverse=True)
    # rects packed and plotted
    packed_plotted_rects = []

    packer = Packer(bin, rotating=True)

    def pack(frame_nr):
        if boxes:
            b = boxes.pop(0)
            packer.pack(b)
            l = len(packed_plotted_rects)
            for p in packer.packed[l: ]:
                packed_plotted_rects.extend(plot_rect(p, 0, fill=True, fc='b', ec='k'))
        return packed_plotted_rects + [o for p in packer.free_rects for o in plot_rect(p, 1)]

    fa = FuncAnimation(fig, pack, interval=100, blit=True, repeat=True)
    plt.show()

if __name__ == '__main__':
    main()