import os
import random

folder_path = "./JPEGImages/"

file_names = [os.path.splitext(file)[0] for file in os.listdir(folder_path)]
random.shuffle(file_names)

total_files = len(file_names)
train_ratio = int(0.8 * total_files)
test_ratio = int(0.1 * total_files)

train_files = file_names[:train_ratio]
test_files = file_names[train_ratio:train_ratio + test_ratio]
val_files = file_names[train_ratio + test_ratio:]

def write_file(file_names, file_path):
    with open(file_path, "w") as file:
        file.write("\n".join(file_names))

write_file(train_files, "train.txt")
write_file(test_files, "test.txt")
write_file(val_files, "val.txt")
print("INFO: Export completed.")