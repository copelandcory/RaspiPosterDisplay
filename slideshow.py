import pygame
import csv

imgloc = []

with open('C:/Users/ccopeland/Desktop/AggregatedDEM/imagelocation.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        imgloc.append(row[1])


imgloc = imgloc[1:88]
year = 0
defsurf = pygame.image.load(imgloc[year])
pygame.init()
screen_width=480
screen_height=480
screen=pygame.display.set_mode([screen_width,screen_height])

screen.blit(defsurf, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and year == 0:
                print(year)
                pygame.display.update()
                screen.blit(pygame.image.load(imgloc[year]), (0, 0))
            if event.key == pygame.K_LEFT and year > 0:
                year = year-1
                print(year)
                pygame.display.update()
                screen.blit(pygame.image.load(imgloc[year]), (0, 0))
            if event.key == pygame.K_RIGHT and year == 86:
                print(year)
                pygame.display.update()
                screen.blit(pygame.image.load(imgloc[year]), (0, 0))
            if event.key == pygame.K_RIGHT and year < 86:
                year = year+1
                print(year)
                pygame.display.update()
                screen.blit(pygame.image.load(imgloc[year]), (0, 0))


