# -*- coding: utf-8 -*-
#
# Copyright 2015 OpenMarket Ltd
# Copyright 2018 New Vector Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from canonicaljson import (
    encode_canonical_json,
    encode_pretty_printed_json,
)

from frozendict import frozendict

import unittest


class TestCanonicalJson(unittest.TestCase):

    def test_encode_canonical(self):
        self.assertEquals(encode_canonical_json({}), b'{}')

        # non-ascii should come out utf8-encoded.
        self.assertEquals(encode_canonical_json({
                u"la merde amusée": u"💩",
        }), b'{"la merde amus\xc3\xa9e":"\xF0\x9F\x92\xA9"}')

    def test_encode_pretty_printed(self):
        self.assertEquals(encode_pretty_printed_json({}), b'{}')

    def test_frozen_dict(self):
        self.assertEquals(
            encode_canonical_json(frozendict({"a": 1})),
            b'{"a":1}',
        )
        self.assertEquals(
            encode_pretty_printed_json(frozendict({"a": 1})),
            b'{\n    "a": 1\n}')

    def test_unknown_type(self):
        class Unknown(object):
            pass
        unknown_object = Unknown()
        with self.assertRaises(Exception):
            encode_canonical_json(unknown_object)
