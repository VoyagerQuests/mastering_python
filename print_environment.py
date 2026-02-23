import sys
import site
import sysconfig
from importlib.metadata import distributions

LABEL_WIDTH = 18

print(f'{"executable:":<{LABEL_WIDTH}}\t{sys.executable}')
print(f'{"prefix:":<{LABEL_WIDTH}}\t{sys.prefix}')
print(f'{"base_prefix:":<{LABEL_WIDTH}}\t{sys.base_prefix}')
print(f'{"venv:":<{LABEL_WIDTH}}\t{sys.prefix != sys.base_prefix}')

print(f'\n{"site-packages:":<{LABEL_WIDTH}}')
for p in getattr(site, "getsitepackages", lambda: [])():
    print(f'{"":<{LABEL_WIDTH}}\t{p}')


print(f'\n{"full sys.path:":<{LABEL_WIDTH}}')
for p in sys.path:
    print(f'{"":<{LABEL_WIDTH}}\t{p}')

print("\n")
print("*** Installed Python Packages ***\n")
print(f'Found {len(list(distributions()))} installed packages:\n')
# for dist in sorted(distributions(), key=lambda d: d.metadata["Name"].lower()):
#     name = dist.metadata["Name"]
#     version = dist.version
#     print(f"{name}=={version}")

# Terminal commands
#
# python -c "import sys; print(sys.executable)"  # prints the path to the Python executable
# python -c "import sys; print(sys.prefix)"  # prints the prefix of the Python installation
# python -c "import sys; print(sys.base_prefix)"  # prints the base prefix of the Python installation
# python -c "import sys; print(sys.prefix != sys.base_prefix)"  # prints True if in a virtual environment, False otherwise
# python -c "import site; print(site.getsitepackages())"  # prints the list of site-packages directories
# python -c "import sys; print(sys.path)"  # prints the full sys.path
# python -m pip list  # lists all installed Python packages with their versions