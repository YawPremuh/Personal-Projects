#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

int roll_dice(void);
bool play_game(void);

int main(void) {
    char play_again;
    int wins = 0, losses = 0;

    srand((unsigned) time(NULL));

    do {
        if (play_game()) {
            printf("You win!\n");
            wins++;
        } else {
            printf("You lose!\n");
            losses++;
        }
        printf("Play again? ");
        scanf(" %c", &play_again);
    } while (play_again == 'y' || play_again == 'Y');

    printf("Wins: %d Losses: %d\n", wins, losses);
    return 0;
}

int roll_dice(void) {
    int die1 = rand() % 6 + 1;
    int die2 = rand() % 6 + 1;
    return die1 + die2;
}

bool play_game(void) {
    int point, roll = roll_dice();
    printf("You rolled: %d\n", roll);

    if (roll == 7 || roll == 11) {
        return true;
    } else if (roll == 2 || roll == 3 || roll == 12) {
        return false;
    } else {
        point = roll;
        printf("Your point is %d\n", point);
    }

    while (true) {
        roll = roll_dice();
        printf("You rolled: %d\n", roll);

        if (roll == point) {
            return true;
        } else if (roll == 7) {
            return false;
        }
    }
}
