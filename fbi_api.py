import requests 
import pandas as pd
import matplotlib as plt
import json

class Fugitive:

    url = "https://api.fbi.gov/wanted/v1/list"

    def __init__(self):
        pass
        

    def get_data(self):
        """
        gets all data from the FBI Wanted API.
        returns a pandas df with appropriate columns.
        """
        all_fugitives = []

        for page in range(1, 11):

            response = requests.get(self.url, params={"page": page})
            fbi_data = json.loads(response.content)

            items = fbi_data.get("items")

            all_fugitives.extend(items)

        self.df = pd.json_normalize(all_fugitives)  

        return self.df
    

    def save_to_csv(self, filename="fbi_fugitives.csv"):
        """
        Saves the df to a csv file.
        """

        self.df.to_csv(filename, index = False)
        print(filename)
        return(filename)

    
    






