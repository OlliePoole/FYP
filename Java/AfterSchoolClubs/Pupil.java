/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package src;

import java.util.ArrayList;

/**
 *
 * @author Ollie Poole
 */
public class Pupil {
    String firstName, lastName;
    boolean isSaved = false;
    private ArrayList<String> clubsRegistered = new ArrayList<>();
    
    
    /**
     * Constructor
     *
     * @param firstName The first name of the pupil
     * @param secondName The second name of the pupil
     */
    public Pupil(String firstName, String lastName){
        this.firstName=firstName;
        this.lastName=lastName;
    }
    
    /**
     * returns the first name of the student
     *
     * @return firstName The firstName of the student
     */
    public String getFirstName(){
        return firstName;
    }
    
    /**
     * returns the last name of the student
     *
     * @return lastName The last name of the student
     */
    public String getLastName(){
        return lastName;
    }
    
    /**
     * returns the full name of the student
     *
     * @return name The full name of the student
     */
    public String getFullName(){
        return (firstName + " " + lastName);
    }
    
    /**
     * Registers the student on a club
     *
     * @param name The name of the club
     */
    public void registerClub(String clubName){
        clubsRegistered.add(clubName);
    }
    
    /**
     * unregisters a student from a club
     *
     * @param name The name of the club
     */
    public void unRegisterClub(String clubName){
        clubsRegistered.remove(clubName);
    }
    
    
    /**
     * returns the number of clubs the pupil is registered on
     *
     * @return The number of clubs
     */
    public int getNumberOfClubs(){
        return clubsRegistered.size();
    }
    
    /**
     * returns the club for a pupil
     *
     * @param i The index of the club
     */
    public String getClubforPupil(int i) {
        return clubsRegistered.get(i);
    }
    
    /**
     * Checks if the club is in the club list
     *
     * @param clubName The name of the club
     * @return true or false 
     */
    public boolean checkIfClubInList(String clubName) {
        if (clubsRegistered.contains(clubName)){
            return true;
        } else {
            return false;
        }
    }
    
    /**
     * returns the saved state
     *
     * @return isSaved
     */
    public boolean getSaved() {
        return isSaved;
    }
    
    /**
     * sets the saved state
     *
     * @param saved the new save state
     */
    public void setSaved(boolean saved) {
        isSaved = saved;
    }
    
}
