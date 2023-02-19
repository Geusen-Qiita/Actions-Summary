import random
import subprocess

number = random.randint(1,6)
print('サイコロの出目は' + str(number) + 'です')
subprocess.run([f'echo "NUMBER={number}" >> $GITHUB_OUTPUT'], shell=True)
