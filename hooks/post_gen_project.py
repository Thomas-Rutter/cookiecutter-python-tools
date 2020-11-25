"""Code to run pre generation of project."""
import subprocess


if "{{cookiecutter.setup_repo}}" == "y":
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial Commit'])
    subprocess.call(['gh', 'repo', 'create', '{{cookiecutter.project_id}}', '-y', '-d', '{{cookiecutter.description}}', '--private'])
    subprocess.call(['git', 'push', '-u', 'origin', 'master'])
    subprocess.call(['git', 'checkout', '-b', 'develop'])
    subprocess.call(['git', 'push', '-u', 'origin', 'develop'])
