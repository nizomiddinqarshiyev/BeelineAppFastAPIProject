# webscraping
import playwright.sync_api as p

with p as playwright:
    browser = playwright.browser()
    content = browser.content()
    page = content.page()
    page.goto('http://kun.uz')






