import pygame
import logic
import random
import levels


_FRAME_RATE = 30
_WIDTH = 1440
_HEIGHT = 810
_BACKGROUND_COLOR = pygame.Color(30,30,30)
_TEXT_COLOR = pygame.Color(255,255,255)
_RED = pygame.Color(255,0,0)
_GREEN = pygame.Color(0,255,0)


class TypingGame:
    def __init__(self):
        self._state = logic.Gamestate(1)
        self._running = True
        self._word = ''
        self._all_words = self._state.level_words()
        self._current_set = 10
        self._current_index = 0
        self._wow_positions = []
        

        
    def run(self):
        pygame.init()
        pygame.display.set_caption('Typing Game!')
        self._font = pygame.font.SysFont("comicsansms", 30)
        
        self._stat_font = pygame.font.SysFont("comicsansms", 30)
        try:
            clock = pygame.time.Clock()
            self._create_surface((_WIDTH, _HEIGHT))      
            
            while self._running:
                clock.tick(_FRAME_RATE)
                self._handle_events()
                self._draw_frame()
                            
        finally:
            pygame.quit()


    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)   

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            self._handle_event(event)
#         self._handle_keys()


    def _handle_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._stop_running()
        elif event.type == pygame.VIDEORESIZE:
            self._create_surface(event.size)
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if len(key) == 1:
                self._word += key
                print('hi')
                print(self._word)
            elif key == "backspace":
                self._word = self._word[:len(self._word) - 1]
            elif event.key == pygame.K_SPACE:
                self._state._userbox.add_word(self._word)
                self._current_index += 1
                self._reset_word()
            
            
    def _draw_frame(self) -> None:
        self._surface.fill(_BACKGROUND_COLOR)
        
        if self._state._difficulty == 1:
            fs = 57
        elif self._state._difficulty == 2:
            fs = 37
        elif self._state._difficulty == 3:
            fs = 29
        elif self._state._difficulty == 4:
            fs = 23
        self._font = pygame.font.SysFont("comicsansms", round(fs))

        
        self._level_display()  
        self._wpm()  
        self._test_words()
        self._user_words()
        self._errors()
        self._intro()
        self._instruct()
        if self._state._userbox._errors > 0:
            self._wow(self._state._userbox._errors)
        
        pygame.display.flip()
        
        
    def _stop_running(self):
        self._running = False
        
        
    def _wow(self, errors: int):
        if len(self._wow_positions) < errors:
            self._wow_positions.append ([self._surface.get_width()*random.uniform(0.2, 1.0), self._surface.get_height()*random.uniform(0.2, 1.0)])           
        f = pygame.font.SysFont("comicsansms", 50)
        wow = f.render("wow",1, _RED)
        wow_rect = wow.get_rect()
        for w in self._wow_positions:
            w[0]+=random.randint(-50,50)
            w[1]+=random.randint(-50,50)
            wow_rect.center = (w[0],w[1])
            self._surface.blit(wow,wow_rect)
            


        
    def _level_display(self):
        level = 'Level ' + str(self._state.get_level())
        l = self._stat_font.render(level, 1,_TEXT_COLOR)
        l_rect = l.get_rect()
        l_rect.center = (self._surface.get_width()/2, self._surface.get_height()*0.8)
        self._surface.blit(l,l_rect)
    
    
    def _wpm(self):
        self._state.get_wpm()
        wpm = self._state.current_wpm
        wpm_s = "Words Per Minute: " + str(wpm)
        w = self._stat_font.render(wpm_s,1,_TEXT_COLOR)
        w_rect = w.get_rect()
        w_rect.center = (self._surface.get_width() * 0.8, self._surface.get_height()*0.1)
        self._surface.blit(w,w_rect)

    def _errors(self):
        errors = self._state._userbox._errors
        error = "Number of errors: " + str(errors)
        e = self._stat_font.render(error,1,_TEXT_COLOR)
        e_rect = e.get_rect()
        e_rect.center = (self._surface.get_width() * 0.8, self._surface.get_height() * 0.2)
        self._surface.blit(e,e_rect)
        
    def _intro(self):
        intro = "TYPE AS FAST AS YOU CAN (HINT: FULLSCREEN)"
        i = self._stat_font.render(intro,1,(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        i_rect = i.get_rect()
        i_rect.center = (self._surface.get_width() * 0.25, self._surface.get_height() * 0.1)
        self._surface.blit(i,i_rect)
    
    def _instruct(self):
        instruct = "TO LEVEL UP: ERRORS < 30% AND WPM > 45"
        z = self._stat_font.render(instruct,1,(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        z_rect = z.get_rect()
        z_rect.center = (self._surface.get_width() * 0.25, self._surface.get_height() * 0.2)
        self._surface.blit(z,z_rect)
        
    def _test_words(self):
        try:
            words = self._all_words[:]
            typed = self._state._userbox.get_typed()
            t_len = len(typed)
            line = ''
            if t_len >= self._current_set:
                self._current_set += 10   
            if t_len < self._current_set:
                words[self._current_index] = words[self._current_index].upper()
                line = '    '.join( words[self._current_set - 10:self._current_set])
            l = self._font.render(line, 1,_TEXT_COLOR)
            l_rect = l.get_rect()
            l_rect.center = self._surface.get_rect().center
            self._surface.blit(l, l_rect)
        except IndexError:
            self._state.get_wpm()
            wpm = self._state.current_wpm
            new_level = levels.level(self._state._userbox._errors/len(self._all_words), wpm, self._state._difficulty)
            print(new_level)
            self._state = logic.Gamestate(new_level )
            self._all_words = self._state.level_words()
            self._current_set = 10
            self._current_index = 0
            self._wow_positions = []

    
    def _user_words(self):
        label = self._stat_font.render(self._word, 1, _TEXT_COLOR)
        label_rect = label.get_rect()
        label_rect.center = (self._surface.get_width()/2, self._surface.get_height()*0.35)
        self._surface.blit(label, label_rect)
        
        
    def _reset_word(self) -> None:
        self._word = ''


    def _current_iteration(self):
        return len(self._state._userbox.get_typed()) 
    
    def _random_color(self):
        
        return pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
        
        
if __name__ == '__main__':
    TypingGame().run()