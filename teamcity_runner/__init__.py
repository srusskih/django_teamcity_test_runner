__author__ = 'stachern'

import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
from django.test.simple import DjangoTestSuiteRunner


class TeamCityTestRunner(DjangoTestSuiteRunner):

    def run_suite(self, suite, **kwargs):
        if is_running_under_teamcity():
            return TeamcityTestRunner().run(suite)
        else:
            return unittest.TextTestRunner(
                verbosity=self.verbosity, failfast=self.failfast).run(suite)
