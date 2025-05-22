# test.py
#
#  Copyright (C) 2025 Ivan Guerreschi.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from datetime import datetime
import subprocess
import sys
import time
import unittest

class TestZeitdb(unittest.TestCase):

    file_path = '../src/zeitdb'

    def test_datetime_now(self):
        ct = datetime.now()
        cp = subprocess.run(
                [self.file_path],
                capture_output=True,
                check=True,
                text=True,
                )

        ft = ct.strftime("%a %b %d %H:%M:%S %Y\n")
        self.assertEqual(cp.stdout, ft)

if __name__ == '__main__':
    unittest.main()
