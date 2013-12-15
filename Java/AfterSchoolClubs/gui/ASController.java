package gui;


import java.awt.Component;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFileChooser;


/**
 *
 * @author Ollie Poole
 */
public class ASController {
    private ASView view;
    private ASModel model;


    public ASController(ASView view, ASModel model) {
        this.view = view;
        this.model = model;
        enableButtons();
    }

    public void addClub() {
        model.addClub(view.getClubName());
        view.setClubName("");
        enableButtons();
    }

    public void addPupilToClub() {
        String selClub = view.getSelectedClub();
        String selPupilFirst = view.getSelectedFirstName();
        String selPupilLast = view.getSelectedLastName();
        model.addPupilToClub(selClub, selPupilFirst, selPupilLast);
        //System.out.println(model.getClubDetails(selClub));
    }

    public void addPupil() {
        model.addPupil(view.getFirstName(), view.getLastName());
        view.setFirstName("");
        view.setLastName("");
        enableButtons();
    }

    public void selectClub() {
        enableButtons();
        view.setClubDetails();
    }

    public void selectPupil() {
        enableButtons();
        view.setPupilDetails();
        //System.out.println("Selected " + firstName + " " + lastName);
    }

    public void enableButtons() {
        String selClub = view.getSelectedClub();
        String selPupilFirst = view.getSelectedFirstName();
        String selPupilLast = view.getLastName();

        boolean enableAddToClub = (selClub != null) && (selPupilFirst != null)
                                    && (selPupilLast != null);

        view.setAddToClubEnabled(enableAddToClub);

        String firstName = view.getFirstName().trim();
        String lastName = view.getLastName().trim();
        boolean addPupilEnabled =(!firstName.isEmpty()) &&(!lastName.isEmpty());
        view.setAddPupilEnabled(addPupilEnabled);

        String clubName = view.getClubName().trim();
        view.setAddClubEnabled(!clubName.isEmpty());
    }

    public void loadFile(Component parent) {
        JFileChooser chooser = new JFileChooser();
        int returnVal = chooser.showOpenDialog(parent);
        if(returnVal == JFileChooser.APPROVE_OPTION){
           File file = chooser.getSelectedFile();
           String fileName = file.getAbsolutePath();
           try {
                model.loadFile(fileName);
            } catch (FileNotFoundException ex) {
                Logger.getLogger(ASController.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }

    public void saveFile(Component parent) {
        JFileChooser chooser = new JFileChooser();
        int returnVal = chooser.showSaveDialog(parent);
        if(returnVal == JFileChooser.APPROVE_OPTION){
           File file = chooser.getSelectedFile();
           String fileName = file.getAbsolutePath();
           try {
                model.saveFile(fileName);
            } catch (FileNotFoundException ex) {
                Logger.getLogger(ASController.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
    }
}
