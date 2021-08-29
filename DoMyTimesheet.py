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
    logs_per_repo = repo.git.log("--pretty='%s'").replace("'", "").split("\n")

    for l in logs_per_repo:
        all_log_entries.append(l)

print(all_log_entries)
