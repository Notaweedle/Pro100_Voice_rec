import sys, subprocess

if sys.platform == 'win32':
    import winreg


light_theme = """
QPushButton {
    background-color: rgb(248, 248, 248);
    border-radius: 10px;
    color: rgb(82, 82, 82);
    border: 1px solid #ccc;    
    padding: 6px 12px;
    margin-top: 2px;
    margin-bottom: 0px;
}

QPushButton:hover {
    background-color: #e5e5ea;
    margin-top: 0px;
    margin-bottom: 2px;
    border: 1px solid #999;   
}

QPushButton:pressed {
    background-color: #d1d1d6;
    margin-top: 2px;
    margin-bottom: 0px;
}

QPushButton:disabled {
    background-color: rgb(213, 213, 213);
}

QLineEdit{
    font-size: 12px;
    font-weight: 600;
    padding-right: 34px;
    background-color: transparent;
    border: none;
    border-radius: 0px;
    color: rgb(78, 78, 78);
}

QLineEdit#searchInput::placeholder {
	color: rgb(78, 78, 78);
}

QTabWidget {
    background-color: rgb(255, 255, 255);
    border-radius: 10px;
}

QTabBar::tab {
    color: rgb(178, 178, 178);
    font-size: 10px;      
    padding: 2.5px 5px;  
	border-radius:5px ;
	border: 2px black #ccc
}

QTabBar::tab:selected {
    color: black;          

}
QHeaderView::section {
    background-color: #f0f0f0;       /* header background */
    color: #555555;                  /* header text color */
    font-size: 10px;                 /* header font size */
    border: 1px solid #d1d1d6;
    padding: 3px;
}

QTableWidget QScrollBar:horizontal {
    height: 0px;
}

QTableWidget QScrollBar:vertical {
    width: 0px;
}

QListWidget{
	border-radius:5px;
	
	background-color: rgb(224, 224, 224);
	margin-bottom: 4px;
	color:black;
}

QTableWidget {
    background-color: #ffffff;       /* table background */
    color: #323232;                  /* text color */
    font-size: 11px;
    gridline-color: #d1d1d6;        /* grid lines */
    border: 1px solid #ccc;  
	border-radius: 5px;       /* optional border */
}

QTableWidget::item {
    padding: 5px;                    /* cell padding */
}

QHeaderView::section {
    background-color: #f0f0f0;       /* header background */
    color: #555555;                  /* header text color */
    font-size: 10px;                 /* header font size */
    padding: 3px;
}

QTableWidget::item:selected {
    background-color: #e5e5ea;       /* selected cell background */
    color: black;              
}

QTableWidget QHeaderView::section:vertical {
    background: transparent;   /* no background */
    color: transparent;        /* text invisible */
    border: none;              /* remove borders */
    padding: 0px;
    min-width: 0px;            /* collapse width */
    max-width: 0px;            /* collapse width */
}

QTableWidget QHeaderView::section:horizontal {
    border-radius: 3px;
}

QTableWidget {
    background-color: #ffffff;       /* table background */
    color: #323232;                  /* text color */
    font-size: 11px;
    gridline-color: #d1d1d6;        /* grid lines */
    border: 1px solid #ccc;
	 border-radius: 5px;     
}

QTableWidget::item {
    padding: 5px;                    /* cell padding */
}

QHeaderView::section {
    background-color: #f0f0f0;       /* header background */
    color: #555555;                  /* header text color */
    font-size: 10px;                 /* header font size */
    border: 1px solid #d1d1d6;
    padding: 3px;
}

QTableWidget::item:selected {
    background-color: #e5e5ea;       /* selected cell background */
    color: black;                     /* selected text color */
}

QTableWidget QHeaderView::section:vertical {
    background: transparent;   /* no background */
    color: transparent;        /* text invisible */
    border: none;              /* remove borders */
    padding: 0px;
    min-width: 0px;            /* collapse width */
    max-width: 0px;            /* collapse width */
}

QTableWidget QHeaderView::section:horizontal {
    border-radius: 3px;
}

QTableWidget QScrollBar:horizontal {
    height: 0px;
}

QTableWidget QScrollBar:vertical {
    width: 0px;
}


QComboBox {
    background-color: rgb(248, 248, 248);
    border-radius: 10px;
    padding: 5px 30px 5px 10px;
    font-size: 11px;
    color: #323232;
	border: 1px solid #ccc;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px;                  /* width of arrow area */
    border: none;                 /* remove any border */
    background: transparent;      /* remove the grey background */
}

QComboBox:hover {
    background-color: #e5e5ea;
}




QComboBox QAbstractItemView {
    background-color: white;          /* set desired background */
    border: 1px solid #d1d1d6;       /* optional border */
    selection-background-color: #e5e5ea; /* selected item background */
    selection-color: black;           /* selected text color */
    outline: 0;                       /* removes focus rectangle */
}

QSlider::groove:horizontal {
    height: 4px;             /* skinny track */
    border-radius: 2px;       /* smooth edges */
	background-color: rgb(222, 222, 222);
}

QSlider::sub-page:horizontal {
    background: #323232;  
    border-radius: 5px;
	
}


QSlider::handle:horizontal {
	background-color: rgb(136, 136, 136);
    width: 16px;
    height: 16px;
    margin: -5px 0;       
    border-radius: 7.2px;
}

QSlider::handle:horizontal:hover {
    background: #555555;
}

QSlider::handle:horizontal:pressed {
    background: #000000;
}


QDoubleSpinBox {
    background-color: rgb(248, 248, 248);
    border-radius: 6px;
    color: #323232;
    font-size: 11px;
	width:10px;
	border: .5px solid #ccc;
}

/* Hover effect */
QDoubleSpinBox:hover {
    background-color: #e5e5ea;
}

/* Pressed/active effect */
QDoubleSpinBox:pressed {
    background-color: #d1d1d6;
}

/* Disabled state */
QDoubleSpinBox:disabled {
    background-color: #dcdcdc;
    color: #a0a0a0;
}

QDoubleSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 10px;
    border: none;
    background: transparent; /* remove default grey */
}

QDoubleSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 10px;
    border: none;
    background: transparent;
}

QLabel{
color: rgb(82, 82, 82);
}

"""

dark_theme = """
QPushButton {
    background-color: #2b2b2b;
    border-radius: 10px;
    color: #f0f0f0;
    border: 1px solid #555;    
    padding: 6px 12px;
    margin-top: 2px;
    margin-bottom: 0px;
}

QPushButton:hover {
    background-color: #3a3a3a;
    margin-top: 0px;
    margin-bottom: 2px;
    border: 1px solid #888;   
}

QPushButton:pressed {
    background-color: #1e1e1e;
    margin-top: 2px;
    margin-bottom: 0px;
}

QPushButton:disabled {
    background-color: #555;
    color: #888;
}

QLineEdit{
    font-size: 12px;
    font-weight: 600;
    padding-right: 34px;
    background-color: #1e1e1e;
    border: none;
    border-radius: 0px;
    color: #f0f0f0;
}

QLineEdit#searchInput::placeholder {
	color: #aaaaaa;
}

QTabWidget {
    background-color: #2b2b2b;
    border-radius: 10px;
}

QTabBar::tab {
    color: #999999;
    font-size: 10px;      
    padding: 2.5px 5px;  
	border-radius:5px ;
	border: 2px solid #444;
}

QTabBar::tab:selected {
    color: white;          
}

QHeaderView::section {
    background-color: #3a3a3a;  
    color: #cccccc;               
    font-size: 10px;                
    border: 1px solid #555;
    padding: 3px;
}

QTableWidget QScrollBar:horizontal {
    height: 0px;
}

QTableWidget QScrollBar:vertical {
    width: 0px;
}

QListWidget{
	border-radius:5px;
	background-color: #2b2b2b;
	margin-bottom: 4px;
	color: white;
}

QTableWidget {
    background-color: #1e1e1e;       
    color: #f0f0f0;                  
    font-size: 11px;
    gridline-color: #555;        
    border: 1px solid #444;  
	border-radius: 5px;       
}

QTableWidget::item {
    padding: 5px;                    
}

QHeaderView::section {
    background-color: #3a3a3a;      
    color: #cccccc;                 
    font-size: 10px;                 
    padding: 3px;
}

QTableWidget::item:selected {
    background-color: #555;       
    color: white;              
}

QTableWidget QHeaderView::section:vertical {
    background: transparent;
    color: transparent;
    border: none;
    padding: 0px;
    min-width: 0px;
    max-width: 0px;
}

QTableWidget QHeaderView::section:horizontal {
    border-radius: 3px;
}

QComboBox {
    background-color: #2b2b2b;
    border-radius: 10px;
    padding: 5px 30px 5px 10px;
    font-size: 11px;
    color: #f0f0f0;
	border: 1px solid #555;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px;
    border: none;
    background: transparent;
}

QComboBox:hover {
    background-color: #3a3a3a;
}

QComboBox QAbstractItemView {
    background-color: #2b2b2b;
    border: 1px solid #555;
    selection-background-color: #444;
    selection-color: white;
    outline: 0;
}

QSlider::groove:horizontal {
    height: 4px;
    border-radius: 2px;
	background-color: #444;
}

QSlider::sub-page:horizontal {
    background: #f0f0f0;  
    border-radius: 5px;
}

QSlider::handle:horizontal {
	background-color: #888;
    width: 16px;
    height: 16px;
    margin: -5px 0;       
    border-radius: 7.2px;
}

QSlider::handle:horizontal:hover {
    background: #aaa;
}

QSlider::handle:horizontal:pressed {
    background: white;
}

QDoubleSpinBox {
    background-color: #2b2b2b;
    border-radius: 6px;
    color: #f0f0f0;
    font-size: 11px;
	width:10px;
	border: .5px solid #555;
}

QDoubleSpinBox:hover {
    background-color: #3a3a3a;
}

QDoubleSpinBox:pressed {
    background-color: #1e1e1e;
}

QDoubleSpinBox:disabled {
    background-color: #444;
    color: #888;
}

QDoubleSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 10px;
    border: none;
    background: transparent;
}

QDoubleSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 10px;
    border: none;
    background: transparent;
}

QLabel{
    color: #f0f0f0;
}

"""

def is_dark_mode():
    if sys.platform == 'win32':  # Windows
        try:
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return value == 0
        except Exception:
            return False

    elif sys.platform.startswith('linux'):  # Linux
        try:
            result = subprocess.run(
                ["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
                capture_output=True,
                text=True
            )
            return "dark" in result.stdout.lower()
        except Exception:
            return False

    elif sys.platform == 'darwin':
        try:
            result = subprocess.run(
                ["defaults", "read", "-g", "AppleInterfaceStyle"],
                capture_output=True,
                text=True
            )
            return "dark" in result.stdout.lower()
        except Exception:
            return False

    return False  # default to light

def set_theme():
    if is_dark_mode():
        return dark_theme
    else:
        return light_theme

