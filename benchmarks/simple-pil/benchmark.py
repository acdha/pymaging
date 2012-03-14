import os

from PIL import Image

from benchmark_harness.runners import run_benchmark

TEST_DATA_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "test_data")


def benchmark():
    Image.open(os.path.join(TEST_DATA_ROOT, 'testimage.png')).transpose(Image.FLIP_LEFT_RIGHT).save('simple-pil.png', 'PNG')


run_benchmark(benchmark, meta={"title": "PIL baseline comparison"})
