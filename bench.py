from timeit import default_timer as time
import sys

from pymaging import Image

start_time = time()
elapsed = 0

for i in xrange(0, 1000):
    Image.open_from_path('testimage.png').flip_left_right().save_to_path('benchimage.png')
    elapsed = time() - start_time

    if elapsed > 1.0:
        break

trials = i + 1

print "{trials:d} iterations in {elapsed:0.2f} seconds ({average:0.2f}s/call)".format(trials=trials, elapsed=elapsed, average=elapsed / trials)