from distutils.core import setup
import re

VERSION_RE = re.compile(r"__version__\s*=\s*\"(\d+\.\d+\.\d+)\"")

with open("./TagScriptEngine/__init__.py", "r") as init:
    match = VERSION_RE.search(init.read())
if not match:
    raise RuntimeError("failed to find version info")
version = match.group(1)


if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()
    except Exception:
        pass


setup(
    name="TagScriptEngine",
    url="https://github.com/phenom4n4n/TagScript",
    author="PySnow",
    author_email="vasti009@gmail.com",
    version=version,
    packages=[
        "TagScriptEngine",
        "TagScriptEngine.adapter",
        "TagScriptEngine.block",
        "TagScriptEngine.interface",
    ],
)
