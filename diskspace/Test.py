import unittest

from diskspace import diskspace

class BytesToReadableTest(unittest.TestCase):
    # Each block amounts to 512B.

    def test_display_correct_value_for_bytes(self):
        blocks = 1
        size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('512.00B', size)

    def test_display_correct_value_for_kbytes(self):
        blocks = 10
        size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('5.00Kb', size)

    def test_display_correct_value_for_mbytes(self):
        blocks = 10240
        size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('5.00Mb', size)

    def test_display_correct_value_for_gbytes(self):
        blocks = 10485760
        size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('5.00Gb', size)

    def test_display_correct_value_for_tbytes(self):
        blocks = 2147483648
        size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('1.00Tb', size)

    def test_display_correct_value_for_no_blocks(self):
        blocks = 0
        size = diskspace.bytes_to_readable(blocks)
        self.assertEqual('0.00B', size)


class SubprocessCheckOutputTest(unittest.TestCase):
    def test_display_correct_output_for_command(self):
        command = 'echo test'
        output = diskspace.subprocess_check_output(command)
        self.assertEqual('test\n', output)

    def test_raises_error_for_invalid_command(self):
        command = '1'
        with self.assertRaises(OSError):
            output = diskspace.subprocess_check_output(command)
