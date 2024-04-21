#include <iostream>

typedef int64_t CAmount;
static constexpr CAmount COIN = 100000000;
static constexpr CAmount MAX_MONEY = 21000000 * COIN;
int nSubsidyHalvingInterval = 210000;

CAmount GetBlockSubsidy(int nHeight) {

    int halvings = nHeight / nSubsidyHalvingInterval;
    
    if (halvings >= 64) {
        return 0;
    }

    CAmount nSubsidy = 50 * COIN;
    nSubsidy >>= halvings;
    return nSubsidy;
}

int main() {
    int halving = 0;
    int blockHeight = 0;
    int pendingBlocks4Halving = 210000;
    while (true) {
        if (blockHeight % nSubsidyHalvingInterval == 0) {
            CAmount nSubsidy = GetBlockSubsidy(blockHeight);
            std::cout << "Epoch " << halving + 1 << ": Block = " << blockHeight << ", Halving = " << halving << ", Block Subsidy = " << nSubsidy << " satoshis" << std::endl;
            halving+=1;
            pendingBlocks4Halving=210000;
        }
        if (pendingBlocks4Halving < 10000 || blockHeight % 10000 !=0) {
            blockHeight += 1; // Slow progress due to Integer Signed Overflow that changes the height to a negative number not multiple of 10000
            pendingBlocks4Halving-=1;
        }
        else {
            blockHeight += 10000; // Fast foward
            pendingBlocks4Halving-=10000;
        }
    }

    return 0;
}
