import argparse

def parse_command_line():
    parser = argparse.ArgumentParser("Input names surroneded by \" \", if wish to save result use the -S or --save flag.")
    parser.add_argument('names', metavar='N', type=str, nargs="+",help="A name or a list of names of inviduals.")
    parser.add_argument("--save" ) # TODO: An argument with -s and --save to save the search to content
