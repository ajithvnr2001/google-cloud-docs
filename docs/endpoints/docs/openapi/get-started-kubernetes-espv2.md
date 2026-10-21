---
url: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-espv2/
title: Getting started with Cloud Endpoints for Kubernetes with ESPv2 \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:01.232953+00:00
---

# Getting started with Cloud Endpoints for Kubernetes with ESPv2  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-espv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Getting started with Cloud Endpoints for Kubernetes with ESPv2 Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-espv2 "View this page for the Cloud Endpoints gRPC docs")

This tutorial shows you how to configure and deploy a sample API and the [Extensible Service Proxy V2 (ESPv2)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) to a Kubernetes cluster that isn't on Google Cloud. If you want to use Google Kubernetes Engine (GKE), use [Getting started with Endpoints on GKE](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-engine).

The sample API is described using the [OpenAPI specification](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview). The tutorial also shows you how to create an [API key](https://docs.cloud.google.com/endpoints/docs/openapi/when-why-api-key) to send requests to the API.

The tutorial uses prebuilt container images of the sample code and ESPv2, which are stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry). If you are unfamiliar with containers, see the following for more information:

  * [Deploying a containerized web application](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/hello-app).
  * [Kubernetes container images](https://kubernetes.io/docs/concepts/containers/images/).



For an overview of Cloud Endpoints, see [About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints) and [Endpoints architecture](https://docs.cloud.google.com/endpoints/docs/openapi/architecture-overview). 

## Objectives

Use the following high-level task list as you work through the tutorial. All tasks in Part 1 are required to successfully send requests to the API.

**Part 1**

  1. Set up a Google Cloud project. See Before you begin.
  2. Install and configure software used in the tutorial. See Installing and configuring required software.
  3. Optionally, download the sample code. See Getting the sample code.
  4. Download the Kubernetes configuration file. See Getting Kubernetes configuration file.
  5. Configure the `openapi.yaml` file, which is used to configure Endpoints. See Configuring Endpoints.
  6. Deploy the Endpoints configuration to create a Cloud Endpoints service. See Deploying the Endpoints configuration.
  7. Create credentials for your Endpoints service. See Creating credentials for your service.
  8. Deploy the API and ESPv2 to the cluster. See Deploying the API backend.
  9. Get the service's external IP address. See Getting the external IP address.
  10. Send a request to the API by using an IP address. See Sending a request by using an IP address.
  11. Track API activity. See Tracking API activity.



**Part 2**

  1. Configure a DNS record for the sample API. See Configuring DNS for Endpoints.
  2. Send a request to the API by using the domain name. See Sending a request by using FQDN.



**Cleanup**

When you're finished, see Cleaning up to avoid incurring charges to your Google Cloud account.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Endpoints](https://docs.cloud.google.com/endpoints/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

## Before you begin

This tutorial assumes that you already have Minikube or a Kubernetes cluster set up. For more information, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

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

  6. Make a note of the Google Cloud project ID because it is needed later. 



## Installing and configuring required software

In this tutorial, you install the Google Cloud CLI to use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to manage your project. You use [`kubectl`](https://kubernetes.io/docs/user-guide/kubectl-overview/), a command-line interface, to run commands against Kubernetes clusters. You also need a way to test the API.

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

In the new tab that opens, select an account. 
  5. Set the default project to your project ID: 
         
         gcloud config set project YOUR_PROJECT_ID

Replace YOUR_PROJECT_ID with your project ID. If you have other Google Cloud projects, and you want to use `gcloud` to manage them, see [Managing gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/managing-configurations).

  6. Install `kubectl`: 
         
         gcloud components install kubectl

  7. Acquire new user credentials to use for application default credentials. The user credentials authorize `kubectl`. 
         
         gcloud auth application-default login

  8. In the new tab that opens, choose an account.
  9. Run the following command to make sure your Kubernetes client is properly configured: 
         
         kubectl version

You should see output similar to the following:
         
         Client Version: version.Info{Major:"1", Minor:"8", GitVersion:"v1.8.4",
              GitCommit:"9befc2b8928a9426501d3bf62f72849d5cbcd5a3", GitTreeState:"clean",
              BuildDate:"2017-11-20T05:28:34Z", GoVersion:"go1.8.3", Compiler:"gc",
              Platform:"linux/amd64"}
            Server Version: version.Info{Major:"1", Minor:"7+",
              GitVersion:"v1.7.8-gke.0",
              GitCommit:"a7061d4b09b53ab4099e3b5ca3e80fb172e1b018", GitTreeState:"clean",
              BuildDate:"2017-10-10T18:48:45Z", GoVersion:"go1.8.3", Compiler:"gc",
              Platform:"linux/amd64"}
            




## Downloading the sample code

Optionally, download the sample code. In this tutorial, you deploy a prebuilt container image, so you don't have to build a container from the sample code. However, you might want to download the sample code, which is provided in several languages to help you understand how the sample API works.

To download the sample code: Java

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




## Getting the Kubernetes configuration file

  1. Clone the GitHub repository that contains the `yaml` files used in this tutorial to your local machine:
         
         git clone https://github.com/googlecloudplatform/endpoints-samples

Alternatively, [download the sample](https://github.com/GoogleCloudPlatform/endpoints-samples/archive/master.zip) as a zip file and extract it.

  2. Change to the directory that contains the configuration files: 
         
         cd endpoints-samples/kubernetes




## Configuring Endpoints

You must have an OpenAPI document based on either OpenAPI 2.0 or OpenAPI 3.x that describes the [surface](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#surface) of your apps and any authentication requirements. To learn more, see [Supported OpenAPI versions](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview#supported-openapi-versions).

You also need to add a Google-specific field that contains the URL for each app so that ESPv2 has the information it needs to invoke an app. If you are new to OpenAPI, see [OpenAPI overview](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview) for more information.

To configure Endpoints:

  1. Create a new text file called `openapi.yaml`. For convenience, this page refers to the OpenAPI document by that name, but you can name it something else if you prefer. 
  2. Copy the contents of one of the following files into your new `openapi.yaml` file. You can choose to use OpenAPI 2.0 or OpenAPI 3.x. 

### OpenAPI 2.0
         
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

## Creating credentials for your service

To provide management for your API, both ESP and ESPv2 require the services in [Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview). To call these services, ESP and ESPv2 must use access tokens. When you deploy ESP or ESPv2 to Google Cloud environments, such as GKE, Compute Engine, or the App Engine flexible environment, ESP and ESPv2 obtain access tokens for you through the Google Cloud metadata service. 

When you deploy ESP or ESPv2 to a non-Google Cloud environment, such as your local desktop, an on-premises Kubernetes cluster, or another cloud provider, you must provide a [service account JSON file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) that contains a private key. ESP and ESPv2 use the [service account](https://docs.cloud.google.com/iam/docs/service-accounts) to generate access tokens to call the services that it needs to manage your API.

You can use either the Google Cloud console or the Google Cloud CLI to create the service account and private key file:

### Console

  1. In the Google Cloud console, open the **Service Accounts** page . 

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Select a project**.
  3. Select the project that your API was created in and click **Open**.
  4. Click **\+ Create Service Account**.
  5. In the **Service account name** field, enter the name for your service account.
  6. Click **Create**.
  7. Click **Continue**.
  8. Click **Done**.
  9. Click the email address of the newly created service account.
  10. Click **Keys**.
  11. Click **Add key** , then click **Create new key**.
  12. Click **Create**. A JSON key file is downloaded to your computer.

Make sure to store the key file securely, because it can be used to authenticate as your service account. You can move and rename this file however you would like.

  13. Click **Close**.




### `gcloud`

  1. Enter the following to display the project IDs for your Google Cloud projects:
         
         gcloud projects list

  2. Replace PROJECT_ID in the following command to set the default project to the one that your API is in:
         
         gcloud config set project PROJECT_ID

**Important:** You must create the service account in the same project that your API is in.
  3. Make sure that the Google Cloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud:
         
         gcloud auth login

If you have more than one account, make sure to choose the account that is in the Google Cloud project that the API is in. If you run `gcloud auth list`, the account that you selected is shown as the active account for the project.

  4. To create a service account, run the following command and replace SERVICE_ACCOUNT_NAME and `My Service Account` with the name and display name that you want to use:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
            --display-name "My Service Account"

The command assigns an email address for the service account in the following format:

`SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`

This email address is required in the subsequent commands.

  5. Create a service account key file:
         
         gcloud iam service-accounts keys create ~/service-account-creds.json \
            --iam-account SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com




Add required IAM roles:

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

See [`gcloud iam service-accounts`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts) for more information about the commands.

## Deploying the API backend

So far you have deployed the OpenAPI document to Service Management, but you haven't yet deployed the code that serves the API backend. This section walks you through deploying prebuilt containers for the sample API and ESPv2 to Kubernetes.

### Checking required permissions

Grant required permissions to the service account associated with your cluster:
    
    
    gcloud endpoints services add-iam-policy-binding SERVICE_NAME \
        --member "serviceAccount:SERVICE_ACCOUNT" \
        --role roles/servicemanagement.serviceController
    

For more information, see [ What are roles and permissions?](https://docs.cloud.google.com/iam/docs/understanding-roles)

### Providing ESPv2 with the service credentials

ESPv2, which runs inside a container, needs access to the credentials stored locally in the `service-account-creds.json` file. To provide ESPv2 with access to the credentials, you create a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) and mount the Kubernetes secret as a [Kubernetes volume](https://kubernetes.io/docs/concepts/storage/volumes/).

To create the Kubernetes secret and mount the volume:

  1. Make sure to rename the JSON file to `service-account-creds.json` and copy it to `endpoints-samples/kubernetes` if it was downloaded to a different directory. This way, the name matches the options specified in the `echo.yaml` deployment manifest file.
  2. Make sure you are in the `endpoints-samples/kubernetes` directory.
  3. Create a Kubernetes secret with the service account credentials using the following command:
         
         kubectl create secret generic service-account-creds \
            --from-file=service-account-creds.json
         

On success, the following message displays:
         
         secret "service-account-creds" created




The deployment manifest file that you use to deploy the API and ESPv2 to Kubernetes already contains the [secret volume](https://kubernetes.io/docs/concepts/storage/volumes/#secret), as shown in the following two sections of the file:
    
    
    volumes:
      - name: service-account-creds
        secret:
          secretName: service-account-creds
    
    
    volumeMounts:
      - mountPath: /etc/esp/creds
        name: service-account-creds
        readOnly: true

### Configuring the service name and starting the service

ESPv2 needs to know the name of your service to find the configuration that you deployed previously (by using the `gcloud endpoints services deploy` command).

To configure the service name and start the service:

  1. Open the deployment manifest file, `echo.yaml`, and replace SERVICE_NAME in the ESPv2 startup options with the name of your service. This is the same name that you configured in the `host` or `server.url` field of your OpenAPI document. For example:
         
         "--service=echo-api.endpoints.example-project-12345.cloud.goog"
         
         containers:
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:2
           args: [
             "--listener_port=8080",
             "--backend=127.0.0.1:8081",
             "--service=SERVICE_NAME",
             "--rollout_strategy=managed",
             "--non_gcp",
             "--service_account_key=/etc/esp/creds/service-account-creds.json"
           ]
           ports:
             - containerPort: 8080
           volumeMounts:
             - mountPath: /etc/esp/creds
               name: service-account-creds
               readOnly: true
         - name: echo
           image: gcr.io/endpoints-release/echo:latest
           ports:
             - containerPort: 8081
         

The `"--rollout_strategy=managed"` option configures ESPv2 to use the latest deployed service configuration. When you specify this option, within a minute after you deploy a new service configuration, ESPv2 detects the change and automatically begins using it. We recommend that you specify this option instead of providing a specific configuration ID for ESPv2 to use. For information about the other ESPv2 options used, see [ESPv2 startup options](https://docs.cloud.google.com/endpoints/docs/openapi/specify-esp-v2-startup-options).

**Note:** If you are using MiniKube, you need to change the service `type` field from `LoadBalancer` to `NodePort` in the configuration file.**Note:** We recommend that you set the `imagePullPolicy` in the container specification to `Always`. This will allow newly created pods to always pull the latest version of ESPv2. Read about [configuration best practices](https://kubernetes.io/docs/concepts/configuration/overview/#container-images) for more details. When a new version of ESPv2 is released, you can perform a rolling restart of all pods to ensure the newest version is used.
  2. Start the service to deploy the Endpoints service on Kubernetes with the following command:
         
         kubectl create -f echo.yaml

If you see an error message similar to the following:
         
         The connection to the server localhost:8080 was refused - did you specify the right host or port?

This indicates that `kubectl` isn't properly configured. See [Configure kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#configure-kubectl) for more information. For more information, see [Deploying Endpoints on Kubernetes](https://docs.cloud.google.com/endpoints/docs/openapi/kubernetes-concept).




## Get the service's external IP address

If you are using Minikube, skip to Sending a request by using an IP address. It can take a few minutes after you start your service in the container before the external IP address is ready.

To view the service's external IP address:

  1. Run the following command: 
         
         kubectl get service

  2. Make a note of the value for EXTERNAL-IP. You use that IP address when you send a request to the sample API.




## Sending a request by using an IP address

After the sample API is running in the container cluster, you can send requests to the API.

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



### Send the request to `minikube`

The following commands use the ENDPOINTS_KEY environment variable that you set previously.

### Linux or mac OS
    
    
    NODE_PORT=`kubectl get service esp-echo --output='jsonpath={.spec.ports[0].nodePort}'`
    MINIKUBE_IP=`minikube ip`
    curl --request POST \
        --header "content-type:application/json" \
        --data '{"message":"hello world"}' \
        ${MINIKUBE_IP}:${NODE_PORT}/echo?key=${ENDPOINTS_KEY}
    

### PowerShell
    
    
    $Env:NODE_PORT=$(kubectl get service esp-echo --output='jsonpath={.spec.ports[0].nodePort}')
    $Env:MINIKUBE_IP=$(minikube ip)
    (Invoke-WebRequest -Method POST -Body '{"message": "hello world"}' `
        -Headers @{"content-type"="application/json"} `
        -URI "http://$Env:MINIKUBE_IP:$Env:NODE_PORT/echo?key=$Env:ENDPOINTS_KEY").Content
    

### Send the request to other Kubernetes clusters

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

## Sending a request to the FQDN

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

## Cleaning up

  * Delete the Kubernetes service and deployment: 
        
        kubectl delete -f echo.yaml




See [Deleting an API and API instances](https://docs.cloud.google.com/endpoints/docs/openapi/deleting-an-api-and-instances) for information on stopping the services used by this tutorial.

## What's next

  * [Learn how to deploy Endpoints Google Kubernetes Engine](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-engine).
  * [Learn how to build a Docker image](https://docs.cloud.google.com/container-builder/docs).
  * [Share your API with another developer](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys#sharing_apis_protected_by_api_key).
  * [Learn more about authentication](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method).
  * [Learn about community support options](https://docs.cloud.google.com/endpoints/docs/community-support).
  * [Troubleshooting GKE deployment](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gke-deployment). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
