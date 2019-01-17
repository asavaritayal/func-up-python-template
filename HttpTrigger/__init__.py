import logging

import azure.functions as func

 
def main(req: func.HttpRequest) -> func.HttpResponse:
    """ 
    HTTP triggered function looks for a `name` parameter in the query 
    string or body of the request and returns a "Hello <name>!" message.
   
    Parameters
    ----------
    req : azure.functions.HttpRequest
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
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
