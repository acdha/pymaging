import os

from benchmark_harness.runners import run_benchmark

from pymaging import Image

def benchmark():
    i = Image.open_from_path('testimage.png')
    i = i.flip_left_right()
    # Save for quality review
    i .save_to_path('simple.png')

run_benchmark(benchmark)