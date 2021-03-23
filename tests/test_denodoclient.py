#!/usr/bin/env python

"""Tests for `denodoclient` package."""

import pytest
from pathlib import Path
from os import environ


from denodoclient import DenodoClient


def test_cannot_create_client_without_credentials():
    with pytest.raises(ValueError):
        denodoclient = DenodoClient("test")
