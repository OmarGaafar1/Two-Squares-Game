

import pygame
import math



pygame.init()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
OneIsClicked = ""
TwoIsClicked = ""
ThreeIsClicked = ""
FourIsClicked = ""
FiveIsClicked = ""
SixIsClicked = " "
SevenIsClicked = " "
EightIsClicked = " "
NineIsclicked = " "
TenIsClicked = " "
ElevenIsCLicked = ""
TwelveIsClicked = " "
ThirteenIsCLicked = " "
FourteenIsClicked = " "
FifteenIsClicked = " "
SixteenIsClicked = " "

# Displaying Title and Icon
pygame.display.set_caption("Two Squares Game")
icon = pygame.image.load("menu (1).png")
pygame.display.set_icon(icon)

# Displaying the screen.
screen = pygame.display.set_mode((330, 330))

# Background
background = pygame.image.load("Background.png")


def One_two():
    global crossY2, crossX2, OneIsClicked, TwoIsClicked, twoX, twoY, oneY, oneX, oneInScreen, mouse_clicked, crossX, crossY, crossY3, crossX3
    oneInScreen = True
    if oneX not in range(0, 330):
        oneInScreen = False

    if mx in range(10, 81) and my in range(10, 81) and mouse_clicked and oneInScreen:
        OneIsClicked = True

    if mx in range(90, 161) and my in range(10, 80) and mouse_clicked:
        TwoIsClicked = True

    if OneIsClicked == True and TwoIsClicked == True:
        crossX2 = twoX
        crossY2 = twoY
        crossX = oneX
        crossY = oneY
        oneX, twoX = 900, 900
        oneY, twoY = 900, 900
        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(1)
        nums.remove(2)


def Two_three():
    global crossY2, crossX2, OneIsClicked, TwoIsClicked, twoX, twoY, oneY, oneX, oneInScreen, mouse_clicked, crossX, crossY, ThreeIsClicked
    global crossX3, crossY3, threeX, threeY

    ThreeInScreen = True

    # Checking if three is gone and replaced by X or not
    if threeX != 190:
        ThreeInScreen = False

    if mx in range(170, 241) and my in range(10, 81) and mouse_clicked and ThreeInScreen:
        ThreeIsClicked = True

    if ThreeIsClicked == True and TwoIsClicked == True:
        crossX2 = twoX
        crossY2 = twoY
        crossX3 = threeX
        crossY3 = threeY
        threeX, twoX = 900, 900
        threeY, twoY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(2)
        nums.remove(3)


def Three_four():
    global mouse_clicked, ThreeIsClicked, FourIsClicked
    global crossX3, crossY3, threeX, threeY, fourX, fourY, crossY4, crossX4

    FourInScreen = True

    # Checking if three is gone and replaced by X or not
    if fourX != 270:
        FourInScreen = False

    if mx in range(250, 321) and my in range(10, 81) and mouse_clicked and FourInScreen:
        FourIsClicked = True

    if FourIsClicked == True and ThreeIsClicked == True:
        crossX4 = fourX
        crossY4 = fourY
        crossX3 = threeX
        crossY3 = threeY
        threeX, fourX = 900, 900
        threeY, fourY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(3)
        nums.remove(4)


def One_Five():
    global oneX, oneY, fiveX, fiveY, mouse_clicked, OneIsClicked, FiveIsClicked, crossX5, crossY5, crossX, crossY, crossX2, crossY2
    FiveInScreen = True
    if fiveX != 27:
        FiveInScreen = False

    if mx in range(10, 81) and my in range(90, 160) and mouse_clicked and FiveInScreen:
        FiveIsClicked = True

    if mx in range(10, 81) and my in range(10, 81) and mouse_clicked and oneInScreen:
        OneIsClicked = True

    if FiveIsClicked == True and OneIsClicked == True:
        crossX5 = 27
        crossY5 = 110
        crossX = oneX
        crossY = oneY
        oneX, fiveX = 900, 900
        oneY, fiveY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(1)
        nums.remove(5)


def Five_six():
    global fiveX, fiveY, sixX, sixY, mouse_clicked, OneIsClicked, FiveIsClicked, crossX5, crossY5, crossX6, crossY6
    global SixIsClicked
    FiveInScreen = True
    if fiveX != 27:
        FiveInScreen = False

    if mx in range(10, 81) and my in range(90, 161) and mouse_clicked and FiveInScreen:
        FiveIsClicked = True


    if mx in range(90, 161) and my in range(90, 161) and mouse_clicked:
        SixIsClicked = True


    if FiveIsClicked == True and SixIsClicked == True:
        crossX5 = fiveX
        crossY5 = fiveY
        crossX6 = sixX
        crossY6 = sixY
        sixX, fiveX = 900, 900
        sixY, fiveY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(5)
        nums.remove(6)


def Two_six():
    global twoX, twoY, sixX, sixY, mouse_clicked, TwoIsClicked, SixIsClicked, crossX6, crossY6, crossX2, crossY2
    SixInScreen = True
    if sixX != 27:
        SixInScreen = False

    if mx in range(90, 161) and my in range(10, 80) and mouse_clicked and SixInScreen:
        TwoIsClicked = True


    if mx in range(90, 161) and my in range(90, 161) and mouse_clicked:
        SixIsClicked = True


    if TwoIsClicked == True and SixIsClicked == True:
        crossX2 = twoX
        crossY2 = twoY
        crossX6 = sixX
        crossY6 = sixY
        sixX, twoX = 900, 900
        sixY, twoY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(6)
        nums.remove(2)


def Seven_Eight():
    global sevenX, sevenY, eightX, eightY, mouse_clicked, EightIsClicked, SevenIsClicked, crossX7, crossY7, crossX8, crossY8
    SevenInScreen = True
    if sevenX != 27:
        SixInScreen = False

    if mx in range(170, 240) and my in range(90, 161) and mouse_clicked and SevenInScreen:
        SevenIsClicked = True


    if mx in range(250, 321) and my in range(90, 161) and mouse_clicked:
        EightIsClicked = True


    if EightIsClicked == True and SevenIsClicked == True:
        crossX8 = eightX
        crossY8 = eightY
        crossX7 = sevenX
        crossY7 = sevenY
        sevenX, eightX = 900, 900
        sevenY, eightY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(8)
        nums.remove(7)


def Seven_Three():
    global sevenX, sevenY, threeX, threeY, mouse_clicked, SevenIsClicked, ThreeIsClicked, crossX7, crossY7, crossX3, crossY3
    ThreeInScreen = True
    if sevenX != 27:
        SixInScreen = False

    if mx in range(170, 240) and my in range(90, 161) and mouse_clicked and ThreeInScreen:
        SevenIsClicked = True


    if mx in range(170, 240) and my in range(10, 81) and mouse_clicked:
        ThreeIsClicked = True


    if ThreeIsClicked == True and SevenIsClicked == True:
        crossX3 = threeX
        crossY3 = threeY
        crossX7 = sevenX
        crossY7 = sevenY
        sevenX, threeX = 900, 900
        sevenY, threeY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(3)
        nums.remove(7)


def Four_Eight():
    global fourX, fourY, eightX, eightY, mouse_clicked, EightIsClicked, FourIsClicked, crossX4, crossY4, crossX8, crossY8
    eightInScreen = True
    if eightX != 27:
        eightInScreen = False

    if mx in range(250, 321) and my in range(10, 81) and mouse_clicked:
        FourIsClicked = True


    if mx in range(250, 321) and my in range(90, 161) and mouse_clicked and eightInScreen:
        EightIsClicked = True


    if EightIsClicked == True and FourIsClicked == True:
        crossX8 = eightX
        crossY8 = eightY
        crossX4 = fourX
        crossY4 = fourY
        fourX, eightX = 900, 900
        fourY, eightY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(8)
        nums.remove(4)


def Six_seven():
    global sevenX, sevenY, sixY, sixX, mouse_clicked, SixIsClicked, SevenIsClicked, crossX7, crossY7, crossX6, crossY6
    SevenInScreen = True
    if sevenX != 27:
        SixInScreen = False

    if mx in range(170, 240) and my in range(90, 161) and mouse_clicked and SevenInScreen:
        SevenIsClicked = True


    if mx in range(90, 160) and my in range(90, 161) and mouse_clicked:
        SixIsClicked = True


    if SixIsClicked == True and SevenIsClicked == True:
        crossX6 = sixX
        crossY6 = sixY
        crossX7 = sevenX
        crossY7 = sevenY
        sevenX, sixX = 900, 900
        sevenY, sixY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(7)
        nums.remove(6)


def Nine_Ten():
    global nineX, nineY, tenX, tenY, mouse_clicked, TenIsClicked, NineIsclicked, crossX9, crossY9, crossX10, crossY10
    TenInScreen = True
    if tenX != 95:
        TenInScreen = False

    if mx in range(90, 161) and my in range(170, 240) and mouse_clicked and TenInScreen:
        TenIsClicked = True


    if mx in range(10, 80) and my in range(170, 240) and mouse_clicked:
        NineIsclicked = True


    if NineIsclicked == True and TenIsClicked == True:
        crossX9 = nineX
        crossY9 = nineY
        crossX10 = tenX + 10
        crossY10 = nineY
        tenX, nineY = 900, 900
        tenY, nineY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(10)
        nums.remove(9)


def Ten_Eleven():
    global elevenX, elevenY, tenX, tenY, mouse_clicked, TenIsClicked, ElevenIsCLicked, crossX11, crossY11, crossX10, crossY10
    TenInScreen = True
    if tenX != 95:
        TenInScreen = False

    if mx in range(90, 161) and my in range(170, 240) and mouse_clicked and TenInScreen:
        TenIsClicked = True


    if mx in range(170, 240) and my in range(170, 240) and mouse_clicked:
        ElevenIsCLicked = True


    if ElevenIsCLicked == True and TenIsClicked == True:
        crossX11 = elevenX + 10
        crossY11 = 190
        crossX10 = tenX + 10
        crossY10 = 190
        tenX, elevenY = 900, 900
        tenY, elevenX = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(11)
        nums.remove(10)


def Eleven_Twelve():
    global elevenX, elevenY, twelveX, twelveY, mouse_clicked, TwelveIsClicked, ElevenIsCLicked, crossX11, crossY11, crossX12, crossY12
    ElevenInScreen = True
    if elevenX != 175:
        ElevenInScreen = False

    if mx in range(250, 321) and my in range(170, 240) and mouse_clicked and ElevenInScreen:
        TwelveIsClicked = True


    if mx in range(170, 240) and my in range(170, 240) and mouse_clicked:
        ElevenIsCLicked = True


    if ElevenIsCLicked == True and TwelveIsClicked == True:
        crossX11 = elevenX + 15
        crossY11 = 190
        crossX12 = twelveX + 20
        crossY12 = 190
        twelveX, elevenY = 900, 900
        twelveY, elevenX = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(12)
        nums.remove(11)


def Five_Nine():
    global fiveX, fiveY, nineX, nineY, mouse_clicked, NineIsclicked, FiveIsClicked, crossX5, crossY5, crossX9, crossY9
    FiveInScreen = True
    if fiveX != 27:
        FiveInScreen = False

    if mx in range(10, 81) and my in range(90, 161) and mouse_clicked and FiveInScreen:
        FiveIsClicked = True

    if mx in range(10, 81) and my in range(170, 240) and mouse_clicked:
        NineIsclicked = True

    if FiveIsClicked == True and NineIsclicked == True:
        crossX5 = fiveX
        crossY5 = fiveY
        crossX9 = nineX
        crossY9 = nineY
        nineX, fiveX = 900, 900
        nineY, fiveY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(9)
        nums.remove(5)


def Six_Ten():
    global tenX, tenY, sixY, sixX, mouse_clicked, SixIsClicked, TenIsClicked, crossX10, crossY10, crossX6, crossY6
    TenInScreen = True
    if tenX != 95:
        TenInScreen = False

    if mx in range(90, 160) and my in range(170, 240) and mouse_clicked and TenIsClicked:
        TenIsClicked = True


    if mx in range(90, 160) and my in range(90, 161) and mouse_clicked:
        SixIsClicked = True


    if SixIsClicked == True and TenIsClicked == True:
        crossX6 = sixX
        crossY6 = sixY
        crossX10 = tenX + 10
        crossY10 = 190
        tenX, sixX = 900, 900
        tenY, sixY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(10)
        nums.remove(6)


def Eleven_Seven():
    global elevenX, elevenY, sevenX, sevenY, mouse_clicked, SevenIsClicked, ElevenIsCLicked, crossX11, crossY11, crossX7, crossY7
    ElevenInScreen = True
    if elevenX != 175:
        ElevenInScreen = False

    if mx in range(170, 240) and my in range(90, 160) and mouse_clicked:
        SevenIsClicked = True


    if mx in range(170, 240) and my in range(170, 240) and mouse_clicked and ElevenInScreen:
        ElevenIsCLicked = True


    if ElevenIsCLicked == True and SevenIsClicked == True:
        crossX11 = elevenX + 15
        crossY11 = 190
        crossX7 = sevenX
        crossY7 = sevenY
        sevenX, elevenY = 900, 900
        sevenY, elevenX = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(11)
        nums.remove(7)


def Twelve_Eight():
    global eightX, eightY, twelveX, twelveY, mouse_clicked, TwelveIsClicked, EightIsClicked, crossX8, crossY8, crossX12, crossY12
    TwelveInScreen = True
    if twelveX != 250:
        TwelveInScreen = False

    if mx in range(250, 321) and my in range(170, 240) and mouse_clicked and TwelveIsClicked:
        TwelveIsClicked = True


    if mx in range(250, 320) and my in range(90, 160) and mouse_clicked:
        EightIsClicked = True


    if EightIsClicked == True and TwelveIsClicked == True:
        crossX8 = eightX
        crossY8 = eightY
        crossX12 = twelveX + 20
        crossY12 = 190
        twelveX, eightY = 900, 900
        twelveY, eightX = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(8)
        nums.remove(12)


def Thirteen_Fourteen():
    global thirteenX, thirteenY, fourteenX, fourteenY, mouse_clicked, ThirteenIsCLicked, FourteenIsClicked, crossX13, crossY13, crossX14, crossY14
    ThirteenInScreeen = True
    if thirteenX != 15:
        ThirteenInScreeen = False

    if mx in range(10, 80) and my in range(250, 321) and mouse_clicked and ThirteenInScreeen:
        ThirteenIsCLicked = True


    if mx in range(90, 160) and my in range(250, 321) and mouse_clicked:
        FourteenIsClicked = True


    if ThirteenIsCLicked == True and FourteenIsClicked == True:
        crossX13 = thirteenX + 10
        crossY13 = thirteenY + 15
        crossX14 = fourteenX + 10
        crossY14 = fourteenY + 15
        thirteenX, fourteenX = 900, 900
        thirteenY, fourteenY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(14)
        nums.remove(13)


def Fourteen_Fifteen():
    global fifteenX, fifteenY, fourteenX, fourteenY, mouse_clicked, FifteenIsClicked, FourteenIsClicked, crossX15, crossY15, crossX14, crossY14
    FifteenInScreeen = True
    if fifteenX != 175:
        FifteenInScreeen = False

    if mx in range(170, 240) and my in range(250, 321) and mouse_clicked and FifteenInScreeen:
        FifteenIsClicked = True

    if mx in range(90, 160) and my in range(250, 321) and mouse_clicked:
        FourteenIsClicked = True

    if FifteenIsClicked == True and FourteenIsClicked == True:
        crossX15 = fifteenX + 10
        crossY15 = fifteenY + 15
        crossX14 = fourteenX + 10
        crossY14 = fourteenY + 15
        fifteenX, fourteenX = 900, 900
        fifteenY, fourteenY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(15)
        nums.remove(14)


def Fifteen_Sixteen():
    global fifteenX, fifteenY, sixteenX, sixteenY, mouse_clicked, FifteenIsClicked, SixteenIsClicked, crossX15, crossY15, crossX16, crossY16
    FifteenInScreeen = True
    if fifteenX != 175:
        FifteenInScreeen = False

    if mx in range(170, 240) and my in range(250, 321) and mouse_clicked and FifteenInScreeen:
        FifteenIsClicked = True

    if mx in range(250, 320) and my in range(250, 321) and mouse_clicked:
        SixteenIsClicked = True

    if FifteenIsClicked == True and SixteenIsClicked == True:
        crossX15 = fifteenX + 10
        crossY15 = fifteenY + 15
        crossX16 = sixteenX + 10
        crossY16 = sixteenY + 15
        fifteenX, sixteenY = 900, 900
        fifteenY, sixteenX = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(16)
        nums.remove(15)


def Thirteen_Nine():
    global thirteenX, thirteenY, nineX, nineY, mouse_clicked, ThirteenIsCLicked, NineIsclicked, crossX13, crossY13, crossX9, crossY9
    ThirteenInScreeen = True
    if thirteenX != 15:
        ThirteenInScreeen = False

    if mx in range(10, 80) and my in range(250, 321) and mouse_clicked and ThirteenInScreeen:
        ThirteenIsCLicked = True


    if mx in range(10, 80) and my in range(170, 240) and mouse_clicked:
        NineIsclicked = True


    if ThirteenIsCLicked == True and NineIsclicked == True:
        crossX13 = thirteenX + 10
        crossY13 = thirteenY + 15
        crossX9 = nineX
        crossY9 = nineY
        thirteenX, nineX = 900, 900
        thirteenY, nineX = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(13)
        nums.remove(9)


def Fourteen_Ten():
    global tenX, tenY, fourteenX, fourteenY, mouse_clicked, FourteenIsClicked, TenIsClicked, crossX10, crossY10, crossX14, crossY14
    FourteenInScreeen = True
    if fourteenX != 95:
        FourteenInScreeen = False

    if mx in range(90, 160) and my in range(170, 240) and mouse_clicked:
        TenIsClicked = True

    if mx in range(90, 160) and my in range(250, 321) and mouse_clicked and FourteenInScreeen:
        FourteenIsClicked = True

    if TenIsClicked == True and FourteenIsClicked == True:
        crossX10 = tenX + 10
        crossY10 = tenY + 15
        crossX14 = fourteenX + 10
        crossY14 = fourteenY + 15
        tenX, fourteenX = 900, 900
        tenY, fourteenY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(10)
        nums.remove(14)


def Fifteen_Eleven():
    global fifteenX, fifteenY, elevenX, elevenY, mouse_clicked, FifteenIsClicked, ElevenIsCLicked, crossX15, crossY15, crossX11, crossY11
    FifteenInScreeen = True
    if fifteenX != 175:
        FifteenInScreeen = False

    if mx in range(170, 240) and my in range(250, 321) and mouse_clicked and FifteenInScreeen:
        FifteenIsClicked = True

    if mx in range(170, 240) and my in range(170, 240) and mouse_clicked:
        ElevenIsCLicked = True

    if FifteenIsClicked == True and ElevenIsCLicked == True:
        crossX15 = fifteenX + 10
        crossY15 = fifteenY + 15
        crossX11 = elevenX + 10
        crossY11 = elevenY + 15
        fifteenX, elevenX = 900, 900
        fifteenY, elevenY = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(15)
        nums.remove(11)


def Sixteen_Twelve():
    global twelveX, twelveY, sixteenX, sixteenY, mouse_clicked, TwelveIsClicked, SixteenIsClicked, crossX12, crossY12, crossX16, crossY16
    SixteenInScreeen = True
    if sixteenX != 255:
        SixteenInScreeen = False

    if mx in range(250, 320) and my in range(170, 240) and mouse_clicked:
        TwelveIsClicked = True

    if mx in range(250, 320) and my in range(250, 321) and mouse_clicked and SixteenInScreeen:
        SixteenIsClicked = True

    if TwelveIsClicked == True and SixteenIsClicked == True:
        crossX12 = twelveX + 20
        crossY12 = twelveY + 15
        crossX16 = sixteenX + 15
        crossY16 = sixteenY + 15
        twelveY, sixteenY = 900, 900
        twelveX, sixteenX = 900, 900

        mouse_clicked = False
        Reset_all_clicked_To_False()
        nums.remove(16)
        nums.remove(12)


def Reset_all_clicked_To_False():
    global OneIsClicked, TwoIsClicked, ThreeIsClicked, FourIsClicked, FiveIsClicked, SixIsClicked, SevenIsClicked, EightIsClicked
    global NineIsclicked, TenIsClicked, ElevenIsCLicked, TwelveIsClicked, ThirteenIsCLicked, FourteenIsClicked, FifteenIsClicked, SixteenIsClicked
    OneIsClicked = False
    TwoIsClicked = False
    ThreeIsClicked = False
    FourIsClicked = False
    FiveIsClicked = False
    SixIsClicked = False
    SevenIsClicked = False
    EightIsClicked = False
    NineIsclicked = False
    TenIsClicked = False
    ElevenIsCLicked = False
    TwelveIsClicked = False
    ThirteenIsCLicked = False
    FourteenIsClicked = False
    FifteenIsClicked = False
    SixteenIsClicked = False


# Winner !!
def Basic_winCase():
    if len(nums) == 0:
        background_new = pygame.image.load("Untitled-1.jpg")
        screen.blit(background_new, (0, 0))


def Wincase_Two():
    if len(nums) == 2:
        sum = nums[1] - nums[0]
        if sum >= 2 and sum != 4:
            background_new = pygame.image.load("Untitled-1.jpg")
            screen.blit(background_new, (0, 0))


def Wincase_Three():
    if len(nums) == 4 :
        sum1 = nums[3] - nums[2]
        sum2 = nums[1] - nums[0]
        if sum1 !=4  and sum2 !=4:
            if sum1 != 1 and sum2 != 1 :
                background_new = pygame.image.load("Untitled-1.jpg")
                screen.blit(background_new, (0, 0))


# The Crosses >> We need 16 cross

# Cross One
crossImg = pygame.image.load("close.png")
crossX = 900
crossY = 900


def cross():
    screen.blit(crossImg, (crossX, crossY))


# Cross Two

crossImg2 = pygame.image.load("close.png")
crossX2 = 900
crossY2 = 900


def cross2():
    screen.blit(crossImg2, (crossX2, crossY2))


# Cross Three

crossImg3 = pygame.image.load("close.png")
crossX3 = 900
crossY3 = 900


def cross3():
    screen.blit(crossImg3, (crossX3, crossY3))


# Cross 4
crossImg4 = pygame.image.load("close.png")
crossX4 = 900
crossY4 = 900


def cross4():
    screen.blit(crossImg4, (crossX4, crossY4))


# Cross 5
crossImg5 = pygame.image.load("close.png")
crossX5 = 900
crossY5 = 900


def cross5():
    screen.blit(crossImg5, (crossX5, crossY5))


# Cross 6
crossImg6 = pygame.image.load("close.png")
crossX6 = 900
crossY6 = 900


def cross6():
    screen.blit(crossImg6, (crossX6, crossY6))


# Cross 7
crossImg7 = pygame.image.load("close.png")
crossX7 = 900
crossY7 = 900


def cross7():
    screen.blit(crossImg7, (crossX7, crossY7))


# Cross 8
crossImg8 = pygame.image.load("close.png")
crossX8 = 900
crossY8 = 900


def cross8():
    screen.blit(crossImg8, (crossX8, crossY8))


# Cross 9
crossImg9 = pygame.image.load("close.png")
crossX9 = 900
crossY9 = 900


def cross9():
    screen.blit(crossImg9, (crossX9, crossY9))


# Cross 10
crossImg10 = pygame.image.load("close.png")
crossX10 = 900
crossY10 = 900


def cross10():
    screen.blit(crossImg10, (crossX10, crossY10))


# Cross 11
crossImg11 = pygame.image.load("close.png")
crossX11 = 900
crossY11 = 900


def cross11():
    screen.blit(crossImg11, (crossX11, crossY11))


# Cross 12
crossImg12 = pygame.image.load("close.png")
crossX12 = 900
crossY12 = 900


def cross12():
    screen.blit(crossImg12, (crossX12, crossY12))


# Cross 13
crossImg13 = pygame.image.load("close.png")
crossX13 = 900
crossY13 = 900


def cross13():
    screen.blit(crossImg13, (crossX13, crossY13))


# Cross 14
crossImg14 = pygame.image.load("close.png")
crossX14 = 900
crossY14 = 900


def cross14():
    screen.blit(crossImg14, (crossX14, crossY14))


# Cross 15
crossImg15 = pygame.image.load("close.png")
crossX15 = 900
crossY15 = 900


def cross15():
    screen.blit(crossImg15, (crossX15, crossY15))


# Cross 16
crossImg16 = pygame.image.load("close.png")
crossX16 = 900
crossY16 = 900


def cross16():
    screen.blit(crossImg16, (crossX16, crossY16))


# Digit One !
oneImg = pygame.image.load("one (1).png")
oneX = 27
oneY = 27


def digit_one():
    screen.blit(oneImg, (oneX, oneY))


# Digit Two

twoImg = pygame.image.load("two.png")
twoX = 107
twoY = 27


def digit_two():
    screen.blit(twoImg, (twoX, twoY))


# Digit Three
threeImg = pygame.image.load("three.png")
threeX = 190
threeY = 27


def Digit_Three():
    screen.blit(threeImg, (threeX, threeY))


# Digit Four !
fourImg = pygame.image.load("four.png")
fourX = 270
fourY = 27


def Digit_Four():
    screen.blit(fourImg, (fourX, fourY))


# Digit Five !
fiveImg = pygame.image.load("five.png")
fiveX = 27
fiveY = 110


def Digit_Five():
    screen.blit(fiveImg, (fiveX, fiveY))


# Digit Six !
sixImg = pygame.image.load("six.png")
sixX = 107
sixY = 110


def Digit_six():
    screen.blit(sixImg, (sixX, sixY))


# Digit seven !
sevenImg = pygame.image.load("seven.png")
sevenX = 187
sevenY = 110


def Digit_Seven():
    screen.blit(sevenImg, (sevenX, sevenY))


# Digit Eight !
eightImg = pygame.image.load("eight.png")
eightX = 267
eightY = 110


def Digit_Eight():
    screen.blit(eightImg, (eightX, eightY))


# Digit Nine !
nineImg = pygame.image.load("nine.png")
nineX = 27
nineY = 190


def Digit_Nine():
    screen.blit(nineImg, (nineX, nineY))


# Digit Ten !
tenImg = pygame.image.load("ten (1).png")
tenX = 95
tenY = 173


def Digit_Ten():
    screen.blit(tenImg, (tenX, tenY))


# Digit 11 !
elevenImg = pygame.image.load("eleven (1).png")
elevenX = 175
elevenY = 173


def Digit_Eleven():
    screen.blit(elevenImg, (elevenX, elevenY))


# Digit 12 !
twelveImg = pygame.image.load("twelve (1).png")
twelveX = 250
twelveY = 173


def Digit_Twelve():
    screen.blit(twelveImg, (twelveX, twelveY))


# Digit 13 !
thirteenImg = pygame.image.load("thirteen (1).png")
thirteenX = 15
thirteenY = 255


def Digit_Thirteen():
    screen.blit(thirteenImg, (thirteenX, thirteenY))


# Digit 14 !
fourteenImg = pygame.image.load("fourteen (1).png")
fourteenX = 95
fourteenY = 255


def Digit_Fourteen():
    screen.blit(fourteenImg, (fourteenX, fourteenY))


# Digit 15 !
fifteenImg = pygame.image.load("fifteen (1).png")
fifteenX = 175
fifteenY = 255


def Digit_Fifteen():
    screen.blit(fifteenImg, (fifteenX, fifteenY))


# Digit 16 !
sixteenImg = pygame.image.load("sixteen (1).png")
sixteenX = 255
sixteenY = 255


def Digit_Sixteen():
    screen.blit(sixteenImg, (sixteenX, sixteenY))


while True:
    mouse_clicked = False
    screen.blit(background, (0, 0))

    mx, my = pygame.mouse.get_pos()
    # print(mx, my)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True

    digit_one()
    digit_two()
    Digit_Three()
    Digit_Four()
    Digit_Five()
    Digit_six()
    Digit_Seven()
    Digit_Eight()
    Digit_Nine()
    Digit_Ten()
    Digit_Eleven()
    Digit_Twelve()
    Digit_Thirteen()
    Digit_Fourteen()
    Digit_Fifteen()
    Digit_Sixteen()
    cross()
    cross2()
    cross3()
    cross4()
    cross5()
    cross6()
    cross7()
    cross8()
    cross9()
    cross10()
    cross11()
    cross12()
    cross13()
    cross14()
    cross15()
    cross16()
    One_two()
    Two_three()
    Three_four()
    One_Five()
    Five_six()
    Two_six()
    Seven_Eight()
    Seven_Three()
    Four_Eight()
    Six_seven()
    Nine_Ten()
    Ten_Eleven()
    Eleven_Twelve()
    Five_Nine()
    Six_Ten()
    Eleven_Seven()
    Twelve_Eight()
    Thirteen_Fourteen()
    Fourteen_Fifteen()
    Fifteen_Sixteen()
    Thirteen_Nine()
    Fourteen_Ten()
    Fifteen_Eleven()
    Sixteen_Twelve()
    Basic_winCase()
    Wincase_Two()
    Wincase_Three()

    pygame.display.update()
