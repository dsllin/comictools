import os
import re

directory = r""

for file in os.listdir(directory):
    numbers = re.findall(r'\d+', file)
    numbers = [int(num) for num in numbers]
    print(f"{directory}\\{numbers[0]:05d}.jpg")
    os.rename(f"{directory}\\{file}", f"{directory}\\{numbers[0]:05d}.jpg")
