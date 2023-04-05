from microbit import *

images = {
    1: Image.HEART,
    2: Image.HEART_SMALL,
    3: Image.HAPPY,
    4: Image.SAD,
    5: Image.SURPRISED,
    6: Image.ANGRY,
    7: Image.ASLEEP,
    8: Image.BUTTERFLY,
    9: Image.DIAMOND,
    10: Image.CONFUSED,
    11: Image.COW,
    12: Image.PACMAN,
}

index_num = 1

while True:
    if button_b.is_pressed():
        index_num += 1
    if button_a.is_pressed():
        index_num -= 1
    if index_num > 12:
        index_num = 1
    elif index_num < 1:
        index_num = 12
    display.show(images[index_num])
    sleep(500)


