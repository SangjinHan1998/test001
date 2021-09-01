import pygame

pygame.init()   # 초기화. 무조건 필요

# 화면 크기 설정

screen_width = 480  # 가로 크기
screen_height = 640# 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 가로 세로창 이렇게 정의함

# 화면 타이틀 설정 
pygame.display.set_caption("M2Game")    # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\한상진\\Documents\\VS CODE\\SUMMIT\\fastpython\\code01\\pygame_basic\\background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\한상진\\Documents\\VS CODE\\SUMMIT\\fastpython\\code01\\pygame_basic\\s001.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해온다. 
character_width = character_size[0]         # 캐릭터의 가로크기
character_height = character_size[1]        # 캐릭터의 세로크기 
character_x_pos = screen_width / 2 - (character_width / 2)         # 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height            # 화면 세로 크기 가장 아래에 해당하는 위치 

# 이동할 좌표
to_x = 0
to_y = 0
# 이동 속도
character_speed = 0.45

# 적 캐릭터
enemy = pygame.image.load("C:\\Users\\한상진\\Documents\\VS CODE\\SUMMIT\\fastpython\\code01\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해온다. 
enemy_width = enemy_size[0]         # 캐릭터의 가로크기
enemy_height = enemy_size[1]        # 캐릭터의 세로크기 
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)         # 화면 가로의 절반 크기에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)            # 화면 세로 크기 가장 아래에 해당하는 위치 

# 폰트 정의 
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성.  (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()   # 시작 tick을 받아옴


# 이벤트 루프
running = True  # 게임이 진행중인가?? 
while running: 
    dt = clock.tick(60)                 # 게임화면의 초당 프레임 설정

# 캐릭터가 100만큼 이동해야하고 
# 10fps : 1초에 10 번 동작      10만큼 10번
# 20fps : 1초에 20 번 동작      5만큼 20번 

    print("fps : " + str(clock.get_fps()))  # 프레임 확인 / 게임 설정값에 따라 바뀜(30에가까이)

    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가? 
            running = False             # 게임이 진행중이 아니다. 

        if event.type == pygame.KEYDOWN:    # 키를 눌러졌는지 확인 
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로 이동 
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 이동 
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위쪽으로 이동
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래쪽으로 이동
                to_y += character_speed

        if event.type == pygame.KEYUP:       # 방향키를 떼면 멈춘다. 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  
                to_x = 0
            elif event.key ==  pygame.K_UP or event.key == pygame.K_DOWN: 
                to_y = 0
            
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt    # 캐릭터의 위치를 나타낸다.

    # 가로 경계값 처리
    if character_x_pos < 0: 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: 
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height 

    # 충돌 처리
    character_rect = character.get_rect() 
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos    # character 의 정보는  rect 로 업데이트된다. 

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos  
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):  # colliderect는 게임 충돌 감지
        print("충돌했어요.")
        running = False

    screen.blit(background, (0, 0))     # 배경 그리기 맨 왼쪽 위에 위치
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))      # 적 그리기 

    # 타이머 집어 넣기
    # 경과 시간 계산 
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 현재 시간 - 시작시간
    # 경과 시간(ms)을 1000으로 나눠 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))    # 총 시간 - 흘러간시간
    # int는 초단위로만 표현하기위해
    # 출력할 글자 , True, 글자 색상
    screen.blit(timer ,(10, 10))    #타이머 적을 위치

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0: # 시간이 0초 이하이면 
        print("타임 아웃")             #  터미널에 기록 
        running = False

    pygame.display.update()             # 게임화면 다시 그리기 
# 잠시 대기
pygame.time.delay(2000) # 2초 대기 (ms)


# pygame 종료
pygame.quit()