# -*- coding: utf-8 -*-
from evenflow.models.Applications import Applications
from evenflow.models.Base import BaseModel

from peewee import CharField


def test_applications():
    assert isinstance(Applications.name, CharField)
    assert issubclass(Applications, BaseModel)
