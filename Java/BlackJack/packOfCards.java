/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package blackjack;

/**
 *
 * @author Ollie Poole
 */
public class packOfCards {

    int[] deck;
    int usedCardPointer;

    public packOfCards() {
        deck = new int[52];
        usedCardPointer = 0;

    }

    public void initDeck() {
        int track = 0;
        for (int x = 1; x < 5; x++) {
            //First loop for the four suits
            for (int y = 1; y < 14; y++) {
                //second loop for the numbers 1 - 13
                deck[track] = y;
                track += 1;
                //track variable tells the program where to place the number in the array
            }

        }

    }

    public int dealCard() {
        int random;
        int ret;

        random = (int) (Math.random() * 52);
        //gets a random number between 0-52

        while (deck[random] == -1) {
            random = (int) (Math.random() * 52);
        } //If the number has already been used it will generate a new number

        ret = deck[random];

        usedCardPointer++;
        //adds one to the used card count

        deck[random] = -1;
        //sets the used card in the deck array to -1 to show it's been used

        if (usedCardPointer == 52) {
            //if all cards have been drawn return -1
            return -1;
        } else {
            return ret;
        }

    }
}
