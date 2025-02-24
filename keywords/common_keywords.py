# keywords/common_keywords.py

from robot.api.deco import keyword

@keyword
def click_element(element):
    # Logic to click element
    pass

@keyword
def wait_for_element(element, timeout=10):
    # Logic to wait for element to appear
    pass

@keyword
def input_text(element, text):
    # Logic to input text into field
    pass

