# Read in the file
def renpy_tab_check(args):
    with open(args, 'r') as file:
        # reads the file
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('\t', ' '*8)

    # Write the file out again
    with open(args, 'w') as file:
        file.write(filedata)


if __name__ == "__main__":
    import glob

    for filename in glob.glob('*.rpy'):
        renpy_tab_check(filename)
        print(filename, "has been corrected for tabs")
