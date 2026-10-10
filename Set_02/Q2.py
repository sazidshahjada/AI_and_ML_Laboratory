"""Depth-limited search and iterative deepening on a small tree."""

import matplotlib.pyplot as plt


GRAPH = {
    "S": ["A", "B"],
    "A": ["C", "D"],
    "B": ["E", "F"],
    "C": ["H"],
    "D": ["G"],
    "E": ["I"],
    "F": ["J"],
    "G": [],
    "H": [],
    "I": [],
    "J": [],
}


def depth_limited_search(start, goal, limit):
    """Return the found path, visit trace, and search result for one depth limit."""
    trace = []
    path = [start]

    def visit(node, depth):
        trace.append((node, depth))
        if node == goal:
            return "FOUND"
        if depth == limit:
            return "CUTOFF"

        cutoff = False
        for neighbor in GRAPH[node]:
            path.append(neighbor)
            result = visit(neighbor, depth + 1)
            if result == "FOUND":
                return result
            path.pop()
            cutoff |= result == "CUTOFF"

        return "CUTOFF" if cutoff else "FAILURE"

    result = visit(start, 0)
    return (path.copy() if result == "FOUND" else None), trace, result


def iterative_deepening_search(start, goal, max_depth=10):
    """Run depth-limited search repeatedly with increasing limits."""
    all_traces = []
    for limit in range(max_depth + 1):
        path, trace, result = depth_limited_search(start, goal, limit)
        all_traces.append((limit, trace, result))
        print(f"IDDFS limit={limit}: trace={trace}, result={result}")
        if result == "FOUND":
            return path, all_traces
    return None, all_traces


def plot_search_tree(path):
    """Draw the search tree and highlight the returned solution path."""
    # Fixed levels and horizontal positions keep the tree easy to read.
    positions = {
        "S": (0, 3),
        "A": (-1, 2), "B": (1, 2),
        "C": (-1.5, 1), "D": (-0.5, 1), "E": (0.5, 1), "F": (1.5, 1),
        "H": (-1.5, 0), "G": (-0.5, 0), "I": (0.5, 0), "J": (1.5, 0),
    }
    fig, ax = plt.subplots(figsize=(9, 5))
    solution_edges = set(zip(path, path[1:])) if path else set()
    for parent, children in GRAPH.items():
        for child in children:
            is_solution_edge = (parent, child) in solution_edges
            ax.annotate(
                "",
                xy=positions[child],
                xytext=positions[parent],
                arrowprops={
                    "arrowstyle": "->",
                    "color": "#e45756" if is_solution_edge else "#9aa4b2",
                    "linewidth": 2.5 if is_solution_edge else 1.3,
                    "shrinkA": 18,
                    "shrinkB": 18,
                },
            )
    for node, (x, y) in positions.items():
        ax.scatter(
            x,
            y,
            s=1_400,
            color="#f4a261" if node in (path or []) else "#dce8f5",
            edgecolor="#344054",
            zorder=3,
        )
        ax.text(x, y, node, ha="center", va="center", fontsize=11, weight="bold", zorder=4)
    ax.set_title("Search tree and IDDFS solution path")
    ax.axis("off")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    for limit in (2, 3):
        path, trace, result = depth_limited_search("S", "G", limit)
        print(f"DLS limit={limit}: path={path}, trace={trace}, result={result}")

    path, _ = iterative_deepening_search("S", "G")
    print("IDDFS final path:", path)
    plot_search_tree(path)
