import requests
import pandas as pd
import os
from api.models import Covid19Ca


def run():
    # Request updated data
    url = 'https://health-infobase.canada.ca/src/data/covidLive/covid19.csv'
    file = requests.get(url)
    open('data/covid19.csv', 'wb').write(file.content)

    df = pd.read_csv('data/covid19.csv')

    # Add new entries on DB
    for idx, row in df.iterrows():
        pruid = row['pruid']
        prname = row['prname']
        prnameFR = row['prnameFR']
        date = row['date']
        numconf = row['numconf']
        numprob = row['numprob']
        numdeaths = row['numdeaths']
        numtotal = row['numtotal']
        numtested = row['numtested']
        numrecover = row['numrecover']
        percentrecover = row['percentrecover']
        ratetested = row['ratetested']
        numtoday = row['numtoday']
        percentoday = row['percentoday']

        Covid19Ca.objects.create(
            date=date, pruid=pruid, prname=prname, prnameFR=prnameFR,
            numconf=numconf, numprob=numprob, numdeaths=numdeaths,
            numtotal=numtotal, numtested=numtested, numrecover=numrecover,
            percentrecover=percentrecover, ratetested=ratetested,
            numtoday=numtoday, percentoday=percentoday
        )