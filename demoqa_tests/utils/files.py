import os
from demoqa_tests.utils import definitions


def abs_path_from_project_root(relative_path):
    return os.path.join(definitions.ROOT_DIR, relative_path)











