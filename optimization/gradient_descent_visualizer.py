"""
Gradient Descent Visualizer
============================
Interactive visualization of gradient descent on 2D functions.
Great for understanding optimization algorithms.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import Callable, Tuple, List


class GradientDescentVisualizer:
    """Visualize gradient descent optimization in 2D."""

    def __init__(
        self,
        f: Callable,
        grad_f: Callable,
        x_range: Tuple[float, float] = (-3, 3),
        y_range: Tuple[float, float] = (-3, 3),
    ):
        self.f = f
        self.grad_f = grad_f
        self.x_range = x_range
        self.y_range = y_range

    def optimize(
        self,
        x0: np.ndarray,
        lr: float = 0.1,
        n_iter: int = 50,
    ) -> List[np.ndarray]:
        """Run gradient descent and store path."""
        path = [x0.copy()]
        x = x0.copy()

        for _ in range(n_iter):
            grad = self.grad_f(x)
            x = x - lr * grad
            path.append(x.copy())

            # Early stopping if gradient is tiny
            if np.linalg.norm(grad) < 1e-6:
                break

        return path

    def plot_contour(
        self,
        path: List[np.ndarray] | None = None,
        title: str = "Gradient Descent",
    ):
        """Plot function contours with optimization path."""
        fig, ax = plt.subplots(figsize=(10, 8))

        # Create mesh grid
        x = np.linspace(*self.x_range, 100)
        y = np.linspace(*self.y_range, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.array(
            [
                [self.f(np.array([xi, yi])) for xi, yi in zip(x_row, y_row)]
                for x_row, y_row in zip(X, Y)
            ]
        )

        # Contour plot
        contour = ax.contour(X, Y, Z, levels=30, cmap="viridis", alpha=0.7)
        ax.contourf(X, Y, Z, levels=30, cmap="viridis", alpha=0.3)
        plt.colorbar(contour, ax=ax, label="f(x, y)")

        # Plot path if provided
        if path is not None:
            path = np.array(path)
            ax.plot(
                path[:, 0],
                path[:, 1],
                "ro-",
                markersize=4,
                linewidth=1.5,
                label="GD path",
            )
            ax.plot(path[0, 0], path[0, 1], "go", markersize=10, label="Start")
            ax.plot(path[-1, 0], path[-1, 1], "r*", markersize=15, label="End")

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(title)
        ax.legend()
        ax.grid(True, alpha=0.3)

        return fig, ax


# === Demo Functions ===

def rosenbrock(x: np.ndarray) -> float:
    """Rosenbrock function — classic optimization test."""
    return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2


def grad_rosenbrock(x: np.ndarray) -> np.ndarray:
    """Gradient of Rosenbrock function."""
    dx = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0] ** 2)
    dy = 200 * (x[1] - x[0] ** 2)
    return np.array([dx, dy])


def quadratic(x: np.ndarray) -> float:
    """Simple quadratic: f(x,y) = x² + 2y²"""
    return x[0] ** 2 + 2 * x[1] ** 2


def grad_quadratic(x: np.ndarray) -> np.ndarray:
    """Gradient of quadratic."""
    return np.array([2 * x[0], 4 * x[1]])


if __name__ == "__main__":
    # Demo with quadratic function
    viz = GradientDescentVisualizer(quadratic, grad_quadratic)

    # Run optimization from different starting points
    starts = [np.array([2.5, 2.5]), np.array([-2.0, 1.5])]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for ax, x0 in zip(axes, starts):
        path = viz.optimize(x0, lr=0.2, n_iter=30)
        viz.plot_contour(path, title=f"Start: {x0}")

    plt.tight_layout()
    plt.savefig("gradient_descent_demo.png", dpi=150)
    plt.show()

    print(f"Final point: {path[-1]}")
    print(f"Final value: {quadratic(path[-1]):.6f}")
