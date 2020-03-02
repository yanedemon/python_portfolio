from grab import Grab
import requests

g = Grab(log_file = 'out.html')

g.go('https://admin.dobrodel.mosreg.ru/CardEditList')
g.set_input('j_username', 'it-otdel@solreg.ru')
g.set_input('j_password', 'soln141500')
g.submit()
print(g.response.body)
