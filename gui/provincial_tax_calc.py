import sys

from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QFormLayout,
    QDialog,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QLabel,
)
from PyQt6.QtGui import QIcon

class Province_Tax_Calc(QDialog):

    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Provincial Tax Calculator")
        self.setWindowIcon(QIcon("calculator.png"))
        layout=QFormLayout()
        label_province=QLabel('Select Province:')
        self.province_combo=QComboBox()
        self.province_combo.setFixedSize(900,30)
        self.province_combo.addItems(["select one","Alberta","British Columbia","Manitoba","New Brunswick","NewfoundLand","Northwest Territories","Nova Scotia","Nunavut","Ontario","Quebec","Saskatchewan","Yukon"])
        amount_label = QLabel('Enter Amount:')
        self.amount_text = QLineEdit()
        self.amount_text.setFixedHeight(30)
        tax_label = QLabel("Tax for Province:")
        self.pst_label=QLabel("PST:")
        self.tax_pst_text=QLineEdit()
        self.gst_label=QLabel("GST:")
        self.tax_gst_text=QLineEdit()
        self.hst_label=QLabel("HST:")
        self.tax_hst_text=QLineEdit()
        self.total_label = QLabel("Total Amount:")
        self.total_text = QLineEdit()
        self.total_text.setFixedHeight(30)
        calculate=QPushButton("Calculate")
        calculate.setStyleSheet("background-color:green;")
        hbox_province=QHBoxLayout()
        hbox_province.addWidget(label_province)
        hbox_province.addWidget(self.province_combo)
        layout.addRow(hbox_province)
        layout.addRow(amount_label,self.amount_text)
        hbox1_tax=QHBoxLayout()
        hbox1_tax.addWidget(tax_label)
        hbox1_tax.addWidget(self.pst_label)
        hbox1_tax.addWidget(self.tax_pst_text)
        hbox1_tax.addWidget(self.gst_label)
        hbox1_tax.addWidget(self.tax_gst_text)
        hbox1_tax.addWidget(self.hst_label)
        hbox1_tax.addWidget(self.tax_hst_text)
        layout.addRow(hbox1_tax)
        layout.addRow(self.total_label,self.total_text)
        layout.setSpacing(70)
        layout.addRow(calculate)
        self.province_combo.currentIndexChanged.connect(self.update_taxinput_Index)
        calculate.clicked.connect(self.calculate)
        self.setLayout(layout)

    def update_taxinput_Index(self,index):
        province = self.province_combo.itemText(index)
        if province == "Alberta":
            self.pst_label.hide()
            self.tax_pst_text.hide()
            self.gst_label.show()
            self.tax_gst_text.show()
            self.hst_label.hide()
            self.tax_hst_text.hide()
            self.tax_gst_text.setText("5%")
        elif province=="British Columbia":
            self.pst_label.show()
            self.tax_pst_text.show()
            self.gst_label.show()
            self.tax_gst_text.show()
            self.hst_label.hide()
            self.tax_hst_text.hide()
            self.tax_pst_text.setText("7%")
            self.tax_gst_text.setText("5%")
        elif province == "Manitoba":
            self.pst_label.show()
            self.tax_pst_text.show()
            self.gst_label.show()
            self.tax_gst_text.show()
            self.hst_label.hide()
            self.tax_hst_text.hide()
            self.tax_pst_text.setText("7%")
            self.tax_gst_text.setText("5%")
        elif province=="New Brunswick":
            self.pst_label.hide()
            self.tax_pst_text.hide()
            self.gst_label.hide()
            self.tax_gst_text.hide()
            self.hst_label.show()
            self.tax_hst_text.show()
            self.tax_hst_text.setText("15%")
        elif province=="NewfoundLand":
            self.pst_label.hide()
            self.tax_pst_text.hide()
            self.gst_label.hide()
            self.tax_gst_text.hide()
            self.hst_label.show()
            self.tax_hst_text.show()
            self.tax_hst_text.setText("15%")
        elif province=="Northwest Territories":
            self.pst_label.hide()
            self.tax_pst_text.hide()
            self.gst_label.show()
            self.tax_gst_text.show()
            self.hst_label.hide()
            self.tax_hst_text.hide()
            self.tax_gst_text.setText("5%")
        elif province=="Nova Scotia":
            self.pst_label.show()
            self.tax_pst_text.show()
            self.gst_label.show()
            self.tax_gst_text.show()
            self.hst_label.hide()
            self.tax_hst_text.hide()
            self.tax_pst_text.setText("7%")
            self.tax_gst_text.setText("5%")
        elif province=="Nunavut":
            self.pst_label.hide()
            self.tax_pst_text.hide()
            self.gst_label.show()
            self.tax_gst_text.show()
            self.hst_label.hide()
            self.tax_hst_text.hide()
            self.tax_gst_text.clear()
            self.tax_gst_text.setText("5%")
        elif province=="Ontario":
            self.pst_label.hide()
            self.tax_pst_text.hide()
            self.gst_label.hide()
            self.tax_gst_text.hide()
            self.hst_label.show()
            self.tax_hst_text.show()
            self.tax_hst_text.setText("15%")
        elif province=="Quebec":
            self.pst_label.show()
            self.tax_pst_text.show()
            self.gst_label.show()
            self.tax_gst_text.show()
            self.hst_label.hide()
            self.tax_hst_text.hide()
            self.tax_pst_text.setText("9.975%")
            self.tax_gst_text.setText("5%")
        elif province=="Saskatchewan":
            self.pst_label.show()
            self.tax_pst_text.show()
            self.gst_label.show()
            self.tax_gst_text.show()
            self.hst_label.hide()
            self.tax_hst_text.hide()
            self.tax_pst_text.setText("6%")
            self.tax_gst_text.setText("5%")
        else:
            self.pst_label.hide()
            self.tax_pst_text.hide()
            self.gst_label.show()
            self.tax_gst_text.show()
            self.hst_label.hide()
            self.tax_hst_text.hide()
            self.tax_gst_text.clear()
            self.tax_gst_text.setText("5%")

    def calculate(self):
        province=self.province_combo.currentText()
        if province == "select one":
            QMessageBox.warning(self, "Warning", "Please select a province from the dropdown.")
        else:
            amount = self.amount_text.text()
            if amount == "":
                QMessageBox.warning(self, "Warning", "Please enter an amount.")
            elif amount.isalpha():
                QMessageBox.warning(self, "Warning", "Please enter numeric value in the field of amount.")
            else:
                amount = float(amount)
                if province in ["Alberta", "Yukon", "Northwest Territories", "Nunavut"]:
                    tax_rate = float(self.tax_gst_text.text().strip("%"))/100
                elif province in ["Saskatchewan","Manitoba","British Columbia","Nova Scotia","Quebec"]:
                    tax_rate1 = float(self.tax_pst_text.text().strip("%"))
                    tax_rate2= float(self.tax_gst_text.text().strip("%"))
                    tax_rate=(tax_rate1+tax_rate2)/100
                else:
                    tax_rate = float(self.tax_hst_text.text().strip("%"))/100
                total_amount = amount + (amount * tax_rate)
                self.total_text.setText(str(total_amount))
if __name__ == "__main__":
    app = QApplication([])
    window = Province_Tax_Calc()
    window.setStyleSheet("background-color: #e9baa4;font-size:15px;")
    window.show()
    sys.exit(app.exec())