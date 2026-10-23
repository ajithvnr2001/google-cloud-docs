---
url: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-compute-engine-docker/
title: Getting started with Cloud Endpoints for Compute Engine with ESP \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:42.960333+00:00
---

# Getting started with Cloud Endpoints for Compute Engine with ESP  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-compute-engine-docker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Getting started with Cloud Endpoints for Compute Engine with ESP Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-compute-engine-docker "View this page for the Cloud Endpoints gRPC docs")

This tutorial shows you how to configure and deploy a sample API and the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) running in prebuilt [Docker](https://docs.docker.com/) containers on [Compute Engine](https://docs.cloud.google.com/compute). The sample API is described using the [OpenAPI specification](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview). The tutorial also shows you how to create an [API key](https://docs.cloud.google.com/endpoints/docs/openapi/when-why-api-key) and use it in requests to the API.

For an overview of Cloud Endpoints, see [About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints) and [Endpoints architecture](https://docs.cloud.google.com/endpoints/docs/openapi/architecture-overview). 

## Objectives

Use the following high-level task list as you work through the tutorial. All tasks are required to successfully send requests to the API.

  1. Set up a Google Cloud project. See Before you begin. 
  2. Create a Compute Engine VM instance. See Creating a Compute Engine instance.
  3. Download the sample code. See Getting the sample code.
  4. Configure the `openapi.yaml` file, which is used to configure Endpoints. See Configuring Endpoints.
  5. Deploy the Endpoints configuration to create a Endpoints service. See Deploying the Endpoints configuration.
  6. Deploy the API and ESP on the Compute Engine VM. See Deploying the API backend.
  7. Send a request to the API by using an IP address. See Sending a request by using IP address.
  8. Configure a DNS record for the sample API. See Configuring DNS for Endpoints.
  9. Send a request to the API by using the fully qualified domain name. See Sending a request by using FQDN.
  10. Track API activity. See Tracking API activity.
  11. Avoid incurring charges to your Google Cloud account. See Clean up.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)
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

Replace YOUR_PROJECT_ID with your project ID. If you have other Google Cloud projects, and you want to use `gcloud` to manage them, see [Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations).




When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Creating a Compute Engine instance

To create a Compute Engine instance:

     1. In the Google Cloud console, go to the **Create an instance** page. 

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

     2. Click **Select**. 
     3. In the **Firewall** section, select **Allow HTTP traffic** and **Allow HTTPS traffic**. 
     4. To create the VM, click **Create**. 

![Screenshot of the VM instance creation window with the required options set](https://docs.cloud.google.com/static/endpoints/docs/images/gce-vm-deb9-http-https.png)

Allow a short time for the instance to start up. Once ready, it is listed on the **VM Instances** page with a green status icon.

     5. Make sure you that you can connect to your VM instance. 
        1. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 
        2. You can now use the terminal to run Linux commands on your Debian instance.
        3. Enter `exit` to disconnect from the instance.
     6. Make a note the instance name, zone, and external IP address because they are needed later.



## Downloading the sample code

Download the sample code to your local machine.

Java

To clone or download the sample API: 

  1. Clone the sample app repository to your local machine: 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples

Alternatively, [download the sample](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the sample code: 
         
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

To configure Endpoints using an OpenAPI 2.0 specification, you can use the `openapi.yaml` file available in the `endpoints/getting-started` directory of the downloaded sample code.

The contents of the OpenAPI 2.0 specification should look similar to the following:
    
    
    swagger: "2.0"
    info:
      description: "A simple Google Cloud Endpoints API example."
      title: "Endpoints Example"
      version: "1.0.0"
    
    host: "echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog"
    
    consumes:
      - "application/json"
    produces:
      - "application/json"
    
    schemes:
    # Uncomment the next line if you configure SSL for this API.
    # - "https"
      - "http"
    
    paths:
      /echo:
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
            -
              description: "Message to echo"
              in: body
              name: message
              required: true
              schema:
                $ref: "#/definitions/echoMessage"
          security:
            - api_key: []
      /auth/info/googlejwt:
        get:
          description: "Returns the requests' authentication information."
          operationId: "auth_info_google_jwt"
          produces:
            - "application/json"
          responses:
            200:
              description: "Authenication info."
              schema:
                $ref: "#/definitions/authInfoResponse"
          security:
            - api_key: []
              google_jwt: []
      /auth/info/googleidtoken:
        get:
          description: "Returns the requests' authentication information."
          operationId: "authInfoGoogleIdToken"
          produces:
            - "application/json"
          responses:
            200:
              description: "Authentication info."
              schema:
                $ref: "#/definitions/authInfoResponse"
          security:
            - api_key: []
              google_id_token: []
    
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
        x-google-jwks_uri: "https://www.googleapis.com/service_accounts/v1/jwk/YOUR_SERVICE_ACCOUNT_EMAIL"
        # This must match the "aud" field in the JWT. You can add multiple
        # audiences to accept JWTs from multiple clients.
        x-google-audiences: "echo.endpoints.sample.google.com"
      # This section configures authentication using Google OAuth2 ID Tokens.
      # ID Tokens can be obtained using OAuth2 clients, and can be used to access
      # your API on behalf of a particular user.
    
      google_id_token:
        authorizationUrl: ""
        flow: "implicit"
        type: "oauth2"
        x-google-issuer: "https://accounts.google.com"
        x-google-jwks_uri: "https://www.googleapis.com/oauth2/v3/certs"
        # Your OAuth2 client's Client ID must be added here. You can add
        # multiple client IDs to accept tokens from multiple clients.
        x-google-audiences: "YOUR_CLIENT_ID"

### OpenAPI 3.x

To configure Endpoints using an OpenAPI 3.x specification, you can replace the contents of the `openapi.yaml` file available in the `endpoints/getting-started` directory of the downloaded sample code:

  1. Open the `openapi.yaml` in your text editor and replace the contents with the following: 
         
         openapi: 3.0.4
         info:
           description: "A simple Google Cloud Endpoints API example."
           title: "Endpoints Example"
           version: "1.0.0"
         servers:
           - url: "http://echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog"
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
                 '200':
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
                 '200':
                   description: "Authentication info."
                   content:
                     "application/json":
                       schema:
                         $ref: "#/components/schemas/authInfoResponse"
               security:
                 - api_key: []
                   google_jwt: []
         
           "/auth/info/googleidtoken":
             get:
               description: "Returns the requests' authentication information."
               operationId: "authInfoGoogleIdToken"
               responses:
                 '200':
                   description: "Authentication info."
                   content:
                     "application/json":
                       schema:
                         $ref: "#/components/schemas/authInfoResponse"
               security:
                 - api_key: []
                   google_id_token: []
         
         components:
           schemas:
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
         
           securitySchemes:
             api_key:
               type: "apiKey"
               name: "key"
               in: "query"
         
             google_jwt:
               type: "oauth2"
               flows:
                 implicit:
                   authorizationUrl: ""
                   scopes: {}
               google_jwt:
               type: "oauth2"
               flows:
                 implicit:
                   authorizationUrl: ""
                   scopes: {}
               x-google-auth:
                 issuer: "jwt-client.endpoints.sample.google.com"
                 jwksUri: "https://www.googleapis.com/service_accounts/v1/jwk/YOUR_SERVICE_ACCOUNT_EMAIL"
                 audiences: "echo.endpoints.sample.google.com"
         
             google_id_token:
               type: "oauth2"
               flows:
                 implicit:
                   authorizationUrl: ""
                   scopes: {}
               x-google-issuer: "https://accounts.google.com"
               x-google-jwks_uri: "https://www.googleapis.com/oauth2/v3/certs"
               x-google-audiences: "YOUR_CLIENT_ID"

  2. Save the new contents of `openapi.yaml`.



This tutorial uses a Google-specific extension to the OpenAPI specification that lets you configure the service name. The method for specifying the service name depends on which version of the OpenAPI specification you are using.

### OpenAPI 2.0

Use the `host` field to specify the service name:
    
    
    host: echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog

To configure Endpoints:

  1. Open the `openapi.yaml` file.
  2. In the `host` field, replace YOUR_PROJECT_ID with your Google Cloud project ID.
  3. Save the `openapi.yaml` file.



### OpenAPI 3.x

Use the `url` field in the `servers` object to specify the service name:
    
    
    servers:
    - url: https://echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog
        x-google-endpoint: {}

To configure Endpoints:

  1. Open the `openapi.yaml` file.
  2. If your `openapi.yaml` file has a `host` field, remove it.
  3. Add a `servers` object as shown.
  4. In the `url` field, replace YOUR_PROJECT_ID with your Google Cloud project ID.
  5. Save the `openapi.yaml` file.



After you have finished all the following configuration steps such that you can successfully send requests to the sample API by using an IP address, see Configuring Endpoints DNS for information on how to configure `echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog` to be the fully qualified domain name (FQDN).

## Deploying the Endpoints configuration

To deploy the Endpoints configuration, you use the [`gcloud endpoints services deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) command. This command uses [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/manage-config) to create a managed service.

To deploy the Endpoints configuration:

  1. Make sure you are in the directory where your `openapi.yaml` configuration file is located.
  2. Upload the configuration and create a managed service: 
         
         gcloud endpoints services deploy openapi.yaml
         




The `gcloud` command then calls the Service Management API to create a managed service with the name that you specified in the `host` or `servers.url` field of the `openapi.yaml` file. Service Management configures the service according to the settings in the `openapi.yaml` file. When you make changes to `openapi.yaml`, you must redeploy the file to update the Endpoints service.

As it is creating and configuring the service, Service Management outputs information to the terminal. You can safely ignore the warnings about the paths in the `openapi.yaml` file not requiring an API key. When it finishes configuring the service, Service Management displays a message with the service configuration ID and the service name, similar to the following:
    
    
    Service Configuration [2017-02-13r0] uploaded for service [echo-api.endpoints.example-project-12345.cloud.goog]
    

In the preceding example, `2017-02-13r0` is the service configuration ID, and `echo-api.endpoints.example-project-12345.cloud.goog` is the Endpoints service. The service configuration ID consists of a date stamp followed by a revision number. If you deploy the `openapi.yaml` file again on the same day, the revision number is incremented in the service configuration ID. You can view the Endpoints service configuration on the **Endpoints** > **Services** page in the Google Cloud console.

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

So far you have deployed the OpenAPI document to Service Management, but you haven't yet deployed the code that serves the API backend. This section walks you through getting Docker set up on your VM instance and running the API backend code and the [ESP](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) in a Docker container.

### Checking required permissions

**Note:**

This step is not needed if the Compute Engine instance is created with [ Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) and it has been granted with all the required permissions.

  * In the Google Cloud console, go to the Compute Engine instances page. 

[Go to the Compute Engine page](https://console.cloud.google.com/compute)

  * Select your instance from the list.
  * You can see the associated service account and the permissions it has.
  * Grant required permissions to the service account: 
        
        gcloud projects add-iam-policy-binding PROJECT_ID   
        
        --member "serviceAccount:SERVICE_ACCOUNT"   
        
        --role roles/servicemanagement.serviceController

For more information, see [ What are roles and permissions?](https://docs.cloud.google.com/iam/docs/understanding-roles)




### Install Docker on the VM instance

To install Docker on the VM instance:

  1. Set the zone for your project by running the command: 
         
         gcloud config set compute/zone YOUR_INSTANCE_ZONE
         

Replace YOUR_INSTANCE_ZONE with the zone where your instance is running.

  2. Connect to your instance by using the following command: 
         
         gcloud compute ssh INSTANCE_NAME
         

Replace INSTANCE_NAME with your VM instance name.

  3. See the [Docker documentation](https://docs.docker.com/install/linux/docker-ce/debian/) to set up the Docker repository. Make sure to follow the steps that match the version and architecture of your VM instance: 
     * **Jessie or newer**
     * **x86_64 / amd64**



### Run the API and ESP in a Docker container

The ESP is an `nginx`-based proxy that sits in front of your backend code. It processes incoming traffic to provide authentication, API key management, logging, and other Endpoints API management features.

To install and run the sample API and ESP in a Docker container:

  1. Create your own container network called `esp_net`. 
         
         sudo docker network create --driver bridge esp_net
         

  2. Run the sample Echo server that serves the sample API: Java
         
         sudo docker run --detach --name=echo --net=esp_net gcr.io/google-samples/echo-java:1.0
         

Python
         
         sudo docker run --detach --name=echo --net=esp_net gcr.io/google-samples/echo-python:1.0
         

Go
         
         sudo docker run --detach --name=echo --net=esp_net gcr.io/google-samples/echo-go:1.0
         

PHP
         
         sudo docker run --detach --name=echo --net=esp_net gcr.io/google-samples/echo-php:1.0
         

Ruby
         
         sudo docker run --detach --name=echo --net=esp_net gcr.io/google-samples/echo-ruby:1.0
         

NodeJS
         
         sudo docker run --detach --name=echo --net=esp_net gcr.io/google-samples/echo-node:1.0
         

  3. Run the pre-packaged public ESP Docker container. In the ESP startup options, replace SERVICE_NAME with the name of your service. This is the same name that you configured in the `host` field of your OpenAPI document. 
         
         sudo docker run \
             --name=esp \
             --detach \
             --publish=80:8080 \
             --net=esp_net \
             gcr.io/endpoints-release/endpoints-runtime:1 \
             --service=SERVICE_NAME \
             --rollout_strategy=managed \
             --backend=echo:8080
         

The `--rollout_strategy=managed` option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. For information about the other ESP options used, see [ESP startup options](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options). 




If you get an error message, see [Troubleshooting Endpoints on Compute Engine](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gce-deployment).

See [Deploying the API Backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend) for additional information.

## Sending a request by using an IP address

After the sample API and the ESP are running on the Compute Engine instance, you can send requests to the API from your local machine.

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

### Linux or mac OS

Use `curl` to send an HTTP request by using the ENDPOINTS_KEY environment variable you set previously. Replace IP_ADDRESS with the external IP address of your instance.
    
    
    curl --request POST \
       --header "content-type:application/json" \
       --data '{"message":"hello world"}' \
       "http://IP_ADDRESS:80/echo?key=${ENDPOINTS_KEY}"

In the preceding `curl`: 

  * The `--data` option specifies the data to post to the API.
  * The `--header` option specifies that the data is in JSON format.



### PowerShell

Use `Invoke-WebRequest` to send an HTTP request by using the `ENDPOINTS_KEY` environment variable you set previously. Replace IP_ADDRESS with the external IP address of your instance.
    
    
    (Invoke-WebRequest -Method POST -Body '{"message": "hello world"}' `
        -Headers @{"content-type"="application/json"} `
        -URI "http://IP_ADDRESS:80/echo?key=$Env:ENDPOINTS_KEY").Content

In the previous example, the first two lines end in a backtick. When you paste the example into PowerShell, make sure there isn't a space following the backticks. For information about the options used in the example request, see [Invoke-WebRequest](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-6) in the Microsoft documentation.

### Third-party app

You can use a third-party application such as the Chrome browser extension [Postman](https://www.getpostman.com/) to send the request: 

  * Select `POST` as the HTTP verb.
  * For the header, select the key `content-type` and the value `application/json`.
  * For the body, enter the following:  
` {"message":"hello world"} `
  * In the URL, use the actual API key rather than the environment variable. For example:   
` http://192.0.2.0:80/echo?key=AIza... `



The API echoes back the message that you send, and responds with the following:
    
    
    {
      "message": "hello world"
    }
    

If you didn't get a successful response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-response-errors).

You just deployed and tested an API in Endpoints!

**Note** : If you want to let us know what you liked about this tutorial, feel free to provide feedback at the bottom of this page. Your feedback helps us improve these tutorials.  
If you got an error, join the [`google-cloud-endpoints`](https://groups.google.com/forum/#!forum/google-cloud-endpoints) Google group and let us know what went wrong. This group receives responses from other Endpoints users and from Google engineers, who monitor the group.

## Configuring DNS for Endpoints

Because the Endpoints service name for the API is in the `.endpoints.YOUR_PROJECT_ID.cloud.goog` domain, you can use it as the fully qualified domain name (FQDN) by making a small configuration change in your `openapi.yaml` file. This way, you can send requests to the sample API by using `echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog` instead of the IP address.

To configure Endpoints DNS:

### OpenAPI 2.0

  1. Open your OpenAPI configuration file, `openapi.yaml`, and add the `x-google-endpoints` property at the top level of the file (not indented or nested) as shown in the following snippet: 
         
         host: "echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog"
         x-google-endpoints:
         - name: "echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog"
           target: "IP_ADDRESS"

  2. In the `name` property, replace YOUR_PROJECT_ID with your project ID. 
  3. In the `target` property, replace IP_ADDRESS with the IP address that you used when you sent a request to the sample API.
  4. Deploy your updated OpenAPI configuration file to Service Management: 
         
         gcloud endpoints services deploy openapi.yaml
         




### OpenAPI 3.x

  1. Open your OpenAPI configuration file, `openapi.yaml`, and add the `servers.url` property at the top level of the file (not indented or nested) as shown in the following snippet: 
         
         servers:
           - url: "echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog"
             x-google-endpoint:
               target: "IP_ADDRESS"

  2. In the `name` property, replace YOUR_PROJECT_ID with your project ID. 
  3. In the `target` property, replace IP_ADDRESS with the IP address that you used when you sent a request to the sample API.
  4. Deploy your updated OpenAPI configuration file to Service Management: 
         
         gcloud endpoints services deploy openapi.yaml
         




For example, assume the `openapi.yaml` file has the following configured:

### OpenAPI 2.0
    
    
    host: "echo-api.endpoints.example-project-12345.cloud.goog"
    x-google-endpoints:
    - name: "echo-api.endpoints.example-project-12345.cloud.goog"
      target: "192.0.2.1"

### OpenAPI 3.x
    
    
    servers:
      - url: "echo-api.endpoints.example-project-12345.cloud.goog"
        x-google-endpoint:
          target: "192.0.2.1"

When you deploy the `openapi.yaml` file by using the preceding `gcloud` command, Service Management creates a DNS A-record, `echo-api.endpoints.my-project-id.cloud.goog`, which resolves to the target IP address, `192.0.2.1`. It might take a few minutes for the new DNS configuration to propagate.

### Configuring SSL

For more details on how to configure DNS and SSL, see [Enabling SSL for Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/enabling-ssl).

## Sending a request by using FQDN

Now that you have the DNS record configured for the sample API, send a request to it by using the FQDN (replace YOUR_PROJECT_ID with your project ID) and the ENDPOINTS_KEY environment variable set previously:

  * In Linux or mac OS: 
        
        curl --request POST \
            --header "content-type:application/json" \
            --data '{"message":"hello world"}' \
            "http://echo-api.endpoints.YOUR_PROJECT_ID.cloud.goog:80/echo?key=${ENDPOINTS_KEY}"

  * In Windows PowerShell: 
        
        (Invoke-WebRequest -Method POST -Body '{"message": "hello world"}' -Headers @{"content-type"="application/json"} -URI "http://echo-api.endpoints.[YOUR_PROJECT_ID].cloud.goog:80/echo?key=$Env:ENDPOINTS_KEY").Content




## Tracking API activity

To track API activity:

  1. Look at the activity graphs for your API in the **Endpoints** > **Services** page.   


[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  
It may take a few moments for the request to be reflected in the graphs.
  2. Look at the request logs for your API in the Logs Explorer page.   


[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. Delete the API: 
         
         gcloud endpoints services delete SERVICE_NAME

Replace `SERVICE_NAME` with the name of your service.

  2. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. Select the checkbox for the instance that you want to delete. 
  4. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



## What's next

  * [Share your API with another developer](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys#sharing_apis_protected_by_api_key)
  * [Learn more about authentication](https://docs.cloud.google.com/endpoints/docs/openapi/authenticating-users)
  * [Learn about community support options](https://docs.cloud.google.com/endpoints/docs/community-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
