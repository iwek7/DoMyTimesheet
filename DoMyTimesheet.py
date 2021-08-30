import os
import re
from pathlib import Path
from typing import Final
import git

# user input
start_date = "29-08-2021"
root = "/home/iwek/projects/DoMyTimesheetTests"

# constants
JIRA_SIGNATURE_RE: Final = re.compile('([^s]+)')

# program

def print_results(unique_jira_signatures):
    for res in unique_jira_signatures:
        print(res)

all_directories = map(lambda path: root + "/" + path, os.listdir(root))
git_repo_paths = filter(lambda sub_dir: Path(sub_dir + "/.git").exists(), all_directories)

all_jira_signatures = []
for repo_path in git_repo_paths:
    repo = git.Repo(repo_path)
    raw_log_entries = repo.git.log(
        "--pretty='%s'",
        "--after=\'" + start_date + " 00:00\'"
        "--author 'iwek'"     # todo: take author from gitconfig
    ).replace("'", "").split("\n")
    jira_signatures = []
    for log in raw_log_entries:
        split = re.search(r'[a-zA-Z]{3}-\d+', log)
        if split:
            jira_signatures.append(split.group(0))
    all_jira_signatures += jira_signatures

unique_jira_signatures = set(all_jira_signatures)

print_results(unique_jira_signatures)
