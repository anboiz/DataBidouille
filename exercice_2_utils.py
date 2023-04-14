from src import verification
from pathlib import Path

file_location = Path('data/laposte_hexasmal.csv')

correction_exercice_2_1 = verification.Verification_file(file_location)

if __name__ == '__main__':
    file_location = Path('data/laposte_hexasmal.csv')

    correction_exercice_2_1.check(file_location)