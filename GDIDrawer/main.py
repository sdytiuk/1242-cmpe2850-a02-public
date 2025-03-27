import random
import clr #install pythonnet
#add gdidrawer.dll to same directory
#https://github.com/ISTNAIT/GDIDrawer/tree/master
#for guardiafantasma use only
clr.AddReference('GDIDrawer')

from GDIDrawer import CDrawer
from GDIDrawer import RandColor
from System.Drawing import Color

def GDITester():
    canvas = CDrawer()
    canvas.ContinuousUpdate = False
    for x in range(10):
        col = RandColor.GetColor()
        radius = random.randint(20,200)
        canvas.AddCenteredEllipse(
            random.randint(radius,canvas.ScaledWidth-radius),
            random.randint(radius,canvas.ScaledHeight-radius),
            radius*2, radius*2, col
        )
        canvas.Render()
        canvas.KeyboardEvent += canvasKeyboardCallback

def canvasKeyboardCallback(IsDown, keyCode, can):
    print(f"IsDown:{IsDown}, keycode:{keyCode}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GDITester()
    dummy = input("Press something to continue.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
