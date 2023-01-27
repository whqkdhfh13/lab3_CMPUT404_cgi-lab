#!/usr/bin/env python3

import cgi
import cgitb
from templates import login_page, secret_page, after_login_incorrect
import os
import secret
from http.cookies import SimpleCookie

cgitb.enable()

fs = cgi.FieldStorage()
username = fs.getfirst("username")
password = fs.getfirst("password")

form_good = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_username = cookie.get("password").value

cookie_good = cookie_username == secret.username and cookie_password == secret.password

if cookie_good:
    username = cookie_username
    password = cookie_password
print("content-type: text/html")
if form_good:
    print("Set-Cookie: username={username}")
    print("Set-Cookie: password={password}")

print()

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(login_page())
    print("username: ", username)
    print("password: ", password)