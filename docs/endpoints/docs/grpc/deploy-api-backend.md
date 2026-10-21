---
url: https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend/
title: Deploying the API backend \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:07.759509+00:00
---

# Deploying the API backend  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Deploying the API backend Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This page explains how to deploy your API's backend code and the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy) to Google Kubernetes Engine and Compute Engine.

Although the deployment steps vary depending on the platform hosting your API, there is always a step where you provide ESP the [service name](https://docs.cloud.google.com/endpoints/docs/grpc/get-service-name-config-id) and an option that configures ESP to use the latest deployed Cloud Endpoints service configuration. With this information, ESP can obtain your API's Endpoints configuration, which lets ESP proxy requests and responses so that Cloud Endpoints can manage your API.

## Prerequisites

As a starting point, this page assumes that you have:

  * Created a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * [Configured Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints).
  * [Deployed the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config).



## Preparing for deployment

### Compute Engine

For Endpoints to manage your API, you must install and configure ESP as well as the backend server code for your API. You need to install Docker on your Compute Engine VM instance so that you can run the ESP Docker image that is freely available in [Container Registry](https://docs.cloud.google.com/container-registry/docs).

**Before you deploy** :

Before you can deploy your API and ESP to Compute Engine, complete the following steps:

  1. [Create, configure, and start your VM instance](https://docs.cloud.google.com/compute/docs/how-to).
  2. [Install Docker Enterprise Edition (EE) or Docker Community Edition (CE) on your VM instance](https://docs.docker.com/engine/installation/).
  3. [Create a Docker container for your backend server code](https://docs.cloud.google.com/build/docs).
  4. [Push the container to Artifact Registry}](https://docs.cloud.google.com/artifact-registry/docs/pushing-and-pulling) or another registry.
  5. Make sure that you can successfully:

     * [Connect to the VM instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
     * Run the Docker image to start your backend server on the VM instance. See [Docker run reference](https://docs.docker.com/engine/reference/run/).
     * Send requests to your API.



### GKE

When you create a cluster in the Google Cloud console, by default, the OAuth scopes that are granted to the cluster's service account include the scopes that Endpoints requires:

  * Service Control: Enabled
  * Service Management: Read Only



When you create a cluster by using the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) command or by using a third-party configuration file, make sure you specify the following scopes:

  * `"https://www.googleapis.com/auth/servicecontrol"`
  * `"https://www.googleapis.com/auth/service.management.readonly"`



For more information, see [What are access scopes?](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes#what_are_access_scopes_overview).

**Before you deploy** :

With the addition of a small section to your [Deployment manifest file](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/deployment), you can run the ESP Docker image on your container clusters along with your containerized application. Before you can deploy your API with ESP to GKE, complete the following steps:

  1. Deploy your containerized application to the container clusters. The general steps as described in the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs) are:

     1. Package your application into a Docker image.
     2. Upload the image to a registry.
     3. Create a container cluster.
     4. Deploy your application to the cluster.
     5. Expose your application to the internet.
  2. Make sure that you can successfully:

     * Start your API's server.
     * Send requests to your API.



## Deploying your API and ESP

### Compute Engine

**To deploy your API with ESP to Compute Engine with Docker** :

  1. Connect to your VM instance. Replace `INSTANCE_NAME` with the name of your VM instance:
         
         gcloud compute ssh INSTANCE_NAME
         

  2. Create your own container network called `esp_net`:
         
         sudo docker network create --driver bridge esp_net
         

  3. Run an instance of the image of your backend server code and connect it to the `esp_net` container network:
         
         sudo docker run \
             --detach \
             --name=YOUR_API_CONTAINER_NAME \
             --net=esp_net \
             gcr.io/YOUR_PROJECT_ID/YOUR_IMAGE:1
         

     * Replace `YOUR_API_CONTAINER_NAME` with the name of your container.
     * Replace `YOUR_PROJECT_ID` with the Google Cloud project ID that you used when you pushed the image.
     * Replace `YOUR_IMAGE` with the name of your image.
  4. Get the [service name](https://docs.cloud.google.com/endpoints/docs/grpc/get-service-name-config-id) of your API. This is the name that you specified in the `name` field of your service configuration YAML file.

  5. Run an instance of the ESP Docker image:
         
         sudo docker run \
             --detach \
             --name=esp \
             --publish=80:9000 \
             --net=esp_net \
             gcr.io/endpoints-release/endpoints-runtime:1 \
             --service=SERVICE_NAME \
             --rollout_strategy=managed \
             --http2_port=9000 \
             --backend=grpc://YOUR_API_CONTAINER_NAME:8000
         

     * Replace `SERVICE_NAME` with the name of your service.
     * Replace `YOUR_API_CONTAINER_NAME` with the name of your API's container.

The `--rollout_strategy=managed` option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. 




**If you need to configure ESP to use a specific configuration ID** :

  1. Include the `--version` option and set it to a specific [configuration ID](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id).

  2. Either remove the `--rollout_strategy=managed` option or set `--rollout_strategy` to `fixed`. The `fixed` option configures ESP to use the service configuration that you specified in `--version`.

  3. Run the `docker run` command again.




If you specify both `--rollout_strategy=managed` and the `--version` option, ESP starts with the configuration that you specified in `--version`, but then runs in managed mode and obtains the latest configuration.

We recommend that you don't keep ESP configured to use a specific configuration ID for too long because if you deploy an updated service configuration, you have to restart ESP to use the new configuration.

**To remove the specific configuration ID** :

  1. In the ESP flags for `docker run`, remove the `--version` option.

  2. Add the `--rollout_strategy=managed` option.

  3. To restart ESP, run the `docker run` command.




See [ESP startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options) for the full list of options that you can specify when starting ESP.

### GKE

**To deploy ESP to GKE** :

  1. Get the [service name](https://docs.cloud.google.com/endpoints/docs/grpc/get-service-name-config-id) of your API.

  2. Open your Deployment manifest file (referred to as `deployment.yaml`) and add the following to the `containers` section:
         
         containers:
               - name: esp
                 image: gcr.io/endpoints-release/endpoints-runtime:1
                 args: [
                   "--http2_port=9000",
                   "--service=SERVICE_NAME",
                   "--rollout_strategy=managed",
                   "--backend=grpc://127.0.0.1:8000"
                 ]
                 ports:
                   - containerPort: 9000
         

Replace `SERVICE_NAME` with your API's service name.

  3. Start the Kubernetes service by using the [`kubectl create`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create) command:
         
         kubectl create -f deployment.yaml
         




**If you need to configure ESP to use a specific configuration ID** :

  1. In your Deployment manifest file, add the `--version` option and set it to a specific [configuration ID](https://docs.cloud.google.com/endpoints/docs/openapi/get-service-name-config-id).

  2. Either remove `--rollout_strategy=managed` or set `--rollout_strategy` to `fixed`. The `fixed` option configures ESP to use the service configuration that you specified in `--version`.

  3. Start the Kubernetes service: `kubectl create -f deployment.yaml`




If you specify both `--rollout_strategy=managed` and the `--version` option, ESP starts with the configuration that you specified in `--version`, but then it runs in managed mode and obtains the latest configuration.

We recommend that you don't keep ESP configured to use a specific configuration ID for too long because if you deploy an updated service configuration, you have to restart ESP to use the new configuration.

**To remove the specific configuration ID** :

  1. In your Deployment manifest file, remove the `--version` option.

  2. Add `--rollout_strategy=managed`.

  3. Start the Kubernetes service: `kubectl create -f deployment.yaml`




See [ESP startup options](https://docs.cloud.google.com/endpoints/docs/grpc/specify-proxy-startup-options) for the full list of options that you can specify when starting ESP.

## Tracking API activity

After you deploy ESP and your API backend, you can use tools such as `curl` or Postman to send requests to your API. If you don't get a successful response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-response-errors)

After sending some requests, you can:

  * To view the activity graphs for your API, go to **Endpoints** > **Services**. It may take a few moments for the request to be reflected in the graphs.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  * Look at the request logs for your API on the Cloud Logging page.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)




## What's next

  * [Troubleshooting Endpoints on Compute Engine](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gce-deployment)
  * [Troubleshooting Endpoints on GKE](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gke-deployment)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
