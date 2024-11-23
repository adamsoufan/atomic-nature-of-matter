import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # Accept pixels (int), tau (float), delta (float), and pic (Picture)
    # as command-line arguments.
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    pic = Picture(sys.argv[4])

    # Construct BlobFinder object bf for the frame pic and from it get a list of
    # beads prevBeads that have at least pixels pixels.
    bf = BlobFinder(pic, tau)
    prevBeads = bf.getBeads(pixels)

    for i in range(5, len(sys.argv)):
        # For each frame starting at sys.argv[5]...

        # Construct a BlobFinder object and from it get a list of
        # beads currBeads that have at least pixels pixels.
        pic = Picture(sys.argv[i])
        bf = BlobFinder(pic, tau)
        currBeads = bf.getBeads(pixels)

        # For each bead currBead in currBeads, find a bead prevBead from prevBeads that
        # is no further than delta and is closest to to currBead, and if such a bead is found,
        # write its distance to currBead.
        for currBead in currBeads:

            # Set distance to 1000000. This is used to compare the distance from the first
            # prevBead to currBead since there are no distances to compare to.
            distance = 1000000

            for prevBead in prevBeads:
                # For each prevBead in prevBeads...

                # If the distance from prevBead to currBead is less than or equal
                # to delta and less than distance, then the new shortest distance is
                # prevBead.distanceTo(currBead).
                if delta >= prevBead.distanceTo(currBead) < distance:
                    distance = prevBead.distanceTo(currBead)

            # If distance is less than 1000000, then there is such a bead that the
            # distance from prevBead to currBead is less than or equal to delta and less
            # than distance. Write its distance to currBead to standard output.
            if distance < 1000000:
                stdio.writef('%.4f\n', distance)

        # Write a newline character.
        stdio.writeln()

        # Set prevBeads to currBeads.
        prevBeads = currBeads


if __name__ == '__main__':
    main()