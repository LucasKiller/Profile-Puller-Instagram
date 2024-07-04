import requests, json

def getCreds():
	""" 
	Obtem as credenciais necessárias para uso nas aplicações
	
	Returns:
        dict: credenciais necessárias globalmente
	"""

	creds = dict() # dict para guardar as informações de credenciais
	creds['access_token'] = 'ACCESS-TOKEN' # access token para fazer chamadas a API
	creds['client_id'] = 'FB-APP-CLIENT-ID' # client id do facebook app
	creds['client_secret'] = 'FB-APP-CLIENT-SECRET' # client secret do facebook app
	creds['graph_domain'] = 'https://graph.facebook.com/' # base de domínio para fazer chamadas a API
	creds['graph_version'] = 'v6.0' # versão da API
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base de endpoint para fazer chamadas a API
	creds['debug'] = 'no' # debug mode para fazer chamadas a API
	creds['page_id'] = 'FB-PAGE-ID' # id da página do facebook
	creds['instagram_account_id'] = 'INSTAGRAM-BUSINESS-ACCOUNT-ID' # id da conta de negócios do instagram
	creds['ig_username'] = 'IG-USERNAME' # nome de usuário do instagram

	return creds

def makeApiCall(url, endpointParams, debug = 'no'):
	""" 
    	Uma função para fazer chamadas a API
	
	Args:
		url: string da url
		endpointParams: dict dos parâmetros do endpoint

	Returns:
        object: informação da chamada da API
	"""

	data = requests.get(url, endpointParams) # faz a chamada da API

	response = dict() # dict para guardar a resposta da chamada da API
	response['url'] = url # url
	response['endpoint_params'] = endpointParams # parâmetros do endpoint
	response['endpoint_params_pretty'] = json.dumps(endpointParams, indent = 4) # parâmetros do endpoint formatados 
	response['json_data'] = json.loads(data.content) # pega a resposta da chamada da API
	response['json_data_pretty'] = json.dumps(response['json_data'], indent = 4) # formata a resposta da chamada da API

	if ('yes' == debug) : # se debug mode está ativado
		displayApiCallData(response) # mostra a resposta da chamada da API

	return response # pega e retorna a resposta da chamada da API

def displayApiCallData(response):
	"""
	Mostra a resposta da chamada da API formatada
	"""

	print("\nURL: ") # título
	print(response['url']) # display da url
	print("\nEndpoint Params: ") # título
	print(response['endpoint_params_pretty']) # parâmetros do endpoint formatados
	print("\nResponse: ") # título
	print(response['json_data_pretty']) # formata a resposta da chamada da API
