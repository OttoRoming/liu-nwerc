#include <iostream>
#include <vector>

using namespace std;

#define sort(x) sort((x).begin(), (x).end());

bool fits(int lines, int w, const vector<string>& words)
{
    vector<int> columnWidths;
    int j {0};
    for (size_t i = 0; i < words.size(); i++)
    {
        if (columnWidths.size() <= j)
        {
            columnWidths.push_back(0);
        }
        columnWidths[j] = max(columnWidths[j], int(words[i].size()));
        if ((i + 1) % lines == 0 || i != words.size()-1 && words[i+1].size() > columnWidths[j]) // Måste förbättra villkor för byte av kolumn
        {
            j++;
        }
    }  
    
    int totalWidth {0};
    for (size_t i = 0; i < columnWidths.size(); i++)
    {
        totalWidth += columnWidths[i] + 1;
    }

    return (totalWidth - 1) <= w;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, w;
    cin >> n >> w;
    vector<string> words(n);
    vector<int> sizes(n);
    for (int i = 0; i < n; ++i)
    {
        string s;
        cin >> s;
        words[i] = s;
    }

    int lowLines {1}, highLines {n};
    while (lowLines < highLines)
    {
        int midLines = (lowLines + highLines) / 2;
        
        if (fits(midLines, w, words))
        {
            highLines = midLines;
        }
        else
        {
            lowLines = midLines + 1;
        }
    }

    cout << lowLines << "\n";
    return 0;
}