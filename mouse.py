import win32api, win32con

def middleMouse(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,x,y,0,0)
    