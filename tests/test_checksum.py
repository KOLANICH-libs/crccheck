""" Unit tests for checksum module.

  License::

    Copyright (C) 2015-2016 by Martin Scharrer <martin@scharrer-online.de>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import sys
from tests import TestCase, randbytes

from crccheck import checksum
from crccheck.base import CrccheckError
from crccheck.checksum import ALLCHECKSUMCLASSES, Checksum32, Checksum, ChecksumXor


class TestChecksum(TestCase):

    def test_allchecksums_bigendian(self):
        for checksumclass in ALLCHECKSUMCLASSES:
            with self.subTest(checksumclass=checksumclass):
                checksumclass.selftest(byteorder='big')

    def test_allchecksums_littleendian(self):
        for checksumclass in ALLCHECKSUMCLASSES:
            with self.subTest(checksumclass=checksumclass):
                checksumclass.selftest(byteorder='little')

    # noinspection PyProtectedMember
    def test_allchecksums_fail(self):
        with self.assertRaises(CrccheckError):
            checksumclass = ALLCHECKSUMCLASSES[0]
            checksumclass.selftest(checksumclass._check_data, ~checksumclass._check_result)

    def test_generator(self):
        Checksum32.calc((n for n in range(0, 255)))

    def test_list1(self):
        Checksum32.calc([n for n in range(0, 255)])

    def test_list2(self):
        Checksum32.calc([n for n in range(0, 255)], 1)

    def test_bytearray1(self):
        Checksum32.calc(bytearray.fromhex("12345678909876543210"))

    def test_bytes(self):
        if sys.version_info < (3, 3, 0):  # pragma: no cover
            raise self.skipTest("")
        Checksum32.calc(bytes.fromhex("12345678909876543210"))

    def test_string1(self):
        if sys.version_info < (3, 3, 0):  # pragma: no cover
            raise self.skipTest("")
        Checksum32.calc(b"Teststring")

    def test_string3(self):
        if sys.version_info < (3, 3, 0):  # pragma: no cover
            raise self.skipTest("")
        Checksum32.calc("Teststring".encode(), )

    def test_general_checksum_valid_width(self):
        """ Checksum()

            Should allow for any positive width
            which is a multiple of 8.
        """
        for n in range(8, 129, 8):
            Checksum(n)

    def test_general_checksum_invalid_width(self):
        for n in (0, 1, 7, 9, 33):
            with self.assertRaises(ValueError):
                Checksum(n)

    def test_general_checksum_ident(self):
        data = randbytes(1024)
        self.assertEqual(checksum.Checksum32.calc(data), checksum.Checksum(32).process(data).final())
        self.assertEqual(checksum.Checksum16.calc(data), checksum.Checksum(16).process(data).final())
        self.assertEqual(checksum.Checksum8.calc(data), checksum.Checksum(8).process(data).final())

    def test_general_checksumxor_valid_width(self):
        """ Checksum()

            Should allow for any positive width
            which is a multiple of 8.
        """
        for n in range(8, 129, 8):
            ChecksumXor(n)

    def test_general_checksumxor_invalid_width(self):
        for n in (0, 1, 7, 9, 33):
            with self.assertRaises(ValueError):
                ChecksumXor(n)

    def test_general_checksumxor_ident(self):
        data = randbytes(1024)
        self.assertEqual(checksum.ChecksumXor32.calc(data), checksum.ChecksumXor(32).process(data).final())
        self.assertEqual(checksum.ChecksumXor16.calc(data), checksum.ChecksumXor(16).process(data).final())
        self.assertEqual(checksum.ChecksumXor8.calc(data), checksum.ChecksumXor(8).process(data).final())
