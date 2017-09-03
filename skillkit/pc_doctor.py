#
#  pc doctor
#	Provide the status of computer CPU and virtual memory
#

import psutil

def default():
    return cpu()

def memory():
    return psutil.virtual_memory()

def cpu():
    return psutil.cpu_percent()
