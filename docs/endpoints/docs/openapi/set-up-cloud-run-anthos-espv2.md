---
url: https://docs.cloud.google.com/endpoints/docs/openapi/set-up-cloud-run-anthos-espv2/
title: Quickstart: Set up Cloud Endpoints OpenAPI for Knative serving with ESPv2 \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:32.318565+00:00
---

# Quickstart: Set up Cloud Endpoints OpenAPI for Knative serving with ESPv2  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/set-up-cloud-run-anthos-espv2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Cloud Endpoints OpenAPI for Knative serving with ESPv2

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-cloud-run-anthos "View this page for the Cloud Endpoints gRPC docs")

This page shows you how to set up Cloud Endpoints for [Knative serving](https://docs.cloud.google.com/run/docs/gke/setup). Endpoints uses the [Extensible Service Proxy V2 (ESPv2)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) as an [API gateway](https://wikipedia.org/wiki/API_management). To provide API management for Knative serving, you deploy the prebuilt ESPv2 container to [Knative serving](https://docs.cloud.google.com/run/docs) running on a GKE cluster.

With this set up, ESPv2 intercepts all requests to your services and performs any necessary checks (such as authentication) before invoking the service. When the service responds, ESPv2 gathers and reports telemetry.

For an overview of Endpoints, see [About Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/about-cloud-endpoints) and [Endpoints architecture](https://docs.cloud.google.com/endpoints/docs/openapi/architecture-overview).

## Task List

Use the following task list as you work through the tutorial. **All tasks are required to complete this tutorial.**

  1. Create a Google Cloud project, and if you haven't deployed your own Knative serving, deploy a sample service. See Before you begin.

  2. Create a GKE cluster with Knative serving enabled.

  3. Deploy a sample Knative serving service.

  4. Create an [OpenAPI document](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#open_api_doc) that describes your Endpoints API, and configure the routes to your Knative serving service. See Configuring Endpoints.

  5. Deploy the OpenAPI document to create a managed service. See Deploying the Endpoints configuration.

  6. Build a new ESPv2 Docker image with your Endpoints service configuration. See Building a new ESPv2 image.

  7. Deploy the new ESPv2 Knative serving image. See Deploying the ESPv2 Cloud Run image.

  8. Create a domain mapping to the ESPv2 Knative serving service.

  9. Test your configuration by Sending a request to the API.

  10. Track activity to your services. See Tracking API activity.

  11. Clean up.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Knative serving](https://docs.cloud.google.com/anthos/run/pricing)
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

  6. Make a note of the project ID because it is needed later. On the rest of this page, this project ID is referred to as ESPv2_PROJECT_ID.
  7. [Download and install the Google Cloud SDK](https://docs.cloud.google.com/sdk/docs/quickstarts).
  8. [Install curl](https://curl.haxx.se/) if you want to send a request to the deployed sample service.



### Set up the gcloud command line

To set up the gcloud CLI for Knative serving for Anthos:

  1. Make sure that Google Cloud SDK is authorized to access your data and services.

     1. Sign in. 
            
            gcloud auth login

     2. On the new browser tab that opens, choose an account that has the **Editor** or **Owner** role in the Google Cloud project that you created for deploying ESPv2 to Knative serving.

  2. Update installed `gcloud` components:
         
         gcloud components update

  3. Set the platform to `gke` and set your default project setting for `gcloud` to the one you just created:
         
         gcloud config set run/platform gke
         gcloud config set project ESPv2_PROJECT_ID

Replace ESPv2_PROJECT_ID with the project ID of the project you created.

  4. Set the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the new cluster. You can use any zone where GKE is supported, for example:
         
         gcloud config set compute/zone ZONE

Replace ZONE with your zone. For example, use `us-central1-a`. You can use any zone supported by GKE.

  5. Enable the following APIs for the project, which are needed to create a cluster, build and publish a container into the Artifact Registry:
         
         gcloud services enable container.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com




## Create a GKE cluster with Knative serving enabled

To create a cluster and enable it for Knative serving on Google Cloud:

  1. Create a new cluster using the command:
         
         gcloud container clusters create CLUSTER_NAME \
           --addons=HttpLoadBalancing,CloudRun \
           --machine-type=n1-standard-4 \
           --num-nodes=3 \
           --enable-stackdriver-kubernetes

Replace CLUSTER_NAME with the name you want for your cluster.

**Note:** The minimum cluster size is three nodes and the minimum machine type is `n1-standard-4` for this example.

Although these instructions don't enable [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) to resize clusters for demand, Knative serving on Google Cloud automatically scales instances within the cluster.

  2. Wait for the cluster creation to complete. During the creation process, you should see messages similar to the following:
         
         Creating cluster CLUSTER_NAME...done.
         Created [https://container.googleapis.com/v1/projects/ESPv2_PROJECT_ID/zones/ZONE/clusters/CLUSTER_NAME].

The output also shows the cluster version under the `NODE_VERSION` column of the output. For example, `1.15.11-gke.1` or `1.14.10-gke.27`. Make note of the cluster version for use later in this document.

  3. Set `gcloud` defaults to use your new cluster and cluster location, to avoid having to specify these when you use the gcloud CLI:
         
         gcloud config set run/cluster CLUSTER_NAME
         gcloud config set run/cluster_location ZONE

  4. Use the following command to view details about the new cluster:
         
         gcloud container clusters describe CLUSTER_NAME

  5. Use the following command to fetch credentials for your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME




## Deploy a sample Knative serving container

To deploy the "hello" Knative serving sample container to the cluster you just created:

  1. [Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Create service**.

  3. Select **Knative serving** as your development platform.

  4. In the available clusters drop-down menu, select the cluster you just created.

  5. Use the name _hello_ as the **Service name**. You can use some other name, but if you do, make sure you use that name later. These instructions assume you use _hello_.

  6. Select **Internal** under _Connectivity_ so that the service is not externally accessible.

  7. Click **Next** to continue to the second page of the service creation form.

  8. Specify `gcr.io/cloudrun/hello` as the **Container image URL**.

  9. Click **Create** to deploy the image to Knative serving and wait for the deployment to finish.

When you are done, the **Revisions** screen appears. Note that the URL of the deployed service is:

`http://hello.default.svc.cluster.local`

When you create an **Internal** service, GKE creates a DNS name that can only be resolved for requests originating from within the cluster itself, not for external requests. You cannot access this link externally from the cluster. See [Cloud Run services](https://docs.cloud.google.com/run/docs/resource-model#services) for more.

  10. To verify that your service is working correctly using curl, set up a tunnel from your desktop to the cluster. To see these instructions, click the ![More info icon](https://docs.cloud.google.com/static/endpoints/docs/images/more_info.png) icon to the right of the URL on the **Revisions** screen:

![Revisions screen.](https://docs.cloud.google.com/static/endpoints/docs/images/revisions.png)

  11. A panel opens showing the two commands that you use to access the internal service. You must run these commands in two separate terminal windows because the first command sets up port forwarding that is used by the second command.

When you run the curl command, you should see output from your service in the form:
         
         <!doctype html>
         <html lang=en>
         <head>
         <meta charset=utf-8>
         <meta name="viewport" content="width=device-width, initial-scale=1">
         **< title>Congratulations | Cloud Run</title> **
         ...




## Configure Endpoints

You must have an OpenAPI document based on either OpenAPI 2.0 or OpenAPI 3.x that describes the [surface](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#surface) of your apps and any authentication requirements. To learn more, see [Supported OpenAPI versions](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview#supported-openapi-versions).

You also need to add a Google-specific field that contains the URL for each app so that ESPv2 has the information it needs to invoke an app. If you are new to OpenAPI, see [OpenAPI overview](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview) for more information.

### About setting the host field of the OpenAPI spec

In the OpenAPI spec, you specify the Endpoints service name used to access your Knative serving service. The Endpoints service name is in the form of a domain name. The method for specifying the service name depends on which version of the OpenAPI spec you are using.

### OpenAPI 2.0

Use the `host` field to specify the service name:
    
    
    host: API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog

### OpenAPI 3.x

Use the `url` field in the `servers` object to specify the service name:
    
    
    servers:
    - url: https://API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog
      x-google-endpoint: {}

Because the Endpoints service name corresponds to a domain name, the name must follow these rules:

  * Must contain only lowercase letters, numbers, periods, or dashes.
  * Must not start with a dash.
  * Must not contain an underscore.



For example:
    
    
    hello-api.endpoints.ESPv2_PROJECT_ID.cloud.goog

### Creating the OpenAPI spec

  1. Create a text file called `openapi-run-anthos.yaml`.
  2. Your Knative serving backend service is defined at the top of the `openapi-run-anthos.yaml` file. For example: 

### OpenAPI 2.0
         
         swagger: '2.0'
         info:
               title: Cloud Endpoints + Cloud Run
               description: Sample API on Cloud Endpoints with a Cloud Run backend
               version: 1.0.0
         host: API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog
         x-google-endpoints:
             - name: API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog
               target: "INGRESS-IP"
         schemes:
             - https
         produces:
             - application/json
         x-google-backend:
               address: http://hello.default.svc.cluster.local
               disable_auth: true
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

### OpenAPI 3.x
         
         openapi: 3.0.4
         info:
           title: Cloud Endpoints + Cloud Run
           description: Sample API on Cloud Endpoints with a Cloud Run backend
           version: 1.0.0
         servers:
         - url: https://API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog
           x-google-endpoint:
             target: "INGRESS_IP"
         x-google-api-management:
           backends:
             cloudrun_anthos_backend:
               address: http://hello.default.svc.cluster.local
               disable_auth: true
               protocol: "http/1.1"
         x-google-backend: cloudrun_anthos_backend
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

Indentation is important for YAML format. For example the `host` field (for OpenAPI 2.0) or `servers` object (for OpenAPI 3.x) must be at the same level as `info`.

  3. In the `host` field (for OpenAPI 2.0) or `servers` object `url` field (for OpenAPI 3.x), specify the domain name of the Endpoints API used to access your Knative serving service, in the form: 
         
         API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog

For example:
         
         hello-api.endpoints.my-espv2-project-id.cloud.goog

  4. The `x-google-endpoints` extension registers a DNS entry for your Endpoints service on the `cloud.goog` domain, in the form: 

### OpenAPI 2.0
         
         x-google-endpoints:
           - name: "API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog"
           target: "IP_ADDRESS"

### OpenAPI 3.x
         
         servers:
           - url: https://API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog
             x-google-endpoint:
               target: "IP_ADDRESS"

**Note** : If you have your own domain mapping defined for your cluster, you can omit this step. See [Configuring DNS on the cloud.goog domain](/endpoints/docs/openapi/cloud-goog-dns-configure) for more.

The IP_ADDRESS is the IP of the `istio-ingress` service for your cluster. To determine this IP address:

     1. Go to the Google Kubernetes Engine page in the Google Cloud console: 

[Go to Google Kubernetes Engine](https://https://console.cloud.google.com/kubernetes)

     2. Click **Services & Ingress** in the left navigation panel to display a list of services.
     3. If your cluster version is `1.15.3-gke.19` or greater, `1.14.3-gke.12` or greater, or `1.13.10-gke.8` or greater, go to the `istio-ingress` service. For all other cluster versions, go to the `istio-ingressgateway` service
     4. Copy the external IP address shown next to the Load Balancer, without the port setting, if there is one. For example, if the IP is `192.0.2.1:15020`, omit the `:15020`. Ignore the other IP addresses listed.
  5. In the `address` section, specify the internal DNS name of the backend Knative serving `hello` service, and disable authentication to this service. This is necessary because the call from ESPv2 to the Knative serving service is made as an internal call from within the cluster and therefore authentication is not necessary.
  6. Note the value of the `title` property in the `openapi-run-anthos.yaml` file:
         
         title: Cloud Endpoints + Cloud Run 

The value of the `title` property becomes the name of the Endpoints service after you deploy the configuration.

  7. Save your OpenAPI document.




For information about the fields in the OpenAPI document that Endpoints requires, see [Configuring Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints).

## Deploy the Endpoints configuration

To deploy the Endpoints configuration, you use the [gcloud endpoints services deploy](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/services/deploy) command. This command uses [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/manage-config) to create a managed service.

To deploy the Endpoints configuration:

  1. Make sure you are in the directory that contains your OpenAPI document.

  2. Upload the configuration and create a managed service.
         
         gcloud endpoints services deploy openapi-run-anthos.yaml \
           --project ESPv2_PROJECT_ID

This creates a new Endpoints service with the name that you specified as the hostname in your OpenAPI document. The Endpoints service is configured according to your OpenAPI document.

As it is creating and configuring the Endpoints service, Service Management outputs information to the terminal. When the deployment completes, a message similar to the following is displayed:
         
         Service Configuration [CONFIG_ID] uploaded for service [API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog]

CONFIG_ID is the unique Endpoints service configuration ID created by the deployment. For example:
         
         Service Configuration [2019-02-01r0] uploaded for service [hello-api.endpoints.ESPv2_PROJECT_ID.cloud.goog] 

The service configuration ID consists of a date stamp followed by a revision number. If you deploy `openapi-run-anthos.yaml` again on the same day, the revision number is incremented in the service configuration ID. You can view the service configuration and the [deployment history](https://docs.cloud.google.com/endpoints/docs/openapi/config-file-compare) on the **Endpoints > Services** page in the Google Cloud console.

If you get an error message, see [Troubleshooting Endpoints configuration deployment](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-config-deployment).




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

## Build a new ESPv2 Knative serving image

Build the Endpoints service config into a new ESPv2 docker image. After creating this image, you can deploy it to your cluster.

**Note:**

This step is required.

The service config must be built into a new docker image because Cloud Run is a _scale-to-zero_ service. That means when there is no traffic, all instances are deleted. When traffic increases, new instances are created on-demand. This type of service instance creation is also called _cold start_. See the Cloud Run [Concurrency](https://docs.cloud.google.com/run/docs/about-concurrency) documentation for more. 

If the docker image did not have the service config built into it, Cloud Run would have to make two API calls to Google ServiceManagement at cold start. These calls count against your Google ServiceManagement API quota.

By building the service config into the ESPv2 docker image, you remove the two API calls and avoid impacting the quota count for the Google ServiceManagement service. This step also speeds up the new service instance creation and reduces the latency for the requests waiting for the new instance.

You must re-run this entire step and redeploy the new container:

  * Every time you modify and redeploy the Endpoints service configuration. Otherwise, changes to the service configuration will not be propagated to ESPv2.
  * When a new version of ESPv2 is released. Otherwise, the older version of ESPv2 will remain deployed.



To build the service config into a new ESPv2 docker image:

  1. Download this [script](https://github.com/GoogleCloudPlatform/esp-v2/tree/master/docker/serverless/gcloud_build_image) to your local machine where the gcloud CLI is installed and run it as:
         
         chmod +x gcloud_build_image
         ./gcloud_build_image -s API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog \
         -c CONFIG_ID -p ESPv2_PROJECT_ID

**Note:** This script requires bash. If you are not using macOS/Linux, you can run it on [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell), [Compute Engine](https://docs.cloud.google.com/compute), or Windows Subsystem for Linux.

The script uses the `gcloud` command to download the service config, build the service config into a new ESPv2 image, and upload the new image to your project container registry. The script automatically uses the latest release of ESPv2, denoted by the ESPv2_VERSION in the output image name. The output image is uploaded to:
         
         gcr.io/ESPv2_PROJECT_ID/endpoints-runtime-serverless:ESPv2_VERSION-API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog-CONFIG_ID




## Deploy the ESPv2 Knative serving image

Deploy the ESPv2 Knative serving service image to your cluster:

  1. Deploy the ESPv2 Knative serving service with the new image:
         
         gcloud run deploy ESPv2_SERVICE_NAME \
           --image="gcr.io/ESPv2_PROJECT_ID/endpoints-runtime-serverless:ESPv2_VERSION-API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog-CONFIG_ID" \
           --platform gke \
           --project=ESPv2_PROJECT_ID

For ESPv2_PROJECT_ID specify the name that you want to use for the ESPv2 service. In this example, set ESPv2_SERVICE_NAME to `espv2`.

  2. If you want to configure Endpoints to use additional ESPv2 startup options, such as [enabling CORS](https://docs.cloud.google.com/endpoints/docs/openapi/support-cors), you can pass the arguments in the `ESPv2_ARGS` environment variable:
         
         gcloud run deploy ESPv2_SERVICE_NAME \
           --image="gcr.io/ESPv2_PROJECT_ID/endpoints-runtime-serverless:ESPv2_VERSION-API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog-CONFIG_ID" \
           --set-env-vars=ESPv2_ARGS=--cors_preset=basic \
           --platform gke \
           --project ESPv2_PROJECT_ID

For more information and examples on setting the ESPv2_ARGS environment variable, including the list of available options and information on how to specify multiple options, see [Extensible Service Proxy V2 flags](https://docs.cloud.google.com/endpoints/docs/openapi/specify-esp-v2-startup-options).

  3. Grant ESPv2 permission to call [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started) and [Service Control](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started). **Note:** This step is not needed if ESPv2 Cloud Run instance is deployed without using the flag `--service-account`. When the `--service-account` flag is not used, Cloud Run uses the Compute Engine default service account. This service account may not have the `roles/servicemanagement.serviceController` role by default. If you encounter permission issues, either grant the role to the default service account or follow the preceding step. 

     * In the Google Cloud console, go to the Cloud Run page. 

[Go to the Cloud Run page](https://console.cloud.google.com/run)

     * Find the Cloud Run instance you deployed and the service account associated with it.

     * Grant required permissions to the service account: 
           
           gcloud projects add-iam-policy-binding PROJECT_NAME   
           
           --member "serviceAccount:SERVICE_ACCOUNT"   
           
           --role roles/servicemanagement.serviceController

For more information, see [ What are roles and permissions?](https://docs.cloud.google.com/iam/docs/understanding-roles)




The ESPv2 service is deployed as an external service, which means you can access it by using a curl command in the form:
    
    
    curl -H "Host: espv2.default.example.com" http://IP_ADDRESS

where IP_ADDRESS is the IP address of the `istio-ingress` service for your cluster.

To see this curl command, click the IMAGE icon to the right of the ESPv2 URL on the **Revisions** screen of the deployed ESPv2 Knative serving service.

You can now make API calls to your Endpoints service through the ESPv2 service. For example, to make a request to an Endpoints service with a path of `/hello`, you could make a request in the form:
    
    
    curl -H "Host: espv2.default.example.com" http://IP_ADDRESS/hello

However, specifying a `host` header on every request to your Endpoints service is not user-friendly. In the next section, you set up a domain map to make it easier to make a call to your Endpoint service through ESPv2.

## Creating a domain mapping to the ESPv2 Knative serving service

To be able to omit the `host` header when you make a request, add a domain mapping for the ESPv2 service:

  1. [Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Manage Custom Domains**.

  3. Select **Add Mapping**.

  4. From the drop-down, select **Add service domain mapping**.

  5. In the **Select a service to map to** field of the **Add mapping** dialog, select your ESPv2 service.

  6. In the **Enter domain name** field, specify the domain name you want to use to access your Knative serving service through Endpoints. For example, specify:
         
         API_NAME.endpoints.ESPv2_PROJECT_ID.cloud.goog

Where API_NAME is the name of your Endpoints API. For this example, you can use "hello-api": 
         
         hello-api.endpoints.ESPv2_PROJECT_ID.cloud.goog

  7. Click **Continue**. A summary of the mapping appears.

  8. Select **Done** to save the mapping.




## Send requests to the API

Use curl to send an HTTP request to your API:
    
    
    curl -X GET "http://hello-api.endpoints.ESPv2_PROJECT_ID.cloud.goog/hello"

If you didn't get a successful response, see [Troubleshooting Response Errors](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-response-errors).

### Configuring Endpoints API to use HTTPS

Automatic TLS support is disabled by default for Knative serving on Google Cloud. Therefore, in this example when you access your Endpoints API through ESPv2, you make the call using HTTP.

You can configure ESPv2 to support requests using HTTPS. Note that you configure HTTPS support on ESPv2, the external service, not on "hello", the internal backend service.

To support HTTPS with ESPv2, you must:

  1. Own a domain. If you don't have a domain, you can obtain one from [Cloud Domains](https://docs.cloud.google.com/domains/docs) or from another domain vendor.

  2. Create a domain mapping for your ESPv2 service and have updated your DNS record accordingly following the instructions at the [domains mapping page](https://docs.cloud.google.com/run/docs/mapping-custom-domains).

If you obtained your domain from Cloud Domains, use [Cloud DNS](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name), or a DNS server of your choice. Using a domain from Cloud Domains is the easiest option.




### OpenAPI 2.0

In the Endpoints OpenAPI specification:

  * Set the `host` field to refer to your domain instead of to `*.cloud.goog`.
  * Remove the `x-google-endpoints` tag and its two child properties.



### OpenAPI 3.x

Add the following to the Endpoints OpenAPI specification:
    
    
    servers:
      - url: YOUR_DOMAIN
        x-google-endpoint: {}

For complete instructions and tutorial, see [Enabling HTTPS and automatic TLS certificates](https://docs.cloud.google.com/run/docs/gke/auto-tls).

**Note** : If you want to let us know what you liked about this tutorial, feel free to provide feedback at the bottom of this page. Your feedback helps us improve these tutorials.  
If you got an error, join the [`google-cloud-endpoints`](https://groups.google.com/forum/#!forum/google-cloud-endpoints) Google group and let us know what went wrong. This group receives responses from other Endpoints users and from Google engineers, who monitor the group.

## Tracking API activity

  1. View the activity graphs for your API on the **Endpoints** > **Service** page in the Google Cloud console.

[View Endpoints activity graphs](https://console.cloud.google.com/endpoints)

It may take a few moments for the request to be reflected in the graphs.

  2. Look at the request logs for your API on the Logs Explorer page. [View Endpoints request logs](https://console.cloud.google.com/logs/query)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

See [Deleting an API and API instances](https://docs.cloud.google.com/endpoints/docs/openapi/deleting-an-api-and-instances) for information on stopping the services used by this tutorial.

## What's next

  * [Learn more about Cloud Run](https://docs.cloud.google.com/run/docs/deploying)
  * [Learn more about deploying the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config)
  * [Share your API with another developer](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys#sharing_apis_protected_by_api_key)
  * [Learn about authentication](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method)
  * [Learn about community support options](https://docs.cloud.google.com/endpoints/docs/community-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
