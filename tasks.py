import os
from subprocess import call
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(CURR_DIR, "src")
TEST_DIR = os.path.join(CURR_DIR,"test")

UNIT_TEST_DIR = os.path.join(CURR_DIR, "test", "unit")
COV_PATH = os.path.join(CURR_DIR, ".coveragerc")
INTEGRATION_TEST_DIR = os.path.join(CURR_DIR, "test", "integration")


@task
def style(_):
    call(f"pycodestyle {SRC_DIR} --ignore=E501", shell=True)
    call(f"pycodestyle {TEST_DIR} --ignore=E501", shell=True)


@task
def lint(_):
    call(f"pylint {SRC_DIR}", shell=True)
    call(f"pylint {TEST_DIR}", shell=True)


@task
def unit_test(_):
    call(f"pytest --cov={SRC_DIR} {UNIT_TEST_DIR} --cov-config={COV_PATH}", shell=True)


@task
def integration_test(_):
    call(f"pytest {INTEGRATION_TEST_DIR}", shell=True)
