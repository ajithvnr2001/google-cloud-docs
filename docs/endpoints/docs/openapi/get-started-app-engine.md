---
url: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-app-engine/
title: Getting started with Cloud Endpoints for the App Engine flexible environment with ESP \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:07.138702+00:00
---

# Getting started with Cloud Endpoints for the App Engine flexible environment with ESP  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-app-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Getting started with Cloud Endpoints for the App Engine flexible environment with ESP Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to configure and deploy a sample API and the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) running on an instance in the [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible). The sample API is described using the [OpenAPI specification](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview). The tutorial also shows you how to create an [API key](https://docs.cloud.google.com/endpoints/docs/openapi/when-why-api-key) and use it in requests to the API.

For an overview of Cloud Endpoints, see [About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints) and [Endpoints architecture](https://docs.cloud.google.com/endpoints/docs/openapi/architecture-overview). 

## Objectives

Use the following high-level task list as you work through the tutorial. All tasks are required to successfully send requests to the API.

  1. Set up a Google Cloud project, install the required software, and create an App Engine app. See Before you begin.
  2. Download the sample code. See Getting the sample code.
  3. Configure the `openapi-appengine.yaml` file, which is used to configure Endpoints. See Configuring Endpoints.
  4. Deploy the Endpoints configuration to create an Endpoints service. See Deploying the Endpoints configuration.
  5. Deploy the API and ESP to App Engine. See Deploying the API backend.
  6. Send a request to the API. See Sending a request to the API.
  7. Track API activity. See Tracking API activity.
  8. Avoid incurring charges to your Google Cloud account. See Clean up.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [App Engine](https://docs.cloud.google.com/appengine/pricing)
  * [Endpoints](https://docs.cloud.google.com/endpoints/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Make a note of the project ID because it's needed later. 
  7. You need an application to send requests to the sample API.

     * Linux and macOS users: This tutorial provides an example of using `curl`, which typically comes pre-installed on your operating system. If you don't have `curl`, you can download it from the `curl` [ Releases and downloads page](https://curl.haxx.se/download.html). 
     * Windows users: This tutorial provides an example using [`Invoke-WebRequest`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest), which is supported in PowerShell 3.0 and later. 
  8. [Download the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts). 
  9. Update the gcloud CLI and install the Endpoints components. 
         
         gcloud components update

  10. Make sure that the Google Cloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud: 
         
         gcloud auth login

In the new browser tab that opens, select an account. 
  11. Set the default project to your project ID. 
         
         gcloud config set project YOUR_PROJECT_ID

Replace YOUR_PROJECT_ID with your project ID. If you have other Google Cloud projects, and you want to use `gcloud` to manage them, see [ Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations).

  12. Select the region where you want to create your App Engine application. Run the following command to get a list of regions: 
         
         gcloud app regions list

  13. Create an App Engine application. Replace YOUR_PROJECT_ID with your Google Cloud project ID and YOUR_REGION with the region that you want the App Engine application created in. 
         
         gcloud app create \
           --project=YOUR_PROJECT_ID \
           --region=YOUR_REGION
         

  14. If your App Engine default service account does not have the Editor (`roles/editor`) role, then grant the following permissions: 
     * Grant `roles/servicemanagement.serviceConsumer` to the App Engine default service account at the service level. 
     * Grant `roles/servicemanagement.serviceController` to the App Engine default service account at the project level. 

For information on granting roles to the service account, see [ Managing access using Google Cloud console](https://docs.cloud.google.com/service-infrastructure/docs/service-management/access-control#managing_access_using).




## Getting the sample code

Java

To clone or download the sample API: 

  1. The sample code uses Maven. If you don't have Maven 3.3.9 or higher, [download](http://maven.apache.org/download.cgi) and [install](http://maven.apache.org/install.html) it. 
  2. Clone the sample app repository to your local machine: 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples

Alternatively, [download the sample](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/master.zip) as a zip file and extract it. 

  3. Change to the directory that contains the sample code: 
         
         cd java-docs-samples/endpoints/getting-started


Python

To clone or download the sample API: 

  1. Clone the sample app repository to your local machine: 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples

Alternatively, [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the sample code: 
         
         cd python-docs-samples/endpoints/getting-started


Go

To clone or download the sample API: 

  1. Make sure your [ `GOPATH` environment variable](https://golang.org/cmd/go/#hdr-GOPATH_environment_variable) is set. 
  2. Clone the sample app repository to your local machine: 
         
         go get -d github.com/GoogleCloudPlatform/golang-samples/endpoints/getting-started

  3. Change to the directory that contains the sample code: 
         
         cd $GOPATH/src/github.com/GoogleCloudPlatform/golang-samples/endpoints/getting-started


PHP

To clone or download the sample API: 

  1. Clone the sample app repository to your local machine: 
         
         git clone https://github.com/GoogleCloudPlatform/php-docs-samples

Alternatively, [download the sample](https://github.com/GoogleCloudPlatform/php-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the sample code: 
         
         cd php-docs-samples/endpoints/getting-started


Ruby

To clone or download the sample API: 

  1. Clone the sample app repository to your local machine: 
         
         git clone https://github.com/GoogleCloudPlatform/ruby-docs-samples

Alternatively, [download the sample](https://github.com/GoogleCloudPlatform/ruby-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the sample code: 
         
         cd ruby-docs-samples/endpoints/getting-started


NodeJS

To clone or download the sample API: 

  1. Clone the sample app repository to your local machine: 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples

Alternatively, [download the sample](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the sample code: 
         
         cd nodejs-docs-samples/endpoints/getting-started




## Configuring Endpoints

You must have an OpenAPI document based on either OpenAPI 2.0 or OpenAPI 3.x that describes the [surface](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#surface) of your apps and any authentication requirements. To learn more, see [Supported OpenAPI versions](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview#supported-openapi-versions).

You also need to add a Google-specific field that contains the URL for each app so that ESPv2 has the information it needs to invoke an app. If you are new to OpenAPI, see [OpenAPI overview](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview) for more information.

### OpenAPI 2.0

To configure Endpoints using an OpenAPI 2.0 specification, you can use the `openapi-appengine.yaml` file available in the `dotnet-docs-samples-master\endpoints\getting-started` directory of the downloaded sample code.

The contents of the OpenAPI 2.0 specification should look similar to the following:
    
    
    swagger: "2.0"
    info:
      description: "A simple Google Cloud Endpoints API example."
      title: "Endpoints Example"
      version: "1.0.0"
    host: "YOUR_PROJECT_ID.appspot.com"
    consumes:
    - "application/json"
    produces:
    - "application/json"
    schemes:
    - "https"
    paths:
      "/echo":
        post:
          description: "Echo back a given message."
          operationId: "echo"
          produces:
          - "application/json"
          responses:
            200:
              description: "Echo"
              schema:
                $ref: "#/definitions/echoMessage"
          parameters:
          - description: "Message to echo"
            in: body
            name: message
            required: true
            schema:
              $ref: "#/definitions/echoMessage"
          security:
          - api_key: []
      "/auth/info/googlejwt":
        get:
          description: "Returns the requests' authentication information."
          operationId: "auth_info_google_jwt"
          produces:
          - "application/json"
          responses:
            200:
              description: "Authentication info."
              schema:
                $ref: "#/definitions/authInfoResponse"
          x-security:
          - google_jwt:
              audiences:
              # This must match the "aud" field in the JWT. You can add multiple
              # audiences to accept JWTs from multiple clients.
              - "echo.endpoints.sample.google.com"
      "/auth/info/googleidtoken":
        get:
          description: "Returns the requests' authentication information."
          operationId: "authInfoGoogleIdToken"
          produces:
          - "application/json"
          responses:
            200:
              description: "Authenication info."
              schema:
                $ref: "#/definitions/authInfoResponse"
          x-security:
          - google_id_token:
              audiences:
              # Your OAuth2 client's Client ID must be added here. You can add
              # multiple client IDs to accept tokens from multiple clients.
              - "YOUR-CLIENT-ID"
    
    definitions:
      echoMessage:
        type: "object"
        properties:
          message:
            type: "string"
      authInfoResponse:
        properties:
          id:
            type: "string"
          email:
            type: "string"
    
    securityDefinitions:
      # This section configures basic authentication with an API key.
      api_key:
        type: "apiKey"
        name: "key"
        in: "query"
      # This section configures authentication using Google API Service Accounts
      # to sign a json web token. This is mostly used for server-to-server
      # communication.
      google_jwt:
        authorizationUrl: ""
        flow: "implicit"
        type: "oauth2"
        # This must match the 'iss' field in the JWT.
        x-google-issuer: "jwt-client.endpoints.sample.google.com"
        # Update this with your service account's email address.
        x-google-jwks_uri: "https://www.googleapis.com/service_accounts/v1/jwk/YOUR-SERVICE-ACCOUNT-EMAIL"
      # This section configures authentication using Google OAuth2 ID Tokens.
      # ID Tokens can be obtained using OAuth2 clients, and can be used to access
      # your API on behalf of a particular user.
      google_id_token:
        authorizationUrl: ""
        flow: "implicit"
        type: "oauth2"
        x-google-issuer: "https://accounts.google.com"
        x-google-jwks_uri: "https://www.googleapis.com/oauth2/v1/certs"

On the line with the host field, replace YOUR_PROJECT_ID with your Google Cloud project ID.

### OpenAPI 3.x

To configure Endpoints using an OpenAPI 3.x specification, you can replace the contents of the `openapi-appengine.yaml` file available in the `dotnet-docs-samples-master\endpoints\getting-started` directory of the downloaded sample code:

  1. Open the `openapi-appengine.yaml` in your text editor and replace the contents with the following: 
         
         openapi: 3.0.4
         info:
           description: "A simple Google Cloud Endpoints API example."
           title: "Endpoints Example"
           version: "1.0.0"
         servers:
           - url: "https://YOUR_PROJECT_ID.appspot.com"
             x-google-endpoint: {}
         paths:
           "/echo":
             post:
               description: "Echo back a given message."
               operationId: "echo"
               requestBody:
                 description: "Message to echo"
                 required: true
                 content:
                   "application/json":
                     schema:
                       $ref: "#/components/schemas/echoMessage"
               responses:
                 "200":
                   description: "Echo"
                   content:
                     "application/json":
                       schema:
                         $ref: "#/components/schemas/echoMessage"
               security:
                 - api_key: []
           "/auth/info/googlejwt":
             get:
               description: "Returns the requests' authentication information."
               operationId: "auth_info_google_jwt"
               responses:
                 "200":
                   description: "Authenication info."
                   content:
                     "application/json":
                       schema:
                         $ref: "#/components/schemas/authInfoResponse"
               security:
                 - google_jwt: []
           "/auth/info/googleidtoken":
             get:
               description: "Returns the requests' authentication information."
               operationId: "authInfoGoogleIdToken"
               responses:
                 "200":
                   description: "Authenication info."
                   content:
                     "application/json":
                       schema:
                         $ref: "#/components/schemas/authInfoResponse"
               security:
                 - google_id_token: []
         
         components:
           schemas:
             echoMessage:
               type: "object"
               properties:
                 message:
                   type: "string"
             authInfoResponse:
               type: "object"
               properties:
                 id:
                   type: "string"
                 email:
                   type: "string"
         
           securitySchemes:
             # This section configures basic authentication with an API key.
             api_key:
               type: apiKey
               name: key
               in: query
             # This section configures authentication using Google API Service Accounts
             # to sign a json web token. This is mostly used for server-to-server
             # communication.
             google_jwt:
               type: oauth2
               flows:
                 implicit:
                   authorizationUrl: ""
                   scopes: {}
               x-google-auth:
                 issuer: "jwt-client.endpoints.sample.google.com"
                 jwksUri: "https://www.googleapis.com/service_accounts/v1/jwk/YOUR_SERVICE_ACCOUNT_EMAIL"
                 # This must match the "aud" field in the JWT. You can add multiple
                 # audiences to accept JWTs from multiple clients.
                 audiences:
                   - "echo.endpoints.sample.google.com"
             # This section configures authentication using Google OAuth2 ID Tokens.
             # ID Tokens can be obtained using OAuth2 clients, and can be used to access
             # your API on behalf of a particular user.
             google_id_token:
               type: oauth2
               flows:
                 implicit:
                   authorizationUrl: ""
                   scopes: {}
               x-google-auth:
                 issuer: "https://accounts.google.com"
                 jwksUri: "https://www.googleapis.com/oauth2/v1/certs"
                 audiences:
                   - "YOUR_CLIENT_ID"

  2. Save the new contents of `openapi.yaml`.



**Note:** The example openapi-appengine.yaml file contains a section for configuring authentication that isn't needed for this tutorial. You don't need to configure the lines with YOUR_SERVICE_ACCOUNT_EMAIL and YOUR_CLIENT_ID.

This tutorial uses a Google-specific extension to the OpenAPI specification that lets you configure the service name. The method for specifying the service name depends on which version of the OpenAPI spec you are using.

### OpenAPI 2.0

Use the `host` field to specify the service name:
    
    
    host: YOUR_PROJECT_ID.appspot.com

To configure Endpoints:

  1. Open the `openapi-appengine.yaml` file.
  2. In the `host` field, replace YOUR_PROJECT_ID with your Google Cloud project ID.
  3. Save the `openapi-appengine.yaml` file.



### OpenAPI 3.x

Use the `url` field in the `servers` object to specify the service name:
    
    
    servers:
    - url: https://YOUR_PROJECT_ID.appspot.com
      x-google-endpoint: {}

To configure Endpoints:

  1. Open the `openapi-appengine.yaml` file.
  2. If your `openapi-appengine.yaml` file has a `host` field, remove it.
  3. Add a `servers` object as shown.
  4. In the `url` field, replace YOUR_PROJECT_ID with your Google Cloud project ID.
  5. Save the `openapi-appengine.yaml` file.

**Note** : You must include `x-google-endpoint: {}` in the `server` object to specify the correct URL for servers to use. Other servers can be included in this list, but exactly one must have x-google-endpoint: {} to specify the correct one. All others will be ignored.

## Deploying the Endpoints configuration

To deploy the Endpoints configuration, you use the [`gcloud endpoints services deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) command. This command uses [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/manage-config) to create a managed service.

To deploy the Endpoints configuration:

  1. Make sure you are in the directory where your `openapi.yaml` configuration file is located.
  2. Upload the configuration and create a managed service: 
         
         gcloud endpoints services deploy openapi.yaml
         




The `gcloud` command then calls the Service Management API to create a managed service with the name that you specified in the `host` or `servers.url` field of the `openapi.yaml` file. Service Management configures the service according to the settings in the `openapi.yaml` file. When you make changes to `openapi.yaml`, you must redeploy the file to update the Endpoints service.

As it is creating and configuring the service, Service Management outputs information to the terminal. You can safely ignore the warnings about the paths in the `openapi.yaml` file not requiring an API key. When it finishes configuring the service, Service Management displays a message with the service configuration ID and the service name, similar to the following:
    
    
    Service Configuration [2017-02-13r0] uploaded for service [example-project-12345.appspot.com]
    

In the preceding example, `2017-02-13r0` is the service configuration ID, and `example-project-12345.appspot.com` is the Endpoints service. The service configuration ID consists of a date stamp followed by a revision number. If you deploy the `openapi.yaml` file again on the same day, the revision number is incremented in the service configuration ID. You can view the Endpoints service configuration on the **Endpoints** > **Services** page in the Google Cloud console.

If you get an error message, see [ Troubleshooting Endpoints configuration deployment](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-config-deployment).

### Checking required services

At a minimum, Endpoints and ESP require the following Google services to be enabled: Name | Title  
---|---  
`servicemanagement.googleapis.com` | Service Management API  
`servicecontrol.googleapis.com` | Service Control API  
  
In most cases, the `gcloud endpoints services deploy` command enables these required services. However, the `gcloud` command completes successfully but doesn't enable the required services in the following circumstances:

  * If you used a third-party application such as Terraform, and you don't include these services.

  * You deployed the Endpoints configuration to an existing Google Cloud project in which these services were explicitly disabled.




Use the following command to confirm that the required services are enabled:
    
    
    gcloud services list

If you do not see the required services listed, enable them:
    
    
    gcloud services enable servicemanagement.googleapis.com
    gcloud services enable servicecontrol.googleapis.com

Also enable your Endpoints service:
    
    
    gcloud services enable ENDPOINTS_SERVICE_NAME

To determine the ENDPOINTS_SERVICE_NAME you can either:

  * After deploying the Endpoints configuration, go to the **Endpoints** page in the Cloud console. The list of possible ENDPOINTS_SERVICE_NAME are shown under the **Service name** column.

  * For OpenAPI, the ENDPOINTS_SERVICE_NAME is what you specified in the `host` field of your OpenAPI spec. For gRPC, the ENDPOINTS_SERVICE_NAME is what you specified in the `name` field of your gRPC Endpoints configuration.




For more information about the `gcloud` commands, see [`gcloud` services](https://docs.cloud.google.com/sdk/gcloud/reference/services).

## Deploying the API backend

So far you have deployed the OpenAPI document to Service Management, but you haven't yet deployed the code that serves the API backend. This section walks you through deploying the sample API and ESP to App Engine. 

To deploy the API backend:

  1. Add your service name to the `app.yaml` file: 

Java

Open the `endpoints/getting-started/src/main/appengine/app.yaml` file.
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

Python

Open the `endpoints/getting-started/app.yaml` file.
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

Go

Open the `endpoints/getting-started/app.yaml` file.
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

PHP

Open the `endpoints/getting-started/app.yaml` file.
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command. If you have
           # previously run the deploy command, you can list your existing configuration
           # ids using the 'configs list' command as follows:
           #
           #     gcloud endpoints configs list --service=YOUR-PROJECT-ID.appspot.com
           #
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

Ruby

Open the `endpoints/getting-started/app.yaml` file.
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

NodeJS

Open the `endpoints/getting-started/app.yaml` file.
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

Replace ENDPOINTS-SERVICE-NAME with the name of your Endpoints service. This is the same name that you configured in the `host` field of your OpenAPI document. For example: 
         
         endpoints_api_service:
           name: example-project-12345.appspot.com
           rollout_strategy: managed

The `rollout_strategy: managed` option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. 

  2. Save the `app.yaml` file. 

Because the `endpoints_api_service` section is included in the `app.yaml` file, the `gcloud app deploy` command deploys and configures ESP in a separate container to your App Engine flexible environment. All request traffic is routed through ESP, and it proxies requests and responses to and from the container running your backend server code.

  3. Make sure you are in the directory where your `openapi.yaml` configuration file is located.
  4. Run the following command to deploy the sample API and ESP to App Engine:
Java

Deploy using Maven:
    
    mvn appengine:stage
    gcloud app deploy target/appengine-staging
    

Python`gcloud app deploy` Go`gcloud app deploy` PHP`gcloud app deploy` Ruby`gcloud app deploy` NodeJS`gcloud app deploy`

The `gcloud app deploy` command creates a DNS record in the format YOUR_PROJECT_ID.appspot.com, which you use when you send requests to the API. We recommend that you wait a few minutes before sending requests to your API while App Engine completely initializes.




If you get an error message, see [Troubleshooting App Engine flexible deployment](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-aeflex-deployment).

For more information, see [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend).

## Sending requests to the API

Now that the service is running on App Engine you can send requests to it.

### Create an API key and set an environment variable

The sample code requires an API key. To simplify the request, you set an environment variable for the API key.

  1. In the same Google Cloud project that you used for your API, create an API key on the API credentials page. If you want to create an API key in a different Google Cloud project, see [Enabling an API in your Google Cloud project](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).

[Go to the Credentials page](https://console.cloud.google.com/apis/credentials)

  2. Click **Create credentials** , and then select **API key**.
  3. Copy the key to the clipboard.
  4. Click **Close**.
  5. On your local computer, paste the API key to assign it to an environment variable: 
     * In Linux or macOS: `export ENDPOINTS_KEY=AIza...`
     * In Windows PowerShell: `$Env:ENDPOINTS_KEY="AIza..."`



### Send the request

### Linux or Mac OS

  1. Create an environment variable for your App Engine project URL. Replace YOUR_PROJECT_ID with your Google Cloud project ID:

`export ENDPOINTS_HOST=https://YOUR_PROJECT_ID.appspot.com`

  2. Send an HTTP request using the `ENDPOINTS_HOST` and `ENDPOINTS_KEY` environment variables you set previously:
         
         curl --request POST \
           --header "content-type:application/json" \
           --data '{"message":"hello world"}' \
           "${ENDPOINTS_HOST}/echo?key=${ENDPOINTS_KEY}"




In the preceding `curl`: 

  * The `--data` option specifies the data to post to the API.
  * The `--header` option specifies that the data is in JSON format.



### PowerShell

  1. Create an environment variable for your App Engine project URL. Replace YOUR_PROJECT_ID with your Google Cloud project ID:

`$Env:ENDPOINTS_HOST="https://YOUR_PROJECT_ID.appspot.com"`

  2. Send an HTTP request using the `ENDPOINTS_HOST` and `ENDPOINTS_KEY` environment variables you set previously:
         
         (Invoke-WebRequest -Method POST -Body '{"message": "hello world"}' `
             -Headers @{"content-type"="application/json"} `
             -URI "$Env:ENDPOINTS_HOST/echo?key=$Env:ENDPOINTS_KEY").Content
         




In the previous example, the first two lines end in a backtick. When you paste the example into PowerShell, make sure there isn't a space following the backticks. For information about the options used in the example request, see [Invoke-WebRequest](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-6) in the Microsoft documentation.

### Third-party app

You can use a third-party application such as the Chrome browser extension [Postman](https://www.getpostman.com/) to send the request: 

  * Select `POST` as the HTTP verb.
  * For the header, select the key `content-type` and the value `application/json`.
  * For the body, enter the following:  
` {"message":"hello world"} `
  * In the URL, use the actual `appspot.com` address and API key rather than the environment variables. For example:   
` https://example-project-12345.appspot.com/echo?key=AIza... `



The API echoes back the message that you send it, and responds with the following:
    
    
    {
      "message": "hello world"
    }
    

If you didn't get a successful response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-response-errors).

You just deployed and tested an API in Endpoints!

**Note** : If you want to let us know what you liked about this tutorial, feel free to provide feedback at the bottom of this page. Your feedback helps us improve these tutorials.  
If you got an error, join the [`google-cloud-endpoints`](https://groups.google.com/forum/#!forum/google-cloud-endpoints) Google group and let us know what went wrong. This group receives responses from other Endpoints users and from Google engineers, who monitor the group.

## Tracking API activity

  1. View the activity graphs for your API in the Endpoints page.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

It might take a few moments for the request to be reflected in the graphs.

  2. Look at the request logs for your API in the Logs Explorer page.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

See [Deleting an API and API instances](https://docs.cloud.google.com/endpoints/docs/openapi/deleting-an-api-and-instances) for information on stopping the services used by this tutorial.

## What's next

  * [Share your API with another developer](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys#sharing_apis_protected_by_api_key)
  * [Learn more about authentication](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method)
  * [Learn about community support options](https://docs.cloud.google.com/endpoints/docs/community-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
