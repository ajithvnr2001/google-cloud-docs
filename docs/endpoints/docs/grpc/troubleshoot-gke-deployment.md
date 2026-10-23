---
url: https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gke-deployment/
title: Troubleshooting Cloud Endpoints in GKE \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:36.108439+00:00
---

# Troubleshooting Cloud Endpoints in GKE  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gke-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Troubleshooting Cloud Endpoints in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gke-deployment "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This document presents troubleshooting techniques for Endpoints deployments on Google Kubernetes Engine (GKE) and Kubernetes.

## Failed in `kubectl create -f gke.yaml`

If you see the `Failed in kubectl create -f gke.yaml` error message, take the following steps:

  1. Authorize `gcloud`:
         
         gcloud auth login
         gcloud auth application-default login
         

  2. Create a cluster. You can either use the following `gcloud`command, or create a cluster using [Google Cloud console](https://console.cloud.google.com/kubernetes).
         
         gcloud container clusters create CLUSTER_NAME
         

Replace `CLUSTER_NAME` with your cluster's name.

  3. Get credentials for your cluster and make them available to `kubectl`:
         
         gcloud container clusters get-credentials CLUSTER_NAME
         




## Endpoints metrics and logs aren't displayed

If you can successfully send requests to your API, but you don't see any metrics or logs on the **Endpoints** > **Services** page in the Google Cloud console, take the following steps:

  1. Check all the [required services](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-engine#checking_required_services) are enabled.
  2. Check all the [required permissions](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-engine#checking_required_permissions) are granted.



## Accessing logs from Extensible Service Proxy

If you need to access the Extensible Service Proxy (ESP) logs to diagnose problems, use `kubectl` as follows:

  1. Get the name of the pod:
         
         kubectl get pod
         
         NAME                       READY     STATUS    RESTARTS   AGE
         esp-echo-174578890-x09gl   2/2       Running   2          21s
         

The pod name is `esp-echo-174578890-x09gl` and it has two containers: `esp` and `echo`.

  2. To view the logs in a pod use `kubectl logs`:
         
         kubectl logs POD_NAME -c CONTAINER_NAME
         

Where `POD_NAME` and `CONTAINER_NAME` are returned from the `kubectl get pod` command, in the previous step. For example:
         
         kubectl logs esp-echo-174578890-x09gl -c esp
         




## Verifying the service name

If you see the error message `Fetching service config failed`, verify that the service name that you specified in the `--service` field in your Deployment manifest file (referred to as the `deployment.yaml` file) matches the host name in the `name` property specified in your gRPC API configuration YAML file (referred to as the `api_config.yaml` file). 

**If the incorrect name is in the`deployment.yaml` file**:

  1. Open the `deployment.yaml` file and go to the section configured for the ESP container. For example:
         
         containers:
         - name: esp
           image: gcr.io/endpoints-release/endpoints-runtime:1
           args: [
             "--http_port=8081",
             "--backend=127.0.0.1:8080",
             "--service=SERVICE_NAME",
             "--rollout_strategy=managed"
           ]
           

Change `SERVICE_NAME` so that it matches the host name specified in the `name` property in the `api_config.yaml` file and save the `deployment.yaml` file.

  2. Start the Kubernetes service:
         
         kubectl create -f deployment.yaml
         




**If the incorrect name is in the`api_config.yaml` file**:

  1. [Get the service name](https://docs.cloud.google.com/endpoints/docs/grpc/get-service-name-config-id) that Endpoints was configured to use.

  2. Delete the service:
         
         gcloud endpoints services delete SERVICE_NAME
         

Replace `SERVICE_NAME` with the name from the previous step. It takes 30 days for the service to be deleted from Google Cloud. You aren't able to reuse the service name during this time.

  3. Open the `api_config.yaml` file and correct the host name in the `name` property and save the file.

  4. Deploy the updated service configuration:
         
         gcloud endpoints services deploy api_descriptor.pb api_config.yaml api_config_http.yaml
         

Wait for the service configuration to be successfully deployed.

  5. Start the Kubernetes service:
         
         kubectl create -f deployment.yaml
         




## Checking configuration files

  1. Use `ssh` to connect to the pod using `kubectl`:
         
         kubectl exec -ti -c CONTAINER_NAME POD_NAME bash
         

Replace `CONTAINER_NAME` with the name of your container and POD_NAME with the name of your pod.

  2. In the `etc/nginx/endpoints/` directory, check the following configuration files for errors:

     * `nginx.conf`\- The `nginx` config file with ESP directives
     * `service.jso` \- The service configuration file



## Accessing the Endpoints status page

If you set `rollout_strategy` to `managed` when you started ESP, and you need to find out the configuration ID that an instance of ESP is using, the Endpoints status page has the information.

To access the Endpoints status page:

  1. Use `ssh` to connect to the pod using `kubectl`:
         
         kubectl exec -ti -c CONTAINER_NAME POD_NAME bash
         

Replace `CONTAINER_NAME` with the name of your container and `POD_NAME` with the name of your pod.

  2. Install [`curl`](https://curl.haxx.se/download.html).

  3. Enter the following:
         
         curl http://localhost:8090/endpoints_status
         

It displays something similar the following:
         
         "serviceConfigRollouts": {
             "rolloutId": "2017-08-09r27",
             "percentages": {
                  "2017-08-09r26": "100"
             }
         }
         




The value in the `rolloutId` is the service configuration ID that ESP is using. To make sure that ESP is using the same configuration as Endpoints, see [Getting the service name and configuration ID](https://docs.cloud.google.com/endpoints/docs/grpc/get-service-name-config-id).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
