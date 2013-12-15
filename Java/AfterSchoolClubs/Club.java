import java.util.ArrayList;

public class Club {

    String name;
    private ArrayList<String> pupilsRegistered = new ArrayList<>();

    /**
     * Constructor
     *
     * @param name The name of the club
     */
    public Club(String name) {
        this.name = name;
    }


    /**
     * Get Name
     *
     * @return name The name of the club
     */
    public String getName() {
        return name;
    }


    /**
     * Registers a pupil
     *
     * @param firstName The first name of the student
     * @param lastName The last name of the student
     */
    public void registerPupil(String firstName, String lastName) {
        pupilsRegistered.add(firstName + " " + lastName);
    }

    /**
     * gets the number of pupils
     *
     * @return size The number of pupils registered 
     */
    public int getNumberOfPupils() {
        return pupilsRegistered.size();
    }

    /**
     * returns the name of the pupil
     *
     * @param index The index of the pupil to be searched for
     */
    public String getPupilInClub(int index) {
        return pupilsRegistered.get(index);
    }
}
