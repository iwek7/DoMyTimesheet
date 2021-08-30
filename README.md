Ever been into position that at the end of the month you have to log time for all that period?
Do you know the struggle of remembering what jira tickets were you working on? Here comes solution.

This simple python script scans all git repositiories in provided folder and prints all unique jira signatures found in commits.
For script to work commit messages have to have to start with jira signatures like `TST-12 message`.

Usage:
`python3 DoMyTimesheet.py --since=29-08-2021 --root='/path/to/repos'`

For easier use modify variable `ROOT_ARG` in script to set path desired path so that you don't have to pass `root` arg each time

