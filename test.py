from app.libs.http import HTTP

r = HTTP()
response = r.http_get('http://www.asdfsda.com')
print(response.status_code)