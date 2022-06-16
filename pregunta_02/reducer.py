#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    curkey=None
    max=0

    for line in sys.stdin:

        row=line.split("\t")
        key=row[0]
        value=int(row[1])

        if curkey==key:
            if value>max:
                max=value
            else:
                value=max
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, max))

            curkey=key
            max=value

    sys.stdout.write("{}\t{}\n".format(curkey, max))
