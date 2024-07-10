from defines import getCreds, makeApiCall

def getUserPages(params):
	""" 
	Pega informações sobre a página do usuário
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}

	Returns:
		object: informações do endpoint
	"""

	endpointParams = dict() # parâmetros do endpoint
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + 'me/accounts' # endpoint url

	return makeApiCall(url, endpointParams, params['debug']) # faz a chamada da API

params = getCreds() # pega as credenciais
params['debug'] = 'no' # seta o debug
response = getUserPages(params) # pega a informação do debug

n = 1 # contador
for page in response['json_data']['data']:
	print(f"\n---- FACEBOOK PAGE INFO {n} ----\n") # título
	print("Nome da página:") # título
	print(page['name']) # nome da página
	print("\nCategoria da página:") # título
	print(page['category']) # categoria da página
	print("\nPage Id:") # título
	print(page['id']) # id da página
	n += 1 # incrementa o contador para possíveis páginas adicionais