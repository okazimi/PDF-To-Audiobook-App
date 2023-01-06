# IMPORT PYSIDE6 FOR GUI
from PySide6 import QtWidgets, QtCore
# IMPORTS PDF READING
import PyPDF3
import pyttsx3
import pdfplumber


# CLASS WHICH EXTENDS QWIDGET
class MyWidget(QtWidgets.QWidget):

    # INITIALIZATION METHOD
    def __init__(self):
        # SUPER INIT
        super().__init__()
        # SET WIDGET WINDOW TITLE
        self.setWindowTitle("The Converter")
        # HEADER
        self.title = QtWidgets.QLabel("PDF to Audio Converter")
        # DESCRIPTION
        self.desc = QtWidgets.QLabel("Upload your PDF using the button below")
        # UPLOAD BUTTON
        self.button = QtWidgets.QPushButton("Upload")
        # LAYOUT PROPERTIES
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.title, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.desc, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)
        # IF BUTTON IS CLICKED, CALL CONVERTPDF METHOD
        self.button.clicked.connect(self.convertPdf)

    # QTCORE.SLOT NOTES:
    # ALLOWS PYTHON TO INTERFACE WITH QT SLOT DELIVERY MECHANISM
    # HELPS CONNECT BUTTON TO METHOD WHEN CLICKED
    # SAVES MEMORY AND IS FASTER
    @QtCore.Slot()
    # CONVERTPDF METHOD
    def convertPdf(self):
        # PROMPT USER TO SELECT PDF FILE
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open PDF", "C:/", "PDF (*.pdf)")[0]
        # INITIALIZE PDF FILE OBJECT
        pdf_file = open(filename, "rb")
        # INITIALIZE PDF READER OBJECT
        pdf_reader = PyPDF3.PdfFileReader(pdf_file)
        # COUNT NUMBER OF PAGES IN PDF
        pages = pdf_reader.numPages
        # EXTRACT TEXT FROM PDF FILE
        # INITIALIZE EMPTY TEXT STRING TO APPEND TO
        final_text = ""
        # OPEN FILE WITH PDFPLUMBER
        with pdfplumber.open(filename) as pdf:
            # LOOP THROUGH ALL PAGES OF THE PDF FILE
            for i in range(0, pages):
                # SELECT DESIRED PAGE
                page = pdf.pages[i]
                # EXTRACT TEXT ON SELECTED PAGE
                text = page.extract_text()
                # APPEND EXTRACTED TEXT TO FINALTEXT STRING
                final_text += text
        # VOICE
        # START ENGINE
        engine = pyttsx3.init()
        # SET VOICE
        engine.setProperty('voice',
                           "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        # RECITE EXTRACTED TEXT
        engine.say(final_text)
        # RUN
        engine.runAndWait()





