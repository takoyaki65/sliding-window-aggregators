#!/usr/bin/env python3

import run_utility as u

aggregators = [
                "bfinger2",
                "bfinger4",
                "bfinger8",
                "amta",
                "two_stacks_lite",
                "daba_lite",
              ]

degrees = [0]

base_window_sizes = [4*u.MB]

base_iterations = 10 * u.MILLION

bulk_sizes = [1, 256]

functions = { 
             "sum": (base_iterations, base_window_sizes),
             "geomean": (base_iterations, base_window_sizes),
             "bloom": (base_iterations/100, base_window_sizes),
            }

def main():
    u.run_bulk(aggregators, functions, degrees, bulk_sizes, 'bulk_evict')

if __name__ == "__main__":
    main()
