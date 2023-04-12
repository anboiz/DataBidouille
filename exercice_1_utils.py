from pathlib import Path
import os

from src import verification
import pandas as pd

data = pd.read_excel('data/batiments/batiments_00.xlsx')
correction_exercice_1_1 = verification.Verification_df(data)

data = pd.read_csv('data/laposte_hexasmal.csv',sep=";")
correction_exercice_1_2 = verification.Verification_df(data)

correction_exercice_1_3_1 = verification.Verification_any(Path('data/batiments'))

file_gen = Path('data/batiments').glob('*.xlsx')
correction_exercice_1_3_2 = verification.Verification_list(file_gen)

data_liste = [pd.read_excel(e) for e in file_gen]
correction_exercice_1_3_3 = verification.Verification_df(pd.concat(data_liste))

if __name__ == '__main__':
    print([x for x in Path('data/batiments').glob('**/*') if x.is_file()])