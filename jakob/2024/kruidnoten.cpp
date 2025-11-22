#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <iomanip>
#include <limits.h>
#include <utility>

using namespace std;

double dijkstras(const unordered_map<int, vector<pair<int, int>>> & um, int from, int to)
{
    unordered_map<int, float> distance;
    priority_queue<pair<float, int>, vector<pair<float, int>>, greater<pair<float, int>>> pq;

    pq.push({0, from});
    distance[from] = 0;

    while (!pq.empty())
    {
        auto [dist, curr] = pq.top(); pq.pop();
        
        if (curr == to)
            return dist;

        if (distance.count(curr) && dist > distance[curr])
            continue;

        for (const auto& [neighbor, length] : um.at(curr))
        {
            float newDist = dist + length;

            if (!distance.count(neighbor) || newDist < distance[neighbor])
            {
                distance[neighbor] = newDist;
                pq.push({newDist, neighbor});
            }
        }
    }
    return -1;
}

int main()
{
    int n, m, k;
    cin >> n >> m >> k;

    unordered_map<int, vector<pair<int, int>>> um;

    while (m--)
    {
        int i, j, lenght;
        cin >> i >> j >> lenght;
        um[i].push_back({j, lenght});
        um[j].push_back({i, lenght});
    }

    vector<int> stores;
    vector<double> probs;

    while (k--)
    {
        int store;
        double probability;
        cin >> store >> probability;
        stores.push_back(store);
        probs.push_back(probability);
    }

    vector<float> distFrom1(stores.size());
    vector<float> distToN(stores.size());

    for (int i = 0; i < stores.size(); i++)
    {
        distFrom1[i] = dijkstras(um, 1, stores[i]);
        distToN[i] = dijkstras(um, stores[i], n);
    }

    int numStores = stores.size();
    double expectedValue = 0.0;
    double totalProb = 0.0;

    for (int mask = 1; mask < (1 << numStores); mask++)
    {
        double prob = 1.0;
        float minDist = 1e9;
        
        for (int i = 0; i < numStores; i++)
        {
            if (mask & (1 << i))
            {
                prob *= probs[i];
                float totalDist = distFrom1[i] + distToN[i];
                minDist = min(minDist, totalDist);
            }
            else
            {
                prob *= (1.0 - probs[i]);
            }
        }
        
        expectedValue += prob * minDist;
        totalProb += prob;
    }
    
    if (totalProb < 1.0 - 1e-9)
    {
        cout << "impossible" << endl;
    }
    else
    {
        cout << fixed << setprecision(2) << expectedValue << endl;
    }

    return 0;
}