---
url: https://docs.cloud.google.com/api-gateway/docs/get-started-cloud-run/
title: Getting started with API Gateway and Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:55.729939+00:00
---

# Getting started with API Gateway and Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/get-started-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Getting started with API Gateway and Cloud Run 

This page shows you how to set up API Gateway to manage and secure a [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) backend service.

## Task List

Use the following task list as you work through the tutorial. All tasks are required to deploy an API Gateway for your Cloud Run backend service.

  1. Create or select a Google Cloud project.
  2. If you haven't deployed your own Cloud Run, deploy a sample service. See step 7 in Before you begin.
  3. Enable the required API Gateway services.
  4. Create an [OpenAPI description](https://docs.cloud.google.com/api-gateway/docs/openapi-overview) that describes your API, and configure the routes to your Cloud Run backend service. See Creating an API config.
  5. Deploy an API gateway using your API config. See Deploying an API gateway.
  6. Track activity to your services. See Tracking API activity.
  7. Avoid incurring charges to your Google Cloud account. See Clean up.



## Before you begin

  1. In the Google Cloud console, go to the **Dashboard** page and select or create a Google Cloud project. 

[Go to Dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

**Note:** If you don't plan to keep the resources you create in this tutorial, create a new project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  2. Make sure that billing is enabled for your project. 

[Enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

  3. Make a note of the project ID you want to use for this tutorial. On the rest of this page, this project ID is referred to as PROJECT_ID.

  4. Download and install the Google Cloud CLI. 

[Download the gcloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts)

  5. Update `gcloud`components:
         
         gcloud components update

  6. Set the default project. Replace PROJECT_ID with your Google Cloud project ID
         
         gcloud config set project PROJECT_ID

  7. If you haven't deployed your own Cloud Run service, follow the steps in [Quickstart: Deploy a Prebuilt Sample Container](https://docs.cloud.google.com/run/docs/quickstarts/deploy-container) to select or create a Google Cloud project and deploy a sample backend. Make a note of the app URL, as well as the region and project ID where your apps are deployed.




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

## Create an API config

Before API Gateway can be used to manage traffic to your deployed Cloud Run backend, it needs an API config.

You can create an API config using an OpenAPI description that contains specialized annotations to define the chosen API Gateway behavior. You will need to add a Google-specific field that contains the URL for each Cloud Run app so that API Gateway has the information it needs to invoke an app.

For more details on supported OpenAPI extensions, see the following:

  * [OpenAPI 2.0 extensions in API Gateway](https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions)
  * [OpenAPI 3.x extensions in API Gateway](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions)



To create your API config:

  1. Create a text file called `openapi-run.yaml`. For convenience, this page refers to the OpenAPI description by that filename, but you can name it something else if you prefer. 
  2. Copy the contents of the following file into your `openapi-run.yaml` file: 

### OpenAPI 2.0
         
         # openapi-run.yaml
         swagger: '2.0'
         info:
           title: **API_ID optional-string**
           description: Sample API on API Gateway with a Cloud Run backend
           version: 1.0.0
         schemes:
         - https
         produces:
         - application/json
         x-google-backend:
           address: APP_URL
         paths:
           /assets/{asset}:
             get:
               parameters:
                 - in: path
                   name: asset
                   type: string
                   required: true
                   description: Name of the asset.
               summary: Assets
               operationId: getAsset
               responses:
                 '200':
                   description: A successful response
                   schema:
                     type: string
           /hello:
             get:
               summary: Cloud Run hello world
               operationId: hello
               responses:
                 '200':
                   description: A successful response
                   schema:
                     type: string

     * In the `title` field, replace API_ID with the name of your API and replace optional-string with a brief description of your choosing. If your API does not already exist, the command to create the API Config will also create the API with the name you specify. The value of the `title` field is used when minting API keys that grant access to this API. See [API ID requirements](https://docs.cloud.google.com/api-gateway/docs/creating-api#api_id_requirements) for API naming guidelines.
     * In the `address` field in the `x-google-backend` section, replace APP_URL with the actual URL of your Cloud Run service (the full path of the called API). For example: `https://hello-abc1def2gh-uc.a.run.app`. **Note** : If you plan to use the [deterministic URL](https://docs.cloud.google.com/run/docs/triggering/https-request#deterministic) to version your Cloud Run service backend, you must specify the [`jwt_audience`](https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions#jwt_audience_disable_auth) field under `address` in the `x-google-backend` section. The value of the `jwt_audience` field should be the Cloud Run service hostname. For example: 
           
           ...
             x-google-backend:
                 address: https://VERSION_TAG---SERVICE_HOSTNAME/PATH
                 jwt_audience: https://SERVICE_HOSTNAME
           ...

If the `jwt_audience` field is not present, the `x-google-backend` extension defaults to the value of the `address` field for the JWT audience claim. This can result in an unexpected JWT audience claim for Cloud Run if the revision tag URL is used for `address` and no `jwt_audience` is specified.

### OpenAPI 3.x
    
    # openapi-run.yaml
    openapi: 3.0.4
    info:
      title: API_ID optional-string
      description: Sample API on API Gateway with a Cloud Run backend
      version: 1.0.0
    # Define reusable components in x-google-api-management
    x-google-api-management:
      backends:
        cloudrun_backend:
          address: APP_URL
          deadline: 30.0
          pathTranslation: APPEND_PATH_TO_ADDRESS
          protocol: "http/1.1"
    # Apply the backend configuration by referencing it by name. Set at the root so this applies to all operations unless overridden.
    x-google-backend: cloudrun_backend
    paths:
      /hello:
        get:
          summary: Greet a user
          operationId: hello
          responses:
            "200":
              description: A successful response
              content:
                application/json:
                  schema:
                    type: string

     * In the `title` field, replace API_ID with the name of your API and replace optional-string with a brief description of your choosing. If your API does not already exist, the command to create the API Config will also create the API with the name you specify. The value of the `title` field is used when minting API keys that grant access to this API. See [API ID requirements](https://docs.cloud.google.com/api-gateway/docs/creating-api#api_id_requirements) for API naming guidelines.
     * In the `address` field, replace APP_URL with the actual URL of your Cloud Run service (the full path of the called API). For example: `https://hello-687541448612.us-central1.run.app`.
**Note** : If you plan to use the [deterministic URL](https://docs.cloud.google.com/run/docs/triggering/https-request#deterministic) to version your Cloud Run service backend, you must specify the [`jwtAudience`](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions#backend_object) field under `address` in the `x-google-api-management` section. The value of the `jwtAudience` field should be the Cloud Run service hostname. For example: 
    
    ...
      x-google-api-management:
        backends:
          cloudrun_backend:
            address: https://VERSION_TAG---SERVICE_HOSTNAME/PATH
            jwtAudience: https://SERVICE_HOSTNAME
    ...

If the `jwtAudience` field is not present, the `x-google-backend` extension defaults to the value of the `address` field for the JWT audience claim. This can result in an unexpected JWT audience claim for Cloud Run if the revision tag URL is used for `address` and no `jwtAudience` is specified.

  3. Enter the following command, where: 
     * CONFIG_ID specifies the name of your API config.
     * API_ID specifies the name of your API. If the API does not already exist then this command creates it.
     * PROJECT_ID specifies the name of your Google Cloud project.
     * SERVICE_ACCOUNT_EMAIL specifies the service account used to sign tokens for backends with authentication configured. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). **Note** : The service account used to create an API config for a Cloud Run backend must have the `run.invoker` role assigned.
    
    gcloud api-gateway api-configs create CONFIG_ID \
      --api=API_ID --openapi-spec=openapi2-run.yaml \
      --project=PROJECT_ID --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL

This operation may take several minutes to complete as the API config is propagated to downstream systems. Creation of a complex API config could take up to ten minutes to complete successfully.

  4. After the API config is created, you can view its details by running this command: 
         
         gcloud api-gateway api-configs describe CONFIG_ID \
           --api=API_ID




## Deploy an API gateway

Now you can deploy your API on API Gateway. Deploying an API on API Gateway also defines an external URL that API clients can use to access your API.

Run the following command to deploy the API config you just created to API Gateway:
    
    
    gcloud api-gateway gateways create GATEWAY_ID \
      --api=API_ID --api-config=CONFIG_ID \
      --location=GCP_REGION --project=PROJECT_ID

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
  * PROJECT_ID specifies the name of your Google Cloud project.




On successful completion, you can use the following command to view details about the gateway:
    
    
    gcloud api-gateway gateways describe GATEWAY_ID \
      --location=GCP_REGION --project=PROJECT_ID

Note the value of the `defaultHostname` property in the output of this command. This is the hostname portion of the gateway URL you use to test your deployment in the next step.

## Test your API deployment

Now you can send requests to your API using the URL generated upon deployment of your gateway.

Enter the following URL in your web browser, where:

  * DEFAULT_HOSTNAME specifies the hostname portion of your deployed gateway URL.
  * `hello` is the path specified in your API config.


    
    
    https://DEFAULT_HOSTNAME/hello

For example: 
    
    
    https://**my-gateway-687541448612.us-central1.run.app** /hello
    

You should see your Cloud Run container running your app in the browser.

Success! Your gateway is managing access to your Cloud Run backend service.

## Track API activity

  1. View the activity graphs for your API on the **API Gateway** page in the Google Cloud console. Click your API to view its activity graphs on the **Overview** page. It may take a few moments for the requests to be reflected in the graphs.

  2. Look at the request logs for your API on the **Logs Explorer** page. A link to the **Logs Explorer** page can be found on the **API Gateway** page in the Google Cloud console.

Once on the API Gateway page:

     1. Select the API to view.
     2. Click the **Details** tab.
     3. Click the link under **Logs.**



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, you can:

  * [Delete your gateways](https://docs.cloud.google.com/api-gateway/docs/deploying-api#deleting_a_gateway)
  * [Delete your API](https://docs.cloud.google.com/api-gateway/docs/creating-api#deleting-an-api)



Alternatively, you can also delete the Google Cloud project used for this tutorial.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
