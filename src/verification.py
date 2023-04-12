from colorama import Fore, Style # just_fix_windows_console
import random
import pandas as pd

class Verification():
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

if __name__ == '__main__':
    a = pd.DataFrame({"col1":[1,2,3],"col2":[4,5,6]})
    exo = Verification(a)

    b = a.copy()

    exo.check(b)

    b['col3'] = None
    exo.check(b)


    b.loc[2,"col2"] = "nnbbjsmkd"

    exo.check(b)