import pygame
import csv

imgloc = []

with open('data/imagelocation.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        imgloc.append(row[1])
        


imgloc1 = []

with open('data/Subimagelocation.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        imgloc1.append(row[1])


imgloc = imgloc[1:88]
imgloc1 = imgloc1[1:88]
imgarray = [imgloc, imgloc1]
year = 0
defsurf = pygame.image.load(imgloc[year])
pygame.init()
screen_width=480
screen_height=480
screen=pygame.display.set_mode([screen_width,screen_height])
arraylength = len(imgarray)-1

imgSelect = 0

screen.blit(defsurf, (0, 0))
pygame.display.update()
pygame.key.set_repeat(1,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if imgSelect < arraylength:
                    imgSelect = imgSelect + 1
                    screen.blit(pygame.image.load(imgarray[1][year]), (0, 0))
                    pygame.display.update()
                elif imgSelect == arraylength:
                    imgSelect = 0
                    screen.blit(pygame.image.load(imgarray[0][year]), (0, 0))
                    pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and year == 0:
                screen.blit(pygame.image.load(imgarray[imgSelect][year]), (0, 0))
                pygame.display.update()
            if event.key == pygame.K_LEFT and year > 0:
                year = year-1
                screen.blit(pygame.image.load(imgarray[imgSelect][year]), (0, 0))
                pygame.display.update()
            if event.key == pygame.K_RIGHT and year == 86:
                screen.blit(pygame.image.load(imgarray[imgSelect][year]), (0, 0))
                pygame.display.update()
            if event.key == pygame.K_RIGHT and year < 86:
                year = year+1
                screen.blit(pygame.image.load(imgarray[imgSelect][year]), (0, 0))
                pygame.display.update()



