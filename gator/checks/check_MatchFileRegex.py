"""Check that a file's contents match a specified regular expression."""

import argparse

from gator import checkers
from gator import constants
from gator import invoke


def get_parser():
    """Get a parser for the arguments provided on the command-line."""
    # create the parser with the default help formatter
    # use a new description since this is a stand-alone check
    parser = argparse.ArgumentParser(
        prog="MatchFileRegex",
        description="Check Provided by GatorGrader: MatchFileRegex",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Required Named Checker Arguments {{{

    required_group = parser.add_argument_group("required checker arguments")

    # FILE: the file
    # REQUIRED? Yes
    required_group.add_argument(
        "--file", type=str, help="file for checking", required=True
    )

    # DIRECTORY: the directory containing the file
    # REQUIRED? Yes
    required_group.add_argument(
        "--directory",
        type=str,
        metavar="DIR",
        help="directory with file for checking",
        required=True,
    )

    # REGEX: the regular expression that should match the command's output
    # REQUIRED? Yes
    required_group.add_argument(
        "--regex",
        type=str,
        help="regular expression that matches file contents",
        required=True,
    )

    # COUNT: the number of lines of output
    # REQUIRED? Yes
    required_group.add_argument(
        "--count", type=int, help="how many regex matches should exist", required=True
    )

    # }}}

    # Optional Named Checker Arguments {{{

    optional_group = parser.add_argument_group("optional check arguments")

    # EXACT: perform exact checking for commit counts (i.e,. "==" instead of ">=")
    # REQUIRED? No
    optional_group.add_argument(
        "--exact",
        help="equals instead of a minimum number",
        default=False,
        action="store_true",
    )

    optional_group.add_argument(
        "--reach",
        help="creates a higher goal for students to potentially reach",
        default=False,
        action="store_true",
    )

    # }}}
    return parser


def parse(args, parser=None):
    """Use the parser on the provided arguments."""
    return checkers.parse(get_parser, args, parser)


# pylint: disable=unused-argument
def act(main_parsed_arguments, check_remaining_arguments):
    """Perform the action for this check."""
    # extract the two arguments for this check:
    # --> fragment is the content that should appear in the file
    # --> file is the name of the file for which the search is conducted
    # --> directory is the name of the directory that should contain the specified file
    # --> count is required to specify the number of fragments to appear in the output
    # --> exact is optional, but will either be True or False and False by default
    check_parsed_arguments = parse(check_remaining_arguments)
    # Directly run the check since at least one of the argument's for it is mandatory.
    # This means that the use of check_MatchFileRegex would have already failed by this
    # point since argparse will exit the program if a command-line argument is not provided.
    regex = check_parsed_arguments.regex
    count = check_parsed_arguments.count
    file = check_parsed_arguments.file
    directory = check_parsed_arguments.directory
    exact = check_parsed_arguments.exact
    reach = check_parsed_arguments.reach
    return [
        invoke.invoke_all_regex_checks(
            regex, count, file, directory, constants.markers.Nothing, exact, reach
        )
    ]
