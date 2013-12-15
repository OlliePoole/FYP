package gui;


import java.io.FileNotFoundException;
import java.util.Observable;
import java.util.Vector;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Ollie Poole
 */
public class ASModel extends Observable {
    private IAfterSchoolBase asBase;

    public ASModel(IAfterSchoolBase asBase) {
        this.asBase = asBase;
    }

    public Vector<String> getClubs() {
        Vector<String> result = new Vector<String>();
        int nbrClubs = asBase.getNbrClubs();
        for (int i=0;i<nbrClubs;i++) {
            result.add(asBase.getClub(i));
        }
                
        return result;
    }

    public Vector<String> getPupils() {
        Vector<String> result = new Vector<String>();
        int nbrPupils = asBase.getNbrPupils();
        for (int i=0;i<nbrPupils;i++) {
            result.add(asBase.getPupil(i));
        }

        return result;
    }

    public void addClub(String club) {
        asBase.addClub(club);
        setChanged();
        notifyObservers();
    }

    public void addPupil(String firstName, String lastName) {
        asBase.addPupil(firstName, lastName);
        setChanged();
        notifyObservers();
    }

    public void addPupilToClub(String club, String pupilFirst, String pupilLast) {
        asBase.addPupilToClub(club, pupilFirst, pupilLast);
        setChanged();
        notifyObservers();
    }

    public String getClubDetails(String club ) {
        StringBuffer resultBuf = new StringBuffer("Club: "+club+"\nMembers\n");
        int nbrPupils = asBase.getNbrPupilsForClub(club);
        for (int i=0;i<nbrPupils;i++) {
            resultBuf.append(asBase.getPupilForClub(club, i));
            resultBuf.append("\n");
        }

        String result = resultBuf.toString();
        return result;
    }

    public String getPupilDetails(String firstName, String lastName ) {
        StringBuffer resultBuf = new StringBuffer("Pupil: "+
                        firstName + " " +lastName + "\nClubs\n");
        int nbrClubs = asBase.getNbrClubsForPupil(firstName, lastName);
        for (int i=0;i<nbrClubs;i++) {
            resultBuf.append(asBase.getClubForPupil(firstName, lastName,i));
            resultBuf.append("\n");
        }

        String result = resultBuf.toString();
        return result;
    }

    void loadFile(String fileName) throws FileNotFoundException {
        asBase.load(fileName);
        setChanged();
        notifyObservers();
    }

    String getPupilFirstName(int index) {
        return asBase.getPupilFirstName(index);
    }

    String getPupilLastName(int index) {
        return asBase.getPupilLastName(index);
    }

    public void saveFile(String fileName) throws FileNotFoundException {
        asBase.save(fileName);
    }
}
