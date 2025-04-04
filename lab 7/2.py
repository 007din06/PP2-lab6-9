import pygame
import os

pygame.init()
pygame.mixer.init()


WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 40)


songs = [
    {"name": "Song 1", "path": "1.mp3"},
    {"name": "Song 2", "path": "2.mp3"},
    {"name": "Song 3", "path": "song3.mp3"}
]

curr_index = 0

def play(index):
    if os.path.exists(songs[index]["path"]):
        pygame.mixer.music.load(songs[index]["path"])
        pygame.mixer.music.play()
        print(f"Playing: {songs[index]['name' ]}")
    else:
        print(f"File {songs[index]['path']} not found!")

def stop():
    pygame.mixer.music.stop()
    print("Music Stopped")

def next_song():
    global curr_index
    curr_index = (curr_index + 1) % len(songs)
    play(curr_index)

def prev_song():
    global curr_index
    curr_index = (curr_index - 1) % len(songs)
    play(curr_index)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                play(curr_index)
            elif event.key == pygame.K_s:  
                stop()
            elif event.key == pygame.K_RIGHT:  
                next_song()
            elif event.key == pygame.K_LEFT:  
                prev_song()
    
    screen.fill((255, 255, 255))
    text = font.render(f"Now Playing: {songs[curr_index]['name']}", True, (0, 0, 0))
    screen.blit(text, (50, 130))
    pygame.display.flip()

pygame.quit()
