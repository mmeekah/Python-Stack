import urllib.request

response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)

# import arithmetic
# print(arithmetic.add(5, 8))
# print(arithmetic.subtract(10, 5))
# print(arithmetic.multiply(12, 6))