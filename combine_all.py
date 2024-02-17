import os
import re

# Get the directory of the current script
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"

all_files = os.listdir(dir_path)
all_content = []
count_done = 0
for file in all_files:
    if "done" in file:
        # count_done += 1
        with open(dir_path+file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_content += lines
print(f"len(all_content):", len(all_content))
# print("Count done =", count_done)

with open("combined_ar_questions.txt", "w", encoding="utf-8") as f:
    for content in all_content:
        f.write(content)



