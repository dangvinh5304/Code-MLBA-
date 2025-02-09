import matplotlib.pyplot as plt
import numpy as np

# Input data
x = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]).T
y = np.array([[2, 4, 3, 6, 9, 12, 13, 15, 18, 20]]).T


# Function to calculate b1 and b0
def calculateb1b0(x, y):
    xbar = np.mean(x)
    ybar = np.mean(y)
    x2bar = np.mean(x ** 2)
    xybar = np.mean(x * y)

    b1 = (xbar * ybar - xybar) / (xbar ** 2 - x2bar)
    b0 = ybar - b1 * xbar
    return b1, b0


# Calculate b1 and b0
b1, b0 = calculateb1b0(x, y)
print("b1 =", b1)
print("b0 =", b0)


# Function to visualize data and regression line
def showGraph(x, y, b1, b0, title="", xlabel="", ylabel=""):
    plt.figure(figsize=(14, 8))

    # Plot original data points
    plt.plot(x, y, 'r-o', label="Value sample")

    # Calculate regression line
    y_pred = b1 * x + b0
    plt.plot(x, y_pred, 'b-', linewidth=2, label="Regression line")

    # Determine axes limits
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)

    # Mean y
    ybar = np.mean(y)
    plt.axhline(ybar, linestyle='--', linewidth=4, label="Mean (ȳ)")

    # Set plot limits and labels
    plt.axis([x_min * 0.95, x_max * 1.05, y_min * 0.95, y_max * 1.05])
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.text(x_min, ybar * 1.01, "mean", fontsize=16)
    plt.legend(fontsize=15)
    plt.title(title, fontsize=20)
    plt.show()


# Show graph
showGraph(x, y, b1, b0,
          title="Giá trị Y theo X",
          xlabel="Giá trị X",
          ylabel="Giá trị Y")