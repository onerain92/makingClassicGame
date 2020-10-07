import pygame
import random

###################################################################################
# 기본 초기화( 반드시 해야 하는 것들 )
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥피하기")  # 게임 이름

# FPS
clock = pygame.time.Clock()
###################################################################################

# 1. 사용자 게임 초기화( 배경 화면, 게임 이미지, 좌표, 폰트 등 )

# 배경 만들기
background = pygame.image.load("./background.png")

# 스프라이트( 캐릭터 ) 만들기
character = pygame.image.load("./character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_position = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 ( 가로 )
character_y_position = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치( 세로 )

# 이동 위치
to_x = 0

# 이동 속도
character_speed = 0.5

# 똥 만들기
dung = pygame.image.load("./enemy.png")
dung_size = dung.get_rect().size # 이미지 크기를 구해옴
dung_width = dung_size[0] # 캐릭터의 가로 크기
dung_height = dung_size[1] # 캐릭터의 세로 크기
dung_x_position = random.randint(0, screen_width - dung_width)
dung_y_position = 0
dung_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성(폰트, 크기)

# 이벤트 루프
running = True  # 게임이 진행중인지 확인
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리( 키보드, 마우스 등 )
    for event in pygame.event.get():  # 이벤트가 발생했는지?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생했는지?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_position += to_x * dt

    # 가로 경계값 처리
    if character_x_position < 0:
        character_x_position = 0
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width

    dung_y_position += dung_speed

    if dung_y_position > screen_height:
        dung_y_position = 0
        dung_x_position = random.randint(0, screen_width - dung_width)

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_position
    character_rect.top = character_y_position

    dung_rect = dung.get_rect()
    dung_rect.left = dung_x_position
    dung_rect.top = dung_y_position

    # 충돌 체크
    if character_rect.colliderect(dung_rect):
        print("충돌했어요!")
        running = False

    # screen.fill((0, 0, 255)) # 이미지 대신 rgb 값으로 배경 채우기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_position, character_y_position))
    screen.blit(dung, (dung_x_position, dung_y_position))

    pygame.display.update() # 게임 화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기(ms)

# pygame 종료
pygame.quit()
