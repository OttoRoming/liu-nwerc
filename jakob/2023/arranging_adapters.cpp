#include <iostream>
#include <vector>
#include <algorithm>

#define all(x) begin(x), end(x)

using namespace std;

int main()
{
    int n, s;
    cin >> n >> s;

    int count {0};

    int sumSocket {0};

    vector<int> chargers (n);
    for (size_t i = 0; i < n; i++)
    {
        cin >> chargers[i];
        sumSocket += chargers[i];
    }

    sort(all(chargers));

    for (int i = 0; i < 2 && s > 0 && n > 0; i++) {
        count++;
        chargers.pop_back();
        n--;
        s--;
    }
    
    long long availableSpace = (long long)s * 3;

    int left {0};
    int right {n + 1};

    while (left + 1 < right)
    {
        int mid = (left + right) / 2;

        long long totalWidth {0};
        int mod1 {0}, mod2 {0};

        for (int i = 0; i < mid; i++)
        {
            totalWidth += chargers[i];
            int remainder = chargers[i] % 3;
            if (remainder == 1)
                mod1++;
            else if (remainder == 2)
                mod2++;
        }

        long long freeSpace {0};
        int diff = abs(mod1 - mod2);

        if (mod1 < mod2)
        {
            freeSpace += diff;
        }
        else if (mod1 > mod2)
        {
            freeSpace += diff / 2;
            freeSpace += diff % 2;
        }

        if (totalWidth + freeSpace <= availableSpace)
        {
            left = mid;
        }
        else
            right = mid;

    }

    cout << left + count << endl;

    return 0;
}