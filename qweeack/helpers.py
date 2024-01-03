import decimal
import requests
import requests_cache
import json

requests_cache.install_cache('qweeack_cache', backend='sqlite')

def get_stock_data(search):
    url = "https://wall-street-journal.p.rapidapi.com/api/v1/searchKeyword"

    querystring = {"query":"<REQUIRED>"}

    headers = {
	    "X-RapidAPI-Key": "abee8f758fmshe6e4f66562e5b3ep13fbeajsnc583a9839270",
	    "X-RapidAPI-Host": "wall-street-journal.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())


    


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(JSONEncoder, self).default(o)

   



    
    

