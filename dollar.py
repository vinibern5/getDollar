import urllib.request

#id="nacional" value="3,14" <- 
def price():
    pagina = urllib.request.urlopen('http://dolarhoje.com')
    html = pagina.read().decode('utf8')
    pos = html.find('id="nacional" value="') + len('id="nacional" value="')
    dolar = html[pos:html.find('"',pos)] #value="3,14" acha o ultimo " 
    dolar = dolar.replace(',','.') #3,14 -> 3.14 
    dolar = float(dolar) 
    return dolar
    
print("1 USD = %.2f BRL" %price())
