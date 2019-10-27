#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Chu
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
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import ham
import math
import sip
import sys
from gnuradio import qtgui


class chu(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Chu")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Chu")
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

        self.settings = Qt.QSettings("GNU Radio", "chu")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.space_tone = space_tone = 2025
        self.samp_rate = samp_rate = 48000
        self.mark_tone = mark_tone = 2225
        self.channel_rate = channel_rate = 4800

        ##################################################
        # Blocks
        ##################################################
        self.root_raised_cosine_filter_0 = filter.fir_filter_fff(1, firdes.root_raised_cosine(
        	1, channel_rate, 300, 0.35, 100))
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	2600, #size
        	channel_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.1, 0, 1, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
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

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)

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
        self.low_pass_filter_1 = filter.fir_filter_ccf(10, firdes.low_pass(
        	1, samp_rate, 200, 50, firdes.WIN_HAMMING, 6.76))
        self.hilbert_fc_0 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.ham_chu_decode_0 = ham.chu_decode()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/argilo/Documents/bso2019/chu/alien-clock.wav', True)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.audio_sink_0_0 = audio.sink(48000, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -(space_tone + mark_tone) / 2, 1, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(channel_rate / (3.1416*(mark_tone - space_tone)))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_multiply_xx_2, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.audio_sink_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.ham_chu_decode_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.low_pass_filter_1, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_time_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "chu")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_space_tone(self):
        return self.space_tone

    def set_space_tone(self, space_tone):
        self.space_tone = space_tone
        self.analog_sig_source_x_1.set_frequency(-(self.space_tone + self.mark_tone) / 2)
        self.analog_quadrature_demod_cf_0.set_gain(self.channel_rate / (3.1416*(self.mark_tone - self.space_tone)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, 200, 50, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_mark_tone(self):
        return self.mark_tone

    def set_mark_tone(self, mark_tone):
        self.mark_tone = mark_tone
        self.analog_sig_source_x_1.set_frequency(-(self.space_tone + self.mark_tone) / 2)
        self.analog_quadrature_demod_cf_0.set_gain(self.channel_rate / (3.1416*(self.mark_tone - self.space_tone)))

    def get_channel_rate(self):
        return self.channel_rate

    def set_channel_rate(self, channel_rate):
        self.channel_rate = channel_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.channel_rate, 300, 0.35, 100))
        self.qtgui_time_sink_x_0.set_samp_rate(self.channel_rate)
        self.analog_quadrature_demod_cf_0.set_gain(self.channel_rate / (3.1416*(self.mark_tone - self.space_tone)))


def main(top_block_cls=chu, options=None):

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
