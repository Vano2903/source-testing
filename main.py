#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_testing import SourceTesting

if __name__ == "__main__":
    source = SourceTesting()
    launch(source, sys.argv[1:])
