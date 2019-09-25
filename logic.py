import words
import time
import levels

# Note to Travis: Only show 20 words at a time
# After 20, show the next 20

_MAX_WORDS = 10

class Wordbox:
    def __init__(self, random_words_on_screen: list):
        self._all_words = random_words_on_screen
        
    
    def get_all_words(self) -> list:
        return self._all_words
        
        
    
    
    
#The list here is going to be the current user input
class Typebox:
    def __init__(self, all_words):
        self._all_words = all_words
        self._user_input = []
        self._correct_words = []
        
        
        self._errors = 0

        
        self._start_time = 0
        self._current_time = 0
        self._total_time = 0
            

    def add_word(self, new_word: str) -> None:
        self._user_input.append(new_word)
#         print(self._user_input)
        self._checker(new_word, self._all_words)
        
        if len(self._user_input) == 1:
            self._set_start_time()
        if len(self._user_input) == _MAX_WORDS:
            self._total_time = self._end_time()
            

        
    def _checker(self, word: str, screen_words: list) -> None:
        try:
            if word != screen_words[len(self._user_input) - 1]:
                self._errors += 1

            else:
                self._correct_words.append(word)

        except:
            pass
    
    def get_typed(self) -> list:
        return self._user_input
    
    def get_errors(self) -> int:
        return self._errors
    
    def _end_time(self) -> float:
        return time.time() - self._start_time
    
    def _set_start_time(self):
        self._start_time = time.time()
    
    def _get_current_time(self):
        return time.time() - self._start_time

        
    
    
    

    
    
    
#calculate time
            
   


# call get_random_words more in while loop, erase them
# call function again when run out
class Gamestate:
    def __init__(self, difficulty: int):
        self._difficulty = difficulty

        
        
        self._words_for_screen = words.get_random_words(self._difficulty, _MAX_WORDS)
        self._wordbox = Wordbox(self._words_for_screen)
        self._userbox = Typebox(self._words_for_screen)
        self._userbox._set_start_time()
        
        def change_difficulty(self, new_difficulty) -> None:
            self._difficulty = new_difficulty
        
    
    def level_words(self) -> list:
        '''Travis: Returns a list of all words the user is going to type'''
        return self._words_for_screen
    
    def get_level(self) -> int:    
        return self._difficulty
    
    def get_wpm(self):
        
        self.current_wpm =  levels.calc_wpm(self._userbox._correct_words, self._userbox._get_current_time())
    


#     def level_change(self, new_level):
#         self._difficulty = new_level
#         self._words_for_screen = words.get_random_words(self._difficulty, _MAX_WORDS)
#         self._wordbox = Wordbox(self._words_for_screen)
#         self._userbox = Typebox(self._words_for_screen)
#         self._userbox._set_start_time()
        
        
        




#match
        

        