Ever been into position that at the end of the month you have to log time for all that period?
Do you know the struggle of remembering what jira tickets were you working on? Here comes solution.

This simple python script scans all git repositiories in provided folder and prints all unique jira signatures found in commits.
For script to work commit messages have to have to start with jira signatures like `TST-12 message`.

Usage:
`python3 DoMyTimesheet.py --since=2021-08-01 --root='/path/to/repos' --author='iwek'`

Date needs to be in `iso8601` format

For easier use modify variables `DEFAULT_ROOT` and `DEFAULT_AUTHOR` with your defaults (so that you dont have to pass them each time)

Required dependencies: `GitPython`

