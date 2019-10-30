import os

def load_style(obj):
    # return obj.setStyleSheet(open("%s/Style.css" % os.path.dirname(__file__)).read().replace("%PATH%", os.path.dirname(
    #     __file__).replace("\\", "/")))
    # return obj.setStyleSheet(open("%s\\Style.css" % os.path.dirname(os.path.abspath(__file__))).read().replace("%PATH%",
    #         os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")))
    # return obj.setStyleSheet(open("%s/Style.css" % os.path.dirname(__file__)).read().replace("%PATH%", os.path.dirname(
    #     __file__).replace("\\", "/")))
    return obj.setStyleSheet(open('./Style.css').read())
def button_style(button, style):
    """
    style:['MediumGray','DarkGray','BlueJeans','Aqua','Mint','Grass','Sunflower','Bittersweet','Grapefruit','Lavender','PinkRose']
    """
    return button.setProperty("class", style)