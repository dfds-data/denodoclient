#!/usr/bin/env python

"""Tests for `denodoclient` package."""

import pytest
from pathlib import Path


from denodoclient import VqlQuery


@pytest.fixture
def path_to_query():
    return Path("tests/data/template.sql")


def test_vqlquery_constructor_sets_attributes(path_to_query):
    vqlquery = VqlQuery(path_to_query, nils="gunnar")
    assert hasattr(vqlquery, "nils")


def test_vqlquery_fails_if_missing_tokens(path_to_query):
    vqlquery = VqlQuery(path_to_query)

    with pytest.raises(ValueError):
        str(vqlquery)


def test_vqlquery_replaces_tokens_correctly(path_to_query):
    vqlquery = VqlQuery(path_to_query, dateupdated="2021-03-23")

    assert str(vqlquery).endswith(r"WHERE updated > '2021-03-23'")


def test_vqlquery_attributes_can_be_set_directly(path_to_query):
    vqlquery = VqlQuery(path_to_query)

    vqlquery.dateupdated = "2020-01-01"

    assert str(vqlquery).endswith(r"WHERE updated > '2020-01-01'")


def test_vqlquery_tokens_property_returns_only_tokens(path_to_query):
    vqlquery = VqlQuery(path_to_query, foo="bar", baz="lol")

    print(vqlquery.tokens)

    assert vqlquery.tokens == {"foo": "bar", "baz": "lol"}


def test_vqlquery_tokens_property_immutable(path_to_query):
    vqlquery = VqlQuery(path_to_query)

    with pytest.raises(AttributeError):
        vqlquery.tokens = {"foo": "bar"}
