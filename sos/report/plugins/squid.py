# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.report.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin


class Squid(Plugin):

    short_desc = 'Squid caching proxy'

    plugin_name = 'squid'
    profiles = ('webserver', 'services', 'sysmgmt')


class RedHatSquid(Squid, RedHatPlugin):

    files = ('/etc/squid/squid.conf',)
    packages = ('squid',)

    def setup(self):
        self.add_copy_spec([
            "/etc/squid/squid.conf",
            "/var/log/squid/access.log*",
            "/var/log/squid/cache.log*",
            "/var/log/squid/squid.out*"
        ])


class DebianSquid(Squid, DebianPlugin, UbuntuPlugin):

    plugin_name = 'squid'
    files = ('/etc/squid/squid.conf',)
    packages = ('squid',)

    def setup(self):
        self.add_copy_spec([
            "/etc/squid/squid.conf",
            "/var/log/squid/*",
            "/etc/squid-deb-proxy",
            "/var/log/squid-deb-proxy/*",
        ])

# vim: set et ts=4 sw=4 :
