#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import dayu_theme
from dayu_widgets.MItemModel import MSortFilterModel, MTableModel
from dayu_widgets.MItemView import MTableView, MTreeView, MBigView
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.qt import *


class MItemViewSet(QWidget):
    sig_double_clicked = Signal(QModelIndex)
    sig_left_clicked = Signal(QModelIndex)
    TableViewType = MTableView
    BigViewType = MBigView
    TreeViewType = MTreeView

    def __init__(self, type=None, searchable=False, parent=None):
        super(MItemViewSet, self).__init__(parent)
        self.main_lay = QVBoxLayout()
        self.main_lay.setSpacing(5)
        self.main_lay.setContentsMargins(0, 0, 0, 0)

        self.sort_filter_model = MSortFilterModel()
        self.source_model = MTableModel()
        self.sort_filter_model.setSourceModel(self.source_model)
        view_class = type or MItemViewSet.TableViewType
        self.item_view = view_class()
        self.item_view.doubleClicked.connect(self.sig_double_clicked)
        self.item_view.pressed.connect(self.slot_left_clicked)
        self.item_view.setModel(self.sort_filter_model)

        if searchable:
            search_size = dayu_theme.size.small
            self.search_line_edit = MLineEdit.search(size=search_size)
            self.search_attr_button = MToolButton(type=MToolButton.IconOnlyType, icon=MIcon('down_fill.svg'),
                                                  size=search_size)
            self.search_line_edit.add_prefix_widget(self.search_attr_button)
            self.search_line_edit.textChanged.connect(self.sort_filter_model.set_search_pattern)
            self.main_lay.addWidget(self.search_line_edit)
        self.main_lay.addWidget(self.item_view)
        self.setLayout(self.main_lay)

    @Slot(QModelIndex)
    def slot_left_clicked(self, start_index):
        button = QApplication.mouseButtons()
        if button == Qt.LeftButton:
            real_index = self.sort_filter_model.mapToSource(start_index)
            self.sig_left_clicked.emit(real_index)

    def set_header_list(self, header_list):
        self.source_model.set_header_list(header_list)
        self.sort_filter_model.set_header_list(header_list)
        self.sort_filter_model.setSourceModel(self.source_model)
        self.item_view.set_header_list(header_list)

    @Slot()
    def setup_data(self, data_list):
        self.source_model.clear()
        if data_list:
            self.source_model.set_data_list(data_list)

    def get_data(self):
        return self.source_model.get_data_list()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MItemViewSet(type=MItemViewSet.ListViewType)
    test.set_header_list(
        [{'label': 'Name', 'key': 'name', 'editable': True, 'selectable': True, 'exclusive': False, 'width': 200,
          }])
    # only_work_check_box = QCheckBox('Show Special Tasks')
    # only_work_check_box.setChecked(False)
    # only_work_check_box.stateChanged.connect(test.slot_update)
    # test.add_button(only_work_check_box)
    test.setup_data([{'name': ['xiaoming'], 'name_list': ['li', 'haha', 'xiaoming']}])
    test.show()
    sys.exit(app.exec_())
