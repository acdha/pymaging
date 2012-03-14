import os

from benchmark_harness.runners import run_benchmark

from pymaging import Image

TEST_DATA_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "test_data")


def benchmark():
    i = Image.open_from_path(os.path.join(TEST_DATA_ROOT, 'testimage.png'))
    i = i.flip_left_right()
    # Save for quality review
    i .save_to_path('simple.png')

run_benchmark(benchmark)