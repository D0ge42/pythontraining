import time
import datetime
import pygame

sound_file = "Classic Alarm Clock - Sound Effect for Editing.mp3"

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")


if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP")
            is_running = False
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
        time.sleep(1)
