import os
from pathlib import Path

root = "/home/iwek/projects/DoMyTimesheetTests"
all_directories = os.listdir(root)
git_repos = filter(lambda sub_dir: Path(root + "/" + sub_dir + "/.git").exists(), all_directories)

print(list(git_repos))
