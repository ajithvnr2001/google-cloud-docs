---
url: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-engine/
title: Getting started with Cloud Endpoints for GKE with ESP \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:55.736853+00:00
---

# Getting started with Cloud Endpoints for GKE with ESP  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Getting started with Cloud Endpoints for GKE with ESP Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine "View this page for the Cloud Endpoints gRPC docs")

This tutorial shows you how to configure and deploy a sample API and the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) to a [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/clusters) (GKE) cluster.

The sample API is described using the [OpenAPI specification](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview). The tutorial also shows you how to create an [API key](https://docs.cloud.google.com/endpoints/docs/openapi/when-why-api-key) and use it when sending requests to the API.

The tutorial uses prebuilt container images of the sample code and ESP, which are stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry).

For an overview of Cloud Endpoints, see [About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints) and [Endpoints architecture](https://docs.cloud.google.com/endpoints/docs/openapi/architecture-overview). 

## Objectives

Use the following high-level task list as you work through the tutorial. All tasks in Part 1 are required to successfully send requests to the API.

**Part 1**

  1. Set up a Google Cloud project. See Before you begin.
  2. Create a container cluster on GKE. See Creating a container cluster.
  3. Install and configure software used in the tutorial. See Installing and configuring required software.
  4. Download the sample code. See Getting the sample code.
  5. Configure the `openapi.yaml` file, which is used to configure Cloud Endpoints. See Configuring Endpoints.
  6. Deploy the Endpoints configuration to create a Endpoints service. See Deploying the Endpoints configuration.
  7. Deploy the API and ESP to the cluster. See Deploying the API backend.
  8. Get the cluster's IP address. See Getting the cluster's external IP address.
  9. Send a request to the API by using an IP address. See Sending a request by using an IP address.
  10. Track API activity. See Tracking API activity.



**Part 2**

  1. Configure a DNS record for the sample API. See Configuring DNS for Endpoints.
  2. Send a request to the API using the fully qualified domain name. See Sending a request by using FQDN.



**Cleanup**

When you're finished, see Cleaning up to avoid incurring charges to your Google Cloud account.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
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

  6. Make a note of the Google Cloud project ID, because it's needed later. 



## Creating a container cluster

You must create a container cluster on GKE for the sample API backend code to run on.

To create a container cluster for the sample API:

  1. In the Google Cloud console, go to the GKE clusters page.  


[Go to the Kubernetes clusters page](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create cluster**.

  3. Accept the defaults and click **Create**. This step can take a few minutes to complete.

  4. Make a note the cluster name and zone because they are needed when you authenticate [`kubectl`](https://kubernetes.io/docs/user-guide/kubectl-overview) to the container cluster.




## Installing and configuring required software

In this tutorial, you install the gcloud CLI so that you can use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) to manage your project. You use `kubectl` to run commands against GKE clusters. You also need a way to test the API.

In the following procedure, if you already have the required software installed, continue with the next step.

To install and configure required software:

  1. You need an application to send requests to the sample API.

     * Linux and macOS users: This tutorial provides an example of using `curl`, which typically comes pre-installed on your operating system. If you don't have `curl`, you can download it from the `curl` [ Releases and downloads page](https://curl.haxx.se/download.html). 
     * Windows users: This tutorial provides an example using [`Invoke-WebRequest`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest), which is supported in PowerShell 3.0 and later. 
  2. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts). 
  3. Update the gcloud CLI and install the Endpoints components: 
         
         gcloud components update

  4. Make sure that the Google Cloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud: 
         
         gcloud auth login

In the new browser tab that opens, select an account. 
  5. Set the default project to your project ID: 
         
         gcloud config set project YOUR_PROJECT_ID

Replace YOUR_PROJECT_ID with your project ID. If you have other Google Cloud projects, and you want to use `gcloud` to manage them, see [Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations).

  6. Install `kubectl`: 
         
         gcloud components install kubectl

  7. Acquire new user credentials to use for Application Default Credentials. The user credentials are needed to authorize `kubectl`. 
         
         gcloud auth application-default login

In the new browser tab that opens, select an account. 



## Downloading the sample code

To help you get up and running quickly, sample code is provided in several languages.

To download the sample code to your local machine:

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
               x-google-auth:
                 issuer: "https://accounts.google.com"
                 jwksUri: "https://www.googleapis.com/oauth2/v3/certs"
                 audiences:
                   - "YOUR_CLIENT_ID"

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

So far you have deployed the OpenAPI document to Service Management, but you haven't yet deployed the code that serves the API backend. This section walks you through deploying prebuilt containers for the sample API and ESP to the cluster.

### Checking required permissions

ESP and ESPv2 calls Google services which use IAM to verify if the calling identity has enough permissions to access the used IAM resources. The calling identity is the attached service account deploying ESP and ESPv2.

When deployed in GKE pod, the attached service account is the node service account. Usually it is the Compute Engine default service account. Please follow this permission [recommendation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#permissions) to choose a proper node service account.

If [ Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) is used, a separate service account other than the node service account can be used to talk to Google services. You can create a Kubernetes service account for the pod to run ESP and ESPv2, create a Google service account and associate the Kubernetes service account to the Google service account.

Follow these [ steps](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to associate a Kubernetes service account with a Google service account. This Google service account is the attached service account.

If the attached service account is the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) of the project and the endpoint service configuration is deployed in the **same project** , the service account should have enough permissions to access the IAM resources, following IAM roles setup step can be skipped. Otherwise following IAM roles should be added to the attached service account.

#### Add required IAM roles:

This section describes the IAM resources used by ESP and ESPv2 and the IAM roles required for the attached service account to access these resources.

##### Endpoint Service Configuration

ESP and ESPv2 call Service Control which uses the endpoint service configuration. The endpoint service configuration is an IAM resource and ESP and ESPv2 need the [Service Controller](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) role to access it.

The IAM role is on the endpoint service configuration, not on the project. A project may have multiple endpoint service configurations.

Use the following gcloud command to add the role to the attached service account for the endpoint service configuration.
    
    
    gcloud endpoints services add-iam-policy-binding SERVICE_NAME \
      --member serviceAccount:SERVICE_ACCOUNT_NAME@DEPLOY_PROJECT_ID.iam.gserviceaccount.com \
      --role roles/servicemanagement.serviceController

Where  
* `SERVICE_NAME` is the endpoint service name  
* `SERVICE_ACCOUNT_NAME@DEPLOY_PROJECT_ID.iam.gserviceaccount.com` is the attached service account.

##### Cloud Trace

ESP and ESPv2 call [ Cloud Trace](https://cloud.google.com/trace) service to export Trace to a project. This project is called the tracing project. In ESP, the tracing project and the project that owns the endpoint service configuration are the same. In ESPv2, the tracing project can be specified by the flag `--tracing_project_id`, and defaults to the deploying project.

ESP and ESPv2 require the [Cloud Trace Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace) role to enable Cloud Trace.

Use the following gcloud command to add the role to the attached service account:
    
    
    gcloud projects add-iam-policy-binding TRACING_PROJECT_ID \
      --member serviceAccount:SERVICE_ACCOUNT_NAME@DEPLOY_PROJECT_ID.iam.gserviceaccount.com \
      --role roles/cloudtrace.agent

Where  
* TRACING_PROJECT_ID is the tracing project ID  
* SERVICE_ACCOUNT_NAME@DEPLOY_PROJECT_ID.iam.gserviceaccount.com is the attached service account. For more information, see [ What are roles and permissions?](https://cloud.google.com/iam/docs/understanding-roles)

### Deploying the containers to the cluster

[Containers](https://docs.cloud.google.com/containers) offer a logical packaging mechanism in which you can abstract applications from the environment in which they actually run. You use the following procedure to deploy the sample API and ESP to the cluster.

To deploy the containers to the cluster: 

  1. Get cluster credentials and make them available to `kubectl`: 
         
         gcloud container clusters get-credentials NAME   
         
             --zone ZONE

Replace NAME with the cluster name and ZONE with the cluster zone. 

  2. Deploy a Kubernetes service to the GKE cluster. The Kubernetes service implements the API. Edit the Kubernetes configuration file `/endpoints/getting-started/deployment.yaml`, and replace SERVICE_NAME in the ESP startup options with the name of your service. Java
         
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:1
           args: [
             "--http_port=8081",
             "--backend=127.0.0.1:8080",
             "--service=SERVICE_NAME",
             "--rollout_strategy=managed",
           ]

Python
         
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:1
           args: [
             "--http_port=8081",
             "--backend=127.0.0.1:8080",
             "--service=SERVICE_NAME",
             "--rollout_strategy=managed",
           ]

Go
         
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:1
           args: [
             "--http_port", "8081",
             "--backend", "127.0.0.1:8080",
             "--service", "SERVICE_NAME",
             "--rollout_strategy", "managed",
           ]

PHP
         
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:1
           args: [
             "--http_port", "8081",
             "--backend", "127.0.0.1:8080",
             "--service", "SERVICE_NAME",
             "--rollout_strategy", "managed",
           ]

Ruby
         
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:1
           args: [
             "--http_port", "8081",
             "--backend", "127.0.0.1:8080",
             "--service", "SERVICE_NAME",
             "--rollout_strategy", "managed",
           ]

NodeJS
         
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:1
           args: [
             "--http_port", "8081",
             "--backend", "127.0.0.1:8080",
             "--service", "SERVICE_NAME",
             "--rollout_strategy", "managed",
           ]

For example:
         
         args: [
             "--http_port=8081",
             "--backend=127.0.0.1:8080",
             "--service=echo-api.endpoints.example-project-12345.cloud.goog ",
             "--rollout_strategy=managed",
           ]

The `--rollout_strategy=managed` option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. For information about the other ESP options used, see [ESP startup options](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options). 

We recommend that you set the `imagePullPolicy` in the container spec above to `Always`. This will allow newly created pods to always pull the latest version of ESP. Read about [ configuration best practices](https://kubernetes.io/docs/concepts/configuration/overview/#container-images) for more details. When a new version of ESP is released, you can perform a rolling restart of all pods to ensure the newest version is used. 

  3. Start the Kubernetes service using the [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) command: 
         
         kubectl apply -f deployment.yaml


**Note:** If your GKE cluster is private, you need to use the Compute Engine metadata server as the DNS resolver to resolve Google service host names. Add this ESP flag: `--dns=169.254.169.254`

If you get an error message, see [Troubleshooting Endpoints in GKE](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gke-deployment).

See [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend) for additional information.

## Getting the cluster's external IP address

To send requests to the API, you need the external IP of the service. It can take a few minutes after you start your service in the container before the external IP address is ready.

  1. View the external IP address:
         
         kubectl get service
         

  2. Make a note of the value for `EXTERNAL-IP`. You use that IP address when you send a request to the sample API.




## Sending a request by using an IP address

Now that the service is running in the container cluster, and you have the external IP address, you can send requests to the API.

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

## Tracking API activity

To track API activity:

  1. Look at the activity graphs for your API in the **Endpoints** > **Services** page.   


[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  
It may take a few moments for the request to be reflected in the graphs.
  2. Look at the request logs for your API in the Logs Explorer page.   


[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)




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




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

See [Deleting an API and API instances](https://docs.cloud.google.com/endpoints/docs/openapi/deleting-an-api-and-instances) for information on stopping the services used by this tutorial. 

## What's next

  * [Learn how to build a Docker image](https://docs.cloud.google.com/container-builder/docs).
  * [Learn how to deploy Endpoints on Kubernetes](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes).
  * [Share your API with another developer](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys#sharing_apis_protected_by_api_key).
  * [Learn more about authentication](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method).
  * [Learn about community support options](https://docs.cloud.google.com/endpoints/docs/community-support).
  * [Troubleshooting GKE deployment](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gke-deployment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
