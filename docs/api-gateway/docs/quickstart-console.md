---
url: https://docs.cloud.google.com/api-gateway/docs/quickstart-console/
title: Quickstart: Secure traffic to a service with the Google Cloud console \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:09.860370+00:00
---

# Quickstart: Secure traffic to a service with the Google Cloud console  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/quickstart-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Secure traffic to a service with the Google Cloud console

This page shows you how to deploy an API on API Gateway to secure traffic to a backend service.

Follow the steps to deploy a new API to access a backend service on Cloud Run functions using the Google Cloud console. This quickstart also describes how to use an API key to protect your backend from unauthorized access.

## Before you begin

  1. In the Google Cloud console, go to the **API Gateway** page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway/gateway)

**Note:** If you don't plan to keep the resources you create in this quickstart, create a new project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  2. API Gateway requires that you enable the following Google services:

Name | Title  
---|---  
`apigateway.googleapis.com` | API Gateway API  
`servicemanagement.googleapis.com` | Service Management API  
`servicecontrol.googleapis.com` | Service Control API  
  
If you have not previously enabled these services for the project you select, you are prompted to do so.

  3. Confirm that billing is enabled for your project. 

[Learn how to enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project)




## Deploy an API backend

API Gateway sits in front of a deployed backend service and handles all incoming requests. In this quickstart, API Gateway routes incoming calls to a Cloud Run function backend named `helloGET` that contains the Node.js function shown below.
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Register an HTTP function with the Functions Framework that will be executed
    // when you make an HTTP request to the deployed function's endpoint.
    functions.http('helloGET', (req, res) => {
      res.send('Hello World!');
    });

Follow the steps in [Quickstart: Using the Google Cloud CLI](https://docs.cloud.google.com/functions/docs/quickstart) to download the sample Cloud Run functions code and deploy the Cloud Run function backend service.

**Note:** The actual name of the function and backend in the example varies according to the language you choose when completing the Cloud Run functions tutorial. This tutorial uses the **Node.js** example.

Follow the steps in [Quickstart: Using the Google Cloud CLI](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-gcloud) to download the sample Cloud Run functions code and deploy the Cloud Run function backend service. Your administrator will need to grant additional roles to your account and to the Cloud Build service account, as described in this quick start.

Copy the **Service URL** that is displayed when the Cloud Run function is deployed. You'll need it when creating the API config, in the next step.

## Create an API config

API Gateway uses an API config to route calls to the backend service. You can use an OpenAPI specification that contains specialized extensions to define the chosen API Gateway behavior. For more details on supported OpenAPI extensions, see the following:

  * [OpenAPI 2.0 extensions in API Gateway](https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions)
  * [OpenAPI 3.x extensions in API Gateway](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions)



The OpenAPI specification for this quickstart contains routing instructions to the Cloud Run function backend:

### OpenAPI 2.0
    
    
    # openapi-functions.yaml
    swagger: '2.0'
    info:
      title: **API_ID optional-string**
      description: Sample API on API Gateway with a Google Cloud Functions backend
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
            address: **SERVICE_URL /helloGET**
          responses:
            '200':
              description: A successful response
              schema:
                type: string

### OpenAPI 3.x
    
    
    # openapi-functions.yaml
    openapi: 3.0.4
    info:
      title: **API_ID optional-string**
      description: Sample API on API Gateway with a Google Cloud Functions backend
      version: 1.0.0
    # Define reusable components in x-google-api-management
    x-google-api-management:
      backends:
        functions_backend:
          address: **SERVICE_URL /helloGET**
          pathTranslation: APPEND_PATH_TO_ADDRESS
          protocol: "http/1.1"
    # Apply the backend configuration by referencing it by name. Set at the root so this applies to all operations unless overridden.
    x-google-backend: functions_backend
    paths:
      /hello:
        get:
          summary: Greet a user
          operationId: hello
          responses:
            '200':
              description: A successful response
              content:
                application/json:
                  schema:
                    type: string

Use this OpenAPI specification to define your API:

  1. From the command line, create a new file named `openapi-functions.yaml`.

  2. Copy and paste the contents of the OpenAPI specification shown in the previous example into the newly created file.

  3. Edit the file as follows:

     1. In the `title` field, replace API_ID with the name of your API (which you create in the next step) and replace optional-string with a brief description of your choosing. The value of this field is used when minting API keys that grant access to this API. See [API ID requirements](https://docs.cloud.google.com/api-gateway/docs/creating-api#api_id_requirements) for API ID naming guidelines.
     2. In the `address` field, replace SERVICE_URL with the URL where the Cloud Run function backend service is running, copied in the previous step.



## Create a gateway

Now you are ready to create and deploy a gateway on API Gateway.

  1. Open the API Gateway page in the Google Cloud console.

[Go to API Gateway](https://console.cloud.google.com/api-gateway/api)

  2. Click **Create Gateway**.

  3. In the **API** section:

     1. Choose to create a new API or select an existing API from the **Select an API** drop-down. For this tutorial, select **Create a new API**.
     2. Enter the **Display Name** for your API.
     3. Enter the **API ID** for your API.
     4. (Optional) Add labels to your API using a key:value format. To add more than one label, click **Add Label** and enter additional values.
  4. In the **API Config** section:

     1. Choose to create a new API config or select an existing API config from the **Select a Config** drop-down. For this tutorial, select **Create a new API config**.
     2. Use the file browser to upload the `openapi-functions.yaml` used to define your API.
     3. Enter a display name for your API config.
     4. Select a service account from the drop-down list. The service account you select is used as identity for API Gateway. If you don't see a service account listed in the drop-down, see [Configuring a service account](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env#configuring_a_service_account) to verify that a service account is enabled for your project.

**Note:** The service account used to create an API config for a Cloud Run functions backend must have the [Cloud Run Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) role assigned.
     5. (Optional) Add labels to your API config using a key:value format. To add more than one label, click **Add Label** and enter additional values.

  5. In the **Gateway details** section:

     1. Enter the display name of the gateway. The URL to the gateway automatically generates.
     2. Select the location of the gateway from the drop-down menu.
     3. (Optional) Add labels to your gateway using a key:value format. To add more than one label, click **Add Label** and enter additional values.
  6. Click **Create Gateway**.




This deploys the API config on a newly created gateway. Deploying an API config on a gateway defines an external URL that API clients can use to access your API.

The operation may take several minutes to complete. To check the status of the creation and deployment process, click the **Notification** icon in the main navigation bar to display a status notification, as shown in the following image:

![Notification panel for status notifications](https://docs.cloud.google.com/static/api-gateway/docs/images/async-notification.png)

On successful completion, you can view details about the gateway on the Gateways landing page.

[Go to API Gateway](https://console.cloud.google.com/api-gateway/gateway)

Make a note of the gateway URL. You use this to test your deployment in the next step.

**Note:** The URL for your newly created gateway may take a few moments to display. If it does not appear momentarily, click **Refresh** on the Gateways landing page to update the display.

## Test your API deployment

Now you can send requests to your API using the URL generated upon deployment of your gateway.

In your browser, enter the following URL, where:

  * GATEWAY_URL specifies your deployed gateway URL.
  * `hello` is the path specified in your API config.


    
    
    https://GATEWAY_URL/hello

For example: 
    
    
    https://**my-gateway-a12bcd345e67f89g0h.uc.gateway.dev** /hello
    

The message `Hello World!` should display in your browser.

You have successfully created and deployed an API Gateway!

## Secure access with an API key

To secure access to your API backend with an API key, do the following:

  1. Create an API key associated with your project.
  2. Create and deploy a new API config to secure API access using API keys.
  3. Test your API key



See also [Restricting API access with API keys](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys).

### Create an API key

If you don't already have an API key associated with the Google Cloud project you are using in this quickstart, add one as described in [Creating an API Key](https://cloud.google.com/docs/authentication/api-keys#creating_an_api_key).

Copy the returned key string and keep it secure. This is the key value that you will use when testing your API key.

### Create and deploy a new API config

To create and deploy a new API config that secures API access using API keys:

  1. Enable your service: 
     1. In the Google Cloud console, go to **APIs & Services > Library**.
     2. In the search bar, enter the Managed Service name of the API you just created. You can find this value in the **Managed Service** column for your API on the APIs landing page. For example: 
            
            **my-api-123abc456def1**.apigateway.**my-project**.cloud.goog

     3. On the landing page for your service, click **Enable**. Note: There may be a delay of up to 30 minutes or more between the time you create your API and the time it appears in the Library. If your API is not visible in the Library, you can enable it using the `gcloud` command line tool. Enter the following command where MANAGED_SERVICE_NAME specifies the Managed Service name of your API: 
            
            gcloud services enable MANAGED_SERVICE_NAME

  2. Modify the OpenAPI specification used to create your API config to include instructions to enforce an API key validation security policy on all traffic. Add the `security` type and `securitySchemes` as shown: 

### OpenAPI 2.0
         
         # openapi2-functions.yaml
           swagger: '2.0'
           info:
             title: API_ID optional-string
             description: Sample API on API Gateway with a Google Cloud Functions backend
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
                   address: SERVICE_URL/helloGET
                 **security :
                 - api_key: []**
                 responses:
                   '200':
                     description: A successful response
                     schema:
                       type: string
           **securityDefinitions :
             # This section configures basic authentication with an API key.
             api_key:
               type: "apiKey"
               name: "key"
               in: "query"**

The `securityDefinition` configures your API to require an API key passed as a query parameter named `key` when requesting access to all paths defined in the specification.

### OpenAPI 3.x
         
         # openapi-functions.yaml
         openapi: 3.0.4
         info:
           title: API_ID optional-string
           description: Sample API on API Gateway with a Google Cloud Functions backend
           version: 1.0.0
         # Define reusable components in x-google-api-management
         x-google-api-management:
           backends:
             functions_backend:
               address: SERVICE_URL/helloGET
               pathTranslation: APPEND_PATH_TO_ADDRESS
               protocol: "http/1.1"
         # Apply the backend configuration by referencing it by name. Set at the root so this applies to all operations unless overridden.
         x-google-backend: functions_backend
         components:
         # This section configures basic authentication with an API key.
           **securitySchemes :
             google_api_key:
               type: apiKey
               name: x-api-key
               in: header
         security:
           - google_api_key: []**
         paths:
           /hello:
             get:
               summary: Greet a user
               operationId: hello
               responses:
                 '200':
                   description: A successful response
                   content:
                     application/json:
                       schema:
                         type: string

The `securitySchemes` configures your API to require an API key passed as a query parameter named `key` when requesting access to all paths defined in the specification.

  3. Create and deploy a new API config to your existing gateway: 
     1. Go to the Gateways landing page. 

[Go to API Gateway](https://console.cloud.google.com/api-gateway/gateway)

     2. Select your gateway from the list to view details.
     3. Click **Edit** to open the gateway configuration pane.
     4. In the **API config** section: 
        1. Select **Create a new API config** from the available drop-down.
        2. Upload your modified OpenAPI specification using the file browser.
        3. Enter the display name for your new API config.
        4. Select a service account from the drop-down list. The service account you select is used as the identity for API Gateway.
        5. (Optional) Add labels to your API config using a key/value format. To add more than one label, click **Add Label** and enter additional values.
     5. Click **Update**.



### Test your API key

Once you have created and deployed the modified API, try making a request to it.

In your browser, enter the following URL, where:

  * GATEWAY_URL specifies your deployed gateway URL.
  * `hello` is the path specified in your API config.


    
    
    https://GATEWAY_URL/hello

This should result in the following error:
    
    
    UNAUTHENTICATED:Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.

Now, in your browser, enter the following URL, where:

  * GATEWAY_URL specifies your deployed gateway URL.
  * `hello` is the path specified in your API config.
  * API_KEY specifies the value of the API key you created in Create an API key.


    
    
    https://GATEWAY_URL/hello?key=API_KEY

Now you should see `Hello World!` in your browser.

Congratulations! You have successfully protected your API backend with an API Gateway. Now you can start onboarding new API clients by generating additional API keys.

## Track API activity

  1. View the activity graphs for your API on the **API Gateway** page in the Google Cloud console. Click your API to view its activity graphs on the **Overview** page. It may take a few moments for the requests to reflect in the graphs.

  2. Look at the request logs for your API on the **Logs Explorer** page. A link to the **Logs Explorer** page can be found on the **API Gateway API** page in the Google Cloud console.

[Go to API Gateway](https://console.cloud.google.com/api-gateway/api)

Once on the API Gateway APIs page:

     1. Select the API to view.
     2. Click the **Details** tab.
     3. Click the link under **Logs.**



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, you can:

  * [Delete your gateways](https://docs.cloud.google.com/api-gateway/docs/deploying-api#delete_a_gateway)
  * [Delete your API](https://docs.cloud.google.com/api-gateway/docs/creating-api#delete-an-api)



Alternatively, you can also delete the Google Cloud project used for this tutorial.

## What's next

  * Learn more [About API Gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway)
  * Walk through [Configure your development environment](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
