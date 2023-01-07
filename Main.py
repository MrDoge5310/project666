import pygame
import speech_recognition as sr
import Robot
import Aim

pygame.init()

screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))

# отрисовка робота
robot = Robot.Robot(screen, screen_width / 2, screen_height / 2)
robot.draw()

# отрисовка мишени
aim = Aim.Aim(screen)
aim.draw()
pygame.display.update()

# Настраиваем распознавание речи
r = sr.Recognizer()

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        # Распознаем голосовые команды
        command = r.recognize_google(audio, language="ru-RU")
        print(f"Распознана команда: {command}")

        # Обрабатываем команды
        if "влево" in command:
            robot.move("влево")
        elif "вправо" in command:
            robot.move("вправо")
        elif "вверх" in command:
            robot.move("вверх")
        elif "вниз" in command:
            robot.move("вниз")

    except sr.UnknownValueError:
        print("Распознавание не удалось")
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания: {0}".format(e))
    finally:
        robot.draw()
        pygame.display.update()
        continue

pygame.quit()
