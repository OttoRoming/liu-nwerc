#include <iostream>
#include <vector>
#include <regex>

using namespace std;

string caps(string a)
{
    smatch match;
    regex re("[A-Z]");
    regex_search(a, match, re);
    return match.str();
}

int main()
{
    int n;
    cin >> n;
    vector<string> names;
    string name;
    cin.ignore();
    while(n-- && getline(cin, name))
    {
        names.push_back(name);
    }

    sort(names.begin(), names.end(), [](const string& a, const string& b)
    {
        return caps(a) < caps(b);
    });

    cout << endl;

    for (const string & i : names)
    {
        cout << i << endl;
    }

    return 0;
}