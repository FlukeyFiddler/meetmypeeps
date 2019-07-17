from behave import given, when, then
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver


def insert_into_form(context, id, text):
    field = context.event_form.find_element_by_id(id)
    field.send_keys(text)


@then(u'I see the event form')
def step_impl(context):
    context.event_form = context.browser.find_element_by_id('event_form')


@then(u'I enter my location "{loc}", title "{title}" and date "{date}"')
def step_impl(context, loc, title, date):
    context.event_form_data += title, loc, date

    insert_into_form(context, 'event_form_title', title)
    insert_into_form(context, 'event_form_location', loc)
    insert_into_form(context, 'event_form_date', date)
    context.event_form.find_element_by_id('event_form_submit').send_keys(Keys.ENTER)
    time.sleep(1)


@then(u'I will see a table that displays my events')
def step_impl(context):
    table = context.browser.find_element_by_id('own_events_list')
    cols = table.find_elements_by_class_name('event_list_value')

    for data in context.event_form_data:
        context.test.assertIn(data, [col.text for col in cols])



