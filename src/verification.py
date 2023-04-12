from colorama import Fore, Style # just_fix_windows_console
import random
import pandas as pd
from typing import List, Any
from pathlib import Path

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

if __name__ == '__main__':
    a = Path('data/batiments').glob('.xlsx')
    exo = Verification_list(a)
    exo.check(Path('data/batiments').glob('.xlsx'))
    pass



