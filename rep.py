import sys

file_name = sys.argv[1]
with open(file_name, "r") as fp:
    lines = fp.readlines()
    for line in lines:
        if "TMS" in line:
            new_line = '            LOG.info("{}")'.format(line.strip())
            print new_line
        if line:
            print line.strip("\n")

