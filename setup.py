import sys, os, subprocess, sysconfig
from distutils import sysconfig
from distutils.command.build import build
from multiprocessing import cpu_count
from setuptools import setup


platform = sys.platform
supported_platforms = ["Linux", "Mac OS-X"]

if platform.startswith("win"):
    raise RuntimeError("Building pip package on Windows is not currently available ...")
elif platform.startswith("darwin"):
    makefile = "Makefile.macos"
elif platform.startswith("linux"):
    makefile = "Makefile"
else:
    raise RuntimeError("Unrecognized platform: {}".format(sys.platform))

class BuildCommand(build):
    def run(self):
        try:
            src_path = os.path.realpath(os.path.realpath(os.path.join(os.path.dirname(__file__), "Oblige_src")))
            subprocess.check_call("make -f {}".format(makefile), cwd=src_path)

        except subprocess.CalledProcessError:
            sys.stderr.write("\033[1m\nInstallation failed, you may be missing some dependencies. "
                             "\nPlease check https://github.com/mwydmuch/PyOblige/README.md for details\n\n\033[0m")
            raise
        build.run(self)


setup(
    name='pyoblige',
    version='0.1.0',
    description='Reinforcement learning platform based on Doom',
    long_description="ViZDoom allows developing AI bots that play Doom using only the visual information (the screen buffer). " \
                     "It is primarily intended for research in machine visual learning, and deep reinforcement learning, in particular.",
    url='http://oblige.sourceforge.net',
    author='ViZDoom Team',
    author_email='vizdoom@googlegroups.com',

    packages=['pyoblige'],
    package_dir={'pyoblige': package_path},
    package_data={'pyoblige': ['oblige']},
    include_package_data=True,
    cmdclass={'build': BuildCommand},
    platforms=supported_platforms,
    classifiers=[
        'Development Status :: 5 - Production/Stable', # ??
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License', # ??
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)