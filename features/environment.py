import os
import django
from behave.runner import Context
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.management import call_command
from django.shortcuts import resolve_url
from django.test.runner import DiscoverRunner
from splinter.browser import Browser

os.environ["DJANGO_SETTINGS_MODULE"] = "myrecommendations.settings"

class ExtendedContext(Context):
    def get_url(self, to=None, *args, **kwargs):
        return self.test.live_server_url + (
            resolve_url(to, *args, **kwargs) if to else '')

def before_all(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.browser = Browser('chrome', headless=True)

def before_scenario(context, scenario):
    context.test_runner.setup_databases()
    object.__setattr__(context, '__class__', ExtendedContext)
    context.test = StaticLiveServerTestCase
    context.test.setUpClass()

def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test
    call_command('flush', verbosity=0, interactive=False)

def after_all(context):
    context.test_runner.teardown_test_environment()
    context.browser.quit()
    context.browser = None
