import gym
import matplotlib.pyplot as plt
import numpy as np

# 1. Initialize environment (Gym 0.17.0 API)
env = gym.make("LunarLander-v2")
env.reset()

# 2. Capture a frame
frame = env.render(mode="rgb_array")
env.close()

height, width, _ = frame.shape
num_bins = 10

# Compute exact bin boundary coordinates along the x-axis
tick_locations = [int(round(i * (width / num_bins))) for i in range(num_bins + 1)]
tick_locations[-1] = width - 1  # Clamp the rightmost boundary inside frame indices

# 3. Plot with Matplotlib
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=150)

# Render the LunarLander frame
ax.imshow(frame)

# Draw red dotted vertical lines across the full height
for x in tick_locations:
    ax.axvline(
        x=x,
        color="red",
        linestyle=":",
        linewidth=1.8,
        alpha=0.9,
    )

# 4. Configure ticks and axis labels
ax.set_xticks(tick_locations)
ax.set_xticklabels([str(x) for x in tick_locations], fontsize=9, fontweight="bold", color="white")

# Style the bottom axis spine and ticks for clear contrast against dark frames
ax.tick_params(axis="x", colors="white", length=6, width=1.5, direction="out", pad=6)
ax.spines["bottom"].set_color("white")
ax.spines["bottom"].set_linewidth(1.2)

# Hide unnecessary top/left/right spines and y-ticks (or keep them if desired)
ax.set_yticks([])
for spine in ["top", "left", "right"]:
    ax.spines[spine].set_visible(False)

# Keep the axes tight to the image bounds
ax.set_xlim(0, width - 1)
ax.set_ylim(height - 1, 0)  # Inverted so y=0 is at the top, matching pixel space

# Set background to match dark aesthetic
fig.patch.set_facecolor("#111111")
ax.set_facecolor("#111111")

plt.title("LunarLander-v2 — 10 X-Axis Bins", color="white", fontsize=12, pad=12)
plt.tight_layout()

# 5. Display or save
plt.savefig("lunar_lander_matplotlib_bins.png", facecolor=fig.get_facecolor(), bbox_inches="tight")
plt.show()