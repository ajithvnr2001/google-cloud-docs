---
url: https://docs.cloud.google.com/api-gateway/docs/get-started-cloud-run-grpc/
title: Get started with API Gateway and Cloud Run for gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:42.304381+00:00
---

# Get started with API Gateway and Cloud Run for gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/get-started-cloud-run-grpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with API Gateway and Cloud Run for gRPC 

This page shows you how to set up API Gateway to manage and secure a [Cloud Run](https://docs.cloud.google.com/run/docs) backend service with gRPC.

## Task List

Use the following task list as you work through the tutorial. All tasks are required to deploy an API gateway for your Cloud Run backend service with gRPC.

  1. Create or select a Google Cloud project.
  2. If you haven't deployed your own Cloud Run, deploy a sample backend gRPC service. See step 7 in Before you begin.
  3. Enable the required API Gateway services.
  4. Create a [gRPC API configuration document](https://docs.cloud.google.com/api-gateway/docs/glossary#grpc) that describes your API, and configures the routes to your Cloud Run. See Configure an API config with gRPC.
  5. Deploy an API gateway using your API config. See Deploy an API gateway.
  6. Test your API deployment by sending a request. See Send a request to the API.
  7. Track activity to your services. See Track API activity.
  8. Avoid incurring charges to your Google Cloud account. See Clean up.



## Before you begin

  1. In the Google Cloud console, go to the **Dashboard** page and select or create a Google Cloud project. 

[Go to Dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

**Note:** If you don't plan to keep the resources you create in this tutorial, create a new project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  2. Make sure that billing is enabled for your project. 

[Enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

  3. Make a note of the project ID because it is needed later. On the rest of this page, this project ID is referred to as PROJECT_ID.

  4. Make a note of the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) because it is needed later. On the rest of this page, this project number is referred to as PROJECT_NUMBER.

  5. Download and install the Google Cloud CLI. 

[Download the gcloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts)

  6. Follow the steps in the [ gRPC Python quickstart](https://grpc.io/docs/languages/python/quickstart/) to install gRPC and the gRPC tools.

  7. Deploy the **python-grpc-bookstore-server** example backend gRPC Cloud Run service for use with this tutorial. The gRPC service uses the following container image:

`gcr.io/endpointsv2/python-grpc-bookstore-server:2`

Follow the steps in [Quickstart: Deploy a Prebuilt Sample Container](https://docs.cloud.google.com/run/docs/quickstarts/deploy-container) to deploy the service. Make sure to replace the container image specified in that quickstart with `gcr.io/endpointsv2/python-grpc-bookstore-server:2`

Make a note of the service URL, as well as the region and project ID where your service is deployed.




## Enable required services

API Gateway requires that you enable the following Google Cloud services:

Name | Service name  
---|---  
API Gateway API | `apigateway.googleapis.com`  
Service Management API | `servicemanagement.googleapis.com`  
Service Control API | `servicecontrol.googleapis.com`  
  
To enable required services:

###  Google Cloud console

  1. In the Google Cloud console, go to the **APIs & Services > API Library** page.

[Go to API Library](https://console.cloud.google.com/apis/library)

  2. On the **API Library** page, enter the required API name into the search bar.
  3. In the search results, select the API page.
  4. On the API page, click **Enable**.
  5. Repeat these steps for each of the services listed in the preceding table.



### Google Cloud CLI

Use the following commands to enable the services:
    
    
    gcloud services enable apigateway.googleapis.com
    gcloud services enable servicemanagement.googleapis.com
    gcloud services enable servicecontrol.googleapis.com

For more information about the `gcloud` services, see [`gcloud` services](https://docs.cloud.google.com/sdk/gcloud/reference/services).

## Create an API config with gRPC

The [`bookstore-grpc`](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/bookstore-grpc) sample contains the files that you need to copy locally and configure.

  1. Create a self-contained protobuf descriptor file from your service `.proto` file: 
     1. Save a copy of [ `bookstore.proto`](https://raw.githubusercontent.com/GoogleCloudPlatform/python-docs-samples/master/endpoints/bookstore-grpc/bookstore.proto) from the example repository to your current working directory. This file defines the Bookstore service's API. 
     2. Create the following directory under your working directory: `mkdir generated_pb2`
     3. Create the descriptor file, `api_descriptor.pb`, by using the `protoc` protocol buffers compiler. Run the following command in the directory where you saved `bookstore.proto`: 
            
            python3 -m grpc_tools.protoc \
                --include_imports \
                --include_source_info \
                --proto_path=. \
                --descriptor_set_out=api_descriptor.pb \
                --python_out=generated_pb2 \
                --grpc_python_out=generated_pb2 \
                bookstore.proto

In the preceding command, `--proto_path` is set to the current working directory. In your gRPC build environment, if you use a different directory for `.proto` input files, change `--proto_path` so the compiler searches the directory where you saved `bookstore.proto`. 

  2. Create a text file called `api_config.yaml` in your current working directory (the same directory that contains `bookstore.proto`). For convenience, this page refers to the gRPC API configuration document by that filename, but you can name it something else if you prefer. Add the following contents to the file: 
         
         # The configuration schema is defined by the service.proto file.
         # https://github.com/googleapis/googleapis/blob/master/google/api/service.proto
         
         type: google.api.Service
         config_version: 3
         name: "*.apigateway.PROJECT_ID.cloud.goog"
         title: API Gateway + Cloud Run gRPC
         apis:
           - name: endpoints.examples.bookstore.Bookstore
         usage:
           rules:
           # ListShelves methods can be called without an API Key.
           - selector: endpoints.examples.bookstore.Bookstore.ListShelves
             allow_unregistered_calls: true
         backend:
           rules:
             - selector: "*"
               address: grpcs://python-grpc-bookstore-server-HASH-uc.a.run.app

Indentation is important for yaml format. For example the `name` field must be at the same level as `type`.
  3. In the `name` field, a service named `*.apigateway.PROJECT_ID.cloud.goog` where PROJECT_ID is the name of your Google Cloud project ID. 
  4. In the `address` field in the `backend.rules` section, replace grpcs://python-grpc-bookstore-server-HASH-uc.a.run.app with the actual URL of the **python-grpc-bookstore-server** backend gRPC Cloud Run service, where HASH is the unique hash code generated when you created the service.

**Note:** To use gRPC with TLS on Cloud Run, the `address` field must have the scheme grpcs:// instead of https://.

This example assumes that you are using the gRPC Bookstore backend service created in Before you begin. If necessary, replace this value with the URL of your Cloud Run service.

  5. Save your gRPC API configuration document.
  6. Create the API config: 
         
         gcloud api-gateway api-configs create CONFIG_ID \
         --api=API_ID \
         --grpc-files=api_descriptor.pb,api_config.yaml

where: 
     * CONFIG_ID specifies the name of your API config.
     * API_ID specifies the name of your API.
For example: 
    
    gcloud api-gateway api-configs create **grpc-config** \
    --api=**grpc-test** --project=**my-test-project** \
    --grpc-files=api_descriptor.pb,api_config.yaml




## Deploy an API gateway

To deploy the gRPC API config to a gateway, run the following command:
    
    
    gcloud api-gateway gateways create GATEWAY_ID \
      --api=API_ID --api-config=CONFIG_ID \
      --location=GCP_REGION 

where:

  * GATEWAY_ID specifies the name of the gateway.
  * API_ID specifies the name of the API Gateway API associated with this gateway.
  * CONFIG_ID specifies the name of the API config deployed to the gateway.
  * GCP_REGION is the [Google Cloud region](https://cloud.google.com/about/locations/) for the deployed gateway.

**Note:** Allowed values are: 
    * `asia-northeast1`
    * `australia-southeast1`
    * `europe-west1`
    * `europe-west2`
    * `us-east1`
    * `us-east4`
    * `us-central1`
    * `us-west2`
    * `us-west3`
    * `us-west4`



For example:
    
    
    gcloud api-gateway gateways create **bookstore-grpc** \
      --api=**grpc-test** --api-config=**grpc-config** \
      --location=**us-central1** --project=**my-project**

On successful completion, you can use the following command to view details about the gateway:
    
    
    gcloud api-gateway gateways describe GATEWAY_ID \
      --location=GCP_REGION

Note the value of the `defaultHostname` property in the output of this command. This is the hostname portion of the gateway URL you use to test your deployment in the next step.

For example: 
    
    
    https://**my-gateway-a12bcd345e67f89g0h.uc.gateway.dev**
    

## Send a request to the API

To send requests to the sample API, you can use a sample gRPC client written in Python.

  1. Clone the git repository where the gRPC client code is hosted:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

  2. Change your working directory:
         
         cd python-docs-samples/endpoints/bookstore-grpc/

  3. Install dependencies:
         
         pip3 install virtualenv
         virtualenv env
         source env/bin/activate
         pip3 install -r requirements.txt

  4. Send a request to the sample API:
         
         python3 bookstore_client.py --host=DEFAULT_HOSTNAME --port 443 --use_tls true

Specify the `defaultHostname` property of your gateway in DEFAULT_HOSTNAME, without the protocol identifier. For example:
         
         python3 bookstore_client.py --host=**my-gateway-a12bcd345e67f89g0h.uc.gateway.dev** --port 443 --use_tls true




## Track API activity

  1. View the activity graphs for your API on the **API Gateway** page in the Google Cloud console. Click your API to view its activity graphs on the **Overview** page. It may take a few moments for the requests to be reflected in the graphs.

  2. Look at the request logs for your API on the **Logs Explorer** page. A link to the **Logs Explorer** page can be found on the **API Gateway** page in the Google Cloud console.

[Go to API Gateway](https://console.cloud.google.com/api-gateway/gateway)

Once on the API Gateway page:

     1. Select the API to view.
     2. Click the **Details** tab.
     3. Click the link under **Logs.**



You just deployed and tested an API in API Gateway with gRPC!

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, you can:

  * [Delete your gateways](https://docs.cloud.google.com/api-gateway/docs/deploying-api#deleting_a_gateway)
  * [Delete your API](https://docs.cloud.google.com/api-gateway/docs/creating-api#deleting-an-api)



Alternatively, you can also delete the Google Cloud project used for this tutorial.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
