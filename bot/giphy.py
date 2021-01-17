import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
import os
import random

load_dotenv()


class Giphy:
    api_instance = giphy_client.DefaultApi()
    api_key = os.getenv("GIPHY_API_KEY")
    limit = int(os.getenv("GIPHY_LIMIT"))
    rating = os.getenv("GIPHY_RATING")

    def get_trending(self):
        try:
            api_response = self.api_instance.gifs_trending_get(
                self.api_key, limit=self.limit, rating=self.rating)
            return self.get_url(api_response)

        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_trending_get: %s\n" % e)

    def get_url(self, api_response):
        lst = list(api_response.data)
        gif = random.choices(lst)
        return gif[0].url

    def get_search(self, query):
        try:
            api_response = self.api_instance.gifs_search_get(
                self.api_key, limit=self.limit, rating=self.rating, q=query)
            return self.get_url(api_response)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    def get_random(self):
        try:
            api_response = self.api_instance.gifs_random_get(self.api_key)
            return self.get_random_url(api_response)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    def get_random_url(self, api_response):
        return api_response.data.url
