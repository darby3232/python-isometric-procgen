from ui.ui_object import UIObject
import ui.ui_immediate_functions as ui_int
from ui.ui_immediate_functions import UIWindowFlags

class UITestObject(UIObject):

    def draw(self) -> None:
        if ui_int.begin_main_menu_bar():
            if ui_int.begin_menu("File", True):

                clicked_quit, selected_quit = ui_int.menu_item(
                    "Quit", 'Cmd+Q', False, True
                ) 

                if clicked_quit:
                    exit(1)

                ui_int.end_menu()

            ui_int.end_main_menu_bar()

        ui_int.begin("Custom window",
            False, 
            [
                UIWindowFlags.NO_MOVE,
                UIWindowFlags.NO_TITLE_BAR,
                UIWindowFlags.NO_RESIZE
            ]
        )       

        ui_int.text("Bar")
        ui_int.text_colored("Eggs", 0.2, 1., 0., 1.)

        # not yet implemented
		# imgui.text_ansi("B\033[31marA\033[mnsi ")
		# imgui.text_ansi_colored("Eg\033[31mgAn\033[msi ", 0.2, 1., 0.)

        ui_int.end()
