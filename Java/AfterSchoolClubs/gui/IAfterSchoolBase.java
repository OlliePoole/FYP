package gui;


import java.io.FileNotFoundException;

/**
 *
 * @author Ollie Poole
 */

public interface IAfterSchoolBase {

    void addPupil(String firstName, String lastName);

    boolean addPupilToClub(String clubName, String firstName, String lastName);

    void addClub(String club);

    String getPupil(int i);

    String getPupilFirstName(int i);

    String getPupilLastName(int i);

    String getPupilForClub(String clubName, int i);

    String getClub(int i);

    String getClubForPupil(String firstName, String lastName, int i);

    int getNbrPupils();

    int getNbrPupilsForClub(String clubName);

    int getNbrClubs();

    int getNbrClubsForPupil(String firstName, String lastName);

    void load(String fileName) throws FileNotFoundException;

    void save(String fileName) throws FileNotFoundException;

}
