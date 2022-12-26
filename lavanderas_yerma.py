#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

text_path = "data/yerma_cuadro2_acto2.txt"

with open(text_path) as f:
    lines = f.readlines()

dialogue = [line for line in lines if line.startswith("Lavandera")]
pattern = [line.split(" ")[1][0] for line in dialogue]
pattern = [1 if char == "I" else int(char) for char in pattern]
# add initial and final chorus (all sing) as 0
pattern.insert(0, 0)
pattern.append(0)
characters = sorted(set(pattern))

fig, ax = plt.subplots(figsize=(12, 4))
ax.scatter(range(len(pattern)), pattern, s=75, c=pattern, cmap="Set2")
ax.plot(pattern, zorder=0, color="lightgray", linestyle="dotted")
for i in characters:
    ax.hlines(i, 0, len(pattern) - 1, zorder=0, color="lightgray")

ax.hlines(7, 1, 40, zorder=1, color="darkorange")
ax.text((40 - 1) / 2, 7.5, s="diálogo", horizontalalignment="center")
ax.hlines(7, 41, len(pattern) - 1, zorder=1, color="orchid")
ax.text(
    41 + (len(pattern) - 1 - 41) / 2, 7.5, s="canción", horizontalalignment="center"
)

ax.set_yticklabels(
    [
        "",
        "todas",
        "lavandera 1",
        "lavandera 2",
        "lavandera 3",
        "lavandera 4",
        "lavandera 5",
        "lavandera 6",
    ]
)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_xlim(-1, len(pattern))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
plt.tick_params(left=False)
plt.tight_layout()

plt.savefig("lavanderas_yerma.png", dpi=300)
