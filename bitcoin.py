import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Halving': list(range(0, 34)),
    'Year': [
        2009, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044,
        2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084,
        2088, 2092, 2096, 2100, 2104, 2108, 2112, 2116, 2120, 2124,
        2128, 2132, 2136, 2140
    ],
    'Block Reward (satoshis)': [
        5000000000, 2500000000, 1250000000, 625000000, 312500000,
        156250000, 78125000, 39062500, 19531250, 9765625,
        4882812, 2441406, 1220703, 610351, 305175,
        152587, 76293, 38146, 19073, 9536,
        4768, 2384, 1192, 596, 298,
        149, 74, 37, 18, 9,
        4, 2, 1, 0
    ],
    'Total (%)': [
        0, 50, 75, 87.5, 93.75, 96.875, 98.4375, 99.21875, 99.609375, 99.804688,
        99.9023438, 99.9511719, 99.9755859, 99.987793, 99.99389647, 99.99694822,
        99.99847409, 99.99923702, 99.99961848, 99.99980921, 99.99990457,
        99.99996225, 99.99997609, 99.99998801, 99.99999397, 99.99999695,
        99.99999854, 99.99999912, 99.99999955, 99.99999973, 99.99999982,
        99.99999986, 99.99999988, 99.99999989
    ],
    'Pending (%)': [
        100, 50, 25, 12.5, 6.25, 3.125, 1.5625, 0.78125, 0.390625, 0.195312,
        0.0976562, 0.0488281, 0.0244141, 0.012207, 0.00610353, 0.00305178,
        0.00152591, 0.00076298, 0.00038152, 0.00019079, 0.00009543,
        0.00003775, 0.00002391, 0.00001199, 0.00000603, 0.00000305,
        0.00000156, 0.00000088, 0.00000045, 0.00000027, 0.00000018,
        0.00000014, 0.00000012, 0.00000011
    ]
}

df = pd.DataFrame(data)


fig, ax1 = plt.subplots(figsize=(12, 8))

ax2 = ax1.twinx()
ax3 = ax1.twinx()

ax3.spines['right'].set_position(('outward', 60))

ax1.step(df['Halving'], df['Block Reward (satoshis)'], 'bo-', where='post', label='Block Reward (satoshis)')
ax1.set_xlabel('Halving Index')
ax1.set_ylabel('Block Reward (satoshis)', color='blue')
ax1.set_yscale('log')
ax1.set_yticks([10**i for i in range(1, 10)])
ax1.set_yticklabels([f'$10^{i}$' for i in range(1, 10)], color='blue')

ax1.set_xticks(df['Halving'][::5])
ax1.set_xticklabels(df['Year'][::5])
ax1.set_xlim(0, 35)

ax2.plot(df['Halving'], df['Total (%)'], '-o', color='green', label='Total (%)')
ax2.plot(df['Halving'], df['Pending (%)'], '-o', color='red', label='Pending (%)')
ax2.set_ylabel('Percentage (%)', color='green')
ax2.set_ylim(0, 100)

ax3.set_ylabel('Supply (satoshis)', color='orange')
ax3.set_ylim(0, 2100000000000000)

ax1.grid(True, which='both', linestyle='--', zorder=1)
lns1 = ax1.get_lines()
lns2 = ax2.get_lines()
lns3 = ax3.get_lines()
lns = lns1 + lns2 + lns3
labels = [l.get_label() for l in lns]
ax1.legend(lns, labels, loc='center', bbox_to_anchor=(0.88, 0.5))

plt.title('Bitcoin Halving Chart: Block Reward, Supply and Percentages')
for spine in [ax1.spines.values(), ax2.spines.values(), ax3.spines.values()]:
    for s in spine:
        s.set_visible(False)

plt.savefig("bitcoin/bitcoin.png", dpi=1200, bbox_inches='tight')