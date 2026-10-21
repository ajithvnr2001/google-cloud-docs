---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-op/
title: Get an online prediction \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:40:07.941425+00:00
---

# Get an online prediction  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-op/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Get an online prediction Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** Online Prediction is a Preview feature that is available as-is and is not recommended for production environments. Google provides no service-level agreements (SLA) or technical support commitments for Preview features. For more information, see GDC's [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).**Note:** Authorization is not enforced for Online Prediction because it is a Preview feature.

The Online Prediction service of Vertex AI lets you make synchronous requests to your own prediction model endpoint.

This page shows you how to send requests to your model so that it can serve online predictions with low latency.

## Before you begin

Before you can start using the Online Prediction API, you must have a project and appropriate credentials.

Follow these steps before getting an online prediction:

  1. [Set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project).
  2. To get the permissions that you need to access Online Prediction, ask your Project IAM Admin to grant you the Vertex AI Prediction User (`vertex-ai-prediction-user`) role.

For information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

  3. Create and train a prediction model targeting one of the [supported containers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#available-container-images).

  4. Create the [prediction cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/prediction-user-cluster) and ensure your project allows incoming external traffic.

  5. [Export your model artifacts for prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-export-model-artifacts).

  6. [Deploy your model to an endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-deploy-model).

  7. Show details of the `Endpoint` custom resource of your prediction model:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG get endpoint PREDICTION_ENDPOINT -n PROJECT_NAMESPACE -o jsonpath='{.status.endpointFQDN}'
         

Replace the following:

     * `PREDICTION_CLUSTER_KUBECONFIG`: the path to the kubeconfig file in the prediction cluster.
     * `PREDICTION_ENDPOINT`: the name of the endpoint.
     * `PROJECT_NAMESPACE`: the name of the prediction project namespace.

The output must show the `status` field, displaying the endpoint fully-qualified domain name on the `endpointFQDN` field. Register this endpoint URL path to use it for your requests.




## Set your environment variables

If you want to send a request to your model endpoint using a Python script and you [set up a service account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project#set-up-service) in your project to make authorized API calls programmatically, you can define environment variables in the script to access values such as the service account keys when running.

Follow these steps to set required environment variables on a Python script:

  1. [Create a JupyterLab notebook](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench#create-notebook) to interact with the Online Prediction API.

  2. Create a Python script on the JupyterLab notebook.

  3. Add the following code to the Python script:
         
         import os
         
         os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "APPLICATION_DEFAULT_CREDENTIALS_FILENAME"
         

Replace `APPLICATION_DEFAULT_CREDENTIALS_FILENAME` with the name of the JSON file that contains [the service account keys you created](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project#set-up-service) in the project, such as `my-service-key.json`.

  4. Save the Python script with a name, such as `prediction.py`.

  5. Run the Python script to set the environment variables:
         
         python SCRIPT_NAME
         

Replace `SCRIPT_NAME` with the name you gave to your Python script, such as `prediction.py`.


**Note:** Keep the script open when using the environment variables from Python or getting an authentication token.

## Send a request to an endpoint

**Note:** HTTPS is used in Distributed Cloud and the certificate authority (CA) issues the certificate for the machine. For more information, see [Security](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/security).

Make a request to the model's endpoint to get an online prediction:

###  curl 

Follow these steps to make a `curl` request:

  1. Create a JSON file named `request.json` for your request body.

You must add and [format your input for online prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-format-online-prediction) with the request body details that [the target container](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#available-container-images) requires.

  2. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  3. Make the request:
         
         curl -X POST -H "Content-Type: application/json; charset=utf-8" -H "Authorization: Bearer TOKEN"
         https://ENDPOINT_HOSTNAME:443/v1/model:predict -d @request.json
         

Replace the following:

     * `TOKEN`: [the authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `ENDPOINT_HOSTNAME`: your model endpoint FQDN for the online prediction request.



If successful, you receive a JSON response to your online prediction request.

The following output shows an example:
    
    
    {
        "predictions": [[-357.10849], [-171.621658]
        ]
    }
    

For more information about responses, see [Response body details](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-format-online-prediction#response-body-details).

###  Python 

Follow these steps to use the Online Prediction service from a Python script:

  1. Create a JSON file named `request.json` for your request body.

You must add and [format your input for online prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-format-online-prediction) with the request body details that [the target container](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#available-container-images) requires.

  2. [Install the latest version of the Vertex AI Platform client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries).

  3. Set the required environment variables on a Python script.

  4. [Authenticate your API request](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).

  5. Add the following code to the Python script you created:

**Important:** The example explicitly sets a root Certificate Authority (CA) `path-to-ca-cert-file.cert` file, which might not be applicable to your environment. You must perform the necessary adjustments for your specific case.
         
         import json
         import os
         from typing import Sequence
         
         import grpc
         from absl import app
         from absl import flags
         import [google](https://docs.cloud.google.com/python/docs/reference/pubsub/latest)
         
         from google.auth.transport import [requests](https://docs.cloud.google.com/python/docs/reference/google-resumable-media/latest/google.resumable_media.requests.html)
         from google.protobuf import json_format
         from google.protobuf.struct_pb2 import Value
         from google.cloud.aiplatform_v1.services import prediction_service
         
         _INPUT = flags.DEFINE_string("input", None, "input", required=True)
         _ENDPOINT_HOSTNAME = flags.DEFINE_string("endpoint_hostname", None, "Prediction endpoint FQDN", required=True)
         _PROJECT_NAME = flags.DEFINE_string("project_name", None, "project name", required=True)
         _ENDPOINT_NAME = flags.DEFINE_string("endpoint_name", None, "endpoint name", required=True)
         
         os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "path-to-ca-cert-file.cert"
         
         def get_sts_token(endpoint_hostname):
           creds = None
           try:
             creds, _ = [google](https://docs.cloud.google.com/python/docs/reference/pubsub/latest).auth.default()
             creds = creds.with_gdch_audience("https://"+endpoint_hostname+":443")
             req = [requests](https://docs.cloud.google.com/python/docs/reference/google-resumable-media/latest/google.resumable_media.requests.html).[Request](https://docs.cloud.google.com/python/docs/reference/policytroubleshooter-iam/latest/google.cloud.policytroubleshooter_iam_v3.types.ConditionContext.Request.html)()
             creds.refresh(req)
             print("Got token: ")
             print(creds.token)
           except Exception as e:
             print("Caught exception" + str(e))
             raise e
           return creds.token
         
         # predict_client_secure builds a client that requires TLS
         def predict_client_secure(endpoint_hostname, token):
           with open(os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"], 'rb') as f:
             channel_creds = grpc.ssl_channel_credentials(f.read())
         
           call_creds = grpc.access_token_call_credentials(token)
         
           creds = grpc.composite_channel_credentials(
             channel_creds,
             call_creds,
           )
         
           client = prediction_service.PredictionServiceClient(
               transport=prediction_service.transports.grpc.PredictionServiceGrpcTransport(
                channel=grpc.secure_channel(target=endpoint_hostname+":443", credentials=creds)))
         
           return client
         
         def predict_func(client, instances):
           # The endpoint resource name is required for authorization.
           # A wrong value might lead to an access denied error.
           endpoint_resource_name = f"projects/{_PROJECT_NAME.value}/locations/{_PROJECT_NAME.value}/endpoints/{_ENDPOINT_NAME.value}"
           resp = client.[predict](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.prediction_service.PredictionServiceClient.html)(
             endpoint=endpoint_resource_name,
             instances=instances,
             metadata=[("x-vertex-ai-endpoint-id", _ENDPOINT_NAME.value)]
           )
           print(resp)
         
         def main(argv: Sequence[str]):
           del argv  # Unused.
           with open(_INPUT.value) as json_file:
               data = json.[load](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.Predictor.html#google_cloud_aiplatform_prediction_Predictor_load)(json_file)
               instances = [json_format.ParseDict(s, Value()) for s in data["instances"]]
         
           token = get_sts_token(_ENDPOINT_HOSTNAME.value)
           client = predict_client_secure(_ENDPOINT_HOSTNAME.value, token)
           predict_func(client=client, instances=instances)
         
         if __name__=="__main__":
           app.run(main)
         

  6. Save the Python script with a name, such as `prediction.py`.

  7. Make the request to the prediction server:
         
         python SCRIPT_NAME --input request.json \
             --endpoint_hostname ENDPOINT_FQDN \
             --project_name PROJECT_NAME \
             --endpoint_name ENDPOINT_NAME \
         

Replace the following:

     * `SCRIPT_NAME`: the name of the Python script, such as `prediction.py`.
     * `ENDPOINT_FQDN`: Fully Qualified Domain Name of the endpoint for the online prediction request.
     * `PROJECT_NAME`: project name of the endpoint.
     * `ENDPOINT_NAME`: the name of the endpoint to call.



If successful, you receive a JSON response to your online prediction request. For more information about responses, see [Response body details](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-format-online-prediction#response-body-details).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
