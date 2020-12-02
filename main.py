"""
Yer a wizard, Harry!

This code takes you through your first day at Hogwarts!
You will be sorted and then you will go through a normal
day at school; you will learn the levitating charm, how
to change a bird into a cup, and the Boggart-banishing
spell.

By: Carmina Nicolas

"""
import os
import random
import time
from tkinter import simpledialog
from tkinter.font import Font
import pygame
from PIL import ImageTk, Image
from graphics import Canvas

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

MARGIN = 50

dx = 0
dy = -1
x = 0
y = 1


def main():
    """
    Goes through one normal day. Sets up canvas, house, schedule,
    and goes through three classes!
    dialog box credit: https://stackoverflow.com/a/62672469 & https://djangocentral.com/creating-user-input-dialog/
    music code credit: https://opensource.com/article/20/9/add-sound-python-game
    resize credit: https://www.codegrepper.com/code-examples/delphi/how+to+resize+image+in+python+tkinter
    """

    canvas = Canvas(WINDOW_WIDTH, WINDOW_HEIGHT, 'Hogwarts')

    # background music
    s = 'sound'
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join('HarryPotterMusic.mp3'))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    # sets up house
    sorting = opening_scene(canvas)
    house_points = 0

    # fonts
    title = Font(family='4 Privet Drive', size='60')
    classes = Font(family='DearMrPotter', size='30')
    bold = Font(family='4 Privet Drive', size='25', underline=1, weight='bold')

    # NARRATOR: welcome to first day of classes
    between_classes(canvas, bold, "Welcome to your first day of school! You will receive your schedule shortly.")

    # creates schedule
    create_schedule(canvas, title, classes, bold)

    # NARRATOR: go to charms
    between_classes(canvas, bold, "Today is Monday and you have Charms first! Let's go before you're late.")

    # charms class
    house_points = charms_lesson(canvas, sorting, house_points)

    # NARRATOR:
    between_classes(canvas, bold, "Time for Transfiguration with Professor McGonagall!")

    # transfiguration class
    house_points = transfiguration_lesson(canvas, sorting, house_points)
    between_classes(canvas, bold, "Time for Defense Against the Dark Arts with Professor Lupin!")

    # defense against the dark arts
    house_points = dada_lesson(canvas, sorting, house_points)

    # finale
    ending(canvas, bold, sorting, house_points)

    canvas.mainloop()


def opening_scene(canvas):
    # welcome page
    hogwarts = Image.open("hogwartsexpress.jpg")
    hogwarts = hogwarts.resize((1788, WINDOW_HEIGHT), Image.ANTIALIAS)
    opened_hogwarts = ImageTk.PhotoImage(hogwarts)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=opened_hogwarts)
    canvas.update()

    welcome = Image.open("welcome.png")
    welcome = welcome.resize((696, 100), Image.ANTIALIAS)
    opened_welcome = ImageTk.PhotoImage(welcome)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=opened_welcome)
    canvas.update()
    time.sleep(3)

    # asks for house or will sort you
    sorting = simpledialog.askstring(title="What's your Hogwarts House?", prompt="Are you a Gryffindor, Ravenclaw, "
                                                                                 "Hufflepuff, or Slytherin? If "
                                                                                 "neither, type in Sort Me")
    sorting = str(sorting)
    sorting = sorting.lower()

    #chooses random house
    if sorting == 'sort me' or sorting == '':
        house_list = ['gryffindor', 'ravenclaw', 'hufflepuff', 'slytherin']
        sorting = random.choice(house_list)
    sorting_hat(canvas, sorting)
    return sorting


def sorting_hat(canvas, sorting):
    sorting_gryffindor(sorting, canvas)
    sorting_ravenclaw(sorting, canvas)
    sorting_slytherin(sorting, canvas)
    sorting_hufflepuff(sorting, canvas)


def sorting_gryffindor(sorting, canvas):
    if sorting == 'gryffindor':
        sets_audio_hat(canvas, "Sorting Hat Gryffindor.mp3")
        sorted_house(canvas, 'gryff_greathall.jpg', 'gryf.png', 'grywelcome.png')


def sorting_ravenclaw(sorting, canvas):
    if sorting == 'ravenclaw':
        sets_audio_hat(canvas, "Sorting Hat Ravenclaw.mp3")
        sorted_house(canvas, 'raven_greathall.jpg', 'raven.png', 'ravwelcome.png')


def sorting_slytherin(sorting, canvas):
    if sorting == 'slytherin':
        sets_audio_hat(canvas, "Sorting Hat Slytherin.mp3")
        sorted_house(canvas, 'sly_greathall.jpg', 'sly.png', 'slywelcome.png')


def sorting_hufflepuff(sorting, canvas):
    if sorting == 'hufflepuff':
        sets_audio_hat(canvas, "Sorting Hat Hufflepuff.mp3")
        sorted_house(canvas, 'huffle_greathall.jpg', 'huffle.png', 'hufflepuffwelcome.png')


def sorted_house(canvas, hall_photo, crest, welcoming):
    # background hall themed to house
    hall = Image.open(hall_photo)
    hall = hall.resize((WINDOW_WIDTH, WINDOW_HEIGHT), Image.ANTIALIAS)
    hall = ImageTk.PhotoImage(hall)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=hall)
    # house crest
    house = Image.open(crest)
    house = house.resize((300, 360), Image.ANTIALIAS)
    house = ImageTk.PhotoImage(house)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=house)
    # welcome to ___
    wel = Image.open(welcoming)
    wel = ImageTk.PhotoImage(wel)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 6, anchor="center", image=wel)

    canvas.update()
    time.sleep(7.0)


def sets_audio_hat(canvas, file):
    # sorting hat audio
    sound = pygame.mixer.Sound(file)
    pygame.mixer.Sound.play(sound)
    sec = pygame.mixer.Sound.get_length(sound)
    # hat and background
    canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill='black')
    hat = Image.open("sortinghat.png")
    hat = hat.resize((800, 400), Image.ANTIALIAS)
    hat = ImageTk.PhotoImage(hat)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=hat)
    canvas.update()
    time.sleep(sec - 3)


def between_classes(canvas, bold, message):
    # transition scene
    hallway = Image.open("passinghallway.jpg")
    hallway = hallway.resize((1244, WINDOW_HEIGHT), Image.ANTIALIAS)
    opened_hallway = ImageTk.PhotoImage(hallway)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=opened_hallway)
    # guide
    canvas.create_rectangle(0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, WINDOW_HEIGHT, fill='black')
    canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50, anchor='center', font=bold, fill='white',
                       text=message)
    canvas.update()
    time.sleep(6)


def create_schedule(canvas, title, classes, bold):

    schedule = Image.open("parchment.jpg")
    schedule = schedule.resize((WINDOW_WIDTH, WINDOW_HEIGHT), Image.ANTIALIAS)
    schedule = ImageTk.PhotoImage(schedule)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=schedule)
    canvas.create_text(WINDOW_WIDTH / 2, MARGIN, anchor='center', font=title, text='Class Schedule')

    logo = Image.open("hogwartslogo.png")
    logo = logo.resize((84, 100), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)
    canvas.create_image(WINDOW_WIDTH - MARGIN / 2, MARGIN / 3, anchor="ne", image=logo)

    # class times
    times = ['10-11 am', '11-12 pm', '12-1 pm', '1-2 pm', '2-3 pm']
    multiplications = [2, 4, 6, 8, 10]
    for i in range(len(times)):
        canvas.create_text(10, MARGIN * multiplications[i] + 100, anchor='w', font=classes, text=times[i])
    # monday
    mon_classes = ['Charms', 'Lunch', 'Transfiguration', 'DADA']
    for i in range(len(mon_classes)):
        canvas.create_text(MARGIN * 2.5, MARGIN * multiplications[i] + 100, anchor='w', font=classes,
                           text=mon_classes[i])
    # tuesday
    tues_classes = ['Herbology', 'Lunch', 'CoMC', 'Potions', 'Potions']
    for i in range(len(tues_classes)):
        canvas.create_text(MARGIN * 6, MARGIN * multiplications[i] + 100, anchor='w', font=classes,
                           text=tues_classes[i])
    # wednesday
    wed_classes = ['HoM', 'Lunch', 'Flying', 'Transfiguration']
    for i in range(len(wed_classes)):
        canvas.create_text(MARGIN * 9.5, MARGIN * multiplications[i] + 100, anchor='w', font=classes,
                           text=wed_classes[i])
    # thursday
    thurs_classes = ['Herbology', 'Lunch', 'DADA', 'CoMC']
    for i in range(len(thurs_classes)):
        canvas.create_text(MARGIN * 13, MARGIN * multiplications[i] + 100, anchor='w', font=classes,
                           text=thurs_classes[i])
    # friday
    fri_classes = ['Flying', 'Lunch', 'HoM', 'Transfiguration']
    for i in range(len(wed_classes)):
        canvas.create_text(MARGIN * 16, MARGIN * multiplications[i] + 100, anchor='w', font=classes,
                           text=fri_classes[i])
    canvas.create_text(WINDOW_WIDTH / 2, MARGIN * 13.5, anchor='center', font=bold,
                       text='ASTRONOMY IS AT MIDNIGHT EVERY WEDNESDAY.')
    # days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    x_values = [2.5, 6, 9.5, 13, 16]
    for i in range(len(days)):
        canvas.create_text(MARGIN * x_values[i], MARGIN * 2 + 50, anchor='w', font=classes, text=days[i])
    # lines for schedule
    canvas.create_line(5, 175, WINDOW_WIDTH - 5, 175, width=3)
    line_x_values = [MARGIN * 1.75, MARGIN * 5, MARGIN * 8, MARGIN * 12, MARGIN * 15]
    for i in range(len(line_x_values)):
        canvas.create_line(line_x_values[i], 100, line_x_values[i], MARGIN * 12.5, width=3)
    canvas.update()
    time.sleep(10)


def charms_lesson(canvas, sorting, house_points):
    # charms classroom
    charms_img = Image.open("Charms_class_in_1991.jpg")
    charms_img = charms_img.resize((WINDOW_WIDTH, WINDOW_HEIGHT), Image.ANTIALIAS)
    charms_img = ImageTk.PhotoImage(charms_img)
    background = canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=charms_img)

    # feather
    feather_img = Image.open("feather.png")
    feather_img = feather_img.resize((250, 250), Image.ANTIALIAS)
    feather_img = ImageTk.PhotoImage(feather_img)
    feather = canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100, anchor="center", image=feather_img)

    # wand
    wand = Image.open("wand2.png")
    wand = wand.resize((600, 400), Image.ANTIALIAS)
    wand = ImageTk.PhotoImage(wand)
    wand_img = canvas.create_image(WINDOW_WIDTH / 2 - 25, WINDOW_HEIGHT + 20, anchor="sw", image=wand)
    # moves feather up and down as a demo
    pygame.mixer.music.pause()
    feather_demo(canvas, feather)
    pygame.mixer.music.unpause()
    pygame.mixer.music.set_volume(0.5)
    # student input
    incantation = say_spell("Type 'Wingardium Leviosa':")
    house_points = student_feather(incantation, canvas, feather, sorting, house_points)
    return house_points


def say_spell(text):
    incantation = simpledialog.askstring(title="Your turn!", prompt=text)
    incantation = str(incantation)
    incantation = incantation.lower()
    return incantation


def speaking_professor(canvas, message):
    canvas.create_polygon(10, 10, 60, 20, 20, 60, fill='navajo white', outline='navajo white')
    canvas.create_rectangle(20, 20, 525, 80, fill='navajo white', outline='navajo white')
    canvas.create_text(MARGIN, MARGIN, anchor='w', font='Times 20', text=message)
    canvas.update()


def student_feather(incantation, canvas, feather, sorting, house_points):
    if incantation == 'wingardium leviosa':
        pygame.mixer.music.pause()
        sound = pygame.mixer.Sound("incantation.mp3")
        pygame.mixer.Sound.play(sound)
        sound.set_volume(1.5)
        time.sleep(1.5)
        # slowly moves feather up
        while get_feather_height(canvas, feather):
            canvas.move(feather, 0, -2)
            canvas.update()
            time.sleep(1 / 20)

        speaking_professor(canvas, "Well done! See here, everyone! -Professor Flitwick")

        time.sleep(4)
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(0.5)
        speaking_professor(canvas, "10 points to " + sorting.capitalize() + "! - Professor Flitwick")
        # moves feather down
        while max_feather_height(canvas, feather):
            canvas.move(feather, 0, 2)
            canvas.update()
            time.sleep(1 / 50)
        time.sleep(8)
        house_points += 10
    else:
        # if misspelled or not inputted
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(0.5)
        canvas.create_polygon(10, 10, 60, 20, 20, 60, fill='navajo white', outline='navajo white')
        canvas.create_rectangle(20, 20, 500, 80, fill='navajo white', outline='navajo white')
        canvas.create_text(MARGIN, MARGIN, anchor='w', font='Times 20', text="That's okay! You'll get it soon! "
                                                                             "-Professor Flitwick")
        canvas.update()
        time.sleep(8)
    return house_points


def feather_demo(canvas, feather):
    sound = pygame.mixer.Sound("flitwick2.mp3")
    pygame.mixer.Sound.play(sound)
    sound.set_volume(1.5)
    # moves feather up and down
    for i in range(2):
        while get_feather_height(canvas, feather):
            canvas.move(feather, 0, -2)
            canvas.update()
            time.sleep(1 / 50)
        while max_feather_height(canvas, feather):
            canvas.move(feather, 0, 2)
            canvas.update()
            time.sleep(1 / 50)
    time.sleep(2)


def get_feather_height(canvas, object):
    return canvas.get_top_y(object) != WINDOW_HEIGHT / 2


def max_feather_height(canvas, object):
    return canvas.get_top_y(object) != WINDOW_HEIGHT - 100


def transfiguration_lesson(canvas, sorting, house_points):
    # transfiguration class
    pygame.mixer.music.pause()
    sound = pygame.mixer.Sound("mcgonagall.mp3")
    pygame.mixer.Sound.play(sound)

    tf = Image.open("Charms_class_in_1991.jpg")
    tf = tf.resize((WINDOW_WIDTH, WINDOW_HEIGHT + 5), Image.ANTIALIAS)
    tf = ImageTk.PhotoImage(tf)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=tf)

    bird = Image.open("bird.png")
    bird = bird.resize((300, 220), Image.ANTIALIAS)
    bird_img = ImageTk.PhotoImage(bird)
    birdie = canvas.create_image(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT - 100, anchor="sw", image=bird_img)

    wand = Image.open("wand.png")
    wand = wand.resize((400, 266), Image.ANTIALIAS)
    wand = ImageTk.PhotoImage(wand)
    wand_img = canvas.create_image(WINDOW_WIDTH / 2 - 25, WINDOW_HEIGHT - 60, anchor="sw", image=wand)

    cup = Image.open("cup.png")
    cup = cup.resize((120, 250), Image.ANTIALIAS)
    cup = ImageTk.PhotoImage(cup)
    canvas.update()
    time.sleep(11)
    # bird demo! turns bird into a water goblet
    for i in range(3):
        move_wand(canvas, wand_img)
    time.sleep(1)
    canvas.itemconfig(birdie, state='hidden')
    change_bird(canvas, bird_img, bird, cup, wand_img)

    canvas.itemconfig(birdie, state='hidden')

    cup_demo = canvas.create_image(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT - 100, anchor="sw", image=cup)
    canvas.raise_in_front_of(wand_img, 'all')
    canvas.update()
    time.sleep(3)
    # student's turn!
    house_points = student_transfiguration(canvas, wand_img, cup_demo, sorting, house_points, cup)
    time.sleep(5)
    return house_points


def move_wand(canvas, wand_img):
    # taps wand on bird
    while canvas.get_top_y(wand_img) != WINDOW_HEIGHT - 30:
        canvas.move(wand_img, x, y)
        canvas.update()
        time.sleep(1 / 500)
    while canvas.get_top_y(wand_img) != WINDOW_HEIGHT - 50:
        canvas.move(wand_img, dx, dy)
        canvas.update()
        time.sleep(1 / 500)


def change_bird(canvas, image, img, cup, wand):
    a = 0
    b = 0
    # makes bird smaller to resemble cup
    while image.height() != cup.height():
        img = img.resize((300 - a, 220 + b), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)
        birdie = canvas.create_image(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT - 100, anchor="sw", image=image)
        canvas.raise_in_front_of(wand, 'all')
        time.sleep(1 / 100)
        a += 2
        b += 2
        canvas.update()


def student_transfiguration(canvas, wand_img, cup_demo, sorting, house_points, cup):
    # vera verto
    # returns screen back to bird and guides student
    pygame.mixer.music.unpause()
    pygame.mixer.music.set_volume(0.5)
    box = canvas.create_rectangle(0, 0, WINDOW_WIDTH, 40, fill='black')
    txt = canvas.create_text(WINDOW_WIDTH / 2, 20, anchor='center', font='Courier 20', fill='white',
                             text="Click three times.")

    canvas.itemconfig(cup_demo, state='hidden')
    student_bird = Image.open("bird.png")
    student_bird = student_bird.resize((300, 220), Image.ANTIALIAS)
    student_bird_img = ImageTk.PhotoImage(student_bird)
    student_birdie = canvas.create_image(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT - 100, anchor="sw",
                                         image=student_bird_img)
    canvas.raise_in_front_of(wand_img, 'all')

    # wait for three clicks (taps bird three times)
    for i in range(3):
        canvas.currently_waiting_for_click = True
        canvas.wait_for_click_click_happened = False
        while not canvas.wait_for_click_click_happened:
            canvas.update()
        canvas.currently_waiting_for_click = False
        canvas.wait_for_click_click_happened = False
        move_wand(canvas, wand_img)
    # hides clicking instruction
    canvas.itemconfig(box, state='hidden')
    canvas.itemconfig(txt, state='hidden')

    vera_verto = say_spell("Type 'Vera Verto':")
    vera_verto = vera_verto.lower()
    if vera_verto == 'vera verto':
        sound = pygame.mixer.Sound("good_tf.mp3")
        pygame.mixer.Sound.play(sound)
        sound.set_volume(1.5)
        canvas.itemconfig(student_birdie, state='hidden') # there was a duplicate of the bird
        change_bird(canvas, student_bird_img, student_bird, cup, wand_img)
        canvas.itemconfig(student_birdie, state='hidden')
        canvas.itemconfig(cup_demo, state='normal') #brings cup back
        canvas.raise_in_front_of(wand_img, 'all')
        canvas.update()
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(0.5)
        speaking_professor(canvas, "Brilliant! -Professor McGonagall")
        time.sleep(5)
        speaking_professor(canvas, "10 points to " + sorting.capitalize() +"! - Professor McGonagall")
        time.sleep(3)
        house_points += 10
    else:
        sound = pygame.mixer.Sound("fail_tf.mp3")
        pygame.mixer.Sound.play(sound)
        sound.set_volume(1.5)
        time.sleep(5)
        speaking_professor(canvas, "That wand needs replacing. -Professor McGonagall")
        time.sleep(3)
    return house_points


def dada_lesson(canvas, sorting, house_points):
    # dada
    # boggart
    wardrobe = Image.open("wardrobe.jpg")
    wardrobe = wardrobe.resize((1897, 705), Image.ANTIALIAS)
    opened_wardrobe = ImageTk.PhotoImage(wardrobe)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=opened_wardrobe)
    canvas.update()

    pygame.mixer.music.pause()
    sound = pygame.mixer.Sound("boggart (1).mp3")
    pygame.mixer.Sound.play(sound)
    seconds = pygame.mixer.Sound.get_length(sound)
    sound.set_volume(1.5)
    time.sleep(seconds)

    wand = Image.open("wand2.png")
    wand = wand.resize((600, 400), Image.ANTIALIAS)
    wand = ImageTk.PhotoImage(wand)
    wand_img = canvas.create_image(WINDOW_WIDTH / 2 - 25, WINDOW_HEIGHT + 20, anchor="sw", image=wand)
    canvas.update()

    sound = pygame.mixer.Sound("riddikulus1.mp3")
    pygame.mixer.Sound.play(sound)
    sound.set_volume(1.5)
    time.sleep(11)

    wardrobe = Image.open("boggart.png")
    wardrobe = wardrobe.resize((1400, WINDOW_HEIGHT), Image.ANTIALIAS)
    opened_wardrobe = ImageTk.PhotoImage(wardrobe)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=opened_wardrobe)
    canvas.raise_in_front_of(wand_img, 'all')
    canvas.update()
    time.sleep(12)

    house_points = student_dada(canvas, wand_img, sorting, house_points)
    return house_points


def student_dada(canvas, wand_img, sorting, house_points):
    # riddikulus
    pygame.mixer.music.unpause()
    pygame.mixer.music.set_volume(0.5)
    riddikulus = say_spell("Type 'Riddikulus':")
    riddikulus = riddikulus.lower()

    if riddikulus == 'riddikulus':
        pygame.mixer.music.pause()
        sound = pygame.mixer.Sound("riddikulus2.mp3")
        pygame.mixer.Sound.play(sound)
        sound.set_volume(1.5)
        time.sleep(1.5)
        funny_snape = Image.open("snape.jpg")
        funny_snape = funny_snape.resize((1400, WINDOW_HEIGHT), Image.ANTIALIAS)
        opened_fs = ImageTk.PhotoImage(funny_snape)
        canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=opened_fs)
        canvas.raise_in_front_of(wand_img, 'all')
        canvas.update()
        time.sleep(4)
        speaking_professor(canvas, "Wonderful! -Professor Lupin")
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(0.5)
        time.sleep(5)
        speaking_professor(canvas, "10 points to " + sorting.capitalize() + "! - Professor Lupin")
        time.sleep(3)
        house_points += 10

    else:
        pygame.mixer.music.pause()
        sound = pygame.mixer.Sound("fail_rid.mp3")
        pygame.mixer.Sound.play(sound)
        sound.set_volume(1.5)
        time.sleep(5)
        funny_snape = Image.open("snape.jpg")
        funny_snape = funny_snape.resize((1400, WINDOW_HEIGHT), Image.ANTIALIAS)
        opened_fs = ImageTk.PhotoImage(funny_snape)
        canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=opened_fs)
        canvas.raise_in_front_of(wand_img, 'all')
        canvas.update()
        time.sleep(9)
        pygame.mixer.music.unpause()
        pygame.mixer.music.set_volume(0.5)
    return house_points


def ending(canvas, bold, sorting, house_points):
    # house points
    hogwarts = Image.open("commonroom.jpg")
    hogwarts = hogwarts.resize((1400, WINDOW_HEIGHT), Image.ANTIALIAS)
    opened_hogwarts = ImageTk.PhotoImage(hogwarts)
    canvas.create_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor="center", image=opened_hogwarts)
    canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, anchor='center', font=bold, fill='white',
                       text="You've gained " + sorting.capitalize() + " " + str(house_points) + " House points!")
    canvas.update()
    time.sleep(10)
    canvas.destroy()


if __name__ == '__main__':
    main()
