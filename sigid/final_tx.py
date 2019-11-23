#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Final Tx
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import iqbalance
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import pmt
import sip
import sys
import time
from gnuradio import qtgui


class final_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Final Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Final Tx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "final_tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1920000
        self.q_offset = q_offset = -0.031
        self.phase = phase = 0.02
        self.magnitude = magnitude = 0.04
        self.i_offset = i_offset = 0.125
        self.center_freq = center_freq = 441000000 + 5650000*0

        ##################################################
        # Blocks
        ##################################################
        self._q_offset_range = Range(-0.8, 0.8, 0.001, -0.031, 200)
        self._q_offset_win = RangeWidget(self._q_offset_range, self.set_q_offset, "q_offset", "counter_slider", float)
        self.top_grid_layout.addWidget(self._q_offset_win)
        self._phase_range = Range(-0.1, 0.1, 0.001, 0.02, 200)
        self._phase_win = RangeWidget(self._phase_range, self.set_phase, "phase", "counter_slider", float)
        self.top_grid_layout.addWidget(self._phase_win)
        self._magnitude_range = Range(-0.1, 0.1, 0.001, 0.04, 200)
        self._magnitude_win = RangeWidget(self._magnitude_range, self.set_magnitude, "magnitude", "counter_slider", float)
        self.top_grid_layout.addWidget(self._magnitude_win)
        self._i_offset_range = Range(-0.8, 0.8, 0.001, 0.125, 200)
        self._i_offset_win = RangeWidget(self._i_offset_range, self.set_i_offset, "i_offset", "counter_slider", float)
        self.top_grid_layout.addWidget(self._i_offset_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(25, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(-4, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.iqbalance_fix_cc_0 = iqbalance.fix_cc(magnitude, phase)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/argilo/Documents/bso2019/sigid/sigid.c32', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_add_const_vxx_1 = blocks.add_const_vcc((i_offset + 1j * q_offset, ))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_1, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.iqbalance_fix_cc_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.iqbalance_fix_cc_0, 0), (self.blocks_add_const_vxx_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "final_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_q_offset(self):
        return self.q_offset

    def set_q_offset(self, q_offset):
        self.q_offset = q_offset
        self.blocks_add_const_vxx_1.set_k((self.i_offset + 1j * self.q_offset, ))

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase
        self.iqbalance_fix_cc_0.set_phase(self.phase)

    def get_magnitude(self):
        return self.magnitude

    def set_magnitude(self, magnitude):
        self.magnitude = magnitude
        self.iqbalance_fix_cc_0.set_mag(self.magnitude)

    def get_i_offset(self):
        return self.i_offset

    def set_i_offset(self, i_offset):
        self.i_offset = i_offset
        self.blocks_add_const_vxx_1.set_k((self.i_offset + 1j * self.q_offset, ))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.osmosdr_sink_0.set_center_freq(self.center_freq, 0)


def main(top_block_cls=final_tx, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
