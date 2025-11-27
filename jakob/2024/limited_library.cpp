#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

// Not done

#define sort(x) sort(x.begin(), x.end())

int main()
{
    int n, m, x, y;
    scanf("%d %d %d %d", &n, &m, &x, &y);

    vector<int> shelvesHeight(n);
    vector<int> bookHeight(m);

    for(size_t i = 0; i < n; i++)
        scanf("%d", &shelvesHeight[i]);
    for(size_t i = 0; i < m; i++)
        scanf("%d", &bookHeight[i]);

    if (x * n < m)
    {
        cout << "impossible" << endl;
        return 0;
    }

    sort(bookHeight);

    for (auto i : bookHeight)   
        cout << i << endl;

    return 0;
}

// n = number of shelves
// m = number of books
// x = number of books that fits on a shelf
// y = number of books that fits on a shelf next to an art piece