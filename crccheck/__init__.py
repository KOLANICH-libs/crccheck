""" Classes to calculate CRCs and checksums from binary data
    ========================================================

    The :mod:`crccheck.crc` module implements all CRCs listed in the
    `Catalogue of parametrised CRC algorithms <http://reveng.sourceforge.net/crc-catalogue/>`_:

    CRC-3/GSM, CRC-3/ROHC, CRC-4/G-704, CRC-4/ITU, CRC-4/INTERLAKEN, CRC-5/EPC-C1G2, CRC-5/EPC, CRC-5/G-704, CRC-5/ITU,
    CRC-5/USB, CRC-6/CDMA2000-A, CRC-6/CDMA2000-B, CRC-6/DARC, CRC-6/G-704, CRC-6/ITU, CRC-6/GSM, CRC-7/MMC, CRC-7,
    CRC-7/ROHC, CRC-7/UMTS, CRC-8/AUTOSAR, CRC-8/BLUETOOTH, CRC-8/CDMA2000, CRC-8/DARC, CRC-8/DVB-S2, CRC-8/GSM-A,
    CRC-8/GSM-B, CRC-8/I-432-1, CRC-8/ITU, CRC-8/I-CODE, CRC-8/LTE, CRC-8/MAXIM-DOW, CRC-8/MAXIM, DOW-CRC,
    CRC-8/MIFARE-MAD, CRC-8/NRSC-5, CRC-8/OPENSAFETY, CRC-8/ROHC, CRC-8/SAE-J1850, CRC-8/SMBUS, CRC-8, CRC-8/TECH-3250,
    CRC-8/AES, CRC-8/EBU, CRC-8/WCDMA, CRC-10/ATM, CRC-10, CRC-10/I-610, CRC-10/CDMA2000, CRC-10/GSM, CRC-11/FLEXRAY,
    CRC-11, CRC-11/UMTS, CRC-12/CDMA2000, CRC-12/DECT, CRC-12-X, CRC-12/GSM, CRC-12/UMTS, CRC-12/3GPP, CRC-13/BBC,
    CRC-14/DARC, CRC-14/GSM, CRC-15/CAN, CRC-15, CRC-15/MPT1327, CRC-16/ARC, ARC, CRC-16/LHA, CRC-IBM, CRC-16/CDMA2000,
    CRC-16/CMS, CRC-16/DDS-110, CRC-16/DECT-R, R-CRC-16, CRC-16/DECT-X, X-CRC-16, CRC-16/DNP, CRC-16/EN-13757,
    CRC-16/GENIBUS, CRC-16/DARC, CRC-16/EPC, CRC-16/EPC-C1G2, CRC-16/I-CODE, CRC-16/GSM, CRC-16/IBM-3740,
    CRC-16/AUTOSAR, CRC-16/CCITT-FALSE, CRC-16/IBM-SDLC, CRC-16/ISO-HDLC, CRC-16/ISO-IEC-14443-3-B, CRC-16/X-25, CRC-B,
    X-25, CRC-16/ISO-IEC-14443-3-A, CRC-A, CRC-16/KERMIT, CRC-16/CCITT, CRC-16/CCITT-TRUE, CRC-16/V-41-LSB, CRC-CCITT,
    KERMIT, CRC-16/LJ1200, CRC-16/MAXIM-DOW, CRC-16/MAXIM, CRC-16/MCRF4XX, CRC-16/MODBUS, MODBUS, CRC-16/NRSC-5,
    CRC-16/OPENSAFETY-A, CRC-16/OPENSAFETY-B, CRC-16/PROFIBUS, CRC-16/IEC-61158-2, CRC-16/RIELLO, CRC-16/SPI-FUJITSU,
    CRC-16/AUG-CCITT, CRC-16/T10-DIF, CRC-16/TELEDISK, CRC-16/TMS37157, CRC-16/UMTS, CRC-16/BUYPASS, CRC-16/VERIFONE,
    CRC-16/USB, CRC-16/XMODEM, CRC-16/ACORN, CRC-16/LTE, CRC-16/V-41-MSB, XMODEM, ZMODEM, CRC-17/CAN-FD, CRC-21/CAN-FD,
    CRC-24/BLE, CRC-24/FLEXRAY-A, CRC-24/FLEXRAY-B, CRC-24/INTERLAKEN, CRC-24/LTE-A, CRC-24/LTE-B, CRC-24/OPENPGP,
    CRC-24, CRC-24/OS-9, CRC-30/CDMA, CRC-31/PHILIPS, CRC-32/AIXM, CRC-32Q, CRC-32/AUTOSAR, CRC-32/BASE91-D, CRC-32D,
    CRC-32/BZIP2, CRC-32/AAL5, CRC-32/DECT-B, B-CRC-32, CRC-32/CD-ROM-EDC, CRC-32/CKSUM, CKSUM, CRC-32/POSIX,
    CRC-32/ISCSI, CRC-32/BASE91-C, CRC-32/CASTAGNOLI, CRC-32/INTERLAKEN, CRC-32C, CRC-32/ISO-HDLC, CRC-32,
    CRC-32/ADCCP, CRC-32/V-42, CRC-32/XZ, PKZIP, CRC-32/JAMCRC, JAMCRC, CRC-32/MPEG-2, CRC-32/XFER, XFER, CRC-40/GSM,
    CRC-64/ECMA-182, CRC-64, CRC-64/GO-ISO, CRC-64/WE, CRC-64/XZ, CRC-64/GO-ECMA, CRC-82/DARC.

    For the class names simply remove all dashes and slashes from the above names and apply CamelCase, e.g.
    "CRC-32/MPEG-2" is implemented by :class:`.Crc32Mpeg2`. Other CRC can be calculated by using the general class
    :class:`crccheck.crc.Crc` by providing all required CRC parameters.

    The :mod:`crccheck.checksum` module implements additive and XOR checksums with 8, 16 and 32 bit:
    :class:`.Checksum8`, :class:`.Checksum16`, :class:`.Checksum32` and
    :class:`.ChecksumXor8`, :class:`.ChecksumXor16`, :class:`.ChecksumXor32`.

    Usage example::

        from crccheck.crc import Crc32, CrcXmodem
        from crccheck.checksum import Checksum32

        # Quick calculation
        data = bytearray.fromhex("DEADBEEF")
        crc = Crc32.calc(data)
        checksum = Checksum32.calc(data)

        # Procsss multiple data buffers
        data1 = b"Binary string"  # or use .encode(..) on normal sring - Python 3 only
        data2 = bytes.fromhex("1234567890")  # Python 3 only, use bytearray for older versions
        data3 = (0x0, 255, 12, 99)  # Iterable which returns ints in byte range (0..255)
        crcinst = CrcXmodem()
        crcinst.process(data1)
        crcinst.process(data2)
        crcinst.process(data3[1:-1])
        crcbytes = crcinst.finalbytes()
        crchex = crcinst.finalhex()
        crcint = crcinst.final()

    License:
        MIT License

        Copyright (c) 2015-2022 by Martin Scharrer <martin.scharrer@web.de>

        Permission is hereby granted, free of charge, to any person obtaining a copy of this software
        and associated documentation files (the "Software"), to deal in the Software without
        restriction, including without limitation the rights to use, copy, modify, merge, publish,
        distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
        Software is furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all copies or
        substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
        BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
        DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
from crccheck import crc, checksum
