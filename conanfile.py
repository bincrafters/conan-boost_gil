#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostGilConan(base.BoostBaseConan):
    name = "boost_gil"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_gil"
    lib_short_names = ["gil"]
    header_only_libs = ["gil"]
    b2_requires = [
        "boost_algorithm",
        "boost_bind",
        "boost_concept_check",
        "boost_config",
        "boost_core",
        "boost_filesystem",
        "boost_function",
        "boost_integer",
        "boost_iterator",
        "boost_lambda",
        "boost_mpl",
        "boost_numeric_conversion",
        "boost_preprocessor",
        "boost_static_assert",
        "boost_type_traits"
    ]
