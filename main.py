from src.util import csv_io
from src import facebook_crawler


DEBUG = True

def main():

    timestamp = datetime.datetime.utcnow()

    # extract facebook api data
    total_locations = [{"name": "Toronto", "latitude": "43.700", "longitude": "79.4000"}]
    facebook_results = facebook_crawler.run(total_locations)
    final_results = []
    
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
