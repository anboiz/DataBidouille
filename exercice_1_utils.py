import sys
import os

from src import verification
import pandas as pd

data = pd.read_excel('data/batiments/batiments_00.xlsx')
correction_exercice_1_1 = verification.Verification(data)

data = pd.read_csv('data/laposte_hexasmal.csv',sep=";")
correction_exercice_1_2 = verification.Verification(data)


if __name__ == '__main__':
    data_u = pd.read_csv('data/laposte_hexasmal.csv',sep=";")

    correction_exercice_1_2.check(data_u)