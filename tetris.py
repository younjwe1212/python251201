#cmd
#pip install pygame
# 간단한 테트리스 (pygame 필요)

import pygame
import random
import sys

pygame.init()
FPS = 60
clock = pygame.time.Clock()

# 화면 설정
CELL_SIZE = 30
COLS = 10
ROWS = 20
W = CELL_SIZE * COLS
H = CELL_SIZE * ROWS
SIDE_PANEL = 200
SCREEN = pygame.display.set_mode((W + SIDE_PANEL, H))
pygame.display.set_caption("Tetris - 간단 구현")

# 색상
COLORS = [
    (0, 0, 0),        # 0 empty
    (0, 255, 255),    # I
    (0, 0, 255),      # J
    (255, 165, 0),    # L
    (255, 255, 0),    # O
    (0, 255, 0),      # S
    (128, 0, 128),    # T
    (255, 0, 0),      # Z
    (128, 128, 128)   # boundary / debug
]

# 테트리스 블록 모양 (4x4 matrix 형태)
SHAPES = [
    # I
    [[0,0,0,0],
     [1,1,1,1],
     [0,0,0,0],
     [0,0,0,0]],
    # J
    [[2,0,0],
     [2,2,2],
     [0,0,0]],
    # L
    [[0,0,3],
     [3,3,3],
     [0,0,0]],
    # O
    [[4,4],
     [4,4]],
    # S
    [[0,5,5],
     [5,5,0],
     [0,0,0]],
    # T
    [[0,6,0],
     [6,6,6],
     [0,0,0]],
    # Z
    [[7,7,0],
     [0,7,7],
     [0,0,0]]
]

# 보드 초기화
def create_board():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]

# 회전 (시계 방향)
def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

# 충돌 검사
def check_collision(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                px = x + off_x
                py = y + off_y
                if px < 0 or px >= COLS or py < 0 or py >= ROWS:
                    return True
                if board[py][px]:
                    return True
    return False

# 보드에 고정
def place_shape(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = cell

# 줄 삭제
def clear_lines(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    cleared = ROWS - len(new_board)
    for _ in range(cleared):
        new_board.insert(0, [0 for _ in range(COLS)])
    return new_board, cleared

# 랜덤 블록 생성
def new_piece():
    idx = random.randrange(len(SHAPES))
    shape = SHAPES[idx]
    return [row[:] for row in shape], idx+1

# 그리기
FONT = pygame.font.SysFont("malgun gothic", 18)
BIG_FONT = pygame.font.SysFont("malgun gothic", 36)

def draw_grid(surface, board, current_shape=None, offset=(0,0)):
    surface.fill((10,10,10))
    # 고정된 블록
    for y in range(ROWS):
        for x in range(COLS):
            val = board[y][x]
            color = COLORS[val]
            pygame.draw.rect(surface, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(surface, (30,30,30), (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    # 현재 블록
    if current_shape:
        off_x, off_y = offset
        for y, row in enumerate(current_shape):
            for x, cell in enumerate(row):
                if cell:
                    px = (x+off_x)*CELL_SIZE
                    py = (y+off_y)*CELL_SIZE
                    pygame.draw.rect(surface, COLORS[cell], (px, py, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(surface, (60,60,60), (px, py, CELL_SIZE, CELL_SIZE), 1)

def draw_side(surface, score, next_shape):
    xstart = W + 20
    surface.fill((20,20,20), (W,0,SIDE_PANEL,H))
    label = FONT.render(f"Score: {score}", True, (255,255,255))
    surface.blit(label, (xstart, 20))
    label2 = FONT.render("Next:", True, (255,255,255))
    surface.blit(label2, (xstart, 60))
    # next shape draw
    if next_shape:
        for y, row in enumerate(next_shape):
            for x, cell in enumerate(row):
                if cell:
                    rx = xstart + x*CELL_SIZE
                    ry = 90 + y*CELL_SIZE
                    pygame.draw.rect(surface, COLORS[cell], (rx, ry, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(surface, (60,60,60), (rx, ry, CELL_SIZE, CELL_SIZE), 1)

def game_over_screen(surface, score):
    overlay = pygame.Surface((W, H))
    overlay.set_alpha(180)
    overlay.fill((0,0,0))
    surface.blit(overlay, (0,0))
    txt = BIG_FONT.render("GAME OVER", True, (255,0,0))
    sc = FONT.render(f"Score: {score}", True, (255,255,255))
    surface.blit(txt, (W//2 - txt.get_width()//2, H//2 - 50))
    surface.blit(sc, (W//2 - sc.get_width()//2, H//2 + 10))
    pygame.display.flip()

def main():
    board = create_board()
    shape, shape_id = new_piece()
    next_shape, next_id = new_piece()
    pos_x = COLS//2 - len(shape[0])//2
    pos_y = 0
    fall_time = 0
    fall_speed = 0.5  # 초 단위
    score = 0
    level = 1
    lines_cleared_total = 0
    running = True
    paused = False
    last_move_down = pygame.time.get_ticks()
    soft_drop = False

    while running:
        dt = clock.tick(FPS) / 1000.0
        fall_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    paused = not paused
                if not paused:
                    if event.key == pygame.K_LEFT:
                        if not check_collision(board, shape, (pos_x-1, pos_y)):
                            pos_x -= 1
                    elif event.key == pygame.K_RIGHT:
                        if not check_collision(board, shape, (pos_x+1, pos_y)):
                            pos_x += 1
                    elif event.key == pygame.K_DOWN:
                        # soft drop
                        if not check_collision(board, shape, (pos_x, pos_y+1)):
                            pos_y += 1
                            score += 1
                    elif event.key == pygame.K_UP:
                        # rotate with wall-kick simple
                        new_shape = rotate(shape)
                        if not check_collision(board, new_shape, (pos_x, pos_y)):
                            shape = new_shape
                        else:
                            # try small kicks
                            if not check_collision(board, new_shape, (pos_x-1, pos_y)):
                                pos_x -= 1
                                shape = new_shape
                            elif not check_collision(board, new_shape, (pos_x+1, pos_y)):
                                pos_x += 1
                                shape = new_shape
                    elif event.key == pygame.K_SPACE:
                        # hard drop
                        while not check_collision(board, shape, (pos_x, pos_y+1)):
                            pos_y += 1
                            score += 2
                        # lock immediately
                        place_shape(board, shape, (pos_x, pos_y))
                        board, cleared = clear_lines(board)
                        if cleared:
                            lines_cleared_total += cleared
                            score += (cleared * 100)
                        # next piece
                        shape, shape_id = next_shape, next_id
                        next_shape, next_id = new_piece()
                        pos_x = COLS//2 - len(shape[0])//2
                        pos_y = 0

        if not paused:
            # 자동 낙하 (soft_drop 중이면 더 빠르게)
            current_speed = fall_speed if not soft_drop else max(0.02, fall_speed / 10)
            if fall_time >= current_speed:
                fall_time = 0
                if not check_collision(board, shape, (pos_x, pos_y+1)):
                    pos_y += 1
                    if soft_drop:
                        score += 1
                else:
                    # lock piece
                    place_shape(board, shape, (pos_x, pos_y))
                    board, cleared = clear_lines(board)
                    if cleared:
                        lines_cleared_total += cleared
                        score += (cleared * 100)
                        # 속도 올리기
                        level = 1 + lines_cleared_total // 10
                        fall_speed = max(0.05, 0.5 - (level-1)*0.03)
                    # spawn next
                    shape, shape_id = next_shape, next_id
                    next_shape, next_id = new_piece()
                    pos_x = COLS//2 - len(shape[0])//2
                    pos_y = 0
                    soft_drop = False
                    # 즉시 충돌하면 게임 오버
                    if check_collision(board, shape, (pos_x, pos_y)):
                        game_over_screen(SCREEN, score)
                        pygame.time.wait(1500)
                        running = False

        # 그리기
        draw_grid(SCREEN, board, shape, (pos_x, pos_y))
        draw_side(SCREEN, score, next_shape)
        if paused:
            ptext = BIG_FONT.render("PAUSED", True, (255,255,0))
            SCREEN.blit(ptext, (W//2 - ptext.get_width()//2, H//2 - 20))
        pygame.display.flip()

    # 게임 재시작 묻기
    pygame.quit()

if __name__ == "__main__":
    main()