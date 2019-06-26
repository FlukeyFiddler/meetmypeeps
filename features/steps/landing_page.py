from behave import given, when, then


@given(u'I land on the site')
def step_impl(context):
  context.browser.get('http://localhost:8000')


@then(u'I will see "{title}" in the title bar')
def step_impl(context, title):
    context.test.assertEqual(title, context.browser.title)
