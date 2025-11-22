#include <iostream>
#include <string_view>
#include <unordered_map>
#include <vector>

using namespace std;

string shuffleWord(const string& s)
{
    string newWord;
    newWord.reserve(s.size());
    for (size_t i = 0; i < s.size(); i += 2)
    {
        newWord += s[i];
    }
    for (size_t i = s.size() % 2 == 0 ? 0 : 1; i < s.size(); i += 2)
    {
        newWord += s[i];
    }
    return newWord;
}

int main()
{
    int n; long long k;
    cin >> n >> k;

    string s;
    cin >> s;

    unordered_map<string_view, int> words;
    vector<string> wordsInOrder;

    wordsInOrder.push_back(s);
    string_view sv = wordsInOrder.back();
    words[sv] = 0;

    int index {-1};

    long long start = k;

    int iterations {0};

    while (start > 0)
    {
        s = shuffleWord(s);
        iterations++;

        string_view currentSv = s;
        if (words.count(currentSv))
        {
            int cycleLength = iterations - words[s];
            index = words[s] + ((k - words[s]) % cycleLength);
            break;
        }
        wordsInOrder.push_back(s);
        string_view sv = wordsInOrder.back();
        words[sv] = iterations;
        start--;
    }

    if (index != -1)
        cout << wordsInOrder[index] << endl;
    else
        cout << s << endl;

    return 0;
}