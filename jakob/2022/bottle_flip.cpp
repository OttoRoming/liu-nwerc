#include <stdio.h>
#include <cmath>

using namespace std;

int main()
{
    int h, r, da, dw;
    scanf("%d %d %d %d", &h, &r, &da, &dw);

    double a = double(da) / double(dw);

    double root = sqrt(a);

    double fraction = root / (1 + root);

    double x = fraction * h;

    printf("%f \n", x);

    return 0;
}