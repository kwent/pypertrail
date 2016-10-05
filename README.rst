pypertrail
==========

|pypi| |travis| |doc| |pyup|

Python wrapper library and CLI for papertrail API.

Installation
------------

Install using pip:

.. code:: bash

    $ pip install pypertrail

Requirements
------------

- Python 2.6, 2.7, 3.3, 3.4, or 3.5
- A Papertrail account

Library
-------

Accounts
~~~~~~~~

.. code:: python

    import os
    from pypertrail.accounts import Account

    accounts = Account(os.environ['PAPERTRAIL_API_TOKEN'])

    # List account usage
    accounts.list()

Archives
~~~~~~~~

.. code:: python

    import os
    from pypertrail.archives import Archive

    archives = Archive(os.environ['PAPERTRAIL_API_TOKEN'])

    # List archive information
    archives.list()

Groups
~~~~~~

.. code:: python

    import os
    from pypertrail.groups import Group

    groups = Group(os.environ['PAPERTRAIL_API_TOKEN'])

    # List groups
    groups.list()

    # Show a group
    groups.show(group_id)

    # Update a group
    groups.update(group_id)

    # Delete a group
    groups.delete(group_id)

Saved searches
~~~~~~~~~~~~~~

.. code:: python

    import os
    from pypertrail.saved_searches import SavedSearch

    saved_searches = SavedSearch(os.environ['PAPERTRAIL_API_TOKEN'])

    # List saved_searches
    saved_searches.list()

    # Show a saved search
    saved_searches.show(saved_search_id)

    # Create a saved search
    payload = {'name':'my_query', 'query':'sshd'}
    saved_searches.create(payload)

    # Update a saved search
    payload = {'search[query]':'another_query'}
    saved_searches.update(payload)

    # Delete a saved search
    saved_searches.delete(saved_search_id)

Search
~~~~~~~~~~~~~~

.. code:: python

    import os
    from pypertrail.search import Search

    search = Search(os.environ['PAPERTRAIL_API_TOKEN'])

    # Search events
    search.events("sshd")

Systems
~~~~~~

.. code:: python

    import os
    from pypertrail.systems import System

    systems = Search(os.environ['PAPERTRAIL_API_TOKEN'])

    # List systems
    systems.list()

    # Show a system
    systems.show(system_id)

    # Create a system
    payload = {'system[name]':'foo', 'system[hostname]':'bar', 'destination_port':46865}
    systems.create(payload)

    # Update a system
    payload = {'system[name]':'another_name'}
    systems.update(system_id, payload)

    # Delete a system
    systems.delete(system_id)

    # Join a group
    payload = {'group_id':10}
    systems.join_group(system_id, payload)

    # Leave a group
    payload = {'group_id':10}
    systems.leave_group(system_id, payload)

Users
~~~~~

.. code:: python

    import os
    from pypertrail.users import User

    users = User(os.environ['PAPERTRAIL_API_TOKEN'])

    # List users
    users.list()

    # Invite a user
    payload = {'email':'contact@quent.in', 'read_only':'true'}
    users.invite(payload)

    # Delete a user
    users.delete(user_id)

CLI
---

CLI Authentication
~~~~~~~~~~~~~~~~~~

Via environment variables:

.. code:: bash

    $ export PAPERTRAIL_API_TOKEN=my_token
    $ pypertrail users list

Via implicit ~/.pypertrail.yml:

.. code:: bash

    $ echo "token: my_token" > ~/.pypertrail.yml
    $ pypertrail users list

Via (--conf/-c) option:

.. code:: bash

    $ echo "token: my_token" > /path/to/config
    $ pypertrail --conf /path/to/config users list

Via (--token/-t) option:

.. code:: bash

    $ pypertrail --token my_token users list

Subcommands
~~~~~~~~~~~

.. code:: plain

    Usage: pypertrail.py [OPTIONS] COMMAND [ARGS]...

    Options:
      -d, --debug       Debug mode.
      -p, --pretty      Prettify JSON output.
      -t, --token TEXT  Papertrail API token.
      -c, --conf TEXT   Path to config (~/.pypertrail.yml).
      --version         Show the version and exit.
      -h, --help        Show this message and exit.

    Commands:
      accounts
      archives
      groups
      saved_searches
      search
      systems
      users

Accounts
~~~~~~~~

.. code:: plain

    Usage: papertrail.py accounts [OPTIONS] COMMAND [ARGS]...

    Options:
      -h, --help  Show this message and exit.

    Commands:
      list  List account usage

Examples:

.. code:: bash

    $ pypertrail --pretty accounts list


Archives
~~~~~~~~

.. code:: plain

    Usage: papertrail.py archives [OPTIONS] COMMAND [ARGS]...

    Options:
      -h, --help  Show this message and exit.

    Commands:
      list  List archive information

Examples:

.. code:: bash

    $ pypertrail --pretty archives list

Saved searches
~~~~~~~~~~~~~~

.. code:: plain

    Usage: cli.py saved_searches [OPTIONS] COMMAND [ARGS]...

    Options:
      -h, --help  Show this message and exit.

    Commands:
      create  Create a saved search
      delete  Delete a saved search
      list    List saved_searches
      show    Show a saved search
      update  Update a saved search

Examples:

.. code:: bash

    $ pypertrail saved_searches create --payload '{"search[name]":"foo", "search[query]":"bar"}'
    $ pypertrail saved_searches delete 1
    $ pypertrail saved_searches list
    $ pypertrail saved_searches show 1
    $ pypertrail saved_searches update 1 --payload '{"search[query]":"another_query"}'


Groups
~~~~~~

.. code:: plain

    Usage: papertrail.py groups [OPTIONS] COMMAND [ARGS]...

    Options:
    -h, --help  Show this message and exit.

    Commands:
    delete  Delete a group
    list    List groups
    show    Show a group
    update  Update a group

Examples:

.. code:: bash

    $ pypertrail groups delete 1
    $ pypertrail groups list
    $ pypertrail groups show 1
    $ pypertrail groups update 1 --payload '{"group[name]":"another_name"}'


Search
~~~~~~

.. code:: plain

    Usage: papertrail.py search events [OPTIONS]

      Search events

    Options:
      -q, --query TEXT                Terms to query.
      -s, --system INTEGER            System to search.
      -g, --group INTEGER             Group to search.
      -e, --min-time INTEGER          Earliest time to search from.
      -l, --max-time INTEGER          Latest time to search from.
      -f, --follow                    Continue running and printing new events
                                      (off).
      -d, --delay INTEGER             Delay between refresh (5).
      -j, --json                      Output raw JSON data (off).
      -c, --color [program|system|all|off]
                                      Attribute(s) to colorize based on (program).
      -h, --help                      Show this message and exit.

Examples:

.. code:: bash

    $ pypertrail search events
    $ pypertrail search events --follow
    $ pypertrail search events --follow --color program
    $ pypertrail search events --follow --query sshd
    $ pypertrail search events --follow --json

Systems
~~~~~~~

.. code:: plain

    Usage: papertrail.py systems [OPTIONS] COMMAND [ARGS]...

    Options:
      -h, --help  Show this message and exit.

    Commands:
      create       Create a saved search
      delete       Delete a system
      join_group   Join a group
      leave_group  Leave a group
      list         List systems
      show         Show a system
      update       Update a system

Examples:

.. code:: bash

    $ pypertrail systems create --payload '{"system[name]":"foo", "system[hostname]":"bar", "destination_port":46865}'
    $ pypertrail systems delete 1
    $ pypertrail systems join_group 1 --payload '{"group_id":10}'
    $ pypertrail systems leave_group 1 --payload '{"group_id":10}'
    $ pypertrail systems list
    $ pypertrail systems show 1
    $ pypertrail systems update 1 --payload '{"system[name]":"another_name"}'

Users
~~~~~

.. code:: plain

    Usage: papertrail.py users [OPTIONS] COMMAND [ARGS]...

    Options:
      -h, --help  Show this message and exit.

    Commands:
      delete  Delete a user
      invite  Invite a user
      list    List users

Examples:

.. code:: bash

    $ pypertrail users delete 1
    $ pypertrail users invite --payload '{"email":"contact@quent.in", "read_only":true}'
    $ pypertrail users list

Documentation
=============

- https://pypertrail.readthedocs.io
- http://help.papertrailapp.com/kb/how-it-works/http-api

History
=======

View the `changelog`_

Authors
=======

-  `Quentin Rousseau`_

License
=======

.. code:: plain

    Copyright (c) 2016 Quentin Rousseau <contact@quent.in>

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.

.. _changelog: https://github.com/kwent/pypertrail/blob/master/HISTORY.rst
.. _Quentin Rousseau: https://github.com/kwent

.. |pypi| image:: https://img.shields.io/pypi/v/pypertrail.svg
   :target: https://pypi.python.org/pypi/pypertrail
.. |travis| image:: https://img.shields.io/travis/kwent/pypertrail.svg
   :target: https://travis-ci.org/kwent/pypertrail
.. |doc| image:: https://readthedocs.org/projects/pypertrail/badge/?version=latest
   :target: https://pypertrail.readthedocs.io/en/latest/?badge=latest
.. |pyup| image:: https://pyup.io/repos/github/kwent/pypertrail/shield.svg
   :target: https://pyup.io/repos/github/kwent/pypertrail/
