# -*- coding: utf-8 -*-
#
# Copyright © 2008  Red Hat, Inc. All rights reserved.
#
# This copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the GNU
# General Public License v.2.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY expressed or implied, including the
# implied warranties of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.  You should have
# received a copy of the GNU General Public License along with this program;
# if not, write to the Free Software Foundation, Inc., 51 Franklin Street,
# Fifth Floor, Boston, MA 02110-1301, USA. Any Red Hat trademarks that are
# incorporated in the source code or documentation are not subject to the GNU
# General Public License and may only be used or replicated with the express
# permission of Red Hat, Inc.
#
# Author(s): Toshio Kuratomi <tkuratom@redhat.com>
#
'''Module to provide a library interface to the package database.'''

### FIXME: Functionality to merge:
# cvs-int's CVSROOT/admin/pkgdb-client

### FIXME: when porting to py3k syntax, no need for try: except
# pylint: disable-msg=W0403
try:
    from .baseclient import BaseClient
except SyntaxError:
    from baseclient import BaseClient
# pylint: enable-msg=W0403

class PackageDBClient(BaseClient):
    '''Provide an easy to use interface to the PackageDB.'''
    def __init__(self, base_url='https://admin.fedoraproject.org/pkgdb/',
            *args, **kwargs):
        '''Create the PackageDBClient.

        Keyword Arguments:
        :base_url: Base of every URL used to contact the server.  Defalts to
            the Fedora PackageDB instance.
        :useragent: useragent string to use.  If not given, default to
            "Fedora BaseClient/VERSION"
        :debug: If True, log debug information
        :username: username for establishing authenticated connections
        :password: password to use with authenticated connections
        :session_cookie: user's session_cookie to connect to the server
        :cache_session: if set to true, cache the user's session cookie on the
            filesystem between runs.
        '''
        super(PackageDBClient, self).__init__(base_url, args, kwargs)

    def get_owners(self, package, collection=None, collection_ver=None):
        '''Retrieve the ownership information for a package.

        URL: Same information as /packages/name/%s

        Arguments:
        :package: Name of the package to retrieve package information about.
        :collection: Limit the returned information to this collection
            ('Fedora', 'EPEL', OLPC', etc)
        :collection_ver: If collection is specified, further limit to this
            version of the collection.

        Returns: dict of ownership information for the package.
        '''
        method = '/packages/name/%s' % package
        if collection:
            method = method + '/' + collection
            if collection_ver:
                method = method + '/' + collection_ver
        ###FIXME: Really should reformat the data so we show either a
        # dict keyed by collection + version or
        # list of collection, version, owner
        return self.send_request(method)
