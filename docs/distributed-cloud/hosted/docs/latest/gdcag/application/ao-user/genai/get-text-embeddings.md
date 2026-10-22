---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/get-text-embeddings/
title: Get text embeddings \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:06.825596+00:00
---

# Get text embeddings  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/get-text-embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Get text embeddings Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** This content applies to version 1.14.4 and later.

This page describes how to create a text embedding using the Text Embedding API.

Vertex AI supports text embeddings in Google Distributed Cloud (GDC) air-gapped through the Text Embedding API. Text Embedding uses vector representations.

Text Embedding converts textual data written in any supported language into numerical vectors. These vector representations are designed to capture the semantic meaning and context of the words they represent. Text embedding models can generate optimized embeddings for various task types, such as document retrieval, questions and answers, classification, and fact verification for text.

For more information about key concepts that text embeddings use, see the following documentation:

  * To learn more about embeddings, see the [text embeddings overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/text-embeddings-overview).
  * To learn about text embedding models, see [Embeddings models](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/genai-models#embeddings-models).
  * To learn how task types generate optimized embeddings, see [Choose an embeddings task type](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/text-embeddings-task-type).
  * For information about which languages each embedding model supports, see [Supported text embedding languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/supported-text-languages).



## Before you begin

To generate text embeddings in a GDC project, request the necessary permissions from your administrator.

### Request IAM roles

Contact your Project IAM Admin to request one of the following roles in your project namespace, depending on the model that you want to use:

  * **AI Text Embedding Developer** (`ai-text-embedding-developer`): generate text embeddings using the Text Embedding model.
  * **AI Text Embedding Multilingual Developer** (`ai-text-embedding-multilingual-developer`): generate text embeddings using the Text Embedding Multilingual model.



For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions). For information about role bindings for service accounts, see [Set up service accounts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project#set-up-service).

### Prepare your environment

Before using Text Embedding in a GDC project, follow these steps:

  1. [Set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project).
  2. [Choose one of the available models for text embeddings](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/genai-models#embeddings-models), depending on the [language](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/supported-text-languages) and [task type](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/text-embeddings-task-type).
  3. [Enable the Text Embedding or Text Embedding Multilingual API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-enable-pre-trained-apis), depending on the model you want to use.
  4. [Install the Vertex AI client libraries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries).

**Important:** You must install the Vertex AI Platform client library to use Text Embedding and Text Embedding Multilingual.
  5. [Get an authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth).




You must use the same project for your model requests, the service account, and the IAM role binding.

## Get text embeddings for a snippet of text

After meeting the prerequisites, you can use the Text Embedding or Text Embedding Multilingual models to get text embeddings for a snippet of text by using the API or the SDK for Python.

The following examples use the `text-embedding-004` model.

Make a REST request to the Text Embedding API. Otherwise, interact with the model from a Python script to get a text embedding.

###  REST 

To get text embeddings, send a POST request by specifying the model endpoint.

Follow these steps to make a request:

  1. Save your request content in a JSON file named `request.json`. The file must look like the following example:
         
         {
           "instances": [
             {
               "content": "What is life?",
               "task_type": "",
               "title": ""
             }
           ]
         }
         

  2. Make the request using the `curl` tool:
         
         curl -X POST \
         -H "Authorization: Bearer TOKEN"\
         -H "Content-Type: application/json; charset=utf-8" \
         -d @request.json \
         "https://ENDPOINT:443/v1/projects/PROJECT/locations/PROJECT/endpoints/MODEL:predict"
         

Replace the following:

     * `TOKEN`: the [authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `ENDPOINT`: the Text Embedding or Text Embedding Multilingual endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `PROJECT`: your project name.
     * `MODEL`: the model you want to use. The following are the available values:

       * `endpoint-text-embedding` for the Text Embedding model.
       * `endpoint-text-embedding-multilingual` for the Text Embedding Multilingual model.



You must obtain a JSON response similar to the following:
    
    
    {"predictions":[[-0.00668720435,3.20804138e-05,-0.0281705819,-0.00954890903,-0.0818724185,0.0150693133,-0.00677698106, …. ,0.0167487375,-0.0534791686,0.00208711182,0.032938987,-0.01491543]],"deployedModelId":"text-embedding","model":"models/text-embedding/1","modelDisplayName":"text-embedding","modelVersionId":"1"}
    

###  Python 

Follow these steps to get text embeddings from a Python script:

  1. [Install the Vertex AI Platform client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries).

  2. Save your request content in a JSON file named `request.json`. The file must look like the following example:
         
         {
           "instances": [
             {
               "content": "What is life?",
               "task_type": "",
               "title": ""
             }
           ]
         }
         

  3. Install the required Python libraries:
         
         pip install absl-py
         

  4. Create a Python file named `client.py`. The file must look like the following example:
         
         import json
         import os
         from typing import Sequence
         
         import grpc
         from absl import app
         from absl import flags
         
         from google.protobuf import json_format
         from google.protobuf.struct_pb2 import Value
         from google.cloud.aiplatform_v1.services import prediction_service
         
         _INPUT = flags.DEFINE_string("input", None, "input", required=True)
         _HOST = flags.DEFINE_string("host", None, "Prediction endpoint", required=True)
         _ENDPOINT_ID = flags.DEFINE_string("endpoint_id", None, "endpoint id", required=True)
         _TOKEN = flags.DEFINE_string("token", None, "STS token", required=True)
         
         # ENDPOINT_RESOURCE_NAME is a placeholder value that doesn't affect prediction behavior.
         ENDPOINT_RESOURCE_NAME="projects/PROJECT/locations/PROJECT/endpoints/MODEL"
         
         os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = CERT_NAME
         
         # predict_client_secure builds a client that requires TLS
         def predict_client_secure(host):
           with open(os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"], 'rb') as f:
               creds = grpc.ssl_channel_credentials(f.read())
         
           channel_opts = ()
           channel_opts += (('grpc.ssl_target_name_override', host),)
           client = prediction_service.PredictionServiceClient(
               transport=prediction_service.transports.grpc.PredictionServiceGrpcTransport(
                   channel=grpc.secure_channel(target=host+":443", credentials=creds, options=channel_opts)))
           return client
         
         def predict_func(client, instances, token):
           resp = client.predict(
               endpoint=ENDPOINT_RESOURCE_NAME,
               instances=instances,
               metadata=[ ("x-vertex-ai-endpoint-id", _ENDPOINT_ID.value), ("authorization", "Bearer " + token),])
           print(resp)
         
         def main(argv: Sequence[str]):
           del argv  # Unused.
           with open(_INPUT.value) as json_file:
               data = json.load(json_file)
               instances = [json_format.ParseDict(s, Value()) for s in data["instances"]]
         
           client = predict_client_secure(_HOST.value,)
         
           predict_func(client=client, instances=instances, token=_TOKEN.value)
         
         if __name__=="__main__":
           app.run(main)
         

Replace the following:

     * `PROJECT`: your project name.
     * `MODEL`: the model you want to use. The following are the available values: 
       * `text-embedding` for the Text Embedding model.
       * `text-embedding-multilingual` for the Text Embedding Multilingual model.
     * `CERT_NAME`: the name of the Certificate Authority (CA) certificate file, such as `org-1-trust-bundle-ca.cert`. You only need this value if you are in a development environment. Otherwise, omit it.
  5. Send a request:
         
         python client.py --token=TOKEN --host=ENDPOINT --input=request.json --endpoint_id=MODEL
         

Replace the following:

     * `TOKEN`: the [authentication token](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-auth) you obtained.
     * `ENDPOINT`: the Text Embedding or Text Embedding Multilingual endpoint that you use for your organization. For more information, [view service status and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status).
     * `MODEL`: the model you want to use. The following are the available values:

       * `text-embedding` for the Text Embedding model.
       * `text-embedding-multilingual` for the Text Embedding Multilingual model.



You must obtain a JSON response similar to the following:
    
    
    {"predictions":[[-0.00668720435,3.20804138e-05,-0.0281705819,-0.00954890903,-0.0818724185,0.0150693133,-0.00677698106, …. ,0.0167487375,-0.0534791686,0.00208711182,0.032938987,-0.01491543]],"deployedModelId":"text-embedding","model":"models/text-embedding/1","modelDisplayName":"text-embedding","modelVersionId":"1"}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
