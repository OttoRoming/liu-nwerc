#include <iostream>
#include <vector>
#include <sstream>
#include <set>

using namespace std;

void subsetRecur(int i, vector<int>& arr, vector<set<int>>& res, set<int>& subset)
{
    if (i == arr.size())
    {
        res.push_back(subset);
        return;
    }

    subset.insert(i);
    subsetRecur(i+1, arr, res, subset);

    auto it = prev(subset.end());
    subset.erase(it);
    subsetRecur(i+1, arr, res, subset);
}

vector<set<int>> subsets(vector<int> & arr)
{
    set<int> subset;
    vector<set<int>> res;

    subsetRecur(0, arr, res, subset);
    return res;
}

bool checkSet(const vector<int>& arr, const set<int>& subset, int totalSeats)
{
    int sum {0};
    for (int i : subset)
    {
        sum += arr[i];
    }

    if (sum <= totalSeats / 2)
    {
        return false;
    }


    for (int i : subset)
    {
        if (sum - arr[i] > totalSeats / 2)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int n;
    cin >> n;
    string line;
    cin.ignore();
    getline(cin, line);
    int party;
    stringstream ss{line};
    vector<int> parties;
    int totalSeats {0};
    while (ss >> party)
    {
        parties.push_back(party);
        totalSeats += party;
    }

    vector<set<int>> res = subsets(parties);

    int counter {0};

    for (int i = 0; i < res.size(); i++) {
        if (checkSet(parties, res[i], totalSeats))
        {
            counter++;
        }
    }

    cout << counter << endl;

    return 0;
}