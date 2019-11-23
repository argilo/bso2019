#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Multi Tx
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from rds_tx import rds_tx  # grc-generated hier_block
import ham
import math
import morse_table
import pmt
import sip
from gnuradio import qtgui


class multi_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multi Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multi Tx")
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

        self.settings = Qt.QSettings("GNU Radio", "multi_tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.audio_rate = audio_rate = 48000
        self.wpm = wpm = 10
        self.samp_rate = samp_rate = audio_rate * 40
        self.q_offset = q_offset = -0.031
        self.phase = phase = 0
        self.magnitude = magnitude = 0
        self.i_offset = i_offset = 0.125
        self.gain = gain = 25

        self.dmr_lowpass = dmr_lowpass = firdes.low_pass(4.0, 192000, 12500, 10000, firdes.WIN_HAMMING, 6.76)

        self.center_freq = center_freq = 441000000

        ##################################################
        # Blocks
        ##################################################
        self.root_raised_cosine_filter_1 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, audio_rate, 5, 0.35, 200))
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, audio_rate, 5, 0.35, 200))
        self.rds_tx_0 = rds_tx()
        self.rational_resampler_xxx_3 = filter.rational_resampler_ccc(
                interpolation=192,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=samp_rate,
                decimation=audio_rate,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate / audio_rate / 2,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=samp_rate / audio_rate / 2,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate / audio_rate / 4,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.9, 0, 0, "")
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
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	8192, #size
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
        self._q_offset_range = Range(-0.8, 0.8, 0.001, -0.031, 200)
        self._q_offset_win = RangeWidget(self._q_offset_range, self.set_q_offset, "q_offset", "counter_slider", float)
        self.top_grid_layout.addWidget(self._q_offset_win)
        self._phase_range = Range(-0.1, 0.1, 0.001, 0, 200)
        self._phase_win = RangeWidget(self._phase_range, self.set_phase, "phase", "counter_slider", float)
        self.top_grid_layout.addWidget(self._phase_win)
        self._magnitude_range = Range(-0.1, 0.1, 0.001, 0, 200)
        self._magnitude_win = RangeWidget(self._magnitude_range, self.set_magnitude, "magnitude", "counter_slider", float)
        self.top_grid_layout.addWidget(self._magnitude_win)
        self.low_pass_filter_1 = filter.interp_fir_filter_ccf(1, firdes.low_pass(
        	0.5, audio_rate, 5000, 400, firdes.WIN_HAMMING, 6.76))
        self._i_offset_range = Range(-0.8, 0.8, 0.001, 0.125, 200)
        self._i_offset_win = RangeWidget(self._i_offset_range, self.set_i_offset, "i_offset", "counter_slider", float)
        self.top_grid_layout.addWidget(self._i_offset_win)
        self.ham_varicode_tx_0 = ham.varicode_tx()
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (dmr_lowpass), 22000, 192000)
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=2,
          mod_code="none",
          differential=True,
          samples_per_symbol=8,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_map_bb_0 = digital.map_bb(([1,0]))
        self.blocks_wavfile_source_1_0 = blocks.wavfile_source('/home/argilo/Documents/bso2019/sigid/flag2-3.wav', True)
        self.blocks_wavfile_source_1 = blocks.wavfile_source('/home/argilo/Documents/bso2019/sigid/flag1.wav', True)
        self.blocks_wavfile_source_0_1_0 = blocks.wavfile_source('/home/argilo/Documents/bso2019/sigid/flag6.wav', True)
        self.blocks_wavfile_source_0_1 = blocks.wavfile_source('/home/argilo/Documents/bso2019/sigid/flag7.wav', True)
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source('/home/argilo/Documents/bso2019/sigid/aprs.wav', True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/argilo/Documents/bso2019/sigid/flag5.wav', True)
        self.blocks_vector_source_x_2 = blocks.vector_source_c((1,0,0,0,0), True, 1, [])
        self.blocks_vector_source_x_1 = blocks.vector_source_b([ord(c) for c in "This is VE3IRR. Signal identification challenge #11: flag{no_31_b4uD_i5_en0ugH}\n"], True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_c(morse_table.morse_seq("This is VE3IRR   -   For signal identification challenge 8 the flag is itelilelcsemzpcc   -   "), True, 1, [])
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
        self.blocks_rotator_cc_2_0_0_0_0 = blocks.rotator_cc(-20e3 * 2 * math.pi / audio_rate)
        self.blocks_rotator_cc_2_0_0_0 = blocks.rotator_cc(12e3 * 2 * math.pi / audio_rate)
        self.blocks_rotator_cc_2_0_0 = blocks.rotator_cc(-14e3 * 2 * math.pi / audio_rate)
        self.blocks_rotator_cc_2_0 = blocks.rotator_cc(20e3 * 2 * math.pi / audio_rate)
        self.blocks_rotator_cc_2 = blocks.rotator_cc(0e3 * 2 * math.pi / audio_rate)
        self.blocks_rotator_cc_1_1_0 = blocks.rotator_cc(-150e3 * 2 * math.pi / samp_rate)
        self.blocks_rotator_cc_1_1 = blocks.rotator_cc(-250e3 * 2 * math.pi / samp_rate)
        self.blocks_rotator_cc_1_0 = blocks.rotator_cc(500e3 * 2 * math.pi / samp_rate)
        self.blocks_rotator_cc_1 = blocks.rotator_cc(-400e3 * 2 * math.pi / samp_rate)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(150e3 * 2 * math.pi / samp_rate)
        self.blocks_repeat_1 = blocks.repeat(gr.sizeof_gr_complex*1, 36086*2)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, int(1.2 * audio_rate / wpm))
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.13, ))
        self.blocks_float_to_complex_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/argilo/Documents/bso2019/sigid/dmr.c32', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/argilo/Documents/bso2019/sigid/sigid.c32', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vcc((0.5, ))
        self.band_pass_filter_0_0 = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	1, audio_rate, -2800, -200, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	1, audio_rate, 200, 2800, 200, firdes.WIN_HAMMING, 6.76))
        self.analog_nbfm_tx_0_0 = analog.nbfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate * 2,
        	tau=75e-6,
        	max_dev=5e3,
        	fh=-1.0,
                )
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate * 2,
        	tau=75e-6,
        	max_dev=5e3,
        	fh=-1.0,
                )
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_float_to_complex_0_0_0, 1))
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.analog_nbfm_tx_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_rotator_cc_2_0_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_rotator_cc_2_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_rotator_cc_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.blocks_file_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.root_raised_cosine_filter_1, 0))
        self.connect((self.blocks_repeat_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_rotator_cc_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_rotator_cc_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_rotator_cc_1_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_rotator_cc_1_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_rotator_cc_1_1_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_rotator_cc_2, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_rotator_cc_2_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_rotator_cc_2_0_0, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_rotator_cc_2_0_0_0, 0), (self.blocks_add_xx_1, 3))
        self.connect((self.blocks_rotator_cc_2_0_0_0_0, 0), (self.blocks_add_xx_1, 4))
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.digital_psk_mod_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_vector_source_x_1, 0), (self.ham_varicode_tx_0, 0))
        self.connect((self.blocks_vector_source_x_2, 0), (self.blocks_repeat_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.analog_nbfm_tx_0_0, 0))
        self.connect((self.blocks_wavfile_source_0_1, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_wavfile_source_0_1_0, 0), (self.blocks_float_to_complex_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_1, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.blocks_wavfile_source_1_0, 0), (self.rds_tx_0, 0))
        self.connect((self.blocks_wavfile_source_1_0, 1), (self.rds_tx_0, 1))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))
        self.connect((self.digital_psk_mod_0, 0), (self.rational_resampler_xxx_3, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.ham_varicode_tx_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_rotator_cc_1_1_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_rotator_cc_1, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_rotator_cc_1_1, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.blocks_rotator_cc_1_0, 0))
        self.connect((self.rational_resampler_xxx_3, 0), (self.blocks_rotator_cc_2_0_0_0_0, 0))
        self.connect((self.rds_tx_0, 0), (self.blocks_rotator_cc_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_rotator_cc_2_0_0_0, 0))
        self.connect((self.root_raised_cosine_filter_1, 0), (self.root_raised_cosine_filter_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "multi_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_samp_rate(self.audio_rate * 40)
        self.root_raised_cosine_filter_1.set_taps(firdes.root_raised_cosine(1, self.audio_rate, 5, 0.35, 200))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.audio_rate, 5, 0.35, 200))
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.audio_rate)
        self.low_pass_filter_1.set_taps(firdes.low_pass(0.5, self.audio_rate, 5000, 400, firdes.WIN_HAMMING, 6.76))
        self.blocks_rotator_cc_2_0_0_0_0.set_phase_inc(-20e3 * 2 * math.pi / self.audio_rate)
        self.blocks_rotator_cc_2_0_0_0.set_phase_inc(12e3 * 2 * math.pi / self.audio_rate)
        self.blocks_rotator_cc_2_0_0.set_phase_inc(-14e3 * 2 * math.pi / self.audio_rate)
        self.blocks_rotator_cc_2_0.set_phase_inc(20e3 * 2 * math.pi / self.audio_rate)
        self.blocks_rotator_cc_2.set_phase_inc(0e3 * 2 * math.pi / self.audio_rate)
        self.blocks_repeat_0.set_interpolation(int(1.2 * self.audio_rate / self.wpm))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.audio_rate, -2800, -200, 200, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.audio_rate, 200, 2800, 200, firdes.WIN_HAMMING, 6.76))

    def get_wpm(self):
        return self.wpm

    def set_wpm(self, wpm):
        self.wpm = wpm
        self.blocks_repeat_0.set_interpolation(int(1.2 * self.audio_rate / self.wpm))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_rotator_cc_1_1_0.set_phase_inc(-150e3 * 2 * math.pi / self.samp_rate)
        self.blocks_rotator_cc_1_1.set_phase_inc(-250e3 * 2 * math.pi / self.samp_rate)
        self.blocks_rotator_cc_1_0.set_phase_inc(500e3 * 2 * math.pi / self.samp_rate)
        self.blocks_rotator_cc_1.set_phase_inc(-400e3 * 2 * math.pi / self.samp_rate)
        self.blocks_rotator_cc_0.set_phase_inc(150e3 * 2 * math.pi / self.samp_rate)

    def get_q_offset(self):
        return self.q_offset

    def set_q_offset(self, q_offset):
        self.q_offset = q_offset

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase

    def get_magnitude(self):
        return self.magnitude

    def set_magnitude(self, magnitude):
        self.magnitude = magnitude

    def get_i_offset(self):
        return self.i_offset

    def set_i_offset(self, i_offset):
        self.i_offset = i_offset

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_dmr_lowpass(self):
        return self.dmr_lowpass

    def set_dmr_lowpass(self, dmr_lowpass):
        self.dmr_lowpass = dmr_lowpass
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.dmr_lowpass))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq


def main(top_block_cls=multi_tx, options=None):

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
