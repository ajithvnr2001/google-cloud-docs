---
url: https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend/
title: Deploying the API backend \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:19:51.563823+00:00
---

# Deploying the API backend  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Deploying the API backend Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend "View this page for the Cloud Endpoints gRPC docs")

This page explains how to deploy your API's backend code and the Extensible Service Proxy (ESP) to Google Kubernetes Engine, Compute Engine, and the App Engine flexible environment.

Although the deployment steps vary depending on the platform hosting your API, there is always a step where you provide ESP the [service name](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id) and an option that configures ESP to use the latest deployed Cloud Endpoints service configuration. With this information, ESP can obtain your API's Endpoints configuration, which allows ESP to proxy requests and responses so that Endpoints can manage your API.

**Note:** [ESP](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) and [ESPV2](https://docs.cloud.google.com/endpoints/docs/openapi/\(/endpoints/docs/openapi/glossary#extensible_service_proxy_v2\)) each have different environment support. ESP is only supported on the App Engine flexible environment and is not available on the App Engine standard environment. In contrast, ESPV2 can be deployed on GKE and Kubernetes but does not support App Engine.

## Prerequisites

As a starting point, this page assumes that you have:

  * [Created a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * [Configured Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints).
  * [Deployed the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config).



## Preparing for deployment

### App Engine flexible environment

With the addition of a small configuration step (described in the following steps), deploying your API so that it is managed by Endpoints is the same as deploying any application to the App Engine flexible environment. Follow the App Engine documentation to: 

  * [ Organize your configuration files](https://docs.cloud.google.com/appengine/docs/flexible/python/configuration-files).
  * [ Create the `app.yaml` configuration file](https://docs.cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml)
  * If your application is based on microservices, see [Deploying multiple service applications](https://docs.cloud.google.com/appengine/docs/standard/python/tools/uploadinganapp#deploying_multiple_service_applications) documentation for information on configuring the `app.yaml` files for each service.



You deploy your API to App Engine by using the [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command. This command automatically builds a container image by using the [Container Builder](https://docs.cloud.google.com/container-builder/docs) service and then deploys that image to your App Engine flexible environment.

**Before you deploy:**

  * The [Owner](https://docs.cloud.google.com/appengine/docs/flexible/python/access-control#owner) of the Google Cloud project must create the [App Engine application](https://docs.cloud.google.com/appengine/docs/flexible/python/managing-projects-apps-billing).
  * Ensure that your user account includes the [required privileges](https://docs.cloud.google.com/appengine/docs/standard/python/roles#basic_roles).



### Compute Engine

For Endpoints to manage your API, you must install and configure ESP, as well as the backend server code for your API. You need to install Docker on your Compute Engine VM instance so that you can run the ESP Docker image that is freely available in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).

**Before you deploy:**

The following outlines at a high-level the steps you must take before you can deploy your API and ESP to Compute Engine. In general, you do all the steps that you normally would to run your backend server code on Compute Engine.

  1. Create, configure, and start your VM instance. See the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/how-to).
  2. Install Docker Enterprise Edition (EE) or Docker Community Edition (CE) on your VM instance. See [ Install Docker](https://docs.docker.com/engine/installation/).
  3. Create a Docker container for your backend server code. See [Cloud Build documentation](https://docs.cloud.google.com/container-builder/docs).
  4. Push the container to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/pushing-and-pulling) or another registry.
  5. Make sure that you can successfully: 
     * [Connect to the VM instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
     * Run the Docker image to start your backend server on the VM instance. See [Docker run reference](https://docs.docker.com/engine/reference/run/).
     * Send requests to your API.



### GKE

When you create a cluster in the Google Cloud console, by default, the OAuth scopes that are granted to the cluster's service account include the scopes that Endpoints requires:

  * Service Control: Enabled
  * Service Management: Read Only



When you create a cluster by using the [ `gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) command or by using a third-party configuration file, make sure you specify the following scopes:

  * `"https://www.googleapis.com/auth/servicecontrol"`
  * `"https://www.googleapis.com/auth/service.management.readonly"`



For more information, see [ What are access scopes?](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes#what_are_access_scopes)

**Before you deploy:**

With the addition of a small section to your [Deployment manifest file](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), you can run the ESP Docker image on your container clusters along with your containerized application. The following outlines at a high-level the steps you must take before you can deploy your API with ESP to GKE. In general, you do all the steps that you normally would to run your backend server code on GKE.

  1. Deploy your containerized application to the container clusters. The general steps as described in the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs) are: 
     1. Package your app into a Docker image.
     2. Upload the image to a registry.
     3. Create a container cluster.
     4. Deploy your app to the cluster.
     5. Expose your app to the internet.
  2. Make sure that you can successfully: 
     * Start your API's server.
     * Send requests to your API.



## Deploying your API and ESP

### App Engine flexible environment

**To deploy the API and ESP to App Engine:**

  1. Get the [ service name](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id) of your API. This is the name that you specified in the `host` field of your OpenAPI document. 
  2. Edit the `app.yaml` file, and add a section called `endpoints_api_service` that contains the service name. You can use the `app.yaml` file from the [ tutorial](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-app-engine#deploy_backend) as a model: Java
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

Python
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

Go
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

PHP
         
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
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

NodeJS
         
         endpoints_api_service:
           # The following values are to be replaced by information from the output of
           # 'gcloud endpoints services deploy openapi-appengine.yaml' command.
           name: ENDPOINTS-SERVICE-NAME
           rollout_strategy: managed

Replace `ENDPOINTS-SERVICE-NAME` with your API's service name.

Add the runtime and environment variables in the `app.yaml` configuration file. 

For example: 
         
         runtime: nodejs
         env: flex
         endpoints_api_service:
           name: example-project-12345.appspot.com
           rollout_strategy: managed
           

The `rollout_strategy: managed` option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. 

If your application is based on microservices, you must include the `endpoints_api_service` section in every `app.yaml` file.

  3. Save the `app.yaml` file (or files).
  4. Deploy your backend code and ESP to App Engine: 
         
         gcloud app deploy




Because you added the `endpoints_api_service` section to the `app.yaml` file, the `gcloud app deploy` command deploys and configures ESP in a separate container to your App Engine flexible environment. All request traffic is routed through ESP, and it proxies requests and responses to and from the container running your backend server code.

**If you need to configure ESP to use a specific configuration ID:**

  1. In the `endpoints_api_service` section of your `app.yaml` file, add the `config_id` field and set it to a specific [configuration ID.](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id)
  2. Either remove `rollout_strategy: managed` or set `rollout_strategy` to `fixed`. The `fixed` option configures ESP to use the service configuration that you specified in `config_id`.
  3. Redeploy your API and ESP: `gcloud app deploy`



We recommend that you don't keep ESP configured to use a specific configuration ID for very long because if you deploy an updated service configuration, you have to restart ESP to use the new configuration.

**To remove the specific configuration ID:**

  1. Remove the `config_id`option from the `app.yaml`file.
  2. Add the `rollout_strategy: managed` option.
  3. Issue the `gcloud app deploy` command 



When you use the `rollout_strategy: managed` option, don't include `config_id: YOUR_SERVICE_CONFIG_ID` in the `app.yaml` file. If you do, `gcloud app deploy` fails with the following error:

`config_id is forbidden when rollout_strategy is set to "managed".`

When you deploy your API to the App Engine flexible environment for the first time, there might be a delay as your virtual machine (VM) and other infrastructure are set up. For additional information, see [ Ensuring successful deployment](https://docs.cloud.google.com/appengine/docs/flexible/python/testing-and-deploying-your-app#ensuring_successful_deployment) in the App Engine documentation.

### Compute Engine

**To deploy your API with ESP to Compute Engine with Docker:**

  1. Connect to your VM instance. Replace `INSTANCE_NAME` with the name of your VM instance. 
         
         gcloud compute ssh INSTANCE_NAME

  2. Create your own container network called `esp_net`: 
         
         sudo docker network create --driver bridge esp_net

  3. Run an instance of the image of your backend server code and connect it to the `esp_net` container network: 
         
         sudo docker run \
             --detach \
             --name=YOUR_API_CONTAINER_NAME \
             --net=esp_net \
             gcr.io/YOUR_PROJECT_ID/YOUR_IMAGE:1.0

     * Replace `YOUR_API_CONTAINER_NAME` with the name of your container.
     * Replace `YOUR_PROJECT_ID` with the Google Cloud project ID that you used when you pushed the image.
     * Replace `YOUR_IMAGE` with the name of your image.
  4. Get the [service name](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id) of your API. This is the name that you specified in the `host` field of your OpenAPI document. 
  5. Run an instance of the ESP Docker image: 
         
         sudo docker run \
             --name=esp \
             --detach \
             --publish=80:8080 \
             --net=esp_net \
             gcr.io/endpoints-release/endpoints-runtime:1 \
             --service=SERVICE_NAME \
             --rollout_strategy=managed \
             --backend=YOUR_API_CONTAINER_NAME:8080

     * Replace `SERVICE_NAME` with the name of your service.
     * Replace `YOUR_API_CONTAINER_NAME` with the name of your API's container.

The `--rollout_strategy=managed` option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. 




**If you need to configure ESP to use a specific configuration ID:**

  1. Include the `--version` option and set it to a specific [configuration ID. ](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id)
  2. Either remove the `--rollout_strategy=managed` option or set `--rollout_strategy` to `fixed`. The `fixed` option configures ESP to use the service configuration that you specified in `--version`.
  3. Issue the `docker run` command again.



If you specify both `--rollout_strategy=managed` and the `--version` option, ESP starts with the configuration that you specified in `--version`, but then runs in managed mode and obtains the latest configuration.

We recommend that you don't keep ESP configured to use a specific configuration ID for very long because if you deploy an updated service configuration, you have to restart ESP to use the new configuration.

**To remove the specific configuration ID:**

  1. In the ESP flags for `docker run`, remove the ` --version` option.
  2. Add the `--rollout_strategy=managed` option.
  3. Issue the `docker run` command to restart ESP.



See [ESP startup options](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options) for the full list of options that you can specify when starting ESP.

### GKE

**To deploy ESP to GKE:**

  1. Get the [service name](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id) of your API (the name that you specified in the `host` field of your OpenAPI document). 
  2. Open your Deployment manifest file (referred to as the `deployment.yaml` file) and add the following to the containers section: 
         
         containers:
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:1
           args: [
             "--http_port=8081",
             "--backend=127.0.0.1:8080",
             "--service=SERVICE_NAME",
             "--rollout_strategy=managed"
           ]

Replace `SERVICE_NAME` with your API's service name.

The `--rollout_strategy=managed"` option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. 

  3. Start the Kubernetes service by using the [kubectl create](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create)command: 
         
         kubectl create -f deployment.yaml




**If you need to configure ESP to use a specific configuration ID:**

  1. In your Deployment manifest file, add the `--version` option and set it to a specific [configuration ID. ](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id)
  2. Either remove `--rollout_strategy=managed` or set `--rollout_strategy` to `fixed`. The `fixed` option configures ESP to use the service configuration that you specified in `--version`.
  3. Start the Kubernetes service: `kubectl create -f deployment.yaml`



If you specify both `--rollout_strategy=managed` and the `--version` option, ESP starts with the configuration that you specified in `--version` but then runs in managed mode and obtains the latest configuration.

We recommend that you don't keep ESP configured to use a specific configuration ID for very long because if you deploy an updated service configuration, you have to restart ESP to use the new configuration.

**To remove the specific configuration ID:**

  1. In your Deployment manifest file, remove the `--version` option.
  2. Add the `--rollout_strategy=managed`.
  3. Start the Kubernetes service: `kubectl create -f deployment.yaml `



See [ESP startup options](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options) for the full list of options that you can specify when starting ESP.

## Tracking API activity

After you deploy ESP and your API backend, you can use tools such as `curl` or Postman to send requests to your API. If you don't get a successful response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-response-errors).

After sending some requests, you can:

  * View the activity graphs for your API on **Endpoints** > **Services**.   


[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  
It may take a few moments for the request to be reflected in the graphs.
  * Look at the request logs for your API on the Cloud Logging page.   


[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)




## What's next

  * [ Troubleshooting the App Engine flexible environment deployment](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-aeflex-deployment).
  * [ Troubleshooting Endpoints on Compute Engine](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gce-deployment).
  * [ Troubleshooting Endpoints in Google Kubernetes Engine](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gke-deployment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
