import win32process
import wmi
from win32gui import GetForegroundWindow


timeDict = {}
c = wmi.WMI()


def foreground_window():
    # find process ID of current foreground window
    currentWindow = GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(currentWindow)
    # query for name of process and add time to dictionary
    try:
        for process in c.query("SELECT Name FROM Win32_Process WHERE ProcessId = " + str(pid)):
            return process.Name
    except -2147217385:
        pass