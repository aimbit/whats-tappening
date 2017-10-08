from selenium import webdriver
from selenium.webdriver.common.keys import Keys

t = []

def get_new_brews(iterable):
    new_brews = 0
    for child in iterable:
        if 'PAST BREWS' in child.text:
            return new_brews
        if 'ABV' not in child.text: continue
        t.append(child.text)
        new_brews += 1

    return new_brews


driver = webdriver.Chrome()
driver.get('http://www.bnabrewing.com/beer/')

outside_divs = driver.find_elements_by_xpath('/html/body/div/section/div')
new_brews = get_new_brews(outside_divs)
print new_brews

for beer in t:
    s = beer.splitlines()
    print s
    b.title = s[0]
    b.desc = s[3]

driver.quit()
