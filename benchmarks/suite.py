from datetime import datetime
import os
import tempfile
import timeit
import sys

try:
    from vbench.api import Benchmark, GitRepo, BenchmarkRunner
    HAS_VBENCH = True
except ImportError as exc:
    print >>sys.stderr, "Couldn't load vbench: falling back to stdlib (%s)" % exc
    HAS_VBENCH = False

PYMAGING_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
OUTPUT_DIR = os.path.join(PYMAGING_ROOT, "bench", "output")


def discover_benchmarks():
    for bench in os.listdir(os.path.join(PYMAGING_ROOT, "bench", "benchmarks")):
        if not bench.endswith(".py") or bench.startswith("_"):
            continue
        yield "benchmark()", "from benchmarks.%s import benchmark" % os.path.splitext(bench)[0]


def run_vbench():
    START_DATE = datetime(2012, 2, 27)
    DB_PATH = os.path.join(PYMAGING_ROOT, 'bench', 'benchmarks.db')
    REPO_URL = PYMAGING_ROOT

    repo = GitRepo(PYMAGING_ROOT)

    benchmarks = [Benchmark(stmt, setup) for stmt, setup in discover_benchmarks()]

    runner = BenchmarkRunner(benchmarks, PYMAGING_ROOT, REPO_URL,
                             '', DB_PATH, OUTPUT_DIR, '',
                             run_option='all', start_date=START_DATE,
                             module_dependencies=[])
    runner.run()


def run_simple():
    try:
        repeats, number = map(int, sys.argv[1:2])
    except:
        repeats = 3
        number = 5

    for stmt, setup in discover_benchmarks():
        times = timeit.repeat(stmt, setup, repeat=repeats, number=number)

        print "Results after %s repeats of %d calls:" % (repeats, number)
        print "Min: %0.3f" % min(times)
        print "Max: %0.3f" % max(times)

if __name__ == '__main__':
    if HAS_VBENCH:
        run_vbench()
    else:
        run_simple()
