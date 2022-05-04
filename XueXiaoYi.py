# -*- encoding=utf8 -*-
__author__ = "KirigiriSuzumiya"

from airtest.core.api import *
from airtest.core.android.adb import *
from PIL import Image, ImageGrab
import pyperclip

#auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/emulator-5554",], project_root="C:/Users/boyif/Desktop/airtest脚本")
auto_setup(__file__, logdir=True, devices=["android://"])
print("auto_setup完成")
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# script content

def text_context():
    print("剪贴板内容：")
    print(pyperclip.paste())
    clear_pasta=poco(text="清除并粘贴")
    if not clear_pasta.exists():
        poco(name="com.xuexiaoyi.xxy:id/os").click()
    clear_pasta.wait_for_appearance(10000)
    clear_pasta.click()
    submit_button=poco(text="搜索")
    submit_button.wait_for_appearance(10000)
    submit_button.click()


def img_context():
    adb=ADB("emulator-5554")
    im = ImageGrab.grabclipboard()
    print("Image: size : %s, mode: %s" % (im.size, im.mode))
    im.save("1.png")
    adb.push("1.png","/sdcard/Download/1.png")
    again = poco(text="再拍一题")
    if again.exists():
        again.click()
    pic_album=poco(name="com.xuexiaoyi.xxy:id/n3")
    pic_album.wait_for_appearance(10000)
    pic_album.click()
    pic_1png = poco(text="1.png")
    pic_1png.wait_for_appearance(10000)
    pic_1png.click()
    
    submit_btn=poco(name="com.xuexiaoyi.xxy:id/a1q")
    submit_btn.wait_for_appearance(10000)
    submit_btn.click()
    

while True:
    pyperclip.copy("剪切板初始化>_<!")
    print("等待剪贴板：")
    pyperclip.waitForNewPaste()
    if pyperclip.paste():
        text_context()
    else:
        img_context()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)