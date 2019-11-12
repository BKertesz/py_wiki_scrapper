import argparse

def create_parser_command_line():
    parser = argparse.ArgumentParser("Input names surroneded by \" \", if wish to save result use the -S or --save flag.")
    parser.add_argument('names', metavar='N', type=str, nargs="+",help="A name or a list of names of inviduals.")
    return parser

def parse_arguments(parser):
    return parser.parse_args()

retrive_arguments = lambda: parse_arguments(create_parser_command_line()).names