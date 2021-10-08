from distutils.core import setup

setup(
    name="F10-Cogs-Utils",
    description="A module with utils for Fixator10-Cogs",
    author="Fixator10",
    packages=["cogsutils", "cogsutils.dpy_future"],
    package_dir={"cogsutils": "src"},
)
