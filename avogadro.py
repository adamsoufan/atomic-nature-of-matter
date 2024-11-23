import math
import stdio


def main():
    # Initialize ETA, RHO, T, and R to appropriate values.
    ETA = 9.135e-4
    RHO = 0.5e-6
    T = 297
    R = 8.31457

    # Set n, the number of displacements, to 0.
    n = 0

    # Calculate var as the sum of the squares of the n displacements (each converted
    # from pixels to meters) read from standard input.
    var = 0.0
    while not stdio.isEmpty():
        displacement = (stdio.readFloat() * 0.175e-6) ** 2
        var += displacement

        # For each displacement read, increment n by 1.
        n += 1

    # Divide var by 2 * n.
    var /= 2 * n

    # Estimate Boltzmann's constant as 6 * pi * var * ETA * RHO / T
    k = 6 * math.pi * var * ETA * RHO / T

    # Estimate Avogradro's constant as R / K.
    NA = R / k

    # Write to standard outputs the two constants in scientific notation and
    # separated by a space.
    stdio.writef('%e %e', k, NA)


if __name__ == '__main__':
    main()