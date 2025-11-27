#include <iostream>

using namespace std;

int query(int c, int r)
{
    cout << "? " << c << " " << r << endl;
    int h;
    cin >> h;
    return h;
}

void ans(int c, int r)
{
    cout << "! " << c << " " << r << endl;
}

int main()
{
    int n;
    cin >> n;

    int c = query(n, 1);
    int r {1};
    if (c < n)
        r = query(n - c, 1);
    ans(c, r);


    return 0;
}