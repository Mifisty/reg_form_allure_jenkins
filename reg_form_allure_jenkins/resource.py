import os   # noqa
import test

# def path():
#     return str(
#         os.path.abspath(os.path.join(os.path.dirname(test.__file__), 'pic.jpg'))
#     )

from pathlib import Path


def path(file_name):
    return str(Path(test.__file__).parent.parent.joinpath(f'test/{file_name}'))
