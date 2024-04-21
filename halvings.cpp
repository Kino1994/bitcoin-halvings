#include <iostream>
#include <cmath>
#include <limits>

typedef int64_t CAmount;
static constexpr CAmount COIN = 100000000;
static constexpr CAmount MAX_MONEY = 21000000 * COIN;
int nSubsidyHalvingInterval = 210000;
int nHeight = std::numeric_limits<int>::max(); // if one block more is validated an Signed Overflow occurs and nHeight becomes -2,147,483,648
int maxHalvings = nHeight / nSubsidyHalvingInterval; // so max number of halvings is 10.226 as result of nSubsidyHalvingInterval int type limit which is 2,147,483,647 / 210,000 

CAmount GetBlockSubsidy(int halvings) {
    if (halvings >= 64)
        return 0;

    CAmount nSubsidy = 50 * COIN;
    nSubsidy >>= halvings;
    return nSubsidy;
}

int main() {
    long long finalSupply = 0;
    for (int halvings = 0; halvings <= maxHalvings; halvings++) {
        CAmount nSubsidy = GetBlockSubsidy(halvings);
        long long addedSupply = nSubsidyHalvingInterval * nSubsidy;
        finalSupply += addedSupply;
        long long initialSupply = finalSupply - addedSupply;
        long double percentMined = (static_cast<long double>(finalSupply) / MAX_MONEY) * 100.0;
        long double pending =  100.0 - percentMined;
        std::cout << "Epoch " << halvings + 1 << ": Halving = " << halvings << ", Block Subsidy = " << nSubsidy << " satoshis, Initial Supply = " << initialSupply << " satoshis, Added Supply = " << addedSupply << " satoshis, Final Supply = " << finalSupply << " satoshis, Total = " << percentMined  << "%, Pending = " << pending  << "%" << std::endl;
    }

    return 0;
}