import numpy as np
import matplotlib.pyplot as plt

# Create a 256‑pixel grayscale ramp
img = np.tile(np.arange(256), (50, 1))  # shape (50, 256)

print("mean:", img.mean(), "std:", img.std())

plt.imshow(img, cmap="gray")
plt.title("Grayscale ramp"); plt.axis("off")
