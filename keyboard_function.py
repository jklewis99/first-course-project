import pygame
from pygame.locals import *
import csv
import time
from random import *

# here is the method that contains all that is required to run the program
def marimba():
    SIZE = 16
    FREQUENCY = 44100
    N_CHANNELS = 2
    BUFFER = 512

    pygame.mixer.pre_init(FREQUENCY, SIZE, N_CHANNELS, BUFFER)
    pygame.init()
    pygame.font.init()
    
    # the following does not keep location of the open window consistent...
    screen = pygame.display.set_mode((1000, 600)) # (width, height)
    ''' colors are defined by 3 integer values corresponding to
    values of Red, Blue, Green, respectively. White = (255, 255, 255)
    '''
    screen_color = (255, 255, 255)

    #randomly generate what color the keyboard is
    red_value_key, blue_value_key, green_value_key = randint(0, 250), randint(0, 250), randint(0, 250)
    sky_blue = (red_value_key, blue_value_key, green_value_key)

    #randomly generate a different color for when key is pressed
    red_value_down, blue_value_down, green_value_down = randint(0, 250), randint(0, 250), randint(0, 250)
    #check if this color is too similar to the keyboard color
    if red_value_down < (red_value_key + 15) and red_value_down > (red_value_key - 15)\
    and blue_value_down < (blue_value_key + 15) and blue_value_down > (blue_value_key - 15)\
    and green_value_down < (green_value_key + 15) and green_value_down < (green_value_key - 15):
        red_value_down += 20
        blue_value_down += 20
        green_value_down += 20

    new_color = (red_value_down, blue_value_down, green_value_down)
    screen.fill(screen_color) #changes color of screen


    #numbers
    pygame.draw.rect(screen, sky_blue, Rect((130, 20), (70, 70)))  # 2
    pygame.draw.rect(screen, sky_blue, Rect((210, 20), (70, 70)))  # 3

    pygame.draw.rect(screen, sky_blue, Rect((370, 20), (70, 70)))  # 5
    pygame.draw.rect(screen, sky_blue, Rect((450, 20), (70, 70)))  # 6
    pygame.draw.rect(screen, sky_blue, Rect((530, 20), (70, 70)))  # 7
    pygame.draw.rect(screen, sky_blue, Rect((690, 20), (70, 70)))  # 9
    pygame.draw.rect(screen, sky_blue, Rect((770, 20), (70, 70)))  # 0

    # first row of letters
    pygame.draw.rect(screen, sky_blue, Rect((100, 100), (70, 70)))  # q
    pygame.draw.rect(screen, sky_blue, Rect((180, 100), (70, 70)))  # w
    pygame.draw.rect(screen, sky_blue, Rect((260, 100), (70, 70)))  # e
    pygame.draw.rect(screen, sky_blue, Rect((340, 100), (70, 70)))  # r
    pygame.draw.rect(screen, sky_blue, Rect((420, 100), (70, 70)))  # t
    pygame.draw.rect(screen, sky_blue, Rect((500, 100), (70, 70)))  # y
    pygame.draw.rect(screen, sky_blue, Rect((580, 100), (70, 70)))  # u
    pygame.draw.rect(screen, sky_blue, Rect((660, 100), (70, 70)))  # i
    pygame.draw.rect(screen, sky_blue, Rect((740, 100), (70, 70)))  # o
    pygame.draw.rect(screen, sky_blue, Rect((820, 100), (70, 70)))  # p

    # second row of letters
    pygame.draw.rect(screen, sky_blue, Rect((200, 180), (70, 70))) # s

    pygame.draw.rect(screen, sky_blue, Rect((360, 180), (70, 70))) # f
    pygame.draw.rect(screen, sky_blue, Rect((440, 180), (70, 70))) # g

    pygame.draw.rect(screen, sky_blue, Rect((600, 180), (70, 70))) # j
    pygame.draw.rect(screen, sky_blue, Rect((680, 180), (70, 70))) # k
    pygame.draw.rect(screen, sky_blue, Rect((760, 180), (70, 70))) # l

    # third row of letters
    pygame.draw.rect(screen, sky_blue, Rect((160, 260), (70, 70)))
    pygame.draw.rect(screen, sky_blue, Rect((240, 260), (70, 70)))
    pygame.draw.rect(screen, sky_blue, Rect((320, 260), (70, 70)))
    pygame.draw.rect(screen, sky_blue, Rect((400, 260), (70, 70)))
    pygame.draw.rect(screen, sky_blue, Rect((480, 260), (70, 70)))
    pygame.draw.rect(screen, sky_blue, Rect((560, 260), (70, 70)))
    pygame.draw.rect(screen, sky_blue, Rect((640, 260), (70, 70)))
    pygame.draw.rect(screen, sky_blue, Rect((720, 260), (70, 70)))
    pygame.draw.rect(screen, sky_blue, Rect((800, 260), (70, 70)))

    two = Rect((130, 20), (70, 70))
    three = Rect((210, 20), (70, 70))
    five = Rect((370, 20), (70, 70))
    six = Rect((450, 20), (70, 70))
    seven = Rect((530, 20), (70, 70))
    nine = Rect((690, 20), (70, 70))
    zero = Rect((770, 20), (70, 70))

    q = Rect((100, 100), (70, 70))
    w = Rect((180, 100), (70, 70))
    e = Rect((260, 100), (70, 70))
    r = Rect((340, 100), (70, 70))
    t = Rect((420, 100), (70, 70))
    y = Rect((500, 100), (70, 70))
    u = Rect((580, 100), (70, 70))
    i = Rect((660, 100), (70, 70))
    o = Rect((740, 100), (70, 70))
    p = Rect((820, 100), (70, 70))

    a = Rect((120, 180), (70, 70))
    s = Rect((200, 180), (70, 70))
    d = Rect((280, 180), (70, 70))
    f = Rect((360, 180), (70, 70))
    g = Rect((440, 180), (70, 70))
    h = Rect((520, 180), (70, 70))
    j = Rect((600, 180), (70, 70))
    k = Rect((680, 180), (70, 70))
    l = Rect((760, 180), (70, 70))

    z = Rect((160, 260), (70, 70))
    x = Rect((240, 260), (70, 70))
    c = Rect((320, 260), (70, 70))
    v = Rect((400, 260), (70, 70))
    b = Rect((480, 260), (70, 70))
    n = Rect((560, 260), (70, 70))
    m = Rect((640, 260), (70, 70))
    comma = Rect((720, 260), (70, 70))
    period = Rect((800, 260), (70, 70))

    font_type = pygame.font.SysFont('Copperplate Gothic Bold', 50)
    text_word_A = font_type.render("A", False, (0, 0, 0))
    text_word_B = font_type.render("B", False, (0, 0, 0))
    text_word_C = font_type.render("C", False, (0, 0, 0))
    text_word_D = font_type.render("D", False, (0, 0, 0))
    text_word_E = font_type.render("E", False, (0, 0, 0))
    text_word_F = font_type.render("F", False, (0, 0, 0))
    text_word_G = font_type.render("G", False, (0, 0, 0))
    text_word_A_SH = font_type.render("A#", False, (0, 0, 0))
    text_word_C_SH = font_type.render("C#", False, (0, 0, 0))
    text_word_D_SH = font_type.render("D#", False, (0, 0, 0))
    text_word_F_SH = font_type.render("F#", False, (0, 0, 0))
    text_word_G_SH = font_type.render("G#", False, (0, 0, 0))

    key_font_type = pygame.font.SysFont('Lucida Fax', 20)
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
    key_F = key_font_type.render("F", False, (250, 250, 250))
    key_G = key_font_type.render("G", False, (250, 250, 250))
    key_H = key_font_type.render("H", False, (250, 250, 250))
    key_J = key_font_type.render("J", False, (250, 250, 250))
    key_K = key_font_type.render("K", False, (250, 250, 250))
    key_L = key_font_type.render("L", False, (250, 250, 250))
    key_Z = key_font_type.render("Z", False, (250, 250, 250))
    key_X = key_font_type.render("X", False, (250, 250, 250))
    key_C = key_font_type.render("C", False, (250, 250, 250))
    key_V = key_font_type.render("V", False, (250, 250, 250))
    key_B = key_font_type.render("B", False, (250, 250, 250))
    key_N = key_font_type.render("N", False, (250, 250, 250))
    key_M = key_font_type.render("M", False, (250, 250, 250))
    key_COMMA = key_font_type.render(",", False, (250, 250, 250))
    key_PERIOD = key_font_type.render(".", False, (250, 250, 250))
    key_2 = key_font_type.render("2", False, (250, 250, 250))
    key_3 = key_font_type.render("3", False, (250, 250, 250))
    key_5 = key_font_type.render("5", False, (250, 250, 250))
    key_6 = key_font_type.render("6", False, (250, 250, 250))
    key_7 = key_font_type.render("7", False, (250, 250, 250))
    key_9 = key_font_type.render("9", False, (250, 250, 250))
    key_0 = key_font_type.render("0", False, (250, 250, 250))

    screen.blit(key_Q, (103, 100))
    screen.blit(key_W, (183, 100))
    screen.blit(key_E, (263, 100))
    screen.blit(key_R, (343, 100))
    screen.blit(key_T, (423, 100))
    screen.blit(key_Y, (503, 100))
    screen.blit(key_U, (583, 100))
    screen.blit(key_I, (663, 100))
    screen.blit(key_O, (743, 100))
    screen.blit(key_P, (823, 100))

    screen.blit(key_2, (133, 20))
    screen.blit(key_3, (213, 20))
    screen.blit(key_5, (373, 20))
    screen.blit(key_6, (453, 20))
    screen.blit(key_7, (533, 20))
    screen.blit(key_9, (693, 20))
    screen.blit(key_0, (773, 20))

    screen.blit(key_Z, (163, 260))
    screen.blit(key_X, (243, 260))
    screen.blit(key_C, (323, 260))
    screen.blit(key_V, (403, 260))
    screen.blit(key_B, (483, 260))
    screen.blit(key_N, (563, 260))
    screen.blit(key_M, (643, 260))
    screen.blit(key_COMMA, (728, 260))
    screen.blit(key_PERIOD, (808, 260))

    screen.blit(key_S, (203, 180))
    screen.blit(key_F, (363, 180))
    screen.blit(key_G, (443, 180))
    screen.blit(key_J, (603, 180))
    screen.blit(key_K, (683, 180))
    screen.blit(key_L, (763, 180))

    screen.blit(text_word_C, (122, 138))
    screen.blit(text_word_D, (202, 138))
    screen.blit(text_word_E, (282, 138))
    screen.blit(text_word_F, (362, 138))
    screen.blit(text_word_G, (442, 138))
    screen.blit(text_word_A, (522, 138))
    screen.blit(text_word_B, (602, 138))
    screen.blit(text_word_C, (682, 138))
    screen.blit(text_word_D, (762, 138))
    screen.blit(text_word_E, (842, 138))

    screen.blit(text_word_A, (182, 298))
    screen.blit(text_word_B, (262, 298))
    screen.blit(text_word_C, (342, 298))
    screen.blit(text_word_D, (422, 298))
    screen.blit(text_word_E, (502, 298))
    screen.blit(text_word_F, (582, 298))
    screen.blit(text_word_G, (662, 298))
    screen.blit(text_word_A, (742, 298))
    screen.blit(text_word_B, (822, 298))

    screen.blit(text_word_C_SH, (142, 58))
    screen.blit(text_word_D_SH, (222, 58))
    screen.blit(text_word_F_SH, (382, 58))
    screen.blit(text_word_G_SH, (462, 58))
    screen.blit(text_word_A_SH, (542, 58))
    screen.blit(text_word_C_SH, (702, 58))
    screen.blit(text_word_D_SH, (782, 58))

    screen.blit(text_word_A_SH, (212, 218))
    screen.blit(text_word_C_SH, (372, 218))
    screen.blit(text_word_D_SH, (452, 218))
    screen.blit(text_word_F_SH, (612, 218))
    screen.blit(text_word_G_SH, (692, 218))
    screen.blit(text_word_A_SH, (772, 218))

    soundboard_type = "marimba"
    pygame.display.update()
    
    if soundboard_type == 'drum kit':
        config_file = 'key_to_wav.txt'

    elif soundboard_type == 'marimba':
        config_file = 'key_to_marimba.txt'

    #config_file = 'key_to_sound_effects.txt'
    mode = "player"
    # may include a different mode so that files will repeat or play more than once, time permitting
    fadeout_time = 50

    if mode == "player":
        repeat = 0

    keys = pygame.key.get_pressed()

    # Read configuration file

    key_sound = {}
    key_file = {}
    config = csv.reader(open(config_file, 'r'), delimiter='`')

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
                    if key == '2':
                        pygame.draw.rect(screen, new_color, two)
                        screen.blit(text_word_C_SH, (142, 58))
                        screen.blit(key_2, (133, 20))
                    if key == '3':
                        pygame.draw.rect(screen, new_color, three)
                        screen.blit(text_word_D_SH, (222, 58))
                        screen.blit(key_3, (213, 20))
                    if key == '5':
                        pygame.draw.rect(screen, new_color, five)
                        screen.blit(text_word_F_SH, (382, 58))
                        screen.blit(key_5, (373, 20))
                    if key == '6':
                        pygame.draw.rect(screen, new_color, six)
                        screen.blit(text_word_G_SH, (462, 58))
                        screen.blit(key_6, (453, 20))
                    if key == '7':
                        pygame.draw.rect(screen, new_color, seven)
                        screen.blit(text_word_A_SH, (542, 58))
                        screen.blit(key_7, (533, 20))
                    if key == '9':
                        pygame.draw.rect(screen, new_color, nine)
                        screen.blit(text_word_C_SH, (702, 58))
                        screen.blit(key_9, (693, 20))
                    if key == '0':
                        pygame.draw.rect(screen, new_color, zero)
                        screen.blit(text_word_D_SH, (782, 58))
                        screen.blit(key_0, (773, 20))

                    if key == 'q':
                        pygame.draw.rect(screen, new_color, q)
                        screen.blit(text_word_C, (122, 138))
                        screen.blit(key_Q, (103, 100))
                    if key == 'w':
                        pygame.draw.rect(screen, new_color, w)
                        screen.blit(text_word_D, (202, 138))
                        screen.blit(key_W, (183, 100))
                    if key == 'e':
                        pygame.draw.rect(screen, new_color, e)
                        screen.blit(text_word_E, (282, 138))
                        screen.blit(key_E, (263, 100))
                    if key == 'r':
                        pygame.draw.rect(screen, new_color, r)
                        screen.blit(text_word_F, (362, 138))
                        screen.blit(key_R, (343, 100))
                    if key == 't':
                        pygame.draw.rect(screen, new_color, t)
                        screen.blit(text_word_G, (442, 138))
                        screen.blit(key_T, (423, 100))
                    if key == 'y':
                        pygame.draw.rect(screen, new_color, y)
                        screen.blit(text_word_A, (522, 138))
                        screen.blit(key_Y, (503, 100))
                    if key == 'u':
                        pygame.draw.rect(screen, new_color, u)
                        screen.blit(text_word_B, (602, 138))
                        screen.blit(key_U, (583, 100))
                    if key == 'i':
                        pygame.draw.rect(screen, new_color, i)
                        screen.blit(text_word_C, (682, 138))
                        screen.blit(key_I, (663, 100))
                    if key == 'o':
                        pygame.draw.rect(screen, new_color, o)
                        screen.blit(text_word_D, (762, 138))
                        screen.blit(key_O, (743, 100))
                    if key == 'p':
                        pygame.draw.rect(screen, new_color, p)
                        screen.blit(text_word_E, (842, 138))
                        screen.blit(key_P, (823, 100))


                    if key == 's':
                        pygame.draw.rect(screen, new_color, s)
                        screen.blit(text_word_A_SH, (212, 218))
                        screen.blit(key_S, (203, 180))
                    if key == 'f':
                        pygame.draw.rect(screen, new_color, f)
                        screen.blit(text_word_C_SH, (372, 218))
                        screen.blit(key_F, (363, 180))
                    if key == 'g':
                        pygame.draw.rect(screen, new_color, g)
                        screen.blit(text_word_D_SH, (452, 218))
                        screen.blit(key_G, (443, 180))
                    if key == 'j':
                        pygame.draw.rect(screen, new_color, j)
                        screen.blit(text_word_F_SH, (612, 218))
                        screen.blit(key_J, (603, 180))
                    if key == 'k':
                        pygame.draw.rect(screen, new_color, k)
                        screen.blit(text_word_G_SH, (692, 218))
                        screen.blit(key_K, (683, 180))
                    if key == 'l':
                        pygame.draw.rect(screen, new_color, l)
                        screen.blit(text_word_A_SH, (772, 218))
                        screen.blit(key_L, (763, 180))

                    if key == 'z':
                        pygame.draw.rect(screen, new_color, z)
                        screen.blit(text_word_A, (182, 298))
                        screen.blit(key_Z, (163, 260))
                    if key == 'x':
                        pygame.draw.rect(screen, new_color, x)
                        screen.blit(text_word_B, (262, 298))
                        screen.blit(key_X, (243, 260))
                    if key == 'c':
                        pygame.draw.rect(screen, new_color, c)
                        screen.blit(text_word_C, (342, 298))
                        screen.blit(key_C, (323, 260))
                    if key == 'v':
                        pygame.draw.rect(screen, new_color, v)
                        screen.blit(text_word_D, (422, 298))
                        screen.blit(key_V, (403, 260))
                    if key == 'b':
                        pygame.draw.rect(screen, new_color, b)
                        screen.blit(text_word_E, (502, 298))
                        screen.blit(key_B, (483, 260))
                    if key == 'n':
                        pygame.draw.rect(screen, new_color, n)
                        screen.blit(text_word_F, (582, 298))
                        screen.blit(key_N, (563, 260))
                    if key == 'm':
                        pygame.draw.rect(screen, new_color, m)
                        screen.blit(text_word_G, (662, 298))
                        screen.blit(key_M, (643, 260))
                    if key == ',':
                        pygame.draw.rect(screen, new_color, comma)
                        screen.blit(text_word_A, (742, 298))
                        screen.blit(key_COMMA, (728, 260))
                    if key == '.':
                        pygame.draw.rect(screen, new_color, period)
                        screen.blit(text_word_B, (822, 298))
                        screen.blit(key_PERIOD, (808, 260))

                    pygame.display.update()
                    events_list.append((time.time(), key_file[key]))


                elif event.type == pygame.KEYUP:
                    if key == '2':
                        pygame.draw.rect(screen, sky_blue, two)
                        screen.blit(text_word_C_SH, (142, 58))
                        screen.blit(key_2, (133, 20))
                    if key == '3':
                        pygame.draw.rect(screen, sky_blue, three)
                        screen.blit(text_word_D_SH, (222, 58))
                        screen.blit(key_3, (213, 20))
                    if key == '5':
                        pygame.draw.rect(screen, sky_blue, five)
                        screen.blit(text_word_F_SH, (382, 58))
                        screen.blit(key_5, (373, 20))
                    if key == '6':
                        pygame.draw.rect(screen, sky_blue, six)
                        screen.blit(text_word_G_SH, (462, 58))
                        screen.blit(key_6, (453, 20))
                    if key == '7':
                        pygame.draw.rect(screen, sky_blue, seven)
                        screen.blit(text_word_A_SH, (542, 58))
                        screen.blit(key_7, (533, 20))
                    if key == '9':
                        pygame.draw.rect(screen, sky_blue, nine)
                        screen.blit(text_word_C_SH, (702, 58))
                        screen.blit(key_9, (693, 20))
                    if key == '0':
                        pygame.draw.rect(screen, sky_blue, zero)
                        screen.blit(text_word_D_SH, (782, 58))
                        screen.blit(key_0, (773, 20))

                    if key == 'q':
                        pygame.draw.rect(screen, sky_blue, q)
                        screen.blit(text_word_C, (122, 138))
                        screen.blit(key_Q, (103, 100))
                    if key == 'w':
                        pygame.draw.rect(screen, sky_blue, w)
                        screen.blit(text_word_D, (202, 138))
                        screen.blit(key_W, (183, 100))
                    if key == 'e':
                        pygame.draw.rect(screen, sky_blue, e)
                        screen.blit(text_word_E, (282, 138))
                        screen.blit(key_E, (263, 100))
                    if key == 'r':
                        pygame.draw.rect(screen, sky_blue, r)
                        screen.blit(text_word_F, (362, 138))
                        screen.blit(key_R, (343, 100))
                    if key == 't':
                        pygame.draw.rect(screen, sky_blue, t)
                        screen.blit(text_word_G, (442, 138))
                        screen.blit(key_T, (423, 100))
                    if key == 'y':
                        pygame.draw.rect(screen, sky_blue, y)
                        screen.blit(text_word_A, (522, 138))
                        screen.blit(key_Y, (503, 100))
                    if key == 'u':
                        pygame.draw.rect(screen, sky_blue, u)
                        screen.blit(text_word_B, (602, 138))
                        screen.blit(key_U, (583, 100))
                    if key == 'i':
                        pygame.draw.rect(screen, sky_blue, i)
                        screen.blit(text_word_C, (682, 138))
                        screen.blit(key_I, (663, 100))
                    if key == 'o':
                        pygame.draw.rect(screen, sky_blue, o)
                        screen.blit(text_word_D, (762, 138))
                        screen.blit(key_O, (743, 100))
                    if key == 'p':
                        pygame.draw.rect(screen, sky_blue, p)
                        screen.blit(text_word_E, (842, 138))
                        screen.blit(key_P, (823, 100))


                    if key == 's':
                        pygame.draw.rect(screen, sky_blue, s)
                        screen.blit(text_word_A_SH, (212, 218))
                        screen.blit(key_S, (203, 180))
                    if key == 'f':
                        pygame.draw.rect(screen, sky_blue, f)
                        screen.blit(text_word_C_SH, (372, 218))
                        screen.blit(key_F, (363, 180))
                    if key == 'g':
                        pygame.draw.rect(screen, sky_blue, g)
                        screen.blit(text_word_D_SH, (452, 218))
                        screen.blit(key_G, (443, 180))
                    if key == 'j':
                        pygame.draw.rect(screen, sky_blue, j)
                        screen.blit(text_word_F_SH, (612, 218))
                        screen.blit(key_J, (603, 180))
                    if key == 'k':
                        pygame.draw.rect(screen, sky_blue, k)
                        screen.blit(text_word_G_SH, (692, 218))
                        screen.blit(key_K, (683, 180))
                    if key == 'l':
                        pygame.draw.rect(screen, sky_blue, l)
                        screen.blit(text_word_A_SH, (772, 218))
                        screen.blit(key_L, (763, 180))

                    if key == 'z':
                        pygame.draw.rect(screen, sky_blue, z)
                        screen.blit(text_word_A, (182, 298))
                        screen.blit(key_Z, (163, 260))
                    if key == 'x':
                        pygame.draw.rect(screen, sky_blue, x)
                        screen.blit(text_word_B, (262, 298))
                        screen.blit(key_X, (243, 260))
                    if key == 'c':
                        pygame.draw.rect(screen, sky_blue, c)
                        screen.blit(text_word_C, (342, 298))
                        screen.blit(key_C, (323, 260))
                    if key == 'v':
                        pygame.draw.rect(screen, sky_blue, v)
                        screen.blit(text_word_D, (422, 298))
                        screen.blit(key_V, (403, 260))
                    if key == 'b':
                        pygame.draw.rect(screen, sky_blue, b)
                        screen.blit(text_word_E, (502, 298))
                        screen.blit(key_B, (483, 260))
                    if key == 'n':
                        pygame.draw.rect(screen, sky_blue, n)
                        screen.blit(text_word_F, (582, 298))
                        screen.blit(key_N, (563, 260))
                    if key == 'm':
                        pygame.draw.rect(screen, sky_blue, m)
                        screen.blit(text_word_G, (662, 298))
                        screen.blit(key_M, (643, 260))
                    if key == ',':
                        pygame.draw.rect(screen, sky_blue, comma)
                        screen.blit(text_word_A, (742, 298))
                        screen.blit(key_COMMA, (728, 260))
                    if key == '.':
                        pygame.draw.rect(screen, sky_blue, period)
                        screen.blit(text_word_B, (822, 298))
                        screen.blit(key_PERIOD, (808, 260))

                    pygame.display.update()

            elif event.key == pygame.K_ESCAPE:
                # must hit the escape key to exit the program
                break

        elif event.type == pygame.QUIT:
            # allows one to exit the program by clicking the x in the window
            break
