import logging

import azure.functions as func
import uuid
import json
 
def main(req: func.HttpRequest) -> func.HttpResponse:
    """ 
    HTTP triggered function reads a `name` parameter in the query 
    string or body of the request and uses it to build a JSON document
    returned to the client, with content type - application/json.
    
    Parameters
    ----------
    req: azure.functions.HttpRequest
        HTTP request object associated with the HTTP trigger.
        See ./function.json for configuration properties.

    Returns
    -------
    azure.functions.HttpResponse
        HTTP response object associated with the HTTP output binding.
        See ./function.json for configuration properties.
    """
        
    logging.info('Python HTTP triggered function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        id = uuid.uuid4()
        res = {
            "id":f"{id}",
            "name":f"{name}"
        }
        return func.HttpResponse(
            json.dumps(res),
            status_code=200,
            headers={"Content-Type": "application/json"}
        )
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
