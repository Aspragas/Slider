# Copyright 2023  Projektpraktikum Python.
# SPDX-License-Identifier: Apache-2.0
"""Engine tests."""

from __future__ import annotations

from example import func


def test_func() -> None:
    """Test func returns 42."""
    assert func() == 42
