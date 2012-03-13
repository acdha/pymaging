########
pymaging
########

Pure Python imaging library.

* Author: Jonas Obrist and https://github.com/ojii/pymaging/contributors
* License: BSD (some files have other licenses, see LICENSE.txt)
* Compatibility: Python 2.6, 2.7, 3.1, 3.2 and PyPy 1.8.
* Requirements: distribute
* Docs: http://pymaging.rtfd.org


Running the benchmarks
======================

Each benchmark is a standalone script for simple testing::

    python bench/benchmarks/simple.py

To run the entire suite::

    python bench/suite.py

You will have much nicer result output if you install numpy and vbench::

    pip install numpy
    pip install https://github.com/wesm/vbench/tarball/master
