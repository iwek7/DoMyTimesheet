import os
import re
import sys
from pathlib import Path
from typing import Final

import git

# constants
JIRA_SIGNATURE_RE: Final = re.compile('([^s]+)')
ROOT_ARG: Final = "root"
START_DATE_ARG: Final = "since"

DEFAULT_START_DATE = "29-08-2021"
DEFAULT_ROOT = "/home/iwek/projects/DoMyTimesheetTests"


# program
def parse_args():
    parsed_args = {ROOT_ARG: DEFAULT_ROOT, START_DATE_ARG: DEFAULT_START_DATE}
    for arg in sys.argv:
        parts = arg.split("=")
        if len(parts) != 2:
            continue

        if parts[0] == "--" + ROOT_ARG:
            parsed_args[ROOT_ARG] = parts[1]
        elif parts[0] == "--" + START_DATE_ARG:
            parsed_args[START_DATE_ARG] = parts[1]
    return parsed_args


def print_results(unique_jira_signatures):
    for res in unique_jira_signatures:
        print(res)


def create_timesheet(start_date: str, root: str):
    all_directories = map(lambda path: root + "/" + path, os.listdir(root))
    git_repo_paths = filter(lambda sub_dir: Path(sub_dir + "/.git").exists(), all_directories)

    all_jira_signatures = []
    for repo_path in git_repo_paths:
        repo = git.Repo(repo_path)
        raw_log_entries = repo.git.log(
            "--pretty='%s'",
            "--after=\'" + start_date + " 00:00\'"
                                        "--author 'iwek'"  # todo: take author from gitconfig
        ).replace("'", "").split("\n")
        jira_signatures = []
        for log in raw_log_entries:
            split = re.search(r'[a-zA-Z]{3}-\d+', log)
            if split:
                jira_signatures.append(split.group(0))
        all_jira_signatures += jira_signatures

    unique_jira_signatures = set(all_jira_signatures)

    print_results(unique_jira_signatures)


args = parse_args()
create_timesheet(args[START_DATE_ARG], args[ROOT_ARG])
