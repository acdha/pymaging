import os

from benchmark_harness.runners import run_comparison_benchmark

from pymaging import Image as PY_Image
from PIL import Image as PIL_Image

TEST_DATA_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "test_data")


def benchmark_pil():
    PIL_Image.open(os.path.join(TEST_DATA_ROOT, 'testimage.png')).transpose(PIL_Image.FLIP_LEFT_RIGHT).save('simple-pil.png', 'PNG')


def benchmark_pymaging():
    i = PY_Image.open_from_path(os.path.join(TEST_DATA_ROOT, 'testimage.png'))
    i = i.flip_left_right()
    # Save for quality review
    i .save_to_path('simple.png')


run_comparison_benchmark(benchmark_pymaging, benchmark_pil,
                         meta={"title": "Direct comparison of pymaging vs. PIL"})
