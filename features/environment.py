from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome()


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    if feature.name == 'Add events':
        context.event_form_data = []
