import os
from functools import reduce
from pathlib import Path

import git


def flat_map(array):
    return reduce(lambda a, b: a + b, array)


root = "/home/iwek/projects/DoMyTimesheetTests"
all_directories = map(lambda path: root + "/" + path, os.listdir(root))
git_repo_paths = filter(lambda sub_dir: Path(sub_dir + "/.git").exists(), all_directories)

all_log_entries = []
for repo_path in git_repo_paths:
    repo = git.Repo(repo_path)
    all_log_entries += repo.git.log("--pretty='%s'").replace("'", "").split("\n")

print(all_log_entries)
