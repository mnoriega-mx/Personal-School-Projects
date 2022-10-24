import pygame
import random
import os
from QuestionBank import get_question

pygame.font.init()

# Fonts
QUESTION_FONT = pygame.font.SysFont('comicsans', 45)
WORD_QUESTION_FONT = pygame.font.SysFont('comicsans', 35)
TRY_AGAIN_FONT = pygame.font.SysFont('comicsans', 35)
SCORE_FONT = pygame.font.SysFont('comicsans', 35)
OPTION_FONT = pygame.font.SysFont('comicsans', 40)
DIRECTIONS_FONT = pygame.font.SysFont('comicsans', 30)

# Screen
WIDTH, HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Math Jump')

# Background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets','BACKGROUND.png')), (WIDTH,HEIGHT))

# Character
CHARACTER_WIDTH, CHARACTER_HEIGHT = 60, 60
CHARACTER = pygame.transform.scale(pygame.image.load(os.path.join('Assets','CHARACTER.png')), (CHARACTER_WIDTH,CHARACTER_HEIGHT))
Y_SPEED = 4
X_SPEED = 2

# Colors
BROWN = (58,29,0)
WHITE = (255,255,255)

# Platforms
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100,15
PLATFORM_SPEED = 5

# Events
INCORRECT_PLATFORM_RIGHT = pygame.USEREVENT+1
CORRECT_PLATFORM_LEFT = pygame.USEREVENT+2
INCORRECT_PLATFORM_LEFT = pygame.USEREVENT+3
CORRECT_PLATFORM_RIGHT = pygame.USEREVENT+4

# Text
GAME_OVER = 'Game Over'
TRY_AGAIN = 'Click SPACE BAR to try again'
HOORAY = 'HOORAY!!!'
GAME_COMPLETED = 'You have completed the game, well done!'
DIRECTIONS = '''Click "a" to move left                             Click "d" to move right'''
DIRECTIONS_2 = '''Click "SPACE" to reveal next question'''


def draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct):
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(CHARACTER, (character.x, character.y))

    if len(str(question)) > 15:
        question_text = WORD_QUESTION_FONT.render(question, 1, WHITE)
    else:
        question_text = QUESTION_FONT.render(question, 1, WHITE)

    current_score_text = SCORE_FONT.render('Score: '+ str(current_score), 1, WHITE)
    goal_text = SCORE_FONT.render('Goal: 30', 1, WHITE)
    c_ans_text = OPTION_FONT.render(str(c_ans), 1, WHITE)
    i_ans_text = OPTION_FONT.render(str(i_ans), 1, WHITE)
    directions_text = DIRECTIONS_FONT.render(DIRECTIONS, 1, WHITE)
    directions_text_2 = DIRECTIONS_FONT.render(DIRECTIONS_2, 1, WHITE)

    SCREEN.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, 10))
    SCREEN.blit(current_score_text, (20, 10))
    SCREEN.blit(goal_text, (20, 45))
    SCREEN.blit(directions_text, (20, HEIGHT - 45))
    SCREEN.blit(directions_text_2, (WIDTH // 2 - directions_text_2.get_width() // 2, HEIGHT - 80))

    if correct_platform == 1:
        SCREEN.blit(c_ans_text, (290 - c_ans_text.get_width()//2, 210))
        SCREEN.blit(i_ans_text, (600 - i_ans_text.get_width()//2, 210))
    elif correct_platform == 2:
        SCREEN.blit(c_ans_text, (600 - c_ans_text.get_width()//2, 210))
        SCREEN.blit(i_ans_text, (290 - i_ans_text.get_width()//2, 210))


    pygame.draw.rect(SCREEN, BROWN, left_platform)
    pygame.draw.rect(SCREEN, BROWN, right_platform)

    if level_passed:
        if current_correct == 1:
                pygame.draw.rect(SCREEN, BROWN, low_left_platform)
        elif current_correct == 2:
                pygame.draw.rect(SCREEN, BROWN, low_right_platform)

    pygame.display.update()


def character_to_left_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct):

    while character.x - CHARACTER_WIDTH//4 > 240 or character.y + CHARACTER_HEIGHT > 210:
        if character.y + CHARACTER_HEIGHT > 210:
            character.y -= Y_SPEED
        if character.x - CHARACTER_WIDTH//4 > 240:
            character.x -= X_SPEED
        draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)

    if character.colliderect(left_platform):
        if correct_platform == 1:
            pygame.event.post(pygame.event.Event(CORRECT_PLATFORM_LEFT))
        elif correct_platform == 2:
            pygame.event.post(pygame.event.Event(INCORRECT_PLATFORM_LEFT))


def character_to_right_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct):

    while character.x - CHARACTER_WIDTH//4 < 550 or character.y + CHARACTER_HEIGHT > 210:
        if character.y + CHARACTER_HEIGHT > 210:
            character.y -= Y_SPEED
        if character.x - CHARACTER_WIDTH//4 < 550:
            character.x += X_SPEED
        draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
        
        if character.colliderect(right_platform):
            if correct_platform == 2:
                pygame.event.post(pygame.event.Event(CORRECT_PLATFORM_RIGHT))
            elif correct_platform == 1:
                pygame.event.post(pygame.event.Event(INCORRECT_PLATFORM_RIGHT))


def drop_left_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct):
    for fall in range(80):
        left_platform.y += PLATFORM_SPEED
        character.y += PLATFORM_SPEED
        draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
        if character.y > HEIGHT:
            break


def drop_right_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct):
    for fall in range(80):
        right_platform.y += PLATFORM_SPEED
        character.y += PLATFORM_SPEED
        draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
        if character.y > HEIGHT:
            break


def lower_left_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct):
    
    while left_platform.y < 400:
        right_platform.y += PLATFORM_SPEED + 20
        left_platform.y += PLATFORM_SPEED
        character.y += PLATFORM_SPEED
        draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
    left_platform.x, left_platform.y = WIDTH//2 - CHARACTER_WIDTH - 150, 200
    right_platform.x, right_platform.y = WIDTH//2+100, 200
    character.y = 400 - CHARACTER_HEIGHT

def lower_right_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct):

    if character.y != 400 - CHARACTER_HEIGHT:
        while right_platform.y < 400:
            left_platform.y += PLATFORM_SPEED + 20
            right_platform.y += PLATFORM_SPEED
            character.y += PLATFORM_SPEED
            draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
        left_platform.x, left_platform.y = WIDTH//2 - CHARACTER_WIDTH - 150, 200
        right_platform.x, right_platform.y = WIDTH//2+100, 200
        character.y = 400 - CHARACTER_HEIGHT

def game_over(GAME_OVER, TRY_AGAIN):
    game_over_text = QUESTION_FONT.render(GAME_OVER, 1, WHITE)
    SCREEN.blit(game_over_text, (WIDTH//2-game_over_text.get_width()//2, HEIGHT//2-30))
    try_again_text = TRY_AGAIN_FONT.render(TRY_AGAIN, 1, WHITE)
    SCREEN.blit(try_again_text, (WIDTH // 2 - try_again_text.get_width() // 2, HEIGHT // 2 + 70))

    pygame.display.update()


def game_completed(HOORAY, GAME_COMPLETED):
    hooray_text = QUESTION_FONT.render(HOORAY, 1, WHITE)
    SCREEN.blit(hooray_text, (WIDTH//2-hooray_text.get_width()//2, HEIGHT//2-30))
    game_completed_text = TRY_AGAIN_FONT.render(GAME_COMPLETED, 1, WHITE)
    SCREEN.blit(game_completed_text, (WIDTH // 2 - game_completed_text.get_width() // 2, HEIGHT // 2 + 70))

    pygame.display.update()


def main():
    
    character = pygame.Rect(WIDTH//2 - CHARACTER_WIDTH//2, 350, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    left_platform = pygame.Rect(WIDTH//2 - CHARACTER_WIDTH - 150, 200, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    right_platform = pygame.Rect(WIDTH//2+100, 200, PLATFORM_WIDTH, PLATFORM_HEIGHT)

    low_left_platform = pygame.Rect(WIDTH//2 - CHARACTER_WIDTH - 150, 400, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    low_right_platform = pygame.Rect(WIDTH // 2 + 100, 400, PLATFORM_WIDTH, PLATFORM_HEIGHT)


    clock = pygame.time.Clock()

    level_passed = False

    current_correct = 1

    current_score = 0
    
    question_count = 1

    random_count = random.randint(1,2)
    run = True
    while run:
        
        clock.tick(60)

        if random_count%2 == 0:
            random_correct = 1
        else:
            random_correct = 2
        correct_platform = random_correct
        
        c_question = get_question(question_count)
        question = c_question["question"]
        c_ans = c_question["correct"]
        i_ans = c_question["incorrect"]
        points_added = False
        max_score = 0
        

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    character_to_left_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
                if event.key == pygame.K_d:
                    character_to_right_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)

            if event.type == INCORRECT_PLATFORM_LEFT:
                level_passed = False
                drop_left_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
                
                game_over(GAME_OVER, TRY_AGAIN)
                if current_score > max_score:
                    max_score = current_score
                main()

            elif event.type == INCORRECT_PLATFORM_RIGHT:
                level_passed = False
                drop_right_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
                
                game_over(GAME_OVER, TRY_AGAIN)
                if current_score > max_score:
                    max_score = current_score
                main()

            elif event.type == CORRECT_PLATFORM_LEFT:
                current_correct = 1
                lower_left_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
                
                level_passed = True

                if current_score < 30:
                    current_score += 1
                    if question_count < 30:
                        random_count += random.randint(1,2)
                        question_count += 1
                    draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)
                if current_score == 30:
                    game_completed(HOORAY, GAME_COMPLETED)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            main()

            elif event.type == CORRECT_PLATFORM_RIGHT: 
                current_correct = 2
                lower_right_platform(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)

                level_passed = True
                
                if current_score < 30:
                    if points_added == False:
                        if current_score < 30:
                            current_score += 1
                            if question_count < 30:
                                random_count = random.randint(1,2)
                                question_count += 1
                        points_added = True
                        if character.y != 400 - CHARACTER_HEIGHT:
                            if current_score < 30:
                                current_score += 1
                                if question_count < 30:
                                    random_count = random.randint(1,2)
                                    question_count += 1


                            points_added = True
                    draw_level(character, left_platform, right_platform, question, c_ans, i_ans, current_score, max_score, level_passed, low_left_platform, low_right_platform, correct_platform, current_correct)

                if current_score == 30:
                    game_completed(HOORAY, GAME_COMPLETED)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            main()
            



if __name__ == '__main__':
    main()