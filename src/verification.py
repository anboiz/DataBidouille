from colorama import Fore, Style # just_fix_windows_console
import random
import pandas as pd
from typing import List, Any
from pathlib import Path
import hashlib

class Verification():
    # def __init__(self,data:pd.DataFrame) -> None:
    #     self.data = data

    # def check(self, userdata:pd.DataFrame) -> None:
    #     try:
    #         verif = self.data.compare(userdata)

    #     except ValueError:
    #         self.fail()
    #         return

    #     if verif.size > 0:
    #         self.fail()
    #         return

    #     self.success()
    #     return

    def success(self) -> None:
        print(Fore.GREEN + '👏 Bravo ! 🥳')
        print(Style.RESET_ALL)
    
    def fail(self) -> None:
        answers = [
            "😯 Nope, pas exactement. Essaie encore",
            "🦕 Bad luck kid, maybe next time. Come back whenever you're ready",
            "Le grand serpent ne se laisse pas dompter si facilement... 🐉",
            "Encore un peu d’entraînement ? 🤕"
            
        ]
        print(Fore.RED + f'{random.choice(answers)}')
        print(Style.RESET_ALL)

class Verification_df(Verification):
    def __init__(self,data:pd.DataFrame) -> None:
        self.data = data

    def check(self, userdata:pd.DataFrame) -> None:
        try:
            verif = self.data.compare(userdata)

        except ValueError:
            self.fail()
            return

        if verif.size > 0:
            self.fail()
            return

        self.success()
        return

class Verification_list(Verification):
    def __init__(self,data:List) -> None:
        self.data = data

    def check(self, userdata:List) -> None:
        try:
            result = all(x == y for x, y in zip(self.data, userdata))
            
        except ValueError:
            self.fail()
            return

        if not result:
            self.fail()
            return

        self.success()
        return
    
class Verification_any(Verification):
    def __init__(self,data:Any) -> None:
        self.data = data

    def check(self, userdata:Any) -> None:
        try:
            result = self.data == userdata
            
        except ValueError:
            self.fail()
            return

        if not result:
            self.fail()
            return

        self.success()
        return

def md5(path_to_file:Path) ->str:
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(path_to_file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    
    return hasher.hexdigest()
class Verification_file(Verification):
    def __init__(self,path_to_file:Path) -> None:
        self.hash_md5 = md5(path_to_file)
    
    def check(self, path_to_file:Path) -> None:
        
        try :
            user_file_md5 = md5(path_to_file)
            
            if user_file_md5 == self.hash_md5:
                self.success()
                return 
        except Exception :
            self.fail()
            return
        
        self.fail()
        return
        

if __name__ == '__main__':
    a = Path('data/batiments').glob('.xlsx')
    exo = Verification_list(a)
    exo.check(Path('data/batiments').glob('.xlsx'))
    pass



