"""Tests for the gatorgrader module"""

import pytest

import gatorgrader

VERIFIED = True
NOT_VERIFIED = False


@pytest.fixture
def no_gg_args():
    """Return no command-line arguments"""
    return []


@pytest.fixture
def verifiable_gg_args():
    """Return arguments that are verifiable"""
    return ['--directories', 'D', 'F', 'G', '--checkfiles', 'a', 'b', 'c']


@pytest.fixture
def not_verifiable_gg_args():
    """Return arguments that are verifiable"""
    return ['--directories', 'D', 'F', 'G', '--checkfiles', 'a', 'b']


def test_default_argument_values_correct(no_gg_args):
    """The default command-line arguments are correct"""
    gg_arguments = gatorgrader.parse_gatorgrader_arguments(no_gg_args)
    gatorgrader_args_verified = gatorgrader.verify_gatorgrader_arguments(
        gg_arguments)
    assert gatorgrader_args_verified == VERIFIED


def test_gatorgrader_verified(verifiable_gg_args):
    """Run gatorgrader with verifiable arguments and it is verified"""
    gg_arguments = gatorgrader.parse_gatorgrader_arguments(verifiable_gg_args)
    gg_args_verified = gatorgrader.verify_gatorgrader_arguments(gg_arguments)
    assert gg_args_verified == VERIFIED


def test_gatorgrader_not_verified(not_verifiable_gg_args):
    """Run gatorgrader with not verifiable arguments and it is not verified"""
    gg_arguments = gatorgrader.parse_gatorgrader_arguments(
        not_verifiable_gg_args)
    gg_args_verified = gatorgrader.verify_gatorgrader_arguments(gg_arguments)
    assert gg_args_verified == NOT_VERIFIED


def test_gatorgrader_home_is_set():
    """ Ensure that the gatorgrader_HOME environment variable is set"""
    gatorgrader_home = gatorgrader.get_gatorgrader_home()
    assert gatorgrader_home is not None


def test_gatorgrader_home_verification_working_verified():
    """Run gatorgrader and checks that gatorgrader_HOME verification is working """
    gatorgrader_home_verified = gatorgrader.verify_gatorgrader_home(
        "/home/gkapfham/")
    assert gatorgrader_home_verified == VERIFIED


def test_gatorgrader_home_verification_working_notverified():
    """Run gatorgrader and checks that gatorgrader_HOME verification is working """
    gatorgrader_home_verified = gatorgrader.verify_gatorgrader_home(
        "/home/gkapfham")
    assert gatorgrader_home_verified == NOT_VERIFIED