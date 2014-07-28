from src.util import csv_io
from src import facebook_crawler

import datetime

DEBUG = False

def main():

    timestamp = datetime.datetime.utcnow()
    t = str(timestamp)
    final_results = []

    # pull locations from database
    total_locations = [{"id": "1011", "name": "Toronto", "latitude": "40.1811", "longitude": "44.5136"}]
    
    # extract facebook api data
    facebook_results = facebook_crawler.run(total_locations)

    for key in facebook_results.keys():
        try:
            #populate final_results_array
            for event in facebook_results[key]:
                temp = []
                temp.append(key)
                for field in event.keys():
                    temp.append(event[field])
                final_results.append(temp)
        except:
            pass

    # write output to mysql database
    print(final_results)

    # write output to redshift/upworthy table and log locally as a csv
    if DEBUG == True:
        filename = t[0:4] + t[5:7] + t[8:10] + t[11:13] + t[14:16] + t[17:19] + ".csv"
        csv_io.array_to_csv(filename, final_results)


if __name__ == "__main__":
    main()
