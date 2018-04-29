import sys, os, subprocess
from distutils.command.build import build
from multiprocessing import cpu_count
from setuptools import setup
import glob

platform = sys.platform
supported_platforms = ["Linux", "Mac OS-X"]
package_path = "pyoblige"
oblige_src_path = os.path.join(package_path, "Oblige_src")

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
            cpu_cores = max(1, cpu_count() - 1)
            src_path = os.path.realpath(os.path.realpath(
                os.path.join(os.path.dirname(__file__), oblige_src_path)))
            subprocess.check_call(["make", "-j", str(cpu_cores), "-f", makefile], cwd=src_path)
        except subprocess.CalledProcessError:
            sys.stderr.write("\033[1m\nInstallation failed, you may be missing some dependencies. "
                             "\nPlease check https://github.com/mwydmuch/PyOblige/README.md for details\n\n\033[0m")
            raise
        build.run(self)

# Python 3.5+ only
#extra_files = [x for x in glob.glob("{}/**".format(oblige_src_path), recursive=True)]

# Python 2.7 + Python 3 solution
extra_files = []
for root, dirnames, filenames in os.walk('{}/'.format(oblige_src_path)):
    for filename in filenames:
        extra_files.append(os.path.join(root, filename))

setup(
    name='oblige',
    version='0.1.2',
    description='Level generator for DOOM',
    long_description="Level generator for DOOM. Wrapper for Oblige.",
    url='https://github.com/mwydmuch/PyOblige',
    author='Marek Wydmuch, Michał Kempka',
    author_email='vizdoom@googlegroups.com',
    packages=['oblige'],
    package_dir={'oblige': package_path},
    package_data={'oblige': extra_files},
    include_package_data=True,
    cmdclass={'build': BuildCommand},
    platforms=supported_platforms,
    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        # 'License :: OSI Approved :: MIT License',  # ??
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
