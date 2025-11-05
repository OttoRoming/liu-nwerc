#include <algorithm>
#include <cstddef>
#include <iostream>
#include <set>
#include <vector>

std::vector<int> parties;
int total_seats;
int majority_limit;

std::set<std::vector<size_t>> coalitions{};
int coalition_count{};
std::vector<size_t> stack{};

void input() {
  int party_count;
  std::cin >> party_count;
  std::cin.ignore();
  parties.reserve(party_count);
  stack.reserve(party_count);

  for (int i = 0; i < party_count; i++) {
    int party_seats;
    std::cin >> party_seats;
    parties.push_back(party_seats);
    total_seats += party_seats;
  }

  std::sort(parties.begin(), parties.end());
  majority_limit = total_seats / 2;
}

bool stack_contains(size_t party) {
  for (size_t i = 0; i < stack.size(); i++) {
    if (stack[i] == party) {
      return true;
    }
  }

  return false;
}

void foo(size_t i) {
  stack.push_back(i);

  int seats = 0;
  for (size_t i : stack) {
    seats += parties[i];
  }

  if (seats > majority_limit) {
    coalitions.insert(stack);
    coalition_count++;
    stack.pop_back();
    return;
  }

  for (size_t i = stack[stack.size() - 1] + 1; i < parties.size(); i++) {
    if (stack_contains(i)) {
      continue;
    }

    foo(i);
  }
}

int main() {
  input();

  for (size_t i = 0; i < parties.size(); i++) {
    stack = {};

    foo(i);
  }

  std::cout << std::endl;
  std::cout << std::endl;

  for (std::vector<size_t> coalition : coalitions) {
    for (size_t party : coalition) {
      std::cout << party << " ";
    }
    std::cout << std::endl;
  }

  std::cout << coalitions.size() << std::endl;
}