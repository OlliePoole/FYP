//N.B. You do NOT need to understand what the phrase
//"implements IAfterSchoolBase" means. Just don't delete it!

import gui.IAfterSchoolBase;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;
import src.Pupil;

public class AfterSchoolBase implements IAfterSchoolBase {

    ArrayList<Club> clubs = new ArrayList<>();
    ArrayList<Pupil> pupils = new ArrayList<>();

    /**
     * Add a club to the database.
     *
     * @param club The name of the club to add.
     */
    public void addClub(String club) {
        boolean clubRegistered = false;
        if (clubs.isEmpty()) {
            clubs.add(new Club(club));
        } else {
            for (int x = 0; x < clubs.size(); x++) {
                if (clubs.get(x).getName().equals(club)) {
                    clubRegistered = true;
                }
            }
            if (clubRegistered == false) {
                clubs.add(new Club(club));
            }
        }
    }

    /**
     * Get the number of clubs in the database.
     *
     * @return Number of clubs in the database.
     */
    public int getNbrClubs() {
        return clubs.size();
    }

    /**
     * Get the i'th club in the database.
     *
     * @param i Index of the club (indices start at 0).
     * @return The name of the club.
     */
    public String getClub(int i) {
        return clubs.get(i).getName();
    }

    /**
     * Add a pupil to the database.
     *
     * @param firstName First name of the pupil.
     * @param lastName Last name of the pupil.
     */
    public void addPupil(String firstName, String lastName) {
        boolean pupilRegistered = false;
        if (pupils.isEmpty()) {
            pupils.add(new Pupil(firstName, lastName));
        } else {
            for (int x = 0; x < pupils.size(); x++) {
                if (pupils.get(x).getFullName().equals(firstName + " " + lastName)) {
                    pupilRegistered = true;
                }
            }
            if (pupilRegistered == false) {
                pupils.add(new Pupil(firstName, lastName));
            }
        }
    }

    /**
     * Get the number of pupils in the database.
     *
     * @return Number of pupils in the database.
     */
    public int getNbrPupils() {
        return pupils.size();
    }

    /**
     * Get the full name of the i'th pupil in the database.
     *
     * @param i Index of the pupil (indices start at 0).
     * @return The full name of the pupil.
     */
    public String getPupil(int i) {
        return pupils.get(i).getFullName();
    }

    /**
     * Get the first name of the i'th pupil in the database.
     *
     * @param i Index of the pupil (indices start at 0).
     * @return The first name of the pupil.
     */
    public String getPupilFirstName(int i) {
        return pupils.get(i).getFirstName();
    }

    /**
     * Get the last name of the i'th pupil in the database.
     *
     * @param i Index of the pupil (indices start at 0).
     * @return The last name of the pupil.
     */
    public String getPupilLastName(int i) {
        return pupils.get(i).getLastName();
    }

    /**
     * Add a pupil to a club. The pupil and club must already be present in the
     * database. The pupil must not be already a member of the club.
     *
     * @param clubName The name of the club.
     * @param firstName The first name of the pupil.
     * @param lastName The last name of the pupil.
     * @return true if the pupil was successfully added to the club (this
     * happens if the club and pupil are already in the database, and the pupil
     * has not already been added to the club).
     */
    public boolean addPupilToClub(String clubName, String firstName, String lastName) {
        boolean success = false;
        int y = 0;

        for (y = 0; y < pupils.size(); y++) {
            if (pupils.get(y).getFullName().equals(firstName + " " + lastName)) {
                break;
            }
        }

        for (int x = 0; x < clubs.size(); x++) {
            if (clubs.get(x).getName().equals(clubName) && (pupils.get(y).checkIfClubInList(clubName) == false)) {
                clubs.get(x).registerPupil(firstName, lastName);
                pupils.get(y).registerClub(clubName);
                success = true;
                break;
            } else {
                success = false;
            }
        }
        return success;
    }

    /**
     * Get the number of pupils in a club
     *
     * @param clubName The name of the club.
     * @return The number of pupils in the club.
     */
    public int getNbrPupilsForClub(String clubName) {
        int nbr = 0;
        for (int x = 0; x < clubs.size(); x++) {
            if (clubs.get(x).getName().equals(clubName)) {
                nbr = clubs.get(x).getNumberOfPupils();
                break;
            }
        }
        return nbr;
    }

    /**
     * Get the i'th pupil in a particular club.
     *
     * @param clubName The name of the club.
     * @param i Index of the pupil (indices start at 0). Note that this is the
     * index of the pupil within this particular club, not the index of the
     * pupil in the database.
     * @return The full name of the pupil.
     */
    public String getPupilForClub(String clubName, int i) {
        String name = null;
        for (int x = 0; x < clubs.size(); x++) {
            if (clubs.get(x).getName().equals(clubName)) {
                name = clubs.get(x).getPupilInClub(i);
                break;
            }
        }
        return name;
    }

    /**
     * Get the number of clubs that an pupil has appeared in.
     *
     * @param firstName First name of the pupil.
     * @param lastName Last name of the pupil.
     * @return The number of clubs that the pupil is a member of.
     */
    public int getNbrClubsForPupil(String firstName, String lastName) {
        int nbr = 0;
        for (int x = 0; x < pupils.size(); x++) {
            if (pupils.get(x).getFullName().equals(firstName + " " + lastName)) {
                nbr = pupils.get(x).getNumberOfClubs();
                break;
            }
        }
        return nbr;
    }

    /**
     * Get the i'th club that a pupil is a member of.
     *
     * @param firstName First name of the pupil.
     * @param lastName Last name of the pupil.
     * @param i Index of the club (indices start at 0). Note that this is the
     * index of the club within the list associated with this particular pupil,
     * not the index of the club in the database.
     * @return The name of the club
     */
    public String getClubForPupil(String firstName, String lastName, int i) {
        String clubName = null;
        for (int x = 0; x < pupils.size(); x++) {
            if (pupils.get(x).getFullName().equals(firstName + " " + lastName)) {
                clubName = pupils.get(x).getClubforPupil(i);
                break;
            }
        }
        return clubName;
    }

    /**
     * Save the database to a file.
     *
     * @param fileName name of the file to save to.
     * @throws FileNotFoundException
     */
    public void save(String fileName) throws FileNotFoundException {
        //Sets all the pupils to a not saved state
        for (int x = 0; x < pupils.size(); x++) {
            pupils.get(x).setSaved(false);
        }

        PrintWriter fileOut = new PrintWriter(fileName);
        fileOut.println("//");
        for (int x = 0; x < clubs.size(); x++) {
            fileOut.println(clubs.get(x).getName());
            for (int y = 0; y < clubs.get(x).getNumberOfPupils(); y++) {
                fileOut.println(clubs.get(x).getPupilInClub(y));
                for (int z = 0; z < clubs.get(x).getNumberOfPupils(); z++) {
                    if (clubs.get(x).getPupilInClub(y).equals(pupils.get(z).getFullName())) {
                        pupils.get(z).setSaved(true);
                    }
                }
            }
            fileOut.println("//");
        }
        //Saves all the pupils not attached to a club
        ArrayList<String> nonRegPupils = new ArrayList<>();

        for (int x = 0; x < pupils.size(); x++) {
            if (pupils.get(x).getSaved() == false) {
                nonRegPupils.add(pupils.get(x).getFullName());
            }
        }
        if (nonRegPupils.isEmpty() == false) {
            fileOut.println("UnRegPupils");
            for (int x = 0; x < nonRegPupils.size(); x++) {
                fileOut.println(nonRegPupils.get(x));
            }
            fileOut.println("//");
        }
        fileOut.close();
    }

    /**
     * Load the database from a file.
     *
     * @param fileName Name of the file to load from.
     * @throws FileNotFoundException
     */
    public void load(String fileName) throws FileNotFoundException {
        String firstName, lastName, clubName, temp;
        int clubIndex = 0;
        int pupilIndex = 0;
        boolean studentRegistered = false;
        clubs.clear();
        pupils.clear();
        FileInputStream fileIn = new FileInputStream(fileName);
        Scanner scan = new Scanner(fileIn);

        A:
        while (scan.hasNext()) {
            temp = scan.next();
            if (scan.hasNext()) {
                clubName = scan.next();
            } else {
                break A;
            }

            clubs.add(new Club(clubName));

            while (!(scan.hasNext("//"))) {
                firstName = scan.next();
                lastName = scan.next();
                for (int x = 0; x < pupils.size(); x++) {
                    if (pupils.get(x).getFullName().equals(firstName + " " + lastName)) {
                        clubs.get(clubIndex).registerPupil(firstName, lastName);
                        pupils.get(x).registerClub(clubName);
                        studentRegistered = true;
                        break;
                    } else {
                        studentRegistered = false;
                    }
                }
                if (studentRegistered == false) {
                    clubs.get(clubIndex).registerPupil(firstName, lastName);
                    pupils.add(new Pupil(firstName, lastName));
                    pupils.get(pupilIndex).registerClub(clubs.get(clubIndex).getName());
                    pupilIndex += 1;
                }
                
            }
            clubIndex += 1;
        }
        //Removing the temporary club used when saving
        for (int x = 0; x < clubs.size(); x++) {
            if (clubs.get(x).getName().equals("UnRegPupils")){
                clubs.remove(x);
            }
        }
        //Removing the pupils from the club
        for (int x = 0;x < pupils.size(); x++) {
            if (pupils.get(x).checkIfClubInList("UnRegPupils")){
                pupils.get(x).unRegisterClub("UnRegPupils");
            }
        }
    }
}
