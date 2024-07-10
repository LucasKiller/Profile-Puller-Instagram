from defines import getCreds, makeApiCall
import datetime

def debugAccessToken(params):
	""" 
	Obtem informações sobre o access token 
	
	API Endpoint:
		https://graph.facebook.com/debug_token?input_token={input-token}&access_token={valid-access-token}

	Returns:
		object: informações do endpoint
	"""

	endpointParams = dict() # parâmetros do endpoint
	endpointParams['input_token'] = params['access_token'] # access token para debugar
	endpointParams['access_token'] = params['access_token'] # access token para fazer chamadas a API

	url = params['graph_domain'] + '/debug_token' # endpoint url

	return makeApiCall(url, endpointParams, params['debug']) # faz a chamada da API

params = getCreds() # pega as credenciais
params['debug'] = 'yes' # set debug para sim
response = debugAccessToken(params) # debuga o access token

print("\nAcesso aos dados expira em: ") # título
print(datetime.datetime.fromtimestamp(response['json_data']['data']['data_access_expires_at']).strftime('%d/%m/%Y %H:%M:%S')) # quando o acesso aos dados expira

print("\nO token expira em: ") # título
print(datetime.datetime.fromtimestamp(response['json_data']['data']['expires_at']).strftime('%d/%m/%Y %H:%M:%S')) # quando o token expira