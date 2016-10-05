# -*- coding: utf-8 -*-
import click
import json
import os
import yaml
from .accounts import Account
from .archives import Archive
from .groups import Group
from .saved_searches import SavedSearch
from .search import Search
from .systems import System
from .users import User
from .utils import Utils
from os.path import expanduser
from time import sleep

# Fix Python 2.x vs 3.x.
try:
    bool(type(unicode))
    UNICODE_TYPE = unicode
except NameError:
    UNICODE_TYPE = str


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def json_dumps(dict, pretty=False):
    if pretty:
        return json.dumps(dict, indent=2)
    else:
        return json.dumps(dict)


def parse_payload(ctx, payload):
    if payload:
        try:
            json_object = json.loads(payload)
        except:
            ctx.fail("Payload is not in a JSON format.")
        return json_object


def parse_yml(ctx, path):
    with open(path, 'r') as stream:
        try:
            content = yaml.load(stream)
        except yaml.YAMLError as e:
            ctx.fail(e)
        return content


@click.version_option('1.0.0')
@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--debug', '-d', flag_value=True, default=False,
              help='Debug mode.')
@click.option('--pretty', '-p', flag_value=True, default=False,
              help='Prettify JSON output.')
@click.option('--token', '-t', type=UNICODE_TYPE,
              envvar='PAPERTRAIL_API_TOKEN',
              help='Papertrail API token.')
@click.option('--conf', '-c', type=UNICODE_TYPE,
              default="{0}/{1}".format(expanduser("~"), '.pypertrail.yml'),
              help='Path to config (~/.pypertrail.yml).')
@click.pass_context
def main(ctx, debug, pretty, token, conf):
    if not token:
        if os.path.isfile(conf):
            token = parse_yml(ctx, conf)['token']
        else:
            ctx.fail("""Token not found.
Token not found in PAPERTRAIL_API_TOKEN environment variable.
Token not found in -t/--token option.
Token not found in configuration file: {0}.""".format(conf))

    ctx.obj = {}
    ctx.obj['PRETTY'] = pretty if pretty else None
    ctx.obj['DEBUG'] = debug if debug else None
    ctx.obj['TOKEN'] = token if token else None


@main.group()
@click.pass_context
def accounts(ctx):
    pass


@accounts.command()  # noqa: F811
@click.pass_context
def list(ctx):
    """List account usage."""
    r = Account(ctx.obj['TOKEN'], ctx.obj['DEBUG']).list()
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@main.group()
@click.pass_context
def archives(ctx):
    pass


@archives.command()  # noqa: F811
@click.pass_context
def list(ctx):
    """List archive information."""
    r = Archive(ctx.obj['TOKEN'], ctx.obj['DEBUG']).list()
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@main.group()
@click.pass_context
def groups(ctx):
    pass


@groups.command()  # noqa: F811
@click.pass_context
def list(ctx):
    """List groups."""
    r = Group(ctx.obj['TOKEN'], ctx.obj['DEBUG']).list()
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@groups.command()  # noqa: F811
@click.pass_context
@click.argument('group_id')
def show(ctx, group_id):
    """Show a group."""
    r = Group(ctx.obj['TOKEN'], ctx.obj['DEBUG']).show(group_id)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@groups.command()  # noqa: F811
@click.pass_context
@click.argument('group_id')
def update(ctx, group_id):
    """Update a group."""
    r = Group(ctx.obj['TOKEN'], ctx.obj['DEBUG']).update(group_id)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@groups.command()  # noqa: F811
@click.pass_context
@click.argument('group_id')
def delete(ctx, group_id):
    """Delete a group."""
    r = Group(ctx.obj['TOKEN'], ctx.obj['DEBUG']).delete(group_id)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@main.group()
@click.pass_context
def saved_searches(ctx):
    pass


@saved_searches.command()  # noqa: F811
@click.pass_context
def list(ctx):
    """List saved_searches."""
    r = SavedSearch(ctx.obj['TOKEN'], ctx.obj['DEBUG']).list()
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@saved_searches.command()  # noqa: F811
@click.pass_context
@click.argument('saved_search_id')
def show(ctx, saved_search_id):
    """Show a saved search."""
    r = SavedSearch(ctx.obj['TOKEN'], ctx.obj['DEBUG']).show(saved_search_id)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@saved_searches.command()  # noqa: F811
@click.pass_context
@click.option('--payload', '-p', help='Parameters required by the API.')
def create(ctx, payload):
    """Create a saved search."""
    payload = parse_payload(ctx, payload)
    r = SavedSearch(ctx.obj['TOKEN'], ctx.obj['DEBUG']).create(payload)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@saved_searches.command()  # noqa: F811
@click.pass_context
@click.argument('saved_search_id')
@click.option('--payload', '-p', help='Parameters required by the API.')
def update(ctx, saved_search_id, payload):
    """Update a saved search."""
    payload = parse_payload(ctx, payload)
    r = SavedSearch(ctx.obj['TOKEN'], ctx.obj['DEBUG']).update(payload)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@saved_searches.command()  # noqa: F811
@click.pass_context
@click.argument('saved_search_id')
def delete(ctx, saved_search_id):
    """Delete a saved search."""
    r = SavedSearch(ctx.obj['TOKEN'], ctx.obj['DEBUG']).delete(saved_search_id)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@main.group()
@click.pass_context
def search(ctx):
    pass


@search.command()  # noqa: F811
@click.pass_context
@click.option('--query', '-q',
              type=UNICODE_TYPE,
              help='Terms to query.')
@click.option('--system', '-s',
              type=int,
              help='System to search.')
@click.option('--group', '-g',
              type=int,
              help='Group to search.')
@click.option('--min-time', '-e',
              type=int,
              help='Earliest time to search from.')
@click.option('--max-time', '-l',
              type=int,
              help='Latest time to search from.')
@click.option('--follow', '-f', 'follow',
              flag_value=True,
              default=False,
              help='Continue running and printing new events (off).')
@click.option('--delay', '-d',
              type=int,
              default=5,
              help='Delay between refresh (5).')
@click.option('--json', '-j',
              default=False,
              flag_value=True,
              help='Output raw JSON data (off).')
@click.option('--color', '-c',
              type=click.Choice(['program', 'system', 'all', 'off']),
              default='program',
              help='Attribute(s) to colorize based on (program).')
def events(ctx, query, system, group, min_time, max_time, follow, delay, json,
           color):
    """Search events."""

    search = Search(ctx.obj['TOKEN'], ctx.obj['DEBUG'])

    if follow and delay:
        while True:
            _events(ctx, search, query, system, group, min_time, max_time,
                    follow, delay, json, color)

            sleep(float(delay))
    else:
        _events(ctx, search, query, system, group, min_time, max_time, follow,
                delay, json, color)


def _events(ctx, search, query, system, group, min_time, max_time, follow,
            delay, json, color):

    r = search.events(query, system, group, None, None, min_time, max_time,
                      follow, delay)
    if json:
        click.echo(json_dumps(r, ctx.obj['PRETTY']))
    else:
        if r['events']:
            mapped = (Utils.format_event(e, color) for e in r['events'])
            click.echo('\n'.join(mapped))
        else:
            click.echo('No events found.')


@main.group()
@click.pass_context
def systems(ctx):
    pass


@systems.command()  # noqa: F811
@click.pass_context
def list(ctx):
    """List systems."""
    r = System(ctx.obj['TOKEN'], ctx.obj['DEBUG']).list()
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@systems.command()  # noqa: F811
@click.pass_context
@click.argument('system_id')
def show(ctx, system_id):
    """Show a system."""
    r = System(ctx.obj['TOKEN'], ctx.obj['DEBUG']).show(system_id)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@systems.command()  # noqa: F811
@click.pass_context
@click.option('--payload', '-p', help='Parameters required by the API.')
def create(ctx, payload):
    """Create a system."""
    payload = parse_payload(ctx, payload)
    r = System(ctx.obj['TOKEN'], ctx.obj['DEBUG']).create(payload)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@systems.command()  # noqa: F811
@click.pass_context
@click.argument('system_id')
@click.option('--payload', '-p', help='Parameters required by the API.')
def update(ctx, system_id, payload):
    """Update a system."""
    payload = parse_payload(ctx, payload)
    r = System(ctx.obj['TOKEN'], ctx.obj['DEBUG']).update(system_id, payload)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@systems.command()   # noqa: F811
@click.pass_context
@click.argument('system_id')
def delete(ctx, system_id):
    """Delete a system."""
    r = System(ctx.obj['TOKEN'], ctx.obj['DEBUG']).delete(system_id)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@systems.command()   # noqa: F811
@click.pass_context
@click.argument('system_id')
@click.option('--payload', '-p', help='Parameters required by the API.')
def join_group(ctx, system_id, payload):
    """Join a group."""
    payload = parse_payload(ctx, payload)
    r = System(ctx.obj['TOKEN'],
               ctx.obj['DEBUG']).join_group(system_id, payload)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@systems.command()   # noqa: F811
@click.pass_context
@click.argument('system_id')
@click.option('--payload', '-p', help='Parameters required by the API.')
def leave_group(ctx, system_id, payload):
    """Leave a group."""
    payload = parse_payload(ctx, payload)
    r = System(ctx.obj['TOKEN'],
               ctx.obj['DEBUG']).leave_group(system_id, payload)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@main.group()
@click.pass_context
def users(ctx):
    pass


@users.command()  # noqa: F811
@click.pass_context
def list(ctx):
    """List users."""
    r = User(ctx.obj['TOKEN'], ctx.obj['DEBUG']).list()
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@users.command()  # noqa: F811
@click.pass_context
@click.option('--payload', '-p', help='Parameters required by the API.')
def invite(ctx, payload):
    """Invite a user."""
    payload = parse_payload(ctx, payload)
    r = User(ctx.obj['TOKEN'], ctx.obj['DEBUG']).invite(payload)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


@users.command()  # noqa: F811
@click.pass_context
@click.argument('user_id')
def delete(ctx, user_id):
    """Delete a user."""
    r = User(ctx.obj['TOKEN'], ctx.obj['DEBUG']).delete(user_id)
    click.echo(json_dumps(r, ctx.obj['PRETTY']))


if __name__ == '__main__':
    main()
