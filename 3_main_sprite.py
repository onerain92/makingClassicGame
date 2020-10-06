import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("./background.png")

# 스프라이트( 캐릭터 ) 불러오기
character = pygame.image.load("./character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_position = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 ( 가로 )
character_y_position = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치( 세로 )

# 이벤트 루프
running = True  # 게임이 진행중인지 확인

while running:
    for event in pygame.event.get():  # 이벤트가 발생했는지?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생했는지?
            running = False  # 게임이 진행중이 아님

    # screen.fill((0, 0, 255)) # 이미지 대신 rgb 값으로 배경 채우기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_position, character_y_position))
    pygame.display.update() # 게임 화면을 다시 그리기!

# pygame 종료
pygame.quit()
