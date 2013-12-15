/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package blackjack;

/**
 *
 * @author Ollie Poole
 */
public class Blackjack {

    public static void main(String[] args) {
        int card, p1Total, p2Total, p1Wins, p2Wins;

        p1Total = 0;
        p2Total = 0;
        p1Wins = 0;
        p2Wins = 0;
        card = 0;

        packOfCards deck = new packOfCards();

        deck.initDeck();
        //initalises the deck array

        System.out.println("Welcome to my game of BlackJack");
        System.out.println("The game will now start");

        A:
        while (deck.usedCardPointer <= 51) {

            System.out.println("Player 1 will go first");
            System.out.println("You have been delt:");

            for (int x = 1; x < 3; x++) {
                // loops twice to deal two cards to player 1
                card = deck.dealCard();

                if (card == -1) {
                    break A;
                    //if all cards drawn break the main loop
                }

                p1Total += processCard(card, p1Total);

            }

            System.out.println("Your total is: " + p1Total);

            System.out.println("Player 2 you will now go");
            System.out.println("You have been delt:");
            for (int x = 1; x < 3; x++) {
                //loops twice to deal two cards to player 2

                card = deck.dealCard();
                if (card == -1) {
                    //if all cards drawn then exit main loop
                    break A;
                }

                p2Total += processCard(card, p2Total);

            }

            System.out.println("Your total is: " + p2Total);

            B:
            while (p1Total <= 21 || p2Total <= 21) {
                //loop while totals are less than or equal to 21

                if (p1Total < 21) {
                    System.out.println("Player 1 you will now go again");
                    System.out.println("You have been delt:");

                    card = deck.dealCard();
                    if (card == -1) {
                        break;
                    }

                    p1Total += processCard(card, p1Total);
                }

                if (p1Total > 21) {
                    System.out.println("SORRY! you have gone bust!");
                    p2Wins++;
                    p1Total = 0;
                    p2Total = 0;
                    //resets the total and adds 1 to the player 2 wins
                    break;
                } else {
                    System.out.println("Player 1 total is: " + p1Total);
                }

                if (p2Total < 21) {
                    System.out.println("Player 2 you will now go again");
                    System.out.println("You have been delt:");

                    card = deck.dealCard();
                    if (card == -1) {
                        break;
                    }

                    p2Total += processCard(card, p2Total);

                    if (p2Total > 21) {
                        System.out.println("SORRY! you have gone bust!");
                        p1Wins++;
                        p1Total = 0;
                        p2Total = 0;
                        //resets the totals and adds 1 to the player 1 score
                        break;
                    } else {
                        System.out.println("Player 2 total is: " + p2Total);
                    }

                    if (p1Total == 21 && p2Total == 21) {
                        p1Total = 0;
                        p2Total = 0;
                        //if a draw resets both totals and starts a new round
                        break;
                    }
                }

            }
        }

        System.out.println("All card have been delt, the game will now finish!");

        System.out.println("Scores: ");
        System.out.println("Player 1: " + p1Wins);
        System.out.println("Player 2: " + p2Wins);
        //outputs the scores to the user

        if (p1Wins > p2Wins) {
            System.out.println("Well done player 1, you won");
        } else if (p2Wins > p1Wins) {
            System.out.println("Well done player 2, you won");
        } else {
            System.out.println("The game ended in a draw!");
        }

    }

    public static int processCard(int card, int total) {
        switch (card) {
            case 11:
                System.out.println("Jack");
                return 10;

            case 12:
                System.out.println("Queen");
                return 10;

            case 13:
                System.out.println("King");
                return 10;

            case 1:
                System.out.println("Ace");
                if (total + 11 > 21) {
                    return 1;
                } else {
                    return 11;
                }

            default:
                System.out.println(card);
                return card;

        }
    }
}
