import os
import sys


def test_sys_path_contains_repo_root():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    assert repo_root in sys.path
