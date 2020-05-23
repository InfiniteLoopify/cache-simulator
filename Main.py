import random
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import math
import Gui

# constants
block_size = 8
mem_size = 1024
hit_time = 1
miss_penalty = 20


def computeHit(memory, cache):
    # hit calculator using memory and cache

    time = 0
    compulsory = 0
    capacity = 0
    hit_count = 0
    fifo = deque()

    # for every block in memory
    replace_index = 0
    for mem in memory:
        # cache hit
        if mem in cache:
            hit_count += 1
        else:
            # compulsory cache miss
            if len(fifo) < len(cache):
                cache[replace_index] = mem
                fifo.append(replace_index)
                replace_index += 1
                compulsory += 1
            # capacity cache miss
            else:
                popped = fifo.popleft()
                fifo.append(popped)
                cache[popped] = mem
                capacity += 1

    miss_count = compulsory + capacity
    time = hit_count * hit_time + miss_count * miss_penalty
    return time, hit_count, compulsory, capacity


def displayGraph(times, hit_rates, compulsories, capacities, cache_sizes, memory):
    # plot 3 graphs

    # plot compulsory/capacity miss vs cache size graph
    plt.figure()
    plt.plot(cache_sizes, compulsories, 'r',
             label='Compulsory Misses', marker='.')
    plt.plot(cache_sizes, capacities, 'b', label='Capacity Misses', marker='.')
    plt.title('Compulsory vs Capacity Misses')
    plt.legend(loc='best')
    plt.xlabel('Cache Size')
    plt.ylabel('Misses')
    plt.xticks([i for i in range(0, mem_size+1, mem_size//8)])
    plt.yticks([i for i in range(0, len(memory) + 2, len(memory)//8)])

    # plot hit time vs cache size graph
    plt.figure()
    plt.plot(cache_sizes, times, 'b', marker='.', label='Hit Time')
    plt.title('Hit Time')
    plt.legend(loc='best')
    plt.xlabel('Cache Size')
    plt.ylabel('Approximate Time Taken (ms)')
    plt.xticks([i for i in range(0, mem_size+1, mem_size//8)])

    # calculate hit and miss percentages
    compulsories_percent = [(i / len(memory) * 100) for i in compulsories]
    capacities_percent = [(i / len(memory) * 100) for i in capacities]
    hit_percent = [(i / len(memory) * 100) for i in hit_rates]

    # plot hit and miss percentage vs cache size graph
    plt.figure()
    y_pos = np.arange(len(cache_sizes))
    plt.bar(y_pos, hit_percent, color='b', label='Hit Rate Percent')
    plt.bar(y_pos, compulsories_percent, bottom=hit_percent,
            color='r', label='Compulsory Miss Percent')
    plt.bar(y_pos, capacities_percent, bottom=[
            i+j for i, j in zip(hit_percent, compulsories_percent)], color='g', label='Capacity Miss Percent')
    plt.xticks(y_pos, cache_sizes)
    plt.legend(loc='best')
    plt.title('Hit and Miss Percentage')
    plt.xlabel('Cache Size')
    plt.ylabel('Percentage (%)')
    plt.show()


def main():

    # randomize values in memory and create memory with size 1024 bits
    random.seed(17)
    memory = [random.randrange(0, mem_size // block_size)
              for i in range(mem_size // block_size)]

    # power of 2 cache size [8, 16, 32, 64, 128, 256, 512, 1024]
    cache_sizes = [2**i for i in range(3, math.floor(math.log2(mem_size)) + 1)]

    times = []
    hit_rates = []
    compulsories = []
    capacities = []

    # for every value in cache_sizes, calculate and record hits, misses and time taken
    for cache_size in cache_sizes:
        cache = [-1 for i in range(cache_size // block_size)]
        returnVal = computeHit(memory, cache)
        times.append(returnVal[0])
        hit_rates.append(returnVal[1])
        compulsories.append(returnVal[2])
        capacities.append(returnVal[3])

    # for every cache size, print calculated results
    print("----------------------------------------")
    for i in range(len(cache_sizes)):
        print("Cache Size:\t\t %d" % cache_sizes[i])
        print("Approximate Hit Time:\t %d ms" % times[i])
        print("Hit Rate Percentage:\t %0.2f%%" %
              (hit_rates[i] / len(memory) * 100))
        print("Miss Rate Percentage:\t %0.2f%%" %
              (100 - (hit_rates[i] / len(memory) * 100)))
        print("Compulsory Misses:\t %0.2f%%" %
              (compulsories[i] / len(memory) * 100))
        print("Capacity Misses:\t %0.2f%%" %
              (capacities[i] / len(memory) * 100))
        print()

    # plot 3 graphs
    displayGraph(times, hit_rates, compulsories,
                 capacities, cache_sizes, memory)

    # create gui and ask memory and cache size
    gui = Gui.Gui()
    gui.guiCreate()
    x = gui.answer[0]
    y = gui.answer[1]

    # compute answer for user provided values
    random.seed(17)
    memory = [random.randrange(0, x // block_size)
              for i in range(x // block_size)]
    cache = [-1 for i in range(y // block_size)]
    returnVal = computeHit(memory, cache)
    print("----------------------------------------")
    print("Cache Size:\t\t %d" % y)
    print("Memory Size:\t\t %d" % x)
    print("Approximate Hit Time:\t %d ms" % returnVal[0])
    print("Hit Rate Percentage:\t %0.2f%%" %
          (returnVal[1] / len(memory) * 100))
    print("Miss Rate Percentage:\t %0.2f%%" %
          (100 - returnVal[1] / len(memory) * 100))
    print("Compulsory Misses:\t %0.2f%%" %
          (returnVal[2] / len(memory) * 100))
    print("Capacity Misses:\t %0.2f%%" %
          (returnVal[3] / len(memory) * 100))
    print()


if __name__ == "__main__":
    main()
