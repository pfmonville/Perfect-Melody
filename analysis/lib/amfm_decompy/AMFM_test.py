#!/usr/bin/env python

"""
Script to test the AMFM_decompy package.

Version 1.0.4
13/Jan/2015 Bernardo J.B. Schmitt - bernardo.jb.schmitt@gmail.com
"""

import pYAAPT as pyaapt
import pyQHM as pyqhm
import basic_tools as basic
import os.path

# Declare the variables.
file_name = "sample.wav"
window_duration = 0.015   # in seconds
nharm_max = 25
SNR = float('Inf')

# Create the signal object.
signal = basic.SignalObj(file_name)

# Create the window object.
window = pyqhm.SampleWindow(window_duration, signal.fs)

# Create the pitch object and calculate its attributes.
pitch = pyaapt.yaapt(signal)

# Set the number of modulated components.
signal.set_nharm(pitch.values, nharm_max)

# Check if gaussian noise has to be added.
if SNR != float('Inf'):
    signal.noiser(pitch.values, SNR)

# Perform the QHM extraction.
QHM = pyqhm.qhm(signal, pitch, window, 0.001, N_iter = 3, phase_tech = 'phase')

print ("QHM SRER: %s" % (QHM.SRER))

# Perform the aQHM extraction.
aQHM = pyqhm.aqhm(signal, QHM, pitch, window, 0.001, N_iter = 3, N_runs = 2,
            phase_tech = 'phase')

print ("aQHM SRER: %s" % (aQHM.SRER))

# Perform the eaQHM extraction.
eaQHM = pyqhm.eaqhm(signal, aQHM, pitch, window, 0.001, N_iter=3, N_runs=2,
              phase_tech = 'phase')

print ("eaQHM SRER: %s" % (eaQHM.SRER))

