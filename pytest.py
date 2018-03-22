from ctypes import *
'''
通过监控剪切板, 并清空剪切板, 来达到不允许复制目录,文件的目的. 
比较弱, 但是也是个办法
'''
import time
import win32con
import win32clipboard as clipboard

user32 = windll.user32
kernel32 = windll.kernel32


def get_clipboard():
    clipboard.OpenClipboard()
    savedFile = None
    # formats = []
    # lastFormat = 0
    # while 1:
    #     nextFormat = clipboard.EnumClipboardFormats(lastFormat)
    #     print(nextFormat)
    #     if 0 == nextFormat:
    #         break
    #     else:
    #         formats.append(nextFormat)
    #         lastFormat = nextFormat
    if clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP):
        savedFile = clipboard.GetClipboardData(win32con.CF_HDROP)

    clipboard.CloseClipboard()
    return savedFile


def empty_clipboard():
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.CloseClipboard()


def set_clipboard():
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(win32con.CF_HDROP, "d://data//a//a.txt")
    clipboard.CloseClipboard()


if __name__ == '__main__':
    print('clear clipboard...')
    # set_clipboard()

    # empty_clipboard()
    while True:
        text_raw = get_clipboard()
        print('{0} {1}'.format(text_raw, type(text_raw)))
        time.sleep(1)