import json

print('Loading function')
value=0

def SensorValues(event, context):
	print(event)
	httpmethod=event['httpMethod']
	transactionResponse = {}

	if httpmethod=='GET':
		value = event['queryStringParameters']['value']
	elif httpmethod=='POST':
		body=json.loads(event['body'])
		value=body['value']
	
	if float(value)>400 and float(value)<650 :
		transactionResponse['message'] = 'lights on'
	else:
		transactionResponse['message'] = 'lights off'
		
	#print('value=' + value)
	print('response=' + transactionResponse['message'])

	transactionResponse['value'] = value


	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	return responseObject



