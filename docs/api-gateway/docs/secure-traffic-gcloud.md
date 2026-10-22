---
url: https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud/
title: Quickstart: Secure traffic to a service with the gcloud CLI \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:54.953610+00:00
---

# Quickstart: Secure traffic to a service with the gcloud CLI  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Secure traffic to a service with the gcloud CLI

This page shows you how to deploy an API on API Gateway to secure traffic to a backend service.

Use the following steps to deploy a new API to access a backend service on Cloud Run functions using the Google Cloud CLI. This quickstart also describes how to use an API key to protect your backend from unauthorized access.

## Before you begin

  1. In the Google Cloud console, go to the **Dashboard** page and select or create a Google Cloud project. 

[Go to Dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

**Note:** If you don't plan to keep the resources you create in this quickstart, create a new project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  2. Confirm that billing is enabled for your project. 

[Enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

  3. Verify that the Google Cloud CLI is downloaded and installed on your machine. 

[Download the gcloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts)

  4. Update `gcloud` components:
         
         gcloud components update

  5. Set the default project. Replace PROJECT_ID with your Google Cloud project ID.
         
         gcloud config set project PROJECT_ID




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

## Deploy an API backend

API Gateway sits in front of a deployed backend service and handles all incoming requests. In this quickstart, API Gateway routes incoming calls to a Cloud Run function backend named `helloGET` that contains the Node.js function shown below.
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Register an HTTP function with the Functions Framework that will be executed
    // when you make an HTTP request to the deployed function's endpoint.
    functions.http('helloGET', (req, res) => {
      res.send('Hello World!');
    });

**Note:** The actual name of the function and backend in the example varies according to the language you choose when completing the Cloud Run functions tutorial. This tutorial uses the **Node.js** example.

Follow the steps in [Quickstart: Deploy a Cloud Run function using the Google Cloud CLI](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-gcloud) to download the sample Cloud Run functions code and deploy the Cloud Run function backend service. Your administrator will need to grant additional roles to your account and to the Cloud Build service account, as described in this quick start.

Copy the **Service URL** that is displayed when the Cloud Run function is deployed. You'll need it when creating the API config in a subsequent step.

## Create an API

Now you are ready to create your API on API Gateway.

  1. Enter the following command, where:

     * API_ID specifies the name of your API. See [API ID requirements](https://docs.cloud.google.com/api-gateway/docs/creating-api#api-id-requirements) for API naming guidelines. 
           
           gcloud api-gateway apis create API_ID 

For example:
    
    gcloud api-gateway apis create **my-api**

  2. On successful completion, you can use the following command to view details about the new API:
         
         gcloud api-gateway apis describe API_ID 

For example:
         
         gcloud api-gateway apis describe **my-api** 

This command returns the following:
         
         createTime: '2020-02-29T21:52:20.297426875Z'
           displayName: **my-api**
           **managedService: my-api-123abc456def1.apigateway.my-project.cloud.goog**
           name: projects/**my-project** /locations/global/apis/**my-api**
           state: ACTIVE
           updateTime: '2020-02-29T21:52:20.647923711Z'




Copy the value of the `managedService` property. This value is used to enable your API in a subsequent step.

## Create an API config

Before API Gateway can be used to manage traffic to your deployed API backend, it needs an API config.

You can create an API config using an OpenAPI description that contains specialized annotations to define the chosen API Gateway behavior. For more details on supported OpenAPI extensions, see the following:

  * [OpenAPI 2.0 extensions in API Gateway](https://docs.cloud.google.com/api-gateway/docs/oasv2-extensions)
  * [OpenAPI 3.x extensions in API Gateway](https://docs.cloud.google.com/api-gateway/docs/oasv3-extensions)



The OpenAPI description used for this quickstart contains routing instructions to our Cloud Run function backend:

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

To upload this OpenAPI description and create an API config using the gcloud CLI:

  1. From the command line, create a new file named `openapi-functions.yaml`.

  2. Copy and paste the contents of the OpenAPI description into the newly created file.

  3. Edit the file as follows:

     1. In the `title` field, replace API_ID with the name of your API and replace optional-string with a brief description of your choosing. The value of this field is used when minting API keys that grant access to this API.
     2. In the `address` field, replace SERVICE_URL with the URL where the Cloud Run function backend service is running, copied in a previous step.
  4. Enter the following command, where:

     * CONFIG_ID specifies the name of your API config.
     * API_ID specifies the name of your API.
     * API_DEFINITION specifies the filename of the OpenAPI spec.
     * SERVICE_ACCOUNT_EMAIL specifies the service account used to sign tokens for backends with authentication configured. For more information, see [Configure a service account](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env#configuring_a_service_account). **Note** : The service account used to create an API config for a Cloud Run functions backend must have the `cloudfunctions.invoker` role assigned.
    
    gcloud api-gateway api-configs create CONFIG_ID \
      --api=API_ID --openapi-spec=API_DEFINITION \
       --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL

For example:
    
    gcloud api-gateway api-configs create **my-config** \
      --api=**my-api** --openapi-spec=openapi2-functions.yaml \
      --backend-auth-service-account=**0000000000000-compute@developer.gserviceaccount.com**

This operation may take several minutes to complete as the API config is propagated to downstream systems. Creating a complex API config could take up to ten minutes to complete successfully.

**Note:** If you run this command and receive an error in the form `FAILED_PRECONDITION: Service Account ... does not exist`, see [Configure a service account](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env#configuring_a_service_account) to confirm that a service account is enabled for your project.**Note:** Only one API config at a time may be created for a given API. Wait until the config creation finishes before attempting to create a new config for the same API.
  5. After the API config is created, you can view its details by running this command:
         
         gcloud api-gateway api-configs describe CONFIG_ID \
           --api=API_ID 

For example:
         
         gcloud api-gateway api-configs describe **my-config** \
           --api=**my-api**

The output shows your API config details, including name and state, as shown in the following example:
         
         createTime: '2020-02-07T18:17:01.839180746Z'
         **displayName: my-config**
         gatewayConfig:
         backendConfig:
           googleServiceAccount: 0000000000000-compute@developer.gserviceaccount.com
         name: projects/my-project/locations/global/apis/my-api/configs/my-config
         serviceRollout:
         rolloutId: 2020-02-07r0
         **state: ACTIVE**
         updateTime: '2020-02-07T18:17:02.173778118Z'




## Create a gateway

Now deploy the API config on a gateway. Deploying an API config on a gateway defines an external URL that API clients can use to access your API.

Run the following command to deploy the API config you just created to API Gateway:
    
    
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
  * PROJECT_ID specifies the name of your Google Cloud project.




For example:
    
    
    gcloud api-gateway gateways create **my-gateway** \
      --api=**my-api** --api-config=**my-config** \
      --location=**us-central1** 

On successful completion, use the following command to view details about the gateway:
    
    
    gcloud api-gateway gateways describe GATEWAY_ID \
      --location=GCP_REGION 

For example:
    
    
    gcloud api-gateway gateways describe **my-gateway** \
      --location=**us-central1** 

This command returns the following:
    
    
    apiConfig: projects/my-project/locations/global/apis/my-api/configs/my-config
    createTime: '2020-02-05T13:44:12.997862831Z'
    **defaultHostname: my-gateway-a12bcd345e67f89g0h.uc.gateway.dev**
    displayName: my-gateway
    name: projects/my-project/locations/us-central1/gateways/my-gateway
    serviceAccount:
          email: 0000000000000-compute@developer.gserviceaccount.com
    **state: ACTIVE**
    updateTime: '2020-02-05T13:45:00.844705087Z'

Note the value of the `defaultHostname` property. This is the hostname portion of the gateway URL you use to test your deployment in the next step.

## Test your API deployment

Now you can send requests to your API using the URL generated upon deployment of your gateway.

Enter the following `curl` command, where:

  * DEFAULT_HOSTNAME specifies the hostname portion of your deployed gateway URL, copied in a previous step.
  * `hello` is the path specified in your API config.


    
    
    curl https://DEFAULT_HOSTNAME/hello

For example: 
    
    
    curl https://**my-gateway-a12bcd345e67f89g0h.uc.gateway.dev** /hello

The output is:
    
    
    Hello World!
    

You have successfully created and deployed an API Gateway!

## Secure access using an API key

To secure access to your API backend with an API key, do the following:

  1. Create an API key associated with your project.
  2. Create and deploy a new API config to secure API access using API keys.
  3. Test your API key



See also [Restricting API access with API keys](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys).

### Create an API key

If you don't already have an API key associated with the Google Cloud project you are using in this quickstart, add one as described in [Create an API Key](https://docs.cloud.google.com/docs/authentication/api-keys#creating_an_api_key).

Copy the returned key string and keep it secure. This is the key value that you will use when testing your API key.

### Create and deploy a new API config

To create and deploy a new API config that secures API access using API keys:

  1. Enable your service. Enter the following command, where: 
     * MANAGED_SERVICE_NAME specifies the name of the managed service created when you deployed the API. This can be viewed in the Managed Service property listed with the `gcloud api-gateway apis describe` command.
     * PROJECT_ID specifies the name of your Google Cloud project.
    
    gcloud services enable MANAGED_SERVICE_NAME.apigateway.PROJECT_ID.cloud.goog

For example: 
    
    gcloud services enable **my-api** -**123abc456def1**.apigateway.**my-project**.cloud.goog

  2. Modify the OpenAPI description used to create your API config to include instructions to enforce an API key validation security policy on all traffic. Add the `security` type and `securityDefinitions` as shown: 

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

The `securityDefinition` configures your API to require an API key passed as a query parameter named `key` when requesting access to all paths defined in the spec. 

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

The `securitySchemes` configures your API to require an API key passed as a query parameter named `key` when requesting access to all paths defined in the spec. 

  3. Create a new API config with the modified OpenAPI spec using the following command: 
         
         gcloud api-gateway api-configs create NEW_CONFIG_ID \
         --api=API_ID --openapi-spec=NEW_API_DEFINITION \
         --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL

For example: 
         
         gcloud api-gateway api-configs create **my-config-key** \
           --api=**my-api** --openapi-spec=**openapi2-functions.yaml** \
           --project=**my-project** --backend-auth-service-account=**0000000000000compute@developer.gserviceaccount.com**

  4. Run the following command to [update your existing gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api#update_a_gateway) with the new API config: 
         
         gcloud api-gateway gateways update GATEWAY_ID \
           --api=API_ID --api-config=NEW_CONFIG_ID \
           --location=GCP_REGION 

For example: 
         
         gcloud api-gateway gateways update **my-gateway** \
           --api=**my-api** --api-config=**my-config-key** \
           --location=**us-central1** 




### Test your API key

Once you have created and deployed the modified API, try making a request to it.

Enter the following `curl` command, where:

  * DEFAULT_HOSTNAME specifies the hostname portion of your deployed gateway URL, copied in a previous step.
  * `hello` is the path specified in your API config.


    
    
    curl https://DEFAULT_HOSTNAME/hello

For example: 
    
    
    curl https://**my-gateway-a12bcd345e67f89g0h.uc.gateway.dev** /hello

This should result in the following error:
    
    
    UNAUTHENTICATED:Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.

Now, enter the following `curl` command where:

  * DEFAULT_HOSTNAME specifies the hostname portion of your deployed gateway URL, copied in a previous step.
  * `hello` is the path specified in your API config.
  * API_KEY specifies the API key you created in the previous step.


    
    
    curl https://DEFAULT_HOSTNAME/hello?key=API_KEY

Now you should see `Hello World!` in the response from your API.

Congratulations! You have successfully protected your API backend with an API Gateway. Now you can start onboarding new API clients by generating additional API keys.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, you can:

  * [Delete your API](https://docs.cloud.google.com/api-gateway/docs/creating-api#delete-an-api)
  * [Delete your gateways](https://docs.cloud.google.com/api-gateway/docs/deploying-api#delete_a_gateway)



Alternatively, you can also delete the Google Cloud project used for this tutorial.

## What's next

  * Learn more [About API Gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway)
  * Walk through [Configure the development environment](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env)
  * Learn about [Authentication between services](https://docs.cloud.google.com/api-gateway/docs/authenticate-service-account)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
