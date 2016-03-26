from checksum.base import ChecksumBase, ChecksumError


class Checksum(ChecksumBase):
    _width = 32
    _mask = 0xFFffFFff
    _check_data = (0xDE, 0xAD, 0xBE, 0xEF, 0xAA, 0x55, 0xC2, 0x8C)
    _check_result_littleendian = None

    def __init__(self, initvalue=0, bigendian=True):
        super(Checksum, self).__init__(initvalue)
        self._bigendian = bigendian

    def process(self, data, startindex=0, endindex=None):
        dataword = 0
        n = 0
        for byte in self._iter(data, startindex, endindex):
            if self._bigendian:
                dataword = (dataword << 8) | byte
            else:
                dataword |= (byte << n)
            n += 8
            if n == self._width:
                self._process(dataword)
                dataword = 0
                n = 0

    def _process(self, dataword):
        self._value = self._mask & (self._value + dataword)

    @classmethod
    def selftest(cls, data=None, expectedresult=None, bigendian=True):
        if data is None:
            data = cls._check_data
        if expectedresult is None:
            if bigendian:
                expectedresult = cls._check_result
            else:
                expectedresult = cls._check_result_littleendian
        result = cls.calc(data, bigendian=bigendian)
        if result != expectedresult:
            raise ChecksumError(hex(result))


class Checksum32(Checksum):
    _width = 32
    _mask = 0xFFffFFff
    _check_result = 0x8903817B
    _check_result_littleendian = 0x7C810388


class Checksum16(Checksum):
    _width = 16
    _mask = 0xFFff
    _check_result = 0x0A7D
    _check_result_littleendian = 0x8008


class Checksum8(Checksum):
    _width = 8
    _mask = 0xFF
    _check_result = 0x85
    _check_result_littleendian = _check_result


class ChecksumXor(Checksum):
    def _process(self, dataword):
        self._value = self._mask & (self._value ^ dataword)


class ChecksumXor32(ChecksumXor):
    _width = 32
    _mask = 0xFFffFFff
    _check_result = 0x74F87C63
    _check_result_littleendian = 0x637CF874


class ChecksumXor16(ChecksumXor):
    _width = 16
    _mask = 0xFFff
    _check_result = 0x089B
    _check_result_littleendian = 0x9B08


class ChecksumXor8(ChecksumXor):
    _width = 8
    _mask = 0xFF
    _check_result = 0x93
    _check_result_littleendian = _check_result


ALLCHECKSUMCLASSES = (
    Checksum8, Checksum16, Checksum32,
    ChecksumXor8, ChecksumXor16, ChecksumXor32,
)

