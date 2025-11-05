#include <algorithm>
#include <cstddef>
#include <iostream>
#include <regex>
#include <string>
#include <vector>

std::vector<std::string> surnames;

void input() {
  int count;
  std::cin >> count;
  std::cin.ignore(100, '\n');

  surnames.reserve(count);

  for (int i = 0; i < count; i++) {
    std::string name;
    std::getline(std::cin, name);
    surnames.push_back(name);
  }
}

std::regex needle{"[A-Z](\\w| |')*"};
int main() {
  input();

  std::sort(surnames.begin(), surnames.end(), [](std::string a, std::string b) {
    std::smatch a_match;
    std::regex_search(a, a_match, needle);

    std::smatch b_match;
    std::regex_search(b, b_match, needle);

    return a_match.str() < b_match.str();
  });

  for (const std::string &i : surnames) {
    std::cout << i << std::endl;
  }

  return 0;
}
