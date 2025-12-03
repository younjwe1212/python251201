def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def draw_text(surface, text, position, font, color):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def reset_game_state():
    return {
        'score': 0,
        'lives': 3,
        'level': 1
    }