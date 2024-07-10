from defines import getCreds, makeApiCall

def getUserMedia(params: dict):
	""" 
	Pega as mídias de um usuário

	Os campos (fields) podem ser os valores:
	- id
	- caption
	- is_shared_to_feed
	- media_type
	- media_url
	- permalink
	- thumbnail_url
	- timestamp
	- username
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}

	Returns:
		object: informações do endpoint

	"""

	endpointParams = dict() # parâmetros do endpoint
	endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username' # campos para pegar
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['instagram_account_id'] + '/media' # endpoint url

	return makeApiCall(url, endpointParams, params['debug']) # faz a chamada da API

def getMediaInsights(params: dict):
	""" 
	Pega os insights para uma mídia específica
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-media-id}/insights?metric={metric}

	Returns:
		object: informações do endpoint

	"""
	endpointParams = dict() # parâmetros do endpoint
	endpointParams['metric'] = params['metric'] # campos para pegar
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['latest_media_id'] + '/insights' # endpoint url

	return makeApiCall(url, endpointParams, params['debug']) # faz a chamada da API

def getUserInsights(params: dict):
	""" 
	Pega os insights para a conta do usuário

	Os períodos (period) podem ser os valores:
	- day
	- week
	- days_28
	- month
	- lifetime
	- total_over_range

	As métricas (metric) do usuário incluem:
	- impressions
	- shares
	- comments 
	- plays 
	- likes
	- saved
	- peak_concurrent_viewers
	- replies
	- video_views
	- total_interactions
	- navigation
	- follows
	- profile_visits
	- profile_activity
	- reach
	- ig_reels_video_view_total_time
	- ig_reels_avg_watch_time
	- clips_replays_count
	- ig_reels_aggregated_all_plays_count
	- views
	- thread_replies
	- reposts
	- quotes
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parâmetros do endpoint
	endpointParams['metric'] = 'follower_count,impressions,profile_views,reach' # métrica para pegar
	endpointParams['period'] = 'day' # período para pegar
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['instagram_account_id'] + '/insights' # endpoint url

	return makeApiCall(url, endpointParams, params['debug']) # faz a chamada da API

params = getCreds() # pega as credenciais
response = getUserMedia(params) # pega as mídias do usuário

print ("\n---- ÚLTIMO POST -----\n") # título
print ("\tLink para o post:") # título
print ("\t" + response['json_data']['data'][0]['permalink']) # link para o post
print ("\n\tDescrição do post:") # título
print ("\t" + response['json_data']['data'][0]['caption']) # descrição do post
print ("\n\tTipo de mídia:") # título
print ("\t" + response['json_data']['data'][0]['media_type']) # tipo de mídia
print ("\n\tPostado em:") # título
print ("\t" + response['json_data']['data'][0]['timestamp']) # postado em

params['latest_media_id'] = response['json_data']['data'][0]['id'] # armazena o id da última mídia postada

if 'VIDEO' == response['json_data']['data'][0]['media_type'] : # se a mídia é um vídeo
	params['metric'] = 'engagement,impressions,reach,saved,video_views' # métricas para pegar
else : # se a mídia é uma imagem
	params['metric'] = 'impressions,reach,saved' # métricas para pegar

response = getMediaInsights(params) # pega os insights para a última mídia postada

print ("\n---- INSIGHTS DO ÚLTIMO POST -----\n") # título

for insight in response['json_data']['data'] : # loop sobre os insights
	print ("\t" + insight['title'] + " (" + insight['period'] + "): " + str( insight['values'][0]['value'] )) # mostra as informações

response = getUserInsights(params) # pega os insights do usuário

print ("\n---- INSIGHTS DIÁRIO DO USUÁRIO -----\n") # título

for insight in response['json_data']['data'] : # loop sobre os insights
	print ("\t" + insight['title'] + " (" + insight['period'] + "): " + str( insight['values'][0]['value'] )) # mostra as informações

	for value in insight['values'] : # loop sobre os valores
		print ("\t\t" + value['end_time'] + ": " + str( value['value'] )) # mostra as informações