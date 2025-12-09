import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QGridLayout, QFrame,
    QMenuBar, QToolBar, QMenu,
    QLabel, QPushButton, QRadioButton, QCheckBox,
    QTabWidget, QLineEdit, QComboBox, QTextEdit, QSlider,
    QListWidget, QGroupBox, QSizePolicy
)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Title")  # Set the Window Title
        self.setGeometry(100, 100, 700, 500)  # Initial size

        # 1. Setup Menu Bar and Toolbar
        self._create_menu_bar()
        self._create_toolbar()

        # 2. Setup Central Widget and Layouts
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_v_layout = QVBoxLayout(central_widget)

        # Area for the Panel/Tabs (Top Half)
        top_half = QWidget()
        main_v_layout.addWidget(top_half)

        # Area for Text Fields (Bottom Half)
        bottom_half = QWidget()
        bottom_half.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        main_v_layout.addWidget(bottom_half)

        # Build the contents of the main areas
        self._create_top_half(top_half)
        self._create_bottom_half(bottom_half)

    def _create_menu_bar(self):
        menu_bar = self.menuBar()

        # MenuWidget1
        menu1 = menu_bar.addMenu("MenuWidget1")
        # You'd add QActions here, e.g.:
        # action1 = QAction("Action 1", self); menu1.addAction(action1)

        # MenuWidget2
        menu2 = menu_bar.addMenu("MenuWidget2")

    def _create_toolbar(self):
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # ToolbarButton (Simple Action)
        toolbar_action = QAction("ToolbarButton", self)
        # You would typically set an icon here: toolbar_action.setIcon(QIcon("path/to/icon.png"))
        toolbar.addAction(toolbar_action)

        # ToolbarCheckBox (Checkable Action)
        checkbox_action = QAction("ToolbarCheckBox", self)
        checkbox_action.setCheckable(True)
        checkbox_action.setChecked(True)  # Checked state from the image
        toolbar.addAction(checkbox_action)

    def _create_top_half(self, parent_widget):
        # Use a GroupBox for the "PanelCaption" area
        panel_group = QGroupBox("PanelCaption")

        # Set the GroupBox as the content of the top_half widget
        parent_layout = QVBoxLayout(parent_widget)
        parent_layout.addWidget(panel_group)

        # Layout inside the GroupBox (will use a horizontal split for the main panel area)
        panel_layout = QHBoxLayout(panel_group)

        # --- LEFT SIDE: List and Radio Buttons ---
        left_panel = QWidget()
        left_v_layout = QVBoxLayout(left_panel)
        panel_layout.addWidget(left_panel)

        # Horizontal layout for the List and Radio Buttons
        list_radio_h_layout = QHBoxLayout()
        left_v_layout.addLayout(list_radio_h_layout)

        # QListWidget (Items 1-5)
        list_widget = QListWidget()
        list_widget.addItems(["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"])
        list_widget.setCurrentRow(0)  # Select "Item 1"
        list_radio_h_layout.addWidget(list_widget)

        # Radio Buttons
        radio_group = QWidget()
        radio_v_layout = QVBoxLayout(radio_group)
        radio_v_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        QRadioButton("RadioButton1").setChecked(True);
        radio_v_layout.addWidget(QRadioButton("RadioButton1"))
        radio_v_layout.addWidget(QRadioButton("RadioButton2"))
        radio_v_layout.addWidget(QRadioButton("RadioButton3"))

        # Inactive Radio Button (Disabled)
        inactive_radio = QRadioButton("InactiveRadio")
        inactive_radio.setEnabled(False)
        radio_v_layout.addWidget(inactive_radio)

        list_radio_h_layout.addWidget(radio_group)

        # Button
        left_v_layout.addWidget(QPushButton("Button"))
        left_v_layout.addStretch(1)  # Push content to the top

        # --- RIGHT SIDE: Tab Widget ---
        tab_widget = QTabWidget()
        panel_layout.addWidget(tab_widget)

        # Tab 1: SelectedTab
        selected_tab = QWidget()
        tab_widget.addTab(selected_tab, "SelectedTab")
        tab_v_layout = QVBoxLayout(selected_tab)

        # Check Boxes
        tab_v_layout.addWidget(QCheckBox("UncheckedCheckBox"))
        checked_box = QCheckBox("CheckedCheckBox")
        checked_box.setChecked(True)
        tab_v_layout.addWidget(checked_box)

        inactive_box = QCheckBox("InactiveCheckBox")
        inactive_box.setEnabled(False)
        tab_v_layout.addWidget(inactive_box)

        # Slider (Horizontal)
        slider = QSlider(Qt.Orientation.Horizontal)
        tab_v_layout.addWidget(slider)

        tab_v_layout.addStretch(1)  # Push content to the top

        # Tab 2: OtherTab
        other_tab = QWidget()
        tab_widget.addTab(other_tab, "OtherTab")

    def _create_bottom_half(self, parent_widget):
        bottom_h_layout = QHBoxLayout(parent_widget)

        # --- LEFT SIDE: Text Input Stack ---
        left_stack = QWidget()
        left_stack_v_layout = QVBoxLayout(left_stack)
        left_stack_v_layout.setContentsMargins(0, 0, 0, 0)  # Remove margin for a compact look

        # Text Field (Password)
        left_stack_v_layout.addWidget(QLabel("TextField"))
        text_field = QLineEdit("••••••••••")
        text_field.setEchoMode(QLineEdit.EchoMode.Password)
        left_stack_v_layout.addWidget(text_field)

        # Combo Box (Dropdown)
        combo_box = QComboBox()
        combo_box.addItem("Item 1")
        combo_box.addItem("Item 2")
        combo_box.setCurrentIndex(0)
        left_stack_v_layout.addWidget(combo_box)

        bottom_h_layout.addWidget(left_stack)

        # --- RIGHT SIDE: Text Area ---
        right_stack = QWidget()
        right_stack_v_layout = QVBoxLayout(right_stack)
        right_stack_v_layout.setContentsMargins(0, 0, 0, 0)  # Remove margin for a compact look

        # Text Area
        right_stack_v_layout.addWidget(QLabel("TextArea"))
        text_area = QTextEdit()
        right_stack_v_layout.addWidget(text_area)

        bottom_h_layout.addWidget(right_stack)


# --- Main application execution ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
