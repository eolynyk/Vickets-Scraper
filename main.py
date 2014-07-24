from src.util import csv_io
from src import facebook_crawler

import datetime

DEBUG = True

def main():

    timestamp = datetime.datetime.utcnow()
    t = str(timestamp)
    final_results = []

    # extract facebook api data
    total_locations = [{"id": "1011", "name": "Toronto", "latitude": "40.1811", "longitude": "44.5136"}]
    facebook_results = facebook_crawler.run(total_locations)
    
    for i, item in enumerate(facebook_results):
        temp = []
        try:
            #populate final_results_array
            final_results.append()
        except:
            pass

    # write output to redshift/upworthy table and log locally as a csv
    if DEBUG == True:
        filename = t[0:4] + t[5:7] + t[8:10] + t[11:13] + t[14:16] + t[17:19] + ".csv"
        csv_io.array_to_csv(filename, final_results)


if __name__ == "__main__":
    main()
