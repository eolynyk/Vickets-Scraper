import facebook
from util.secret import *


def run(locations):
    # register facebook api credentials
    oauth_access_token = facebook.get_app_access_token(APP_ID, APP_SECRET)
    graph = facebook.GraphAPI(oauth_access_token)
    results = {}

    # loop through each geo latlong for which to return events
    for item in locations:
        temp = []
        try:
            fql_query_string = """
                                SELECT
                                    name,
                                    description,
                                    attending_count,
                                    location,
                                    ticket_uri,
                                    privacy,
                                    start_time,
                                    end_time 
                                FROM
                                    event 
                                WHERE
                                    creator IN (SELECT page_id FROM place WHERE distance(latitude, longitude, "{0}", "{1}") < 50000 limit 0,15000)
                                    and start_time > now() ORDER BY start_time desc limit 0,1500
                                """.format(item["latitude"],item["longitude"])
            response = graph.fql(fql_query_string)
            
            # loop through all events returned by fb api for current geo latlong
            for event in response:
                temp.append(event)

            results[item['id']] = temp

        except:
            print("Suppressed Exception")

    return results

if __name__ == "__main__":
    run()