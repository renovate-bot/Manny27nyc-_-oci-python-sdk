# coding: utf-8
# Modified Work: Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Copyright 2008-2016 Andrey Petrov and contributors

import sys

try:
    # Our match_hostname function is the same as 3.5's, so we only want to
    # import the match_hostname function if it's at least that good.
    if sys.version_info < (3, 5):
        raise ImportError("Fallback to vendored code")

    from ssl import CertificateError, match_hostname
except ImportError:
    try:
        # Backport of the function from a pypi module
        from backports.ssl_match_hostname import (  # type: ignore
            CertificateError,
            match_hostname,
        )
    except ImportError:
        # Our vendored copy
        from ._implementation import CertificateError, match_hostname  # type: ignore

# Not needed, but documenting what we provide.
__all__ = ("CertificateError", "match_hostname")
