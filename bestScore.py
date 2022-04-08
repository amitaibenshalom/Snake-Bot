
import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
pink = (255, 176, 176)
purple = (164, 2, 172)

dis_width = 800
dis_height = 500

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake AI Best Score')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15000

ok = False

font_style = pygame.font.SysFont("bahnschrift",25)
score_font = pygame.font.SysFont("bahnschrift", 20)


def getScore(score):
    value = score_font.render("score: " + str(score), True, yellow)
    dis.blit(value, [10, 0])

def getBestScore(best):
    value = score_font.render("best: " + str(best), True, yellow)
    dis.blit(value, [10, 20])

def getAverage(average):
    value = score_font.render("average: " + str(average), True, yellow)
    dis.blit(value, [10, 60])

def getGames(count):
    value = score_font.render("games: " + str(count), True, yellow)
    dis.blit(value, [10, 40])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def get_min_index(a, b, c):
   t = min(a, b, c)
   if t == a:
       return 1
   elif t == b:
       return 2
   else: return 3


def isDeath(x, y, temp_list):
    temp = []
    temp.append(x)
    temp.append(y)
    for i in temp_list:
        if i == temp:
            return True
    return False


def getDistance(x1,y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)

def gameLoop(best,count, sum):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = snake_block
    y1_change = 0

    snake_List = []
    snake_List_temp = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            # message("Snake Lost! Press C-Play Again or Q-Quit", red)
            getScore(Length_of_snake - 1)
            if Length_of_snake - 1 > best:
                best = Length_of_snake - 1
            getBestScore(best)
            getAverage((sum+Length_of_snake-1)/count)
            getGames(count)
            pygame.display.update()
            gameLoop(best, count+1, sum+Length_of_snake-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        if x1_change == snake_block and y1_change == 0:
            index = 0

            d1 = not isDeath(x1+snake_block, y1, snake_List)
            d2 = not isDeath(x1, y1 + snake_block, snake_List)
            d3 = not isDeath(x1, y1 - snake_block, snake_List)

            if d1 and d2 and d3:
                index = get_min_index(getDistance(x1 + snake_block, y1, foodx, foody),
                                      getDistance(x1, y1 + snake_block, foodx, foody),
                                      getDistance(x1, y1 - snake_block, foodx, foody))
            if d1 and d2 and not d3:
                index = get_min_index(getDistance(x1 + snake_block, y1, foodx, foody),
                                      getDistance(x1, y1 + snake_block, foodx, foody), 999999)
            if d1 and (not d2) and d3:
                index = get_min_index(getDistance(x1 + snake_block, y1, foodx, foody), 999999,
                                      getDistance(x1, y1 - snake_block, foodx, foody))
            if (not d1) and d2 and d3:
                index = get_min_index(999999, getDistance(x1, y1 + snake_block, foodx, foody),
                                      getDistance(x1, y1 - snake_block, foodx, foody))
            if d1 and (not d2) and (not d3):
                index = 1
            if (not d1) and d2 and (not d3):
                index = 2
            if (not d1) and (not d2) and d3:
                index = 3

            if index == 2:
                y1_change = snake_block
                x1_change = 0
            elif index == 3:
                y1_change = -snake_block
                x1_change = 0

        if x1_change == -snake_block and y1_change == 0:
            index = 0
            d1 = not isDeath(x1 - snake_block, y1, snake_List)
            d2 = not isDeath(x1, y1 + snake_block, snake_List)
            d3 = not isDeath(x1, y1 - snake_block, snake_List)

            if d1 and d2 and d3:
                index = get_min_index(getDistance(x1 - snake_block, y1, foodx, foody),
                                      getDistance(x1, y1 + snake_block, foodx, foody),
                                      getDistance(x1, y1 - snake_block, foodx, foody))
            if d1 and d2 and not d3:
                index = get_min_index(getDistance(x1 - snake_block, y1, foodx, foody),
                                      getDistance(x1, y1 + snake_block, foodx, foody), 999999)
            if d1 and (not d2) and d3:
                index = get_min_index(getDistance(x1 - snake_block, y1, foodx, foody), 999999,
                                      getDistance(x1, y1 - snake_block, foodx, foody))
            if (not d1) and d2 and d3:
                index = get_min_index(999999, getDistance(x1, y1 + snake_block, foodx, foody),
                                      getDistance(x1, y1 - snake_block, foodx, foody))
            if d1 and (not d2) and (not d3):
                index = 1
            if (not d1) and d2 and (not d3):
                index = 2
            if (not d1) and (not d2) and d3:
                index = 3

            if index == 2:
                y1_change = snake_block
                x1_change = 0
            elif index == 3:
                y1_change = -snake_block
                x1_change = 0

        if x1_change == 0 and y1_change == snake_block:
            index = 0
            d1 = not isDeath(x1 + snake_block, y1, snake_List)
            d2 = not isDeath(x1 - snake_block, y1, snake_List)
            d3 = not isDeath(x1, y1 + snake_block, snake_List)

            if d1 and d2 and d3:
                index = get_min_index(getDistance(x1 + snake_block, y1, foodx, foody),
                                      getDistance(x1 - snake_block, y1, foodx, foody),
                                      getDistance(x1, y1 + snake_block, foodx, foody))
            if d1 and d2 and not d3:
                index = get_min_index(getDistance(x1 + snake_block, y1, foodx, foody),
                                      getDistance(x1 - snake_block, y1, foodx, foody), 999999)
            if d1 and (not d2) and d3:
                index = get_min_index(getDistance(x1 + snake_block, y1, foodx, foody), 999999,
                                      getDistance(x1, y1 + snake_block, foodx, foody))
            if (not d1) and d2 and d3:
                index = get_min_index(999999, getDistance(x1 - snake_block, y1, foodx, foody),
                                      getDistance(x1, y1 + snake_block, foodx, foody))
            if d1 and (not d2) and (not d3):
                index = 1
            if (not d1) and d2 and (not d3):
                index = 2
            if (not d1) and (not d2) and d3:
                index = 3

            if index == 1:
                x1_change = snake_block
                y1_change = 0
            elif index == 2:
                x1_change = -snake_block
                y1_change = 0

        if x1_change == 0 and y1_change == -snake_block:
            index = 0
            d1 = not isDeath(x1 + snake_block, y1, snake_List)
            d2 = not isDeath(x1 - snake_block, y1, snake_List)
            d3 = not isDeath(x1, y1 - snake_block, snake_List)

            if d1 and d2 and d3:
                index = get_min_index(getDistance(x1 + snake_block, y1, foodx, foody),
                                      getDistance(x1 - snake_block, y1, foodx, foody),
                                      getDistance(x1, y1 - snake_block, foodx, foody))
            if d1 and d2 and not d3:
                index = get_min_index(getDistance(x1 + snake_block, y1, foodx, foody),
                                      getDistance(x1 - snake_block, y1, foodx, foody), 999999)
            if d1 and (not d2) and d3:
                index = get_min_index(getDistance(x1 + snake_block, y1, foodx, foody), 999999,
                                      getDistance(x1, y1 - snake_block, foodx, foody))
            if (not d1) and d2 and d3:
                index = get_min_index(999999, getDistance(x1 - snake_block, y1, foodx, foody),
                                      getDistance(x1, y1 - snake_block, foodx, foody))
            if d1 and (not d2) and (not d3):
                index = 1
            if (not d1) and d2 and (not d3):
                index = 2
            if (not d1) and (not d2) and d3:
                index = 3

            if index == 1:
                x1_change = snake_block
                y1_change = 0
            elif index == 2:
                x1_change = -snake_block
                y1_change = 0

        if (x1 >= dis_width) or (x1 < 0) or (y1 >= dis_height) or (y1 < 0):
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        snake_List_temp.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            del snake_List_temp[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        getScore(Length_of_snake - 1)
        getGames(count)
        getBestScore(max(best, Length_of_snake-1))
        if (count != 1):
            getAverage(sum/(count-1))
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameLoop(0,1,0)