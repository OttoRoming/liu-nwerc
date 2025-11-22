#include <cstddef>
#include <cstdint>
#include <iostream>
#include <string>

std::string shuffle_word(std::string const &word) {
  std::string new_word = "";
  new_word.reserve(word.length());

  for (size_t i = 0; i < word.length(); i++) {
    size_t c = (i * 2) % word.length();
    new_word.push_back(word[c]);
    // char temp = word[i];
    // word[i] = word[c];
    // word[c] = temp;
  }

  return new_word;
}

int main() {
  size_t string_size;
  std::cin >> string_size;

  intmax_t i;
  std::cin >> i;

  std::cin.ignore(1000, '\n');
  std::string original_word;
  original_word.reserve(string_size);
  std::cin >> original_word;

  std::string word = original_word;
  int iterations = 0;

  while (i > 0) {
    word = shuffle_word(word);
    if (word == original_word) {
      i %= iterations;
    }
    iterations++;
    i--;
  }

  std::cout << word << std::endl;
}
