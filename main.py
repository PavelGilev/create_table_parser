import internal.transform as trm
from rich.traceback import install
import sys
import os
import logging as log
install(show_locals=True)

log.basicConfig(level=log.INFO,filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


class mainError(Exception):

    def __str__(self):
        return "Not Enought args. Specify input and output file"


class file_doesnt_exist(Exception):

    def __str__(self, path):
        return "File %s doesn't exist" % path


if len(sys.argv) < 3:
    raise mainError()

for i in range(2):
    if not os.path.exists(sys.argv[i]):
        raise file_doesnt_exist(sys.argv[i])

log.info("Transform file")
trm.transform(sys.argv[1], sys.argv[2])
