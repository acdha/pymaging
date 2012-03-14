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

The benchmarks use http://pypi.python.org/pypi/benchmark-harness. To run the
benchmarks, you need to install benchmark-harness and will need PIL to run the
comparison benchmarks::

    pip install benchmark-harness PIL

Each benchmark is a standalone script for simple testing::

    python benchmarks/simple/benchmark.py

To run the entire suite::

    benchmark-harness --benchmark-dir=benchmarks
