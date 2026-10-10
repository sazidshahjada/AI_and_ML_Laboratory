# AI & ML Laboratory — Solved Question Sets (1–10)

Each `Set_XX` folder contains one runnable Python script for each programming question (`Q1.py`, `Q2.py`, `Q3.py`). Viva topics are summarized in each set's `VIVA.md`.

## Setup

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

Run a script from the project root, for example:

```bash
python Set_01/Q1.py
python Set_01/Q2.py
python Set_01/Q3.py
```

Plots are displayed with Matplotlib. Close a plot window to let a script continue.

## Notes about the question sheet

- The PDF was image-based, so a few symbols/values were visually ambiguous. The scripts use the most reasonable readings: Set 2 regression data are `(1,4), (2,5), (3,8), (4,9), (5,11), (6,14)`; Set 4's `k=1,3,5` for IBk is interpreted literally; Set 5's `h(B)=S` is read as `h(B)=5`; and Set 10 assigns explicit positive costs and heuristic values as the question requests.
- The WEKA-specific questions are implemented with equivalent scikit-learn experiments because Python cannot reproduce WEKA Explorer screenshots/result buffers. To complete the exact WEKA submission requirement, also run the specified J48/IBk experiments in WEKA Explorer and save screenshots.
- Clustering labels are arbitrary; compare clusters by their membership/plots, not by numeric label alone.
- Search expansion traces define “expanded” as a node removed from the frontier and processed. Goal nodes are reported when popped; implementations stop at the first goal pop.
