
import gui.ASController;
import gui.ASModel;
import gui.ASView;
import gui.IAfterSchoolBase;

/**
 *
 * @author David Sutton
 */
public class GUIMain {
    public static void main(String[] args) {
        IAfterSchoolBase asBase = new AfterSchoolBase();
        ASModel model = new ASModel(asBase);
        ASView view = new ASView(model);
        ASController controller = new ASController(view, model);
        view.setController(controller);
    }
}
