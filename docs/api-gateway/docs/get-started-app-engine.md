---
url: https://docs.cloud.google.com/api-gateway/docs/get-started-app-engine/
title: Getting started with API Gateway and App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:17.007160+00:00
---

# Getting started with API Gateway and App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/get-started-app-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Getting started with API Gateway and App Engine

This page shows you how to set up API Gateway to manage and secure an [App Engine](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine) backend service.

## Task List

Use the following task list as you work through the tutorial. All tasks are required to deploy an API gateway for your App Engine backend service.

  1. Create or select a Google Cloud project.
  2. If you haven't deployed your own App Engine, deploy a sample app. See Before you begin.
  3. Enable the required API Gateway services.
  4. Configure IAP to secure your app. See Configure IAP.
  5. Create an [OpenAPI description](https://docs.cloud.google.com/api-gateway/docs/openapi-overview) that describes your API, and configure the routes to your App Engine. See Create an API config.
  6. Deploy an API gateway using your API config. See Deploying an API Gateway.
  7. Track activity to your apps. See Tracking API activity.
  8. Avoid incurring charges to your Google Cloud account. See Clean up.



## Before you begin

  1. In the Google Cloud console, go to the **Dashboard** page and select or create a Google Cloud project. 

[Go to the Dashboard page](https://console.cloud.google.com/projectselector2/home/dashboard)

**Note:** If you don't plan to keep the resources you create in this tutorial, create a new project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  2. Make sure that billing is enabled for your project. 

[Enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

  3. Make a note of the project ID you want to use for this tutorial. On the rest of this page, this project ID is referred to as PROJECT_ID.

  4. Download and install the Google Cloud CLI. 

[Download the gcloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts)

  5. Update `gcloud`components:
         
         gcloud components update

  6. Set the default project. Replace PROJECT_ID with your Google Cloud project ID:
         
         gcloud config set project PROJECT_ID

  7. If you haven't deployed your own App Engine app, follow the steps in the [App Engine Quickstart](https://docs.cloud.google.com/appengine/docs/standard/python3/create-app) for your language to use the Google Cloud CLI to select or create a Google Cloud project and deploy a sample app. Make a note of the app URL, as well as the region and project ID where your app is deployed.




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

## Configure IAP to secure your app

In order to secure your App Engine app, you must use the [Identity Aware Proxy (IAP)](https://docs.cloud.google.com/iap) to verify that requests are authenticated. This process includes specifying the members who should be granted the `IAP-secured Web App User` role required for the project.

Follow the steps to [Enable IAP](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts#enabling_iap), and verify that you are able to sign in to your application.

**Note:** Once IAP is enabled for your App Engine app, make sure to note the OAuth 2.0 `client_id`. This is used as the IAP_CLIENT_ID later in this tutorial. To locate the OAuth 2.0 `client_id` for your App Engine app, go to the **APIs & Services > Credentials** page in the Google Cloud console. Copy the **Client ID** for your application from the **OAuth 2.0 Client IDs** section of the page.

## Create an API config

Before API Gateway can be used to manage traffic to your deployed App Engine backend, it needs an API config.

You can create an API config using an OpenAPI description that contains specialized annotations to define the chosen API Gateway behavior. You will need to add a Google-specific field that contains the URL for each App Engine app so that API Gateway has the information it needs to invoke an app.

For more details on supported OpenAPI extensions, see the following:

  * [OpenAPI OpenAPI 2.0 extensions in API Gateway](https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions)
  * [OpenAPI OpenAPI 3.x extensions in API Gateway](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions)



To create your API config:

  1. Create a text file called `openapi-appengine.yaml`. For convenience, this page refers to the OpenAPI description by that filename, but you can name it something else if you prefer. 
  2. Copy the contents of the following file into your `openapi-run.yaml` file: 

### OpenAPI 2.0
         
         # openapi-appengine.yaml
         swagger: '2.0'
         info:
           title: **API_ID optional-string**
           description: Sample API on API Gateway with an App Engine backend
           version: 1.0.0
         schemes:
           - https
         produces:
           - application/json
         paths:
           /hello:
             get:
               summary: Greet a user
               operationId: hello
               x-google-backend:
                 address: APP_URL
                 jwt_audience: IAP_CLIENT_ID
               responses:
                 '200':
                   description: A successful response
                   schema:
                     type: string

     * In the `title` field, replace API_ID with the name of your API and replace optional-string with a brief description of your choosing. If your API does not already exist, the command to create the API Config will also create the API with the name you specify. The value of the `title` field is used when minting API keys that grant access to this API. See [API ID requirements](https://docs.cloud.google.com/api-gateway/docs/creating-api#api_id_requirements) for API naming guidelines.
     * In the `address` field in the `x-google-backend` section, replace APP_URL with the actual URL of your App Engine service (the full path of the called API). For example, `https://myapp.an.r.appspot.com/hello`. 

Replace IAP_CLIENT_ID with the OAuth Client ID you created when you set up IAP.

### OpenAPI 3.x
    
    # openapi-appengine.yaml
    openapi: 3.0.4
    info:
      title: **API_ID optional-string**
      description: Sample API on API Gateway with an App Engine backend
      version: 1.0.0
    # Define reusable components in x-google-api-management
    x-google-api-management:
      backends:
        appengine_backend:
          address: APP_URL
          jwtAudience: IAP_CLIENT_ID
          deadline: 30.0
          pathTranslation: APPEND_PATH_TO_ADDRESS
          protocol: "http/1.1"
    # Apply the backend configuration by referencing it by name. Set at the root so this applies to all operations unless overridden.
    x-google-backend: appengine_backend
    paths:
      /hello:
        get:
          summary: Greet a user
          operationId: hello
          responses:
            '200':
              description: A successful response
              schema:
                type: string

     * In the `title` field, replace API_ID with the name of your API and replace optional-string with a brief description of your choosing. If your API does not already exist, the command to create the API Config will also create the API with the name you specify. The value of the `title` field is used when minting API keys that grant access to this API. See [API ID requirements](https://docs.cloud.google.com/api-gateway/docs/creating-api#api_id_requirements) for API naming guidelines.
     * In the `address` field, replace APP_URL with the actual URL of your App Engine service (the full path of the called API). For example, `https://myapp.an.r.appspot.com/hello`. 

Replace IAP_CLIENT_ID with the OAuth Client ID you created when you set up IAP.

  3. Enter the following command, where: 
     * CONFIG_ID specifies the name of your API config.
     * API_ID specifies the name of your API. If the API does not already exist then this command creates it.
     * SERVICE_ACCOUNT_EMAIL specifies the service account used to sign tokens for backends with authentication configured.
    
    gcloud api-gateway api-configs create CONFIG_ID \
      --api=API_ID --openapi-spec=openapi2-appengine.yaml \
     --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL

This operation may take several minutes to complete as the API config is propagated to downstream systems. Creation of a complex API config could take up to ten minutes to complete successfully.

  4. After the API config is created, you can view its details by running this command: 
         
         gcloud api-gateway api-configs describe CONFIG_ID \
           --api=API_ID 




## Deploying an API gateway

Now you can deploy your API on API Gateway. Deploying an API on API Gateway also defines an external URL that API clients can use to access your API.

Run the following command to deploy the API config you just created to API Gateway:
    
    
    gcloud api-gateway gateways create GATEWAY_ID \
      --api=API_ID --api-config=CONFIG_ID \
      --location=GCP_REGION 

Where:

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



On successful completion, you can use the following command to view details about the gateway:
    
    
    gcloud api-gateway gateways describe GATEWAY_ID \
      --location=GCP_REGION

Note the value of the `defaultHostname` property in the output of this command. This is the hostname portion of the gateway URL you use to test your deployment in the next step.

## Testing your API deployment

Now you can send requests to your API using the URL generated upon deployment of your gateway.

Enter the following `curl` command, where:

  * DEFAULT_HOSTNAME specifies the hostname portion of your deployed gateway URL. The value of `defaultHostname` can be found in the output of the `gateways describe` command shown earlier.
  * DEFAULT_HOSTNAME specifies the hostname portion of your deployed gateway URL. The value of `defaultHostname` can be found in the output of the `gateways describe` command shown earlier.
  * `hello` is the path specified in your API config.


    
    
    curl https://DEFAULT_HOSTNAME/hello

For example: 
    
    
    curl https://**my-gateway-a12bcd345e67f89g0h.uc.gateway.dev** /hello

You should see the following output:
    
    
    My-AppEngineApp: Access denied for user gateway-1a2b3c@04d5e6f35FgdsT73dFrty-tp.iam.gserviceaccount.com requesting https://my-project.appspot.com/helloGET. If you should have access, contact myldap@google.com and include the full text of this message.

Success! Your gateway is managing access to your App Engine backend service. To grant access to your App Engine app, you will need to [configure a service account](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env#configuring_a_service_account) with the correct permissions for your gateway.

## Tracking API activity

  1. View the activity graphs for your API on the **API Gateway** page in the Google Cloud console. Click your API to view its activity graphs on the **Overview** page. It may take a few moments for the requests to be reflected in the graphs.

  2. Look at the request logs for your API on the **Logs Explorer** page. A link to the **Logs Explorer** page can be found on the **API Gateway** page in the Google Cloud console. 

[Go to the API Gateway page](https://console.cloud.google.com/api-gateway/api)

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
