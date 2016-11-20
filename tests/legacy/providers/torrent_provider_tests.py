# coding=utf-8
# This file is part of Medusa.
#
# Medusa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Medusa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Medusa. If not, see <http://www.gnu.org/licenses/>.

"""Test TorrentProvider."""

from __future__ import print_function

import os

from medusa import app
from medusa.providers.generic_provider import GenericProvider
from medusa.providers.torrent.torrent_provider import TorrentProvider
from six import iteritems
from .generic_provider_tests import GenericProviderTests


class TorrentProviderTests(GenericProviderTests):
    """Test TorrentProvider."""

    def test___init__(self):
        self.assertEqual(TorrentProvider('Test Provider').provider_type, GenericProvider.TORRENT)

    def test_is_active(self):
        test_cases = {
            (False, False): False,
            (False, None): False,
            (False, True): False,
            (None, False): False,
            (None, None): False,
            (None, True): False,
            (True, False): False,
            (True, None): False,
            (True, True): True,
        }

        for ((use_torrents, enabled), result) in iteritems(test_cases):
            app.USE_TORRENTS = use_torrents

            provider = TorrentProvider('Test Provider')
            provider.enabled = enabled

            self.assertEqual(provider.is_active(), result)

    def test__get_size(self):
        items_list = [
            None, {}, {'size': None}, {'size': ''}, {'size': '0'}, {'size': '123'}, {'size': '12.3'}, {'size': '-123'},
            {'size': '-12.3'}, {'size': '1100000'}, {'size': 0}, {'size': 123}, {'size': 12.3}, {'size': -123},
            {'size': -12.3}, {'size': 1100000}, [], [None], [1100000], [None, None, None], [None, None, ''],
            [None, None, '0'], [None, None, '123'], [None, None, '12.3'], [None, None, '-123'], [None, None, '-12.3'],
            [None, None, '1100000'], [None, None, 0], [None, None, 123], [None, None, 12.3], [None, None, -123],
            [None, None, -12.3], [None, None, 1100000], (), (None, None, None), (None, None, ''), (None, None, '0'),
            (None, None, '123'), (None, None, '12.3'), (None, None, '-123'), (None, None, '-12.3'),
            (None, None, '1100000'), '', '0', '123', '12.3', '-123', '-12.3', '1100000', 0, 123, 12.3, -123, -12.3,
            1100000
        ]
        results_list = [
            -1, -1, -1, -1, 0, 123, -1, -123, -1, 1100000, -1, -1, -1, -1, -1, 1100000, -1, -1, -1, -1, -1, 0, 123, -1,
            -123, -1, 1100000, -1, -1, -1, -1, -1, 1100000, -1, -1, -1, 0, 123, -1, -123, -1, 1100000, -1, -1, -1, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1
        ]

        unicode_items_list = [
            {u'size': None}, {u'size': u''}, {u'size': u'0'}, {u'size': u'123'}, {u'size': u'12.3'}, {u'size': u'-123'},
            {u'size': u'-12.3'}, {u'size': u'1100000'}, {u'size': 0}, {u'size': 123}, {u'size': 12.3}, {u'size': -123},
            {u'size': -12.3}, {u'size': 1100000}, [None, None, u''], [None, None, u'0'], [None, None, u'123'],
            [None, None, u'12.3'], [None, None, u'-123'], [None, None, u'-12.3'], [None, None, u'1100000'],
            (None, None, u''), (None, None, u'0'), (None, None, u'123'), (None, None, u'12.3'), (None, None, u'-123'),
            (None, None, u'-12.3'), (None, None, u'1100000'), u'', u'0', u'123', u'12.3', u'-123', u'-12.3', u'1100000'
        ]
        unicode_results_list = [
            -1, -1, 0, 123, -1, -123, -1, 1100000, -1, -1, -1, -1, -1, 1100000, -1, 0, 123, -1, -123, -1, 1100000, -1,
            0, 123, -1, -123, -1, 1100000, -1, -1, -1, -1, -1, -1, -1
        ]

        self.assertEqual(
            len(items_list), len(results_list),
            'Number of parameters (%d) and results (%d) does not match' % (len(items_list), len(results_list))
        )

        self.assertEqual(
            len(unicode_items_list), len(unicode_results_list),
            'Number of parameters (%d) and results (%d) does not match' % (
                len(unicode_items_list), len(unicode_results_list))
        )

        for (index, item) in enumerate(items_list):
            self.assertEqual(TorrentProvider('Test Provider')._get_size(item), results_list[index])

        for (index, item) in enumerate(unicode_items_list):
            self.assertEqual(TorrentProvider('Test Provider')._get_size(item), unicode_results_list[index])

    def test__get_storage_dir(self):
        test_cases = [
            None, 123, 12.3, '', os.path.join('some', 'path', 'to', 'folder')
        ]

        for torrent_dir in test_cases:
            app.TORRENT_DIR = torrent_dir

            self.assertEqual(TorrentProvider('Test Provider')._get_storage_dir(), torrent_dir)
