package gui;


import java.awt.Component;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.Observable;
import java.util.Observer;
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;



/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Ollie Poole
 */
public class ASView implements Observer {
    private static final int LIST_WIDTH = 400;
    private static final int LIST_HEIGHT = 200;
    private static final int BUTTON_WIDTH = 110;
    private static final int BUTTON_HEIGHT = 25;

    private ASModel model;
    private ASController controller;

    private JFrame frame = new JFrame("After School Database");
    private JList clubList;
    private JList pupilList;
    private JTextArea clubDetailsArea = new JTextArea();
    private JTextArea pupilDetailsArea = new JTextArea();
    private JButton loadButton = new JButton("Load...");
    private JButton saveButton = new JButton("Save...");
    private JButton addClubButton = new JButton("Add Club");
    private JButton addPupilButton = new JButton("Add Pupil");
    private JButton addToClubButton = new JButton("Add Pupil To Club");
    private JTextField clubField = new JTextField();
    private JTextField firstNameField = new JTextField();
    private JTextField lastNameField = new JTextField();

    public ASView(ASModel model) {
        this.model = model;
        model.addObserver(this);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container contentPane = frame.getContentPane();
        contentPane.setLayout(new BoxLayout(contentPane, BoxLayout.Y_AXIS));
        JPanel topPanel = makeTopPanel();
        contentPane.add(topPanel);
        JPanel buttonPanel = makeButtonPanel();
        contentPane.add(buttonPanel);
        JPanel addClubPanel = makeAddClubPanel();
        contentPane.add(addClubPanel);
        JPanel addPupilPanel = makeAddPupilPanel();
        contentPane.add(addPupilPanel);
        
        frame.pack();
        frame.setResizable(false);
        frame.setVisible(true);
    }

    public void setController(ASController controller) {
        this.controller = controller;
    }

    private JPanel makeButtonPanel() {
        JPanel result = new JPanel();
        result.setLayout(new BoxLayout(result, BoxLayout.X_AXIS));

        setStandardSize(loadButton);
        loadButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {
                controller.loadFile(frame);
            }
        });

        setStandardSize(saveButton);
        saveButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {
                controller.saveFile(frame);
            }
        });


        addToClubButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {
                controller.addPupilToClub();
            }
        });

        result.add(loadButton);
        result.add(saveButton);        
        result.add(addToClubButton);
        Component glue = Box.createHorizontalGlue();
        result.add(glue);

        return result;
    }
    private JPanel makeAddClubPanel() {
        JPanel result = new JPanel();
        result.setLayout(new BoxLayout(result, BoxLayout.X_AXIS));

        setStandardSize(addClubButton);

        addClubButton.addActionListener( new ActionListener() {

            public void actionPerformed(ActionEvent e) {
                controller.addClub();
            }
        });

        result.add(addClubButton);

        clubField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyReleased(KeyEvent e) {
                controller.enableButtons();
                if ((e.getKeyCode() == KeyEvent.VK_ENTER) &&
                        addClubButton.isEnabled()){
                    controller.addClub();
                }
            }
        });

        result.add(clubField);


        Component glue = Box.createHorizontalGlue();
        result.add(glue);

        return result;
    }

    private JPanel makeAddPupilPanel() {
        JPanel result = new JPanel();
        result.setLayout(new BoxLayout(result, BoxLayout.X_AXIS));

        setStandardSize(addPupilButton);
        addPupilButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {;
                controller.addPupil();
            }
        });

        result.add(addPupilButton);

        firstNameField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyReleased(KeyEvent e) {
                controller.enableButtons();
            }
        });
        result.add(firstNameField);

        lastNameField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyReleased(KeyEvent e) {
                controller.enableButtons();
                if ((e.getKeyCode() == KeyEvent.VK_ENTER) &&
                        addPupilButton.isEnabled()){
                    controller.addPupil();
                }
            }
        });
        result.add(lastNameField);
        Component glue = Box.createHorizontalGlue();
        result.add(glue);

        return result;
    }

    private JPanel makeTopPanel() {
        JPanel result = new JPanel();
        result.setLayout(new GridLayout(2,2));
        JPanel clubsPanel = makeClubsPanel();
        result.add(clubsPanel);
        JPanel pupilsPanel = makePupilsPanel();
        result.add(pupilsPanel);
        JPanel clubDetailsPanel = makeClubDetailsPanel();
        result.add(clubDetailsPanel);
        JPanel pupilDetailsPanel = makePupilDetailsPanel();
        result.add(pupilDetailsPanel);

        return result;
    }

    private JPanel makeClubsPanel() {
        JPanel result = new JPanel();
        result.setLayout(new BoxLayout(result, BoxLayout.Y_AXIS));

        result.add(new JLabel("Clubs"));

        clubList = new JList();
        clubList.addListSelectionListener(new ListSelectionListener() {

            public void valueChanged(ListSelectionEvent e) {
                    controller.selectClub();
                }
            });

        JScrollPane clubScroll = new JScrollPane(clubList);
        clubScroll.setPreferredSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));
        clubScroll.setMinimumSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));
        clubScroll.setMaximumSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));

        result.add(clubScroll);

        return result;
    }

    private JPanel makeClubDetailsPanel() {
        JPanel result = new JPanel();
        result.setLayout(new BoxLayout(result, BoxLayout.Y_AXIS));

        result.add(new JLabel("Club Details"));

        JScrollPane clubDetailsScroll = new JScrollPane(clubDetailsArea);
        clubDetailsScroll.setPreferredSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));
        clubDetailsScroll.setMinimumSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));
        clubDetailsScroll.setMaximumSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));

        result.add(clubDetailsScroll);

        return result;
    }

    private JPanel makePupilsPanel() {
        JPanel result = new JPanel();
        result.setLayout(new BoxLayout(result, BoxLayout.Y_AXIS));

        result.add(new JLabel("Pupils"));

        pupilList = new JList();

        pupilList.addListSelectionListener( new ListSelectionListener() {

            public void valueChanged(ListSelectionEvent e) {
                controller.selectPupil();
            }
        });

        JScrollPane pupilScroll = new JScrollPane(pupilList);
        pupilScroll.setPreferredSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));
        pupilScroll.setMinimumSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));
        pupilScroll.setMaximumSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));

        result.add(pupilScroll);

        return result;
    }


    private JPanel makePupilDetailsPanel() {
        JPanel result = new JPanel();
        result.setLayout(new BoxLayout(result, BoxLayout.Y_AXIS));

        result.add(new JLabel("Pupil Details"));

        JScrollPane pupilDetailsScroll = new JScrollPane(pupilDetailsArea);
        pupilDetailsScroll.setPreferredSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));
        pupilDetailsScroll.setMinimumSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));
        pupilDetailsScroll.setMaximumSize(new Dimension(LIST_WIDTH,LIST_HEIGHT));

        result.add(pupilDetailsScroll);

        return result;
    }

    public String getClubName() {
        return clubField.getText();
    }

    public void setClubName(String text) {
        clubField.setText(text);
    }

    public String getFirstName() {
        return firstNameField.getText();
    }

    public void setFirstName(String firstName) {
        firstNameField.setText(firstName);
    }

    public String getLastName() {
        return lastNameField.getText();
    }

    public void setLastName(String lastName) {
        lastNameField.setText(lastName);
    }

    public void setAddToClubEnabled(boolean enabled) {
        addToClubButton.setEnabled(enabled);
    }

    public String getSelectedClub() {
        Object obj = clubList.getSelectedValue();
        if (obj != null) {
            return obj.toString();
        }
        else {
            return null;
        }
    }

    public void setClubDetails() {
        String selClub = getSelectedClub();
        if (selClub != null) {
            clubDetailsArea.setText(model.getClubDetails(selClub));
        }
        else {
            clubDetailsArea.setText("");
        }
    }

    public void setPupilDetails() {
        String firstName = getSelectedFirstName();
        String lastName = getSelectedLastName();
        String details;
        if ((firstName != null) && (lastName != null)) {
            details = model.getPupilDetails(firstName, lastName);
        }
        else {
            details = "";
        }
        pupilDetailsArea.setText(details);
    }

    public String getSelectedFirstName() {
        String result;
        int index = pupilList.getSelectedIndex();
        if (index >= 0) {
            result = model.getPupilFirstName(index);
        }
        else {
            result = null;
        }
        return result;
    }

    public String getSelectedLastName() {
        String result;
        int index = pupilList.getSelectedIndex();
        if (index >= 0) {
            result = model.getPupilLastName(index);
        }
        else {
            result = null;
        }
        return result;
    }

    public String getSelectedPupil() {
        Object obj = pupilList.getSelectedValue();
        if (obj != null) {
            return obj.toString();
        }
        else {
            return null;
        }
    }


    public void update(Observable o, Object arg) {
        String selClub = getSelectedClub();
        String selPupil = getSelectedPupil();

        clubList.setListData(model.getClubs());
        clubList.setSelectedValue(selClub, true);

        pupilList.setListData(model.getPupils());
        pupilList.setSelectedValue(selPupil, true);
        
        setClubDetails();
        setPupilDetails();
    }

    public void setAddPupilEnabled(boolean addPupilEnabled) {
        addPupilButton.setEnabled(addPupilEnabled);
    }

    public void setAddClubEnabled(boolean enabled) {
        addClubButton.setEnabled(enabled);
    }

    private void setStandardSize(JButton button) {
        final Dimension size = (new Dimension(BUTTON_WIDTH,BUTTON_HEIGHT));
        button.setPreferredSize(size);
    }

}
