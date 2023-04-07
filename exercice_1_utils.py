import sys
import os
cwd = os.getcwd()
print(cwd)

from src import verification
import pandas as pd

data = pd.read_excel('data/batiments/batiments_00.xlsx')

correction_exercice = verification.Verification(data)

if __name__ == '__main__':
    data_u = pd.read_excel('data/batiments/batiments_01.xlsx')

    correction_exercice.check(data_u)