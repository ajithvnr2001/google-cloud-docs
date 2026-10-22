---
url: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-mig-lb-espv2/
title: Getting started with Cloud Endpoints for Managed Instance Group (MIGs) with ESPv2 \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:33.423067+00:00
---

# Getting started with Cloud Endpoints for Managed Instance Group (MIGs) with ESPv2  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/get-started-mig-lb-espv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Getting started with Cloud Endpoints for Managed Instance Group (MIGs) with ESPv2 Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-mig-lb-espv2 "View this page for the Cloud Endpoints gRPC docs")

This tutorial shows you how to configure and deploy a sample API and the [Extensible Service Proxy V2 (ESPv2)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) running in prebuilt [Docker](https://docs.docker.com/) containers on [Managed Instance Group (MIGs) ](https://docs.cloud.google.com/compute/docs/instance-groups).

The sample code's REST API is described using the [OpenAPI specification](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview). The tutorial also shows you how to create an [API key](https://docs.cloud.google.com/endpoints/docs/openapi/when-why-api-key) and use it in requests to the API.

For an overview of Cloud Endpoints, see [About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints) and [Endpoints architecture](https://docs.cloud.google.com/endpoints/docs/openapi/architecture-overview). 

## Objectives

Use the following high-level task list as you work through the tutorial. All tasks are required to successfully send requests to the API. 

  1. Set up a Google Cloud project. See Before you begin.
  2. Download the sample code. See Getting the sample code.
  3. Configure the `openapi.yaml` file, which is used to configure Endpoints. See Configuring Endpoints.
  4. Deploy the Endpoints configuration to create a Endpoints service. See Deploying the Endpoints configuration.
  5. Deploy the API and ESPv2 on the Managed Instance Group (MIGs) backend. See Deploying the API backend.
  6. Send a request to the API by using an IP address. See Sending a request by using IP address.
  7. Configure a DNS record for the sample API. See Configuring DNS for Endpoints.
  8. Send a request to the API by using the fully qualified domain name. See Sending a request by using FQDN.
  9. Track API activity. See Tracking API activity.
  10. Avoid incurring charges to your Google Cloud account. See Clean up. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)
  * [Endpoints](https://docs.cloud.google.com/endpoints/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

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

## Downloading the sample code

Download the sample code to your local machine. Java

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



**Note:** The example openapi.yaml file contains a section for configuring authentication that isn't needed for this tutorial. You don't need to configure the lines with YOUR_SERVICE_ACCOUNT_EMAIL and YOUR_CLIENT_ID.

This tutorial uses a Google-specific extension to the OpenAPI specification that lets you configure the service name. The method for specifying the service name depends on which version of the OpenAPI spec you are using.

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

## Deploying the API Backend

### Create an instance template

Create a template that you will use to create a group of VM instances. Each instance created from the template launches an ESPv2 and a backend application server.

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.

  3. Under **Name** , enter `load-balancing-espv2-template`.

  4. Under **Machine configuration** , set the **Machine type** to `e2-micro`.

  5. Under **Boot disk** , set the **Image** to `Container Optimized OS stable version`.

  6. Under **Firewall** , select **Allow HTTP traffic**.

  7. Click **Management, security, disks, networking, sole tenancy** to reveal the advanced settings.

  8. Click the **Management** tab. Under **Automation** , enter the following **Startup script**. Remember to update ENDPOINTS_SERVICE_NAME.
         
         sudo docker network create --driver bridge esp_net
         sudo docker run \
           --detach \
           --name=echo \
           --net=esp_net \
           gcr.io/google-samples/echo-python:1.0
         sudo docker run \
           --detach \
           --name=esp \
           --publish=80:9000 \
           --net=esp_net \
           gcr.io/endpoints-release/endpoints-runtime:2 \
           --service=ENDPOINTS_SERVICE_NAME \
           --rollout_strategy=managed \
           --listener_port=9000 \
           --healthz=/healthz \
           --backend=echo:8080
         

The script gets, installs, and launches the echo application server and the ESPv2 proxy server at instance startup.

  9. Click **Create**.




Wait until the template has been created before continuing.

### Create a regional managed instance group

To run the application, use the instance template to create a regional managed instance group:

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/)

  2. Click **Create instance group**.

  3. Under **Name** , enter `load-balancing-espv2-group`.

  4. Under **Location** , select **Multiple zones**.

**Pro Tip:** To ensure your application is available during extreme events, like zonal outages, Compute Engine recommends that you [distribute your application across multiple zones](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups). 

  5. Under **Region** , select **us-central1**.

  6. Click the **Configure zones** drop-down menu to reveal **Zones**. Select the following zones:

     * **us-central1-b**
     * **us-central1-c**
     * **us-central1-f**
  7. Under **Instance template** , select `load-balancing-espv2-template`.

  8. Under **Autoscaling** , select **Don't autoscale**.

  9. Set **Number of instances** to `3`.

**Pro Tip:** When creating a regional managed instance group, Compute Engine recommends that you provision enough instances so that, if all of the instances in any one zone are unavailable, the remaining instances still meet the minimum number of instances that you require. However, provisioning more instances than you need might incur additional costs. For more information, see [ Selecting instance group size to ensure availability](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision). 

  10. Under **Instance redistribution** , select **On**.

  11. Under **Autohealing** and **Health check** , select **No health check**.

  12. Click **Create**. This redirects you back to the **Instance groups** page.

**Note:** You might need to wait a few minutes until all of the instances in the group are running and ready to display the web application.



### Create a load balancer

This section explains the steps required to create a global load balancer that directs HTTP traffic to your instance group. 

This load balancer uses a frontend to receive incoming traffic and a backend to distribute this traffic to healthy instances. Because the load balancer is made of multiple components, this task is divided into several parts:

  * Backend configuration
  * Frontend configuration
  * Review and finalize



Complete all the steps to create the load balancer.

  1. In the Google Cloud console, go to the **Create a load balancer** page.

[Go to Create a load balancer](https://console.cloud.google.com/networking/loadbalancing/add)

  2. In the **Application Load Balancer (HTTP/S)** section, click **Start configuration**.

  3. Under **Internet facing or internal only** , select **From Internet to my VMs**. Then, click **Continue**.

  4. For the **Name** of the load balancer, enter `espv2-load-balancer`.




#### Backend configuration

  1. In the left panel of the **Create global external Application Load Balancer** page, click **Backend configuration**.
  2. Click **Create or select backend services & backend buckets** to open a drop-down menu. Click **Backend services** , then click **Create a backend service**.
  3. In the new window, for the **Name** of the backend application, enter `espv2-backend`.
  4. Set **Instance group** to `load-balancing-espv2-group`.
  5. Set **Port numbers** to `80`. This [allows HTTP traffic](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https) between the load balancer and the instance group.
  6. Under **Balancing mode** , select **Utilization**.
  7. Click **Done** to create the backend.
  8. Create the health check for the backend of the load balancer:

**Pro Tip:** Health checks are used for both load balancing and [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups#autohealing), but for different purposes: 

     * Health checks for load balancing are used for detecting unresponsive instances and directing traffic away from them.
     * Health checks for autohealing are used for detecting and recreating failed instances. 
Use separate health checks for load balancing and for autohealing. Using the same health check for these services would remove the distinction between unresponsive instances and failed instances, causing unnecessary latency and/or unavailability for your users. For more information, see [ Health check concepts](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts). 
     1. Under **Health check** , select **Create a health check** (or **Create another health check**) from the drop-down menu. A new window opens.
     2. In the new window under **Name** , enter `espv2-load-balancer-check`.
     3. Set the **Protocol** to **HTTP**.
     4. Under **Port** , enter `80`.
     5. For this tutorial, set the **Request path** to `/healthz`, which is a path that the ESPv2 is set up to respond to.
     6. Set the following **Health criteria** :

        1. Set **Check interval** to `3` seconds. This defines the amount of time from the start of one probe to the start of the next one.
        2. Set **Timeout** to `3` seconds. This defines the amount of time that Google Cloud waits for a response to a probe. Its value must be less than or equal to the check interval.
        3. Set **Healthy Threshold** to `2` consecutive successes. This defines the number of sequential probes that must succeed in order for the instance to be considered healthy.
        4. Set **Unhealthy Threshold** to `2`consecutive failures. This defines the number of sequential probes that must fail in order for the instance to be considered unhealthy.

**Pro Tip:** For information about refining the **Check interval** and **Timeout** values for your own application, see [How health checks work](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#probes). To refine the **Healthy Threshold** and **Unhealthy Threshold** values for your own application, use the following criteria:

        * If traffic is being directed to instances with high latency even when faster instances are available, decrease the threshold for traffic by making your health check more aggressive. 
        * If traffic is being directed away from instances with low latency, increase the threshold for traffic by making your health check more conservative. 

For detailed information about optimizing and measuring latency, see [ Optimizing Application Latency with Load Balancing](https://docs.cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency)

     7. Click **Save and continue** to create the health check.

  9. Click **Create** to create the backend service.




#### Frontend configuration

  1. In the left panel of the **Create global external Application Load Balancer** page, click **Frontend configuration**.
  2. On the **Frontend configuration** page, under **Name** , enter `espv2-ipv4-frontend`.
  3. Set the **Protocol** to `HTTP`.
  4. Set the **Port** to `80`.
  5. Click **Done** to create the frontend.



#### Review and finalize

  1. Verify your load balancing settings before creating the load balancer:

     1. In the left panel of the **Create global external Application Load Balancer** page, click **Review and finalize**.
     2. On the **Review and finalize** page, verify the following **Backend** settings:

        * The **Backend service** is `espv2-backend`.
        * The **Endpoint protocol** is `HTTP`.
        * The **Health check** is `espv2-load-balancer-check`.
        * The **Instance group** is `load-balancing-espv2-group`.
     3. On the same page, verify that **Frontend** uses an IP address with a **Protocol** of `HTTP`.

  2. In the left panel of the **Create global external Application Load Balancer** page, click **Create** to finish creating the load balancer.

You might need to wait a few minutes for the load balancer creation to finish.

  3. After the load balancer is created, find the IP address from the **Load Balancer** page.

[Go to Load Balancer](https://console.cloud.google.com/networking/loadbalancing/add)




## Sending a request by using an IP address

After the sample API and ESPv2 are running on the deployed backend, you can send requests to the API from your local machine.

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

  1. Make sure that the gcloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud:
         
         gcloud auth login
         

  2. Enter the following to display the project IDs for your Google Cloud projects:
         
         gcloud projects list
         

  3. Using the applicable project ID from the previous step, set the default Google Cloud project to the one that your application is in:
         
         gcloud config set project [YOUR_PROJECT_ID]
         

  4. Obtain the name of all managed services in your Google Cloud project:
         
         gcloud endpoints services list
         

  5. Delete the service from Service Management. Replace `SERVICE_NAME` with the name of the service you want to remove.
         
         gcloud endpoints services delete SERVICE_NAME
         

Running `gcloud endpoints services delete` doesn't immediately delete the managed service. Service Management disables the managed service for 30 days, which allows you time to restore it if you need to. After 30 days, Service Management permanently deletes the managed service.

  6. Go to the **Load Balancer** page.

[Go to Load Balancer](https://console.cloud.google.com/net-services/loadbalancing/list)

Delete load balancer `espv2-load-balancer` with backend service `espv2-backend` and health check `espv2-load-balancer-check`.

  7. Go to the **Instance Groups** page.

[Go to Instance Groups](https://console.cloud.google.com/compute/instanceGroups)

Delete `load-balancing-espv2-group`

  8. Go to the **Instance Template** page.

[Go to Instance Templates](https://console.cloud.google.com/compute/instanceTemplates)

Delete `load-balancing-espv2-template`.




## What's next

  * [Share your API with another developer](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys#sharing_apis_protected_by_api_key)
  * [Learn more about authentication](https://docs.cloud.google.com/endpoints/docs/openapi/authenticating-users)
  * [Learn about community support options](https://docs.cloud.google.com/endpoints/docs/community-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
