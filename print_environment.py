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

print(f'\n{"user site-packages:":<{LABEL_WIDTH}}\t{site.getusersitepackages()}')

print(f'\n{"full sys.path:":<{LABEL_WIDTH}}')
for p in sys.path:
    print(f'{"":<{LABEL_WIDTH}}\t{p}')

print("*** Installed Python Packages ***\n")
for dist in sorted(distributions(), key=lambda d: d.metadata["Name"].lower()):
    name = dist.metadata["Name"]
    version = dist.version
    print(f"{name}=={version}")