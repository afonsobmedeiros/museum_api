import os
import re
import subprocess
from Parameters import ROOT

def run():
    directory = os.path.join(ROOT, "manual_migrations")
    list_files = os.listdir(directory)
    list_migrations = [ x for x in list_files if x.endswith(".py") and re.match(r"^\d", x) ]
    migrations_file = os.path.join(directory, "runned_migrations.txt")
    with open(migrations_file, "r+") as f:
        lines = f.readlines()
        for migration in list_migrations:
            if migration + "\n" not in lines:
                print(f"\nRunning: {migration}")
                file = os.path.join(directory, migration)
                subprocess.run(["python", file], cwd=ROOT, check=True, env={**os.environ, "PYTHONPATH": ROOT})
                f.write(migration + "\n")
        