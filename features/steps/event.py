from behave import given, when, then
from selenium.webdriver.common.keys import Keys
import time


@then(u'I see the event form')
def step_impl(context):
    context.event_form = context.browser.find_element_by_id('event_form')


@then(u'I enter my latitude "{lat}", longitude "{lon}", '
      u'title "{title}" and date "{date}"')
def step_impl(context, lat, lon, title, date):
    insert_into_form(context, 'event_form_title')
    insert_into_form(context, 'event_form_lat')
    insert_into_form(context, 'event_form_lon')
    insert_into_form(context, 'event_form_date')
    context.event_form.find_element_by_id('event_form_submit').send_keys(Keys.ENTER)
    time.sleep(1)


@then(u'I will see a table that displays my events')
def step_impl(context):
    table = context.browser.find_element_by_id('own_events_list')
    rows = table.find_elements_by_tag_name('tr')
    context.test.assertTrue(len(rows) == 1, "there's not exactly 1 row")


def insert_into_form(context, id):
    field = context.event_form.find_element_by_id(id)
    field.send_keys('yadda')

