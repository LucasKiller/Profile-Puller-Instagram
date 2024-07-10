from defines import getCreds, makeApiCall

def getInstagramAccount(params):
	""" 
	Pega informações sobre a conta business do instagram
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{page-id}?access_token={your-access-token}&fields=instagram_business_account

	Returns:
		object: informações do endpoint
	"""

	endpointParams = dict() # parâmetros do endpoint
	endpointParams['access_token'] = params['access_token'] # access token
	endpointParams['fields'] = 'instagram_business_account' # campo para pegar o id da conta business do instagram

	url = params['endpoint_base'] + params['page_id'] # endpoint url

	return makeApiCall(url, endpointParams, params['debug']) # faz a chamada da API

params = getCreds() # pega as credenciais
params['debug'] = 'no' # seta o debug
response = getInstagramAccount(params) # pega a informação do debug

print ("\n---- INSTAGRAM ACCOUNT INFO ----\n")
print ("Page Id:") # label
print (response['json_data']['id']) # display the page id
print ("\nInstagram Business Account Id:") # label
print (response['json_data']['instagram_business_account']['id']) #display the instagram account id