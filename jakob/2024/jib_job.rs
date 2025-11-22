#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

struct Crane
{
    int x;
    int y;
    int h;
};

int main()
{
    int n;
    cin >> n;
    vector<Crane> v;
    int highest {0};
    while(n--)
    {
        int x, y, h;
        Crane crane;
        cin >> crane.x >> crane.y >> crane.h;
        highest = max(crane.h, highest);
        v.push_back(crane);
    }

    vector<int> result;

    for (auto c : v)
    {
        int currMax {0};
        if (highest == c.h)
        {
            result.push_back(c.h);
            continue;
        }
        for (auto c2 : v)
        {
            // If same crane or current crane is higher, then we don't need to calculate distance
            if (c.h == c2.h || c.h > c2.h)
                continue;
            int pyt = sqrt(((c2.x - c.x) * (c2.x - c.x)) + ((c2.y - c.y) * (c2.y - c.y)));
            // Crane can't be longer than tower
            if (pyt > c.h)
                pyt = c.h;
            if (currMax == 0)
                currMax = pyt;
            currMax = min(currMax, pyt);
        }
        result.push_back(currMax);
    }

    for (int i : result)
    {
        cout << i << endl;
    }

    return 0;
}