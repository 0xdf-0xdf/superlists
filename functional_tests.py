from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://0xd4s.pythonanywhere.com')

assert 'Django' in browser.title
