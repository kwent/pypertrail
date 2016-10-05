#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pypertrail
----------------------------------

Tests for `pypertrail` module.
"""


import sys
import unittest
from click.testing import CliRunner

from pypertrail import cli


class TestPypertrail(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_main_output(self):
        runner = CliRunner()
        r = runner.invoke(cli.main)
        assert r.exit_code == 0
        assert '-d, --debug       Debug mode.' in r.output
        assert '-p, --pretty      Prettify JSON output.' in r.output
        assert '-t, --token TEXT  Papertrail API token.' in r.output
        assert '-c, --conf TEXT   Path to config (~/.pypertrail.yml).' in r.output  # noqa: E501
        assert '--version         Show the version and exit.' in r.output
        assert '-h, --help        Show this message and exit.' in r.output
        assert 'accounts' in r.output
        assert 'archives' in r.output
        assert 'groups' in r.output
        assert 'saved_searches' in r.output
        assert 'search' in r.output
        assert 'systems' in r.output
        assert 'users' in r.output

    def test_accounts_output(self):
        runner = CliRunner()
        r = runner.invoke(cli.accounts)
        assert r.exit_code == 0
        assert 'list  List account usage.' in r.output

    def test_archives_output(self):
        runner = CliRunner()
        r = runner.invoke(cli.archives)
        assert r.exit_code == 0
        assert 'list  List archive information.' in r.output

    def test_groups_output(self):
        runner = CliRunner()
        r = runner.invoke(cli.groups)
        assert r.exit_code == 0
        assert 'delete  Delete a group.' in r.output
        assert 'list    List groups.' in r.output
        assert 'show    Show a group.' in r.output
        assert 'update  Update a group.' in r.output

    def test_saved_searches_output(self):
        runner = CliRunner()
        r = runner.invoke(cli.saved_searches)
        assert r.exit_code == 0
        assert 'create  Create a saved search.' in r.output
        assert 'delete  Delete a saved search.' in r.output
        assert 'list    List saved_searches.' in r.output
        assert 'show    Show a saved search.' in r.output
        assert 'update  Update a saved search.' in r.output

    def test_search_output(self):
        runner = CliRunner()
        r = runner.invoke(cli.search)
        assert r.exit_code == 0
        assert 'events  Search events.' in r.output

    def test_search_events_output(self):
        runner = CliRunner()
        r = runner.invoke(cli.search, ['events', '--help'])
        assert r.exit_code == 0
        assert '-q, --query TEXT                Terms to query.' in r.output
        assert '-s, --system INTEGER            System to search.' in r.output
        assert '-g, --group INTEGER             Group to search.' in r.output
        assert '-e, --min-time INTEGER          Earliest time to search from.' in r.output  # noqa: E501
        assert '-l, --max-time INTEGER          Latest time to search from.' in r.output  # noqa: E501
        assert "-f, --follow                    Continue running and printing new events" in r.output  # noqa: E501
        assert '-d, --delay INTEGER             Delay between refresh (5).' in r.output  # noqa: E501
        assert '-j, --json                      Output raw JSON data (off).' in r.output  # noqa: E501
        assert "-c, --color [program|system|all|off]" in r.output

    def test_systems_output(self):
        runner = CliRunner()
        r = runner.invoke(cli.systems)
        assert r.exit_code == 0
        assert 'create       Create a system.' in r.output
        assert 'delete       Delete a system.' in r.output
        assert 'join_group   Join a group.' in r.output
        assert 'leave_group  Leave a group.' in r.output
        assert 'list         List systems.' in r.output
        assert 'show         Show a system.' in r.output
        assert 'update       Update a system.' in r.output

    def test_users_output(self):
        runner = CliRunner()
        r = runner.invoke(cli.users)
        assert r.exit_code == 0
        assert 'delete  Delete a user.' in r.output
        assert 'invite  Invite a user.' in r.output
        assert 'list    List users.' in r.output

if __name__ == '__main__':
    sys.exit(unittest.main())
