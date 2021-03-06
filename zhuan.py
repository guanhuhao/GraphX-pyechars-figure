# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhuan'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import untitled
import sys,os
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl, Qt
from PyQt5 import QtWebEngineWidgets,QtCore,QtGui
from pyecharts import Bar, Pie, Line,Overlap
from pyecharts_javascripthon.api import TRANSLATOR
import time


import re

active_time_list = []
get_data_time_list = []
dcal_time_list = []
active_num_list = []

active_time_info = []
get_data_time_info = []
dcal_time_info = []
active_num_info = []

sync_point_time = []
sync_edge_time = []
cal_time = []
count_time = []
tot_time = []

sync_point_time_info = []
sync_edge_time_info = []
cal_time_info = []
count_time_info = []
tot_time_info = []

current_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
partition_num = 4

labelsize = 16
xysize = 25

def getlist(string):
    string = string[1:-2]
    string = string.split(', ')
    return list(map(float,string))

def getuple(string):
    string = string[0:-1]
    string = string.split(' ')
    return (float(string[1]))

def loaddata(filename):
    global  active_time_list,\
    get_data_time_list,\
    dcal_time_list,\
    active_num_list,\
    active_time_info,\
    get_data_time_info,\
    dcal_time_info,\
    active_num_info,\
    sync_point_time,\
    sync_edge_time,\
    cal_time,\
    count_time,\
    tot_time,\
    sync_point_time_info,\
    sync_edge_time_info,\
    cal_time_info,\
    count_time_info,\
    tot_time_info

    active_time_list = []
    get_data_time_list = []
    dcal_time_list = []
    active_num_list = []

    active_time_info = []
    get_data_time_info = []
    dcal_time_info = []
    active_num_info = []

    sync_point_time = []
    sync_edge_time = []
    cal_time = []
    count_time = []
    tot_time = []

    sync_point_time_info = []
    sync_edge_time_info = []
    cal_time_info = []
    count_time_info = []
    tot_time_info = []

    with open(father_path + '\\'+filename, 'r') as files:
        for i in range(0, partition_num):
            line = files.readline()
            if (len(line) <= 3): continue
            active_time_list.append(getlist(line))
        for i in range(0, partition_num): active_time_info.append(getuple(files.readline()))

        for i in range(0, partition_num):
            line = files.readline()
            if (len(line) <= 3): continue
            get_data_time_list.append(getlist(line))
        for i in range(0, partition_num): get_data_time_info.append(getuple(files.readline()))

        for i in range(0, partition_num):
            line = files.readline()
            if (len(line) <= 3): continue
            dcal_time_list.append(getlist(line))
        for i in range(0, partition_num): dcal_time_info.append(getuple(files.readline()))

        for i in range(0, partition_num):
            line = files.readline()
            if (len(line) <= 3): continue
            active_num_list.append(getlist(line))
        for i in range(0, partition_num): active_num_info.append(getuple(files.readline()))

        sync_point_time = getlist(files.readline())
        sync_point_time_info = getuple(files.readline())

        sync_edge_time = getlist(files.readline())
        sync_edge_time_info = getuple(files.readline())

        line = files.readline()
        if len(line) > 3: cal_time = getlist(line)
        cal_time_info = getuple(files.readline())

        count_time = getlist(files.readline())
        count_time_info = getuple(files.readline())

        tot_time = getlist(files.readline())
        tot_time_info = getuple(files.readline())

class Windows(QDialog):
    def __init__(self,parent=None):
        super(QDialog, self).__init__(parent)

        self.checkOverall = False
        self.checkPartition = False

        self.initUi()
        self.load_url()

        # self.RunBotton.icon

    def initUi(self):
        self.ui = untitled.Ui_Form()
        self.ui.setupUi(self)

        self.OverallCanvas = QtWebEngineWidgets.QWebEngineView()
        self.ui.OverallLayout.addWidget(self.OverallCanvas)

        self.PartitionCanvas = QtWebEngineWidgets.QWebEngineView()
        self.ui.PartitionLayout.addWidget(self.PartitionCanvas)

    def Create_Overall_Iteration_Time(self):
        line = Line("", "",) # main Title and sub title
        X = []
        for i in range(1,len(sync_point_time)+1): X.append(i)

        line.add("GraphX synchronization",X, sync_point_time, is_smooth=True, mark_line=["max"],line_width=2)
        line.add("GraphX maintenance",X, sync_edge_time, is_smooth=True, mark_line=["max"],line_width=2)
        line.add("Computation",X, cal_time, is_smooth=True, mark_line=["max"],line_width=2)
        line.add("Result aggregation", X, tot_time, is_smooth=True, mark_line=["max"], xaxis_name="Iteration", yaxis_name="Time(s)",\
                 label_text_size=labelsize,label_color=None,legend_text_size=labelsize,xaxis_name_size=xysize,yaxis_name_size=xysize,line_width=2)

        snippet = TRANSLATOR.translate(line.options)
        options = snippet.as_snippet()
        print(options)
        return options

    def Runtime_Percentage(self):
        pie = Pie("", "")

        labels = ['GraphX synchronization', 'GraphX maintenance', 'Computation', 'Result aggregation']
        sizes = [sync_point_time_info, sync_edge_time_info, cal_time_info, count_time_info]

        pie.add("Pie",labels,sizes,is_label_show=True,\
                label_text_size=labelsize,label_color=None,legend_text_size=labelsize,xaxis_name_size=xysize,yaxis_name_size=xysize,yaxis_label_textsize=xysize,label_emphasis_textsize=labelsize)

        snippet = TRANSLATOR.translate(pie.options)
        options = snippet.as_snippet()
        self.writelog("Showing percentage pie chart of computing steps...")
        return options

    def NoneSelect(self):
        bar = Bar("", "")
        # v1 = {}
        X = ["Active Vertex Detection", "Active Vertex collection", "Message Generation"]
        Ave = [0,0,0]
        Max = [-1,-1,-1]
        Min = [1000000,100000,1000000]

        for i in range(4):
            Ave[0] += active_time_info[i]/4.0
            Ave[1] += get_data_time_info[i]/4.0
            Ave[2] += dcal_time_info[i]/4.0

            Max[0] = max(Max[0], active_time_info[i])
            Max[1] = max(Max[1], get_data_time_info[i])
            Max[2] = max(Max[2], dcal_time_info[i])

            Min[0] = min(Min[0], active_time_info[i])
            Min[1] = min(Min[1], get_data_time_info[i])
            Min[2] = min(Min[2], dcal_time_info[i])

        bar.add('Minimum', X, Min, is_more_utils=True)
        bar.add('Average', X, Ave, is_more_utils=True)
        bar.add('Maximum', X, Max, is_more_utils=True)

        snippet = TRANSLATOR.translate(bar.options)
        options = snippet.as_snippet()

        return options

    def BothSelect(self):
        item = self.ui.SelectIterator.selectedItems()
        if item == [] :
            iterator = QTreeWidgetItemIterator(self.ui.SelectIterator)
            item = iterator.value()
        else : item = item[0]
        pie = Pie("","")
        labels = ['Active Vertex Detection', 'Active Vertex Collection', 'Message Generation']
        sizes = [float(item.text(1)), float(item.text(2)), float(item.text(3))]

        pie.add("Pie",labels,sizes,is_label_show=True,\
                label_text_size=labelsize,label_color=None,legend_text_size=labelsize,xaxis_name_size=xysize,yaxis_name_size=xysize,label_emphasis_textsize=labelsize)

        snippet = TRANSLATOR.translate(pie.options)
        options = snippet.as_snippet()
        self.writelog("Showing percentage pie chart of computation breakdown by partitions and iterations...")
        return options

    def OnlyPartition(self):

        item = self.ui.SelectPartition.selectedItems()

        if item == [] : row=0
        else : row = int(item[0].text(0)[-1])
        line = Line("", "")  # main Title and sub title
        X = []
        for i in range(1, len(active_time_list[0])+1): X.append(i)
        line.add("Active Vertex Detection", X, active_time_list[row], is_smooth=True, mark_line=["max"],line_width=2)
        line.add("Active Vertex Collection", X, get_data_time_list[row], is_smooth=True, mark_line=["max"],line_width=2)
        line.add("Message Generation", X, dcal_time_list[row], is_smooth=True, mark_line=["max"], xaxis_name="Iteration",\
                 yaxis_name="Time(s)",label_text_size=labelsize,label_color=None,legend_text_size=labelsize,xaxis_name_size=xysize,yaxis_name_size=xysize,line_width=2)
        snippet = TRANSLATOR.translate(line.options)
        options = snippet.as_snippet()
        self.writelog("Showing all iterations by partition ... ")
        return options

    def OnlyIterator(self):
        item = self.ui.SelectIterator.selectedItems()
        if item == [] : row=0
        else : row = int(item[0].text(0))

        bar = Bar("","")
        # v1 = {}
        X = ["Active Vertex Detection","Active Vertex Collection","Message Generation"]

        bar.add('Partition 0', X, [active_time_list[0][row],get_data_time_list[0][row],dcal_time_list[0][row]], is_more_utils=True)
        bar.add('Partition 1', X, [active_time_list[1][row],get_data_time_list[1][row],dcal_time_list[1][row]], is_more_utils=True)
        bar.add('Partition 2', X, [active_time_list[2][row],get_data_time_list[2][row],dcal_time_list[2][row]], is_more_utils=True)
        bar.add('Partition 3', X, [active_time_list[3][row],get_data_time_list[3][row],dcal_time_list[3][row]], is_more_utils=True)
        snippet = TRANSLATOR.translate(bar.options)
        options = snippet.as_snippet()
        return options

    def writelog(self,str):
        path = os.getcwd() + "> "
        curtime = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
        self.ui.textBrowser.append(curtime+path+str)

    def load_url(self):
        # QUrl.fromLocalFile(QtCore.QFileInfo("template.html").absoluteFilePath())
        url = QUrl.fromLocalFile(QtCore.QFileInfo("template.html").absoluteFilePath())
        url2 = QUrl.fromLocalFile(QtCore.QFileInfo("template2.html").absoluteFilePath())
        self.OverallCanvas.load(url)
        self.OverallCanvas.loadFinished.connect(self.SelectGraph)

        self.PartitionCanvas.load(url2)
        self.PartitionCanvas.loadFinished.connect(self.DrawPartitionCanvas)


    # slot function
    def RunBotton(self):
        if self.ui.SelectBox.currentIndex() == 0 : loaddata("data1.txt")
        if self.ui.SelectBox.currentIndex() == 1 : loaddata("data2.txt")
        self.writelog("Switching data source...")
        time.sleep(1)
        # loaddata()
        self.writelog("Finished switching data source...")
        self.ui.SelectIterator.clear()
        for i in range(0, len(active_time_list[0])):
            iitem = QTreeWidgetItem(self.ui.SelectIterator)
            iitem.setText(0, str(i))
            iitem.setText(1, str(active_time_list[0][i]))
            iitem.setText(2, str(get_data_time_list[0][i]))
            iitem.setText(3, str(dcal_time_list[0][i]))

            if active_num_list == []:
                iitem.setText(4, "0")
            else:
                iitem.setText(4, str(active_num_list[0][i]))
        self.DrawPartitionCanvas()
        self.SelectGraph(0)

    def CheckIterator(self, i):
        if i : self.ui.SelectIterator.setEnabled(True)
        else : self.ui.SelectIterator.setEnabled(False)

        row = 0
        self.ui.SelectIterator.clear()

        for i in range(0, len(active_time_list[row])):
            iitem = QTreeWidgetItem(self.ui.SelectIterator)
            iitem.setText(0, str(i))
            iitem.setText(1, str(active_time_list[row][i]))
            iitem.setText(2, str(get_data_time_list[row][i]))
            iitem.setText(3, str(dcal_time_list[row][i]))

            if active_num_list == []:
                iitem.setText(4, "0")
            else:
                iitem.setText(4, str(active_num_list[row][i]))
        self.writelog("Switching iteration checkbox status...")
        self.DrawPartitionCanvas()

    def CheckPartition(self, i):
        if i :  self.ui.SelectPartition.setEnabled(True)
        else :  self.ui.SelectPartition.setEnabled(False)
        row = 0
        self.ui.SelectIterator.clear()
        iterator = QTreeWidgetItemIterator(self.ui.SelectPartition)
        item = iterator.value()

        for i in range(0, len(active_time_list[row])):
            iitem = QTreeWidgetItem(self.ui.SelectIterator)
            iitem.setText(0, str(i))
            iitem.setText(1, str(active_time_list[row][i]))
            iitem.setText(2, str(get_data_time_list[row][i]))
            iitem.setText(3, str(dcal_time_list[row][i]))

            if active_num_list == []:
                iitem.setText(4, "0")
            else:
                iitem.setText(4, str(active_num_list[row][i]))
        self.writelog("Switching partition checkbox status...")
        self.DrawPartitionCanvas()

    def SelectGraph(self,i):
        if self.ui.Tab.currentIndex() != 0 : return
        if not self.checkOverall: # dark style
            # ?????????echarts
            self.OverallCanvas.page().runJavaScript(
                '''
                    var myChart = echarts.init(document.getElementById('container'), 'light', {renderer: 'canvas'});
                '''
            )
            self.checkOverall = True
            i=0

        # if not self.checkOverall: # light style
        #     # ?????????echarts
        #     self.OverallCanvas.page().runJavaScript(
        #         '''
        #             var myChart = echarts.init(document.getElementById('container'), 'light', {renderer: 'canvas'});
        #         '''
        #     )
        #     self.checkOverall = True
        #     i=0

        if i == 0 : options = self.Create_Overall_Iteration_Time()
        if i == 1 : options = self.Runtime_Percentage()

        self.OverallCanvas.page().runJavaScript(
            f'''
                myChart.clear();
                var option = eval({options});
                myChart.setOption(option);
            '''
        )
        self.writelog("Loading overall information page...")

    def SelectPartition(self,item,col):
        row = int(item.text(0)[-1])
        self.ui.SelectIterator.clear()

        iterator = QTreeWidgetItemIterator(self.ui.SelectPartition)
        while iterator.value():
            tmp = iterator.value()
            tmp.setText(1,"")
            iterator.__iadd__(1)
        item.setText(1,"???")

        for i in range(0,len(active_time_list[row])):
            iitem = QTreeWidgetItem(self.ui.SelectIterator)
            iitem.setText(0, str(i))
            iitem.setText(1, str(active_time_list[row][i]))
            iitem.setText(2, str(get_data_time_list[row][i]))
            iitem.setText(3, str(dcal_time_list[row][i]))
            # if active_num_list == [] : iitem.setText(4,"0")
            # else : iitem.setText(4, str(active_num_list[row][i]))
        self.DrawPartitionCanvas()
        self.writelog("selecting Partition ...")
        return 0

    def DrawPartitionCanvas(self):
        if self.ui.Tab.currentIndex() != 1: return

        if not self.checkPartition: # dark style
            # ?????????echarts
            self.PartitionCanvas.page().runJavaScript(
                '''
                    var myChart = echarts.init(document.getElementById('container'), 'light', {renderer: 'canvas'});
                '''
            )
            self.checkPartition = True

        # if not self.checkPartition: # light style
        #     # ?????????echarts
        #     self.PartitionCanvas.page().runJavaScript(
        #         '''
        #             var myChart = echarts.init(document.getElementById('container'), 'light', {renderer: 'canvas'});
        #         '''
        #     )
        #     self.checkPartition = True

        print(self.ui.CheckPartition.isChecked())
        print(self.ui.CheckIterator.isChecked())
        if self.ui.CheckPartition.isChecked() and self.ui.CheckIterator.isChecked():
            options = self.BothSelect()
            self.writelog("Showing all iterations and partitions")
        elif self.ui.CheckPartition.isChecked():
            options = self.OnlyPartition()
            self.writelog("Showing all partitions by iteration")
        elif self.ui.CheckIterator.isChecked():
            options = self.OnlyIterator()
            self.writelog("Showing all iterations by partition")
        else:
            options = self.NoneSelect()
            self.writelog("Showing partition status")
        if not options: return
        self.PartitionCanvas.page().runJavaScript(
            f'''
                myChart.clear();
                var option = eval({options});
                myChart.setOption(option);
            '''
        )
        self.writelog("Loading computing details information page...")

    def SelectIterator(self,tmp,num):
        self.DrawPartitionCanvas()

os.system("Python ./executingMainCalculatorGPU.py")
time.sleep(1)
loaddata("data1.txt")
myapp = QApplication(sys.argv)
# myapp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
myDlg = Windows()

icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("icon.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
myDlg.setWindowIcon(icon)

myDlg.exec()