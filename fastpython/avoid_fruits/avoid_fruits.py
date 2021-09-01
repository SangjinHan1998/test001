import random
import pygame       # 게임에 어느정도 필요한 껍데기
################################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()   # 초기화. 무조건 필요

# 화면 크기 설정

screen_width = 640  # 가로 크기
screen_height = 480# 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 가로 세로창 이렇게 정의함

# 화면 타이틀 설정 
pygame.display.set_caption("Avoid fruits")    # 게임 이름

# FPS
clock = pygame.time.Clock()
################################################################  여기까지는 불변

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경
background = pygame.image.load("C:\\Users\\한상진\\Documents\\VS CODE\\SUMMIT\\fastpython\\code01\\avoid_fruits\\market1.png")

# 나의 캐릭터.
character = pygame.image.load("C:\\Users\\한상진\\Documents\\VS CODE\\SUMMIT\\fastpython\\code01\\avoid_fruits\\main.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해온다. 
character_width = character_size[0]         # 캐릭터의 가로크기
character_height = character_size[1]        # 캐릭터의 세로크기 
character_x_pos = (screen_width / 2) - (character_width / 2)         # 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height   

# 이동할 좌표
to_x = 0
character_speed = 10
# 이동 속도 
character_speed = 10

# 적 캐릭터
fruits = pygame.image.load("C:\\Users\\한상진\\Documents\\VS CODE\\SUMMIT\\fastpython\\code01\\avoid_fruits\\peach.png")
fruits_size = fruits.get_rect().size  # 이미지의 크기를 구해온다. 
fruits_width = fruits_size[0]         # 캐릭터의 가로크기
fruits_height = fruits_size[1]        # 캐릭터의 세로크기 
fruits_x_pos = random.randint(0, screen_width - fruits_width)   # 0부터 가로 이동범위 랜덤값
fruits_y_pos = 0
fruits_speed = 10



running = True  # 게임이 진행중인가?? 
while running: 
    dt = clock.tick(30)                 # 게임화면의 초당 프레임 설정

    print("fps : " + str(clock.get_fps()))  # 프레임 확인 / 게임 설정값에 따라 바뀜(30에가까이)

    # 2. 이벤트 처리(키보드, 마우스 등) 
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
            running = False             # 게임이 진행중이 아니다. 

        if event.type == pygame.KEYDOWN:    # 키를 눌러졌는지 확인 
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로 이동 
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 이동 
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            

    # 3.  게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0 
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    fruits_y_pos += fruits_speed

    if fruits_y_pos > screen_height:
        fruits_y_pos = 0
        fruits_x_pos = random.randint(0, screen_width - fruits_width)
    # 4.  충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    fruits_rect = fruits.get_rect()
    fruits_rect.left = fruits_x_pos
    fruits_rect.top = fruits_y_pos


    if character_rect.colliderect(fruits_rect):     #   colliderect 는 게임충돌감지
        print("He is dead. :(")
        running = False
  
    # 5.  화면에 그리기 
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(fruits, (fruits_x_pos, fruits_y_pos))

    pygame.display.update()             # 게임화면 다시 그리기 

pygame.quit()