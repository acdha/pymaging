import os

from pymaging import Image

def benchmark():
    i = Image.open_from_path('testimage.png')
    i = i.flip_left_right()
    # Save for quality review
    i .save_to_path('simple.png')

if __name__ == "__main__":
    import timeit
    print timeit.timeit("benchmark()", "from simple import benchmark", number=5)