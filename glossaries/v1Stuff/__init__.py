# __init__.py

from .python_glossary import glossary as python_glossary
from .GIT_glossary import glossary as git_glossary
from .gloss_func import gloss_func
from .linux_network_cmds import glossary as linux_network_cmds
from .ubuntu_cmds import glossary as ubuntu_cmds
from .vim_cmds import glossary as vim_cmds
__all__ = ["python_glossary", "GIT_glossary", "gloss_func", "linux_network_cmds", "ubuntu_cmds", "vim_cmds"]

print("Glossaries package initialized")
