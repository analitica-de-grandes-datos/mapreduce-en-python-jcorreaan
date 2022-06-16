#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        credit_type=line.split(",")
        sys.stdout.write("{}\t{}\n".format(credit_type[3], credit_type[4]))
