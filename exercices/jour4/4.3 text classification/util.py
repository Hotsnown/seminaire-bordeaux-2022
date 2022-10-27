import os
import json

import os, json
import pandas as pd

path_to_json = '/content/outcome-prediction/data/manual_annotation/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

# here I define my pandas Dataframe with the columns I want to get from the json
jsons_data = pd.DataFrame(columns=['content', 'role'])

# we need both the json and an index number so use enumerate()
for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        # here you need to know the layout of your json and each json has to have
        # the same structure (obviously not the structure I have here)
        if json_text['annotations'][0].get('content'):
          content = json_text['annotations'][0]['content']
          role = json_text['annotations'][-1]['role']
          # here I push a list of data into a pandas DataFrame at row given by 'index'
          jsons_data.loc[index] = [content, role]

# now that we have the pertinent json data in our DataFrame let's look at it
jsons_data.to_csv("outcome_prediction.csv")