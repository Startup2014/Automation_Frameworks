def getCountries(str, P):
    import requests, json
    URL ='https://jsonmock.hackerrank.com/api/countries/search'
    PARAMS = {'name' :str}
    response = requests.get(url=URL,params=PARAMS )
    #####post call###
    #URL= 'https://api.gemini.com/v1/order/new'
    # payload = {'name' :str}
    # post_response = requests.post(url=URL,data=payload )
    #####post call###
    resp =response.json()
    print(json.dumps(resp, indent =4))
    # print(json.dumps(resp['page'], indent =4))
    # print(json.dumps(resp['per_page'], indent =4))
    # print(json.dumps(resp['total'], indent =4))                     
    # print(json.dumps(resp['total_pages'], indent =4))
    #print(json.dumps(resp['data'], indent =4)) 

    print([x['name'] for x in resp['data']])
    response.raise_for_status()



getCountries('un', 10)

# Assumption you are in trder role assigement to run this Api



def NewOrder_client_order_id_test():
    '''
    Test with all postive values in payload
    '''
    import requests
    base_url ='https://api.gemini.com'
    url = base_url + '/v1/order/new'
    request_headers = { 'Content-Type': "text/plain",
                        'Content-Length': "0",
                        'X-GEMINI-APIKEY': api_key,
                        'X-GEMINI-PAYLOAD': base64.b64encode(encoded_payload),
                        'X-GEMINI-SIGNATURE': hmac.new(secret_key, b64, hashlib.sha384).hexdigest(),
                        'Cache-Control': "no-cache" }

    response = requests.post(url,
                             data=None,
                             headers=request_headers,
                             timeout=timeout,
                             verify=False)
    assert response.status_code == 200
    return response.content


 
    
NewOrder_client_order_id_test()
  
