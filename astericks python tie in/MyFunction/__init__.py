import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()  # Parse the incoming JSON body
        message = req_body.get('message')

        if message:
            return func.HttpResponse(
                json.dumps({"response": f"Received your message: {message}"}),
                mimetype="application/json"
            )
        else:
            return func.HttpResponse(
                json.dumps({"error": "No 'message' field found in the request body."}),
                status_code=400,
                mimetype="application/json"
            )
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON"}),
            status_code=400,
            mimetype="application/json"
        )
