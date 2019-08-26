from behave import given, when, then


@given(u'I land on the site')
def step_impl(context):
  context.browser.get('http://localhost:8000')


@then(u'I will see "{title}" in the title bar')
def step_impl(context, title):
    context.test.assertEqual(title, context.browser.title)


@then(u'I will see "{text}" in the H1 tag')
def step_impl(context, text):
    h1_tag = context.browser.find_element_by_id('h1')
    context.test.assertEqual(text, h1_tag.text)


@then(u'I will see a Google Map')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will see a Google map showing peeps in my vicinity')
