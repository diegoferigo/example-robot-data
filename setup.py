import contextlib
import pathlib
import shutil

import setuptools


@contextlib.contextmanager
def copy_robots_folder(robots_folder: str, destination_in_package: str):

    src_path = pathlib.Path(robots_folder).absolute()
    dst_path = pathlib.Path(destination_in_package).absolute()

    try:
        if not dst_path.parent.is_dir():
            dst_path.parent.mkdir(parents=True)

        shutil.copytree(src=str(src_path), dst=str(dst_path))
        yield
    finally:
        shutil.rmtree(path=dst_path)


# Find the package directory
package = setuptools.find_packages(str(pathlib.Path(".").absolute() / "python"))[0]
package_dir = pathlib.Path(".").absolute() / "python" / package

# Copy the robot folder in the package in a context manager, so that it get safely
# deleted when the process either finishes or fails
with copy_robots_folder(
    robots_folder=str(pathlib.Path(".").absolute() / "robots"),
    destination_in_package=str(package_dir / "share" / "example-robot-data" / "robots"),
):
    setuptools.setup()
