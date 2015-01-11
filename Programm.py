__author__ = 'Ulrich Kaiser'

import os
import Comparer

dllPath = os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"], "Desktop/VSTPlugins 64 bit")


def main():
    print(Comparer.writeinfos(dllPath))


if __name__ == "__main__":
    main()
