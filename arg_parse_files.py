import argparse
import os
import glob


def main():
    # Does not currently have support to read files from folders recursively
    parser = argparse.ArgumentParser(description='Read in a file or set of files, and return the result.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('path', nargs='+',
                        help='Path of a file or a folder of files.')
    parser.add_argument('-r', '--recursive', action='store_true',
                        default=False, help='Search through subfolders')
    parser.add_argument('-e', '--extension', default='',
                        help='File extension to filter by.')
    args = parser.parse_args()

    # Parse paths
    full_paths = [os.path.join(os.getcwd(), path) for path in args.path]
    files = set()
    for path in full_paths:
        if os.path.isfile(path):
            fileName, fileExt = os.path.splitext(path)
            if args.extension == '' or args.extension == fileExt:
                files.add(path)
        else:
            if (args.recursive):
                full_paths += glob.glob(path + '/*')

    for f in files:
        print(f)


if __name__ == '__main__':
    main()
