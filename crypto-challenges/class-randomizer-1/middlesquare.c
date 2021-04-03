#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdint.h>
#include <math.h>

uint64_t seed = 1234567890123456;

uint64_t nextRand() {
  // Keep the 8 middle digits from 5 to 12 and square.
  seed = (seed % lround(pow(10, 12)))/lround(pow(10, 4));
  seed *= seed;
  return seed;
}

void main() {
  printf("\nWelcome to Dr. J's Random Number Generator! \n"
  "[r] Print a new random number \n"
  "[g] Guess the next two random numbers and receive the flag! \n"
  "[q] Quit \n\n");
  char line[100];
  while (true) {
    printf(">");
    fgets (line, sizeof(line), stdin);
    line[strcspn(line, "\n")] = 0;

    if (!strcmp("r", line)) {
      uint64_t r = nextRand();
      printf("%lu\n", r);
    }
    if (!strcmp("g", line)) {
      printf("\nGuess the next two random numbers for a flag! "
      "You have a 0.000000000000001%% chance of guessing both correctly... "
      "Good luck!\nEnter your first guess:\n>");
      uint64_t guess = 0;
      fgets (line, sizeof(line), stdin);
      sscanf(line, "%lu", &guess);
      if (guess == nextRand()) {
        printf("\nWow, lucky guess... You won't be able to guess right a second time.\n"
        "Enter your second guess:\n>");
      }
      else {
        printf("That's incorrect. Get out of here!\n");
        break;
      }
      fgets (line, sizeof(line), stdin);
      sscanf(line, "%lu", &guess);
      if (guess == nextRand()) {
        printf("\nWhat? You must have psychic powers... Well here's your flag: nactf{chunky_turnip}\n");
        break;
      }
    }
    if (!strcmp("q", line)) {
      printf("\nGoodbye!\n");
      break;
    }
  }
}
