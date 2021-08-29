import os
import re
from functools import reduce
from pathlib import Path

import git


def flat_map(array):
    return reduce(lambda a, b: a + b, array)


jira_signature_re = re.compile('([^s]+)')

root = "/home/iwek/projects/DoMyTimesheetTests"
all_directories = map(lambda path: root + "/" + path, os.listdir(root))
git_repo_paths = filter(lambda sub_dir: Path(sub_dir + "/.git").exists(), all_directories)

all_jira_signatures = []
for repo_path in git_repo_paths:
    repo = git.Repo(repo_path)
    # todo: take author from gitconfig
    raw_log_entries = repo.git.log("--pretty='%s' --author 'iwek'").replace("'", "").split("\n")
    jira_signatures = []
    for log in raw_log_entries:
        print(log)
        split = re.search(r'[a-zA-Z]{3}-\d+', log)
        if split:
            jira_signatures.append(split.group(0))
    all_jira_signatures += jira_signatures

unique_jira_signatures = set(all_jira_signatures)


print(unique_jira_signatures)

# git log --pretty