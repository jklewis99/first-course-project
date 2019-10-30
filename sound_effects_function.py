from pygame.locals import *
import pygame
import csv
import time
from random import *
def sound_effects():

    SIZE = 16
    FREQUENCY = 44100
    N_CHANNELS = 2
    BUFFER = 512

    pygame.mixer.pre_init(FREQUENCY, SIZE, N_CHANNELS, BUFFER)
    pygame.init()
    pygame.font.init()
    # the following does not keep location of the open window consistent...
    screen = pygame.display.set_mode((1010, 600)) # (width, height)
    ''' colors are defined by 3 integer values corresponding to
    values of Red, Blue, Green, respectively. White = (255, 255, 255)
    '''

    image_center_x = 505
    screen_color = (255, 255, 255)



    black = (0, 0, 0)
    white = (255, 255, 255)
    new_color = (170, 170, 170)
    screen.fill(screen_color) #changes color of screen


    #numbers

    # first row of numbers
    one = Rect((60, 20), (80, 80))
    two = Rect((150, 20), (80, 80))
    three = Rect((240, 20), (80, 80))
    four = Rect((330, 20), (80, 80))
    five = Rect((420, 20), (80, 80))
    six = Rect((510, 20), (80, 80))
    seven = Rect((600, 20), (80, 80))
    eight = Rect((690, 20), (80, 80))
    nine = Rect((780, 20), (80, 80))
    zero = Rect((870, 20), (80, 80))

    q = Rect((60, 110), (80, 80))
    w = Rect((150, 110), (80, 80))
    e = Rect((240, 110), (80, 80))
    r = Rect((330, 110), (80, 80))
    t = Rect((420, 110), (80, 80))
    y = Rect((510, 110), (80, 80))
    u = Rect((600, 110), (80, 80))
    i = Rect((690, 110), (80, 80))
    o = Rect((780, 110), (80, 80))
    p = Rect((870, 110), (80, 80))

    a = Rect((60, 200), (80, 80))
    s = Rect((150, 200), (80, 80))
    z = Rect((60, 290), (80, 80))
    x = Rect((150, 290), (80, 80))
    l = Rect((780, 200), (80, 80))
    semicolon = Rect((870, 200), (80, 80))
    comma = Rect((780, 290), (80, 80))
    period = Rect((870, 290), (80, 80))

    white_rect = Rect((230, 200), (540, 540))

    pygame.draw.rect(screen, black, one)
    pygame.draw.rect(screen, black, two)
    pygame.draw.rect(screen, black, three)
    pygame.draw.rect(screen, black, four)
    pygame.draw.rect(screen, black, five)
    pygame.draw.rect(screen, black, six)
    pygame.draw.rect(screen, black, seven)
    pygame.draw.rect(screen, black, eight)
    pygame.draw.rect(screen, black, nine)
    pygame.draw.rect(screen, black, zero)

    pygame.draw.rect(screen, black, q) #q
    pygame.draw.rect(screen, black, w) #w
    pygame.draw.rect(screen, black, e) #e
    pygame.draw.rect(screen, black, r) #r
    pygame.draw.rect(screen, black, t) #t
    pygame.draw.rect(screen, black, y) #y
    pygame.draw.rect(screen, black, u) #u
    pygame.draw.rect(screen, black, i) #i
    pygame.draw.rect(screen, black, o) #o
    pygame.draw.rect(screen, black, p) #p

    pygame.draw.rect(screen, black, a)
    pygame.draw.rect(screen, black, s)
    pygame.draw.rect(screen, black, z)
    pygame.draw.rect(screen, black, x)
    pygame.draw.rect(screen, black, l)
    pygame.draw.rect(screen, black, semicolon)
    pygame.draw.rect(screen, black, comma)
    pygame.draw.rect(screen, black, period)

    key_font_type = pygame.font.SysFont('Lucida Fax', 25)
    key_1 = key_font_type.render("1", False, (250, 250, 250))
    key_2 = key_font_type.render("2", False, (250, 250, 250))
    key_3 = key_font_type.render("3", False, (250, 250, 250))
    key_4 = key_font_type.render("4", False, (250, 250, 250))
    key_5 = key_font_type.render("5", False, (250, 250, 250))
    key_6 = key_font_type.render("6", False, (250, 250, 250))
    key_7 = key_font_type.render("7", False, (250, 250, 250))
    key_8 = key_font_type.render("8", False, (250, 250, 250))
    key_9 = key_font_type.render("9", False, (250, 250, 250))
    key_0 = key_font_type.render("0", False, (250, 250, 250))

    key_Q = key_font_type.render("Q", False, (250, 250, 250))
    key_W = key_font_type.render("W", False, (250, 250, 250))
    key_E = key_font_type.render("E", False, (250, 250, 250))
    key_R = key_font_type.render("R", False, (250, 250, 250))
    key_T = key_font_type.render("T", False, (250, 250, 250))
    key_Y = key_font_type.render("Y", False, (250, 250, 250))
    key_U = key_font_type.render("U", False, (250, 250, 250))
    key_I = key_font_type.render("I", False, (250, 250, 250))
    key_O = key_font_type.render("O", False, (250, 250, 250))
    key_P = key_font_type.render("P", False, (250, 250, 250))
    key_S = key_font_type.render("S", False, (250, 250, 250))

    key_A = key_font_type.render("A", False, (250, 250, 250))
    key_S = key_font_type.render("S", False, (250, 250, 250))
    key_Z = key_font_type.render("Z", False, (250, 250, 250))
    key_X = key_font_type.render("X", False, (250, 250, 250))
    key_L = key_font_type.render("L", False, (250, 250, 250))
    key_semicolon = key_font_type.render(";", False, (250, 250, 250))
    key_comma = key_font_type.render(",", False, (250, 250, 250))
    key_period = key_font_type.render(".", False, (250, 250, 250))

    #print keys
    screen.blit(key_1, (64, 18))
    screen.blit(key_2, (154, 18))
    screen.blit(key_3, (244, 18))
    screen.blit(key_4, (334, 18))
    screen.blit(key_5, (424, 18))
    screen.blit(key_6, (514, 18))
    screen.blit(key_7, (604, 18))
    screen.blit(key_8, (694, 18))
    screen.blit(key_9, (784, 18))
    screen.blit(key_0, (874, 18))

    screen.blit(key_Q, (64, 108))
    screen.blit(key_W, (154, 108))
    screen.blit(key_E, (244, 108))
    screen.blit(key_R, (334, 108))
    screen.blit(key_T, (424, 108))
    screen.blit(key_Y, (514, 108))
    screen.blit(key_U, (604, 108))
    screen.blit(key_I, (694, 108))
    screen.blit(key_O, (784, 108))
    screen.blit(key_P, (874, 108))

    screen.blit(key_A, (64, 198))
    screen.blit(key_S, (154, 198))
    screen.blit(key_Z, (64, 288))
    screen.blit(key_X, (154, 288))

    screen.blit(key_L, (784, 198))
    screen.blit(key_semicolon, (879, 198))
    screen.blit(key_comma, (789, 288))
    screen.blit(key_period, (879, 288))

    #images
    #pygame.transform.rotozoom(IMAGE, 0, 2)
    #dark knight
    batman = pygame.image.load('\PythonPrograms\FinalProject\Photos\\batman.jpg')
    joker_2 = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\the_joker.jpg'), 0, 5.13/8)
    joker_1 = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\the_joker_2.jpg'), 0, 1/4)
    joker_3 = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\the_joker_3.jpg'), 0, 8.7/20)
    joker_4 = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\the_joker_4.jpg'), 0, 3.75/10)
    lucious = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\lucious_fox.jpeg'), 0, 2.75/11)
    bane = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\bane.jpg'), 0, 2/3)
    #star wars
    r2d2 = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\r2d2.jpg'), 0, 3.33/5)
    r2d2_2 = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\r2d2_1.jpg'), 0, 0.97/2)
    darth_vader = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\Darth_Vader.jpg'), 0, 0.8/2)
    chewbacca = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\chewbacca_2.png'), 0, 0.94/2)
    not_the_droids = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\not_the_droids.png'), 0, 1.23/2)
    #rocky3
    pity_fool = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\rocky.jpg'), 0, 1.6)
    #godfather
    offer = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\the_godfather_1.jpg'), 0, 4.95/6)
    badabing = pygame.image.load('\PythonPrograms\FinalProject\Photos\\the_godfather_2.jpg')
    #back to the future
    butthead = pygame.image.load('\PythonPrograms\FinalProject\Photos\\butthead.jpg')
    gigawatts = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\back_to_the_future_1.jpg'), 0, 2.63/7)
    great_scott = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\back_to_the_future_2.jpg'), 0, 0.94/2)
    say_hi = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\back_to_the_future_3.jpg'), 0, 1.17/2)
    #office
    creed = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\creed.jpg'), 0, 0.725/3)
    stanley_1 = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\do_not_care.jpg'), 0, 1.485/2)
    dwight = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\dwight.jpg'), 0, 0.94/2)
    kevin = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\kevin.jpg'), 0, 0.75/2)
    michael = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\michael.jpeg'), 0, 1.02/2)
    stanley_2 = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\not_funny.jpg'), 0, 1)
    pam = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\pam.jpg'), 0, 1.05/7)
    stanley_3 = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\pretzel_day.png'), 0, 0.965)
    jim = pygame.transform.rotozoom(pygame.image.load('\PythonPrograms\FinalProject\Photos\\jim_as_dwight.jpg'), 0, 0.75/2)

    soundboard_type = "drum kit"
    pygame.display.update()

    config_file = 'key_to_sound_effects.txt'
    mode = "player"
    # may include a different mode so that files will repeat or play more than once, time permitting
    fadeout_time = 50

    if mode == "player":
        repeat = 0

    # Read configuration file

    key_sound = {}
    key_file = {}
    config = csv.reader(open('key_to_sound_effects.txt', 'r'), delimiter='`')

    for key, soundfile in config:
        key, soundfile = key.strip(' '), soundfile.strip(' ')

        if key is not '#':
            key_file[key] = soundfile
            key_sound[key] = pygame.mixer.Sound(soundfile)

    events_list = []
    currently_playing = {k: False for k in key_sound.__iter__()}
    while True:
        event = pygame.event.wait()

        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            key = pygame.key.name(event.key)

            if key in key_sound:
                if event.type == pygame.KEYDOWN:
                    key_sound[key].play(repeat)
                    currently_playing[key] = True
                    pygame.draw.rect(screen, white, white_rect)
                    if key == '1':
                        pygame.draw.rect(screen, new_color, one)
                        screen.blit(key_1, (64, 18))
                        screen.blit(pam, (image_center_x - 240, 210))
                    if key == '2':
                        pygame.draw.rect(screen, new_color, two)
                        screen.blit(key_2, (154, 18))
                        screen.blit(kevin, (image_center_x - 240, 210))
                    if key == '3':
                        pygame.draw.rect(screen, new_color, three)
                        screen.blit(key_3, (244, 18))
                        screen.blit(jim, (image_center_x - 240, 210))
                    if key == '4':
                        pygame.draw.rect(screen, new_color, four)
                        screen.blit(key_4, (334, 18))
                        screen.blit(michael, (image_center_x - 240, 210))
                    if key == '5':
                        pygame.draw.rect(screen, new_color, five)
                        screen.blit(key_5, (424, 18))
                        screen.blit(stanley_3, (image_center_x - 240, 210))
                    if key == '6':
                        pygame.draw.rect(screen, new_color, six)
                        screen.blit(key_6, (514, 18))
                        screen.blit(stanley_2, (image_center_x - 140, 210))
                    if key == '7':
                        pygame.draw.rect(screen, new_color, seven)
                        screen.blit(key_7, (604, 18))
                        screen.blit(stanley_1, (image_center_x - 240, 210))
                    if key == '8':
                        pygame.draw.rect(screen, new_color, eight)
                        screen.blit(key_8, (694, 18))
                        screen.blit(creed, (image_center_x - 240, 210))
                    if key == '9':
                        pygame.draw.rect(screen, new_color, nine)
                        screen.blit(key_9, (784, 18))
                        screen.blit(dwight, (image_center_x - 240, 210))
                    if key == '0':
                        pygame.draw.rect(screen, new_color, zero)
                        screen.blit(key_0, (874, 18))
                        screen.blit(pity_fool, (image_center_x - 240, 210))

                    if key == ';':
                        pygame.draw.rect(screen, new_color, semicolon)
                        screen.blit(key_semicolon, (879, 198))
                        screen.blit(r2d2_2, (image_center_x - 240, 210))
                    if key == '.':
                        pygame.draw.rect(screen, new_color, period)
                        screen.blit(key_period, (879, 288))
                        screen.blit(chewbacca, (image_center_x - 240, 210))
                    if key == ',':
                        pygame.draw.rect(screen, new_color, comma)
                        screen.blit(key_comma, (789, 288))
                        screen.blit(not_the_droids, (image_center_x - 240, 210))

                    if key == 'q':
                        pygame.draw.rect(screen, new_color, q)
                        screen.blit(joker_1, (image_center_x - 240, 210))
                        screen.blit(key_Q, (64, 108))
                    if key == 'w':
                        pygame.draw.rect(screen, new_color, w)
                        screen.blit(key_W, (154, 108))
                        screen.blit(joker_2, (image_center_x - 240, 210))
                    if key == 'e':
                        pygame.draw.rect(screen, new_color, e)
                        screen.blit(key_E, (244, 108))
                        screen.blit(joker_3, (image_center_x - 240, 210))
                    if key == 'r':
                        pygame.draw.rect(screen, new_color, r)
                        screen.blit(key_R, (334, 108))
                        screen.blit(joker_4, (image_center_x - 240, 210))
                    if key == 't':
                        pygame.draw.rect(screen, new_color, t)
                        screen.blit(key_T, (424, 108))
                        screen.blit(bane, (image_center_x - 240, 210))
                    if key == 'y':
                        pygame.draw.rect(screen, new_color, y)
                        screen.blit(key_Y, (514, 108))
                        screen.blit(lucious, (image_center_x - 240, 210))
                    if key == 'u':
                        pygame.draw.rect(screen, new_color, u)
                        screen.blit(key_U, (604, 108))
                        screen.blit(batman, (image_center_x - 240, 210))
                    if key == 'i':
                        pygame.draw.rect(screen, new_color, i)
                        screen.blit(key_I, (694, 108))
                        screen.blit(badabing, (image_center_x - 193, 210))
                    if key == 'o':
                        pygame.draw.rect(screen, new_color, o)
                        screen.blit(key_O, (784, 108))
                        screen.blit(offer, (image_center_x - 240, 210))
                    if key == 'p':
                        pygame.draw.rect(screen, new_color, p)
                        screen.blit(key_P, (874, 108))
                        screen.blit(r2d2, (image_center_x - 240, 210))

                    if key == 'a':
                        pygame.draw.rect(screen, new_color, a)
                        screen.blit(key_A, (64, 198))
                        screen.blit(gigawatts, (image_center_x - 240, 210))
                    if key == 's':
                        pygame.draw.rect(screen, new_color, s)
                        screen.blit(key_S, (154, 198))
                        screen.blit(butthead, (image_center_x - 240, 210))
                    if key == 'l':
                        pygame.draw.rect(screen, new_color, l)
                        screen.blit(key_L, (784, 198))
                        screen.blit(darth_vader, (image_center_x - 240, 210))

                    if key == 'z':
                        pygame.draw.rect(screen, new_color, z)
                        screen.blit(key_Z, (64, 288))
                        screen.blit(great_scott, (image_center_x - 240, 210))
                    if key == 'x':
                        pygame.draw.rect(screen, new_color, x)
                        screen.blit(key_X, (154, 288))
                        screen.blit(say_hi, (image_center_x - 240, 210))

                    pygame.display.update()
                    events_list.append((time.time(), key_file[key]))



                elif event.type == pygame.KEYUP:

                    if key == '1':
                        pygame.draw.rect(screen, black, one)
                        screen.blit(key_1, (64, 18))
                    if key == '2':
                        pygame.draw.rect(screen, black, two)
                        screen.blit(key_2, (154, 18))
                    if key == '3':
                        pygame.draw.rect(screen, black, three)
                        screen.blit(key_3, (244, 18))
                    if key == '4':
                        pygame.draw.rect(screen, black, four)
                        screen.blit(key_4, (334, 18))
                    if key == '5':
                        pygame.draw.rect(screen, black, five)
                        screen.blit(key_5, (424, 18))
                    if key == '6':
                        pygame.draw.rect(screen, black, six)
                        screen.blit(key_6, (514, 18))
                    if key == '7':
                        pygame.draw.rect(screen, black, seven)
                        screen.blit(key_7, (604, 18))
                    if key == '8':
                        pygame.draw.rect(screen, black, eight)
                        screen.blit(key_8, (694, 18))
                    if key == '9':
                        pygame.draw.rect(screen, black, nine)
                        screen.blit(key_9, (784, 18))
                    if key == '0':
                        pygame.draw.rect(screen, black, zero)
                        screen.blit(key_0, (874, 18))

                    if key == ';':
                        pygame.draw.rect(screen, black, semicolon)
                        screen.blit(key_semicolon, (879, 198))
                    if key == '.':
                        pygame.draw.rect(screen, black, period)
                        screen.blit(key_period, (879, 288))
                    if key == ',':
                        pygame.draw.rect(screen, black, comma)
                        screen.blit(key_comma, (789, 288))

                    if key == 'q':
                        pygame.draw.rect(screen, black, q)
                        screen.blit(key_Q, (64, 108))
                    if key == 'w':
                        pygame.draw.rect(screen, black, w)
                        screen.blit(key_W, (154, 108))
                    if key == 'e':
                        pygame.draw.rect(screen, black, e)
                        screen.blit(key_E, (244, 108))
                    if key == 'r':
                        pygame.draw.rect(screen, black, r)
                        screen.blit(key_R, (334, 108))
                    if key == 't':
                        pygame.draw.rect(screen, black, t)
                        screen.blit(key_T, (424, 108))
                    if key == 'y':
                        pygame.draw.rect(screen, black, y)
                        screen.blit(key_Y, (514, 108))
                    if key == 'u':
                        pygame.draw.rect(screen, black, u)
                        screen.blit(key_U, (604, 108))
                    if key == 'i':
                        pygame.draw.rect(screen, black, i)
                        screen.blit(key_I, (694, 108))
                    if key == 'o':
                        pygame.draw.rect(screen, black, o)
                        screen.blit(key_O, (784, 108))
                    if key == 'p':
                        pygame.draw.rect(screen, black, p)
                        screen.blit(key_P, (874, 108))

                    if key == 'a':
                        pygame.draw.rect(screen, black, a)
                        screen.blit(key_A, (64, 198))
                    if key == 's':
                        pygame.draw.rect(screen, black, s)
                        screen.blit(key_S, (154, 198))

                    if key == 'l':
                        pygame.draw.rect(screen, black, l)
                        screen.blit(key_L, (784, 198))

                    if key == 'z':
                        pygame.draw.rect(screen, black, z)
                        screen.blit(key_Z, (64, 288))
                    if key == 'x':
                        pygame.draw.rect(screen, black, x)
                        screen.blit(key_X, (154, 288))


                    pygame.display.update()

            elif event.key == pygame.K_ESCAPE:
                # must hit the escape key to exit the program
                break

        elif event.type == pygame.QUIT:
            # allows one to exit the program by clicking the x in the window
            break