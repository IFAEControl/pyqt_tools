from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from guiqwt.plot import CurveDialog

def set_size_policy(widget, v_policy, h_policy):
    policy = QSizePolicy(v_policy, h_policy)
    widget.setSizePolicy(policy)

class Plot(QtWidgets.QWidget):

    def __init__(self, main, title, ylabel, xlabel, yunit, xunit):
        super(Plot, self).__init__()

        self._plot = CurveDialog(toolbar=True, wintitle=title,
                                 options=dict(ylabel=ylabel, yunit=yunit,
                                              xlabel=xlabel, xunit=xunit))

        self._plot.get_itemlist_panel().show()

        set_size_policy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        set_size_policy(self._plot, QSizePolicy.Expanding, QSizePolicy.Expanding)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.setObjectName("Plot")

        main.addWidget(self._plot)

    def add(self, item):
        self._plot.get_plot().add_item(item)