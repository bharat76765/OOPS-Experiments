import requests
class apis:
    def facts(self):
        import requests
        # Define the URL
        url = "https://api.adviceslip.com/advice"

        # Send GET request
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            # Extract the advice slip
            advice = data['slip']['advice']
            return advice
        else:
            return(f"Failed to retrieve advice. Status code: {response.status_code}")
    def wheather(self,lon,lat):
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
        querystring = {"lat":str(lat),"lon":str(lon),"units":"imperial","lang":"en"}
        headers = {
          "x-rapidapi-key": "0d839b48d3mshdb2c1ee05b2a2b8p1fafedjsn8404b2c208db",
          "x-rapidapi-host": "weatherbit-v1-mashape.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        d= dict(response.json())
        del(d['data'])
        return d

