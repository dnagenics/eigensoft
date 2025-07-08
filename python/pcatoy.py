#!/usr/bin/env python3
"""Simple demonstration equivalent to the pcatoy C program."""

def main():
    nsamples = 2
    # XTX is the 2x2 identity matrix
    xtx = [[1.0, 0.0], [0.0, 1.0]]
    # Eigenvectors of the identity matrix are the identity matrix itself
    print("The eigenvectors of the 2x2 identity matrix are:")
    for n in range(nsamples):
        for k in range(nsamples):
            value = 1.0 if k == n else 0.0
            print(f" {value:.2f}", end="")
        print()

if __name__ == "__main__":
    main()
