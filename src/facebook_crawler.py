import facebook
from util.secret import *


def run(seeds):
	oauth_access_token = facebook.get_app_access_token(APP_ID, APP_SECRET)
	graph = facebook.GraphAPI(oauth_access_token)
	results = []

	for item in seeds:
		try:
			fql_query_string = "SELECT click_count, like_count,comment_count, share_count, total_count FROM link_stat WHERE url = " + "'" + item[-2] + "'" + ";"
			response = graph.fql(fql_query_string)
			results.append(response[0])
		except:
			results.append([])
			print("Suppressed Exception")

	return results