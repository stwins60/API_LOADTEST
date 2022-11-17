import requests as r

response = r.get("http://localhost:5000/api/v1/transactions_by_id?id=11")

if response.status_code == 200:
        response.cookies.add_cookie_header = response.headers['Status']
        print(response.headers)
        print(response.cookies.get_dict())