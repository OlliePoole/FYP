import java.io.FileNotFoundException;
import java.util.Scanner;


/**
 *
 * @author Ollie Poole
 */
public class Main {


    private static AfterSchoolBase asClubBase = new AfterSchoolBase();
    private static Scanner scan = new Scanner(System.in);


    public static void main(String [] args) throws FileNotFoundException {
        String option;
        do {
            menu();
            option = getOption();
            if (option.equalsIgnoreCase("AC")) {
                System.out.print("Club name ? ");
                String clubName = scan.nextLine();
                asClubBase.addClub(clubName);
            }
            else if (option.equalsIgnoreCase("AP")) {
                System.out.print("Pupil's first name ? ");
                String firstName = scan.nextLine();
                System.out.print("Pupil's last name ? ");
                String lastName = scan.nextLine();
                asClubBase.addPupil(firstName, lastName);
            }
            else if (option.equalsIgnoreCase("LC")) {
                int nbrClubs = asClubBase.getNbrClubs();
                for (int i=0; i<nbrClubs; i++) {
                    String clubName = asClubBase.getClub(i);
                    System.out.println(clubName);
                }
            }
            else if (option.equalsIgnoreCase("LP")) {
                int nbrPupils = asClubBase.getNbrPupils();
                for (int i=0; i<nbrPupils; i++) {
                    String pupil = asClubBase.getPupil(i);
                    System.out.println(pupil);
                }
            }
            else if (option.equalsIgnoreCase("APC")) {
                System.out.print("Club name ? ");
                String club = scan.nextLine();
                System.out.print("Pupil's first name ? ");
                String firstName = scan.nextLine();
                System.out.print("Pupil's last name ? ");
                String lastName = scan.nextLine();
                if (!asClubBase.addPupilToClub(club, firstName, lastName)) {
                    System.out.println("Unable to add pupil to club.");
                    System.out.print("Check that both club and pupil have");
                    System.out.println(" been added to database");
                }
            }
            else if (option.equalsIgnoreCase("LPC")){
                System.out.print("Club name ? ");
                String club = scan.nextLine();
                int nbrPupils = asClubBase.getNbrPupilsForClub(club);
                for (int i=0; i<nbrPupils; i++) {
                    System.out.println(asClubBase.getPupilForClub(club, i));
                }
            }
            else if (option.equalsIgnoreCase("LCP")){
                System.out.print("Pupil's first name ? ");
                String firstName = scan.nextLine();
                System.out.print("Pupil's last name ? ");
                String lastName = scan.nextLine();
                int nbrClubs = asClubBase.getNbrClubsForPupil(firstName,lastName);
                for (int i=0; i<nbrClubs; i++) {
                    String club=asClubBase.getClubForPupil(firstName,lastName,i);
                    System.out.println(club);
                }
            }
            else if (option.equalsIgnoreCase("S")) {
                System.out.println("File name ? ");
                String fileName = scan.nextLine();
                asClubBase.save(fileName);
            }
            else if (option.equalsIgnoreCase("L")) {
                System.out.println("File name ? ");
                String fileName = scan.nextLine();
                asClubBase.load(fileName);
            }
        }
        while(!option.equalsIgnoreCase("Q"));
    }

    private static String getOption() {
        System.out.print("Your option ? ");
        return scan.nextLine();
    }

    /**
     * Displays the menu
     *
     */
    private static void menu() {
        System.out.println("Options are ...");
        System.out.println("AC: add club");
        System.out.println("AP: add pupil");
        System.out.println("APC: add pupil to club");
        System.out.println("LC: list clubs");
        System.out.println("LP: list pupils");
        System.out.println("LPC: list pupils in club");
        System.out.println("LCP: list clups of which pupil is a member");
        System.out.println("S: save to file");
        System.out.println("L: load from file");
        System.out.println("Q: quit program");
    }
}
