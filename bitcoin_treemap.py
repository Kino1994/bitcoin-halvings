import matplotlib.pyplot as plt
import squarify

quantities = [500000000000 / (2 ** i) for i in range(34)]

total_planned = 500000000000 * 2
remaining_quantity = total_planned - sum(quantities)
quantities.append(remaining_quantity)

colors = ["#50C878"] * 4 + ["#FFBF00"] + ["grey"] * (len(quantities) - 5)
labels = [
    "Epoch 1 (2009)", "Epoch 2 (2012)", "Epoch 3 (2016)", "Epoch 4 (2020)", "Epoch 5 (2024)"
] + ["" for _ in range(len(quantities) - 5)]  # Labels only for the first 5 epochs

fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

squarify.plot(sizes=quantities, label=labels, color=colors, alpha=0.7, edgecolor="white", linewidth=2)

plt.title("Treemap of Bitcoin Epochs Based on Quantity Distribution", fontsize=16)
plt.savefig("bitcoin_treemap.png", dpi=1200, bbox_inches='tight')

quantities = [500000000000 / (2 ** i) for i in range(30)]

total_planned = 500000000000 * 2
remaining_quantity = total_planned - sum(quantities)
quantities.append(remaining_quantity)

colors = ["#FFBF00"] + ["grey"] * (len(quantities) - 5)
labels = [
    "Epoch 5 (2024)", "Epoch 6", "Epoch 7", "Epoch 8", "Epoch 9"
] + ["" for _ in range(len(quantities) - 5)]

fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

squarify.plot(sizes=quantities, label=labels, color=colors, alpha=0.7, edgecolor="white", linewidth=2)

plt.title("Treemap of Bitcoin Epochs 5-9 Based on Quantity Distribution", fontsize=16)
plt.savefig("bitcoin/bitcoin_treemap2.png", dpi=1200, bbox_inches='tight')