import matplotlib.pyplot as plt
import numpy as np

# area
x = np.array([[73.5, 75, 76.5, 79, 81.5, 82.5, 84, 85, 86.5, 87.5, 89, 90, 91.5]]).T
# price
y = np.array([[1.49, 1.5, 1.51, 1.54, 1.58, 1.59, 1.6, 1.62, 1.63, 1.64, 1.66, 1.67, 1.68]]).T

def calculate_b1b0(x, y):
    # Tính trung bình
    xbar = np.mean(x)
    ybar = np.mean(y)
    x2bar = np.mean(x ** 2)
    xybar = np.mean(x * y)

    # Tính b0, b1
    b1 = (xybar - xbar * ybar) / (x2bar - (xbar ** 2))
    b0 = ybar - b1 * xbar
    return b1, b0

# Tính b0, b1
b1, b0 = calculate_b1b0(x, y)
print("b1=", b1)
print("b0=", b0)


# Visualize data
def showGraph(x, y, title="", xlabel="", ylabel=""):
    plt.figure(figsize=(4, 8))
    plt.plot(x, y, 'r-o', label="price")

    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)

    # Mean of y
    ybar = np.mean(y)

    plt.axhline(ybar, linestyle='--', linewidth=4, label="mean")
    plt.axis([x_min * 0.95, x_max * 1.05, y_min * 0.95, y_max * 1.05])
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.text(x_min, ybar + 0.1, "mean", fontsize=16)
    plt.legend(fontsize=15)
    plt.title(title, fontsize=20)
    plt.show()


showGraph(x, y,
          title="Giá nhà theo diện tích",
          xlabel="Diện tích (m²)",
          ylabel="Giá nhà (tỷ VND)")