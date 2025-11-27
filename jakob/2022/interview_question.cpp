#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
// Inte klar
using namespace std;

int findPrime(const vector<int>& fizzOrBuzz, const vector<int>& buzzOrFizz, const vector<int>& fizzBuzz, const vector<int>& transcript, const set<int>& possiblePrimes)
{
    int x;
    for (int i : possiblePrimes)
    {
        bool valid {true};
        for (int j : fizzOrBuzz)
            if (j % i != 0)
            {
                valid = false;
                break;
            }
        if (!valid)
            continue;
        for (int j : buzzOrFizz)
            if (j % i == 0)
            {
                valid = false;
                break;
            }
        if (!valid)
            continue;
        for (int j : fizzBuzz)
            if (j % i == 0)
            {
                valid = false;
                break;
            }
        if (!valid)
            continue;
        for (int j : transcript)
            if (j % i == 0)
            {
                valid = false;
                break;
            }
        if (valid)
            return i;
    }

    return 1;
}

int find(const vector<int>& fizzOrBuzz, const vector<int>& buzzOrFizz, const vector<int>& fizzBuzz, const vector<int>& transcript)
{
    int x {0};
    set<int> possiblePrimes;
    for (int i : fizzOrBuzz)
    {
        int n = i;
        for (int p = 2; p*p <= i; ++p)
        {
            while (n % p == 0)
            {
                possiblePrimes.insert(p);
                n /= p;
            }
        }
        if (n > 1)
            possiblePrimes.insert(n);
    }

    if (possiblePrimes.size() == 1)
        return *possiblePrimes.begin();
    else
        return findPrime(fizzOrBuzz, buzzOrFizz, fizzBuzz, transcript, possiblePrimes);
}

int main()
{
    int c, d;
    scanf("%d %d", &c, &d);

    vector<int> transcript;
    vector<int> fizz;
    vector<int> buzz;
    vector<int> fizzBuzz;

    for (size_t i = c; i < d + 1; i++)
    {
        string input;
        cin >> input;
        
        if (input == "Fizz")
            fizz.push_back(i);
        else if (input == "Buzz")
            buzz.push_back(i);
        else if (input == "FizzBuzz")
            fizzBuzz.push_back(i);
        else
            transcript.push_back(i);
    }

    cout << find(fizz, buzz, fizzBuzz, transcript) << " ";
    cout << find(buzz, fizz, fizzBuzz, transcript) << endl;

    return 0;
}