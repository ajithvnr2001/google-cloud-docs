---
url: https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gce-deployment/
title: Troubleshooting Cloud Endpoints on Compute Engine \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:49.634799+00:00
---

# Troubleshooting Cloud Endpoints on Compute Engine  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gce-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Troubleshooting Cloud Endpoints on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-gce-deployment "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This page presents troubleshooting techniques when the Extensible Service Proxy (ESP) is deployed on a Compute Engine virtual machine (VM).

## Viewing logs on the VM instance

You can troubleshoot problems by looking at the Endpoints Runtime log on the VM instance.

To view the log:

  1. Use `ssh` to connect to your virtual machine:
         
         gcloud config set project YOUR_PROJECT_ID
         
         gcloud compute ssh INSTANCE_NAME
         

Replace `YOUR_PROJECT_ID` and `INSTANCE_NAME` with your Google Cloud project ID and virtual machine instance name, respectively.

  2. View the `nginx` error log:

If you are running endpoints-runtime on a raw VM:
         
         tail -f /var/log/nginx/error.log
         

If you are running `endpoints-runtime` within Docker:
         
         docker ps
         
         docker logs CONTAINER_NAME
         

Replace `CONTAINER_NAME` with the name of your container.




## Displaying ESP status

To display ESP status:

  1. Use `ssh` to connect to your your virtual machine:
         
         gcloud config set project YOUR_PROJECT_ID
         
         gcloud compute ssh INSTANCE_NAME
         

Replace `YOUR_PROJECT_ID` and `INSTANCE_NAME` with your Google Cloud project ID and virtual machine instance name, respectively.

  2. Retrieve the name of the ESP container (typically the container name is `esp`):
         
         docker ps
         

  3. Get a bash shell in the container:
         
         docker exec -it ESP_CONTAINER_NAME /bin/bash
         

Replace `ESP_CONTAINER_NAME` with the name of the ESP container from the previous step.

  4. Install [`curl`](https://curl.haxx.se/download.html).

  5. Enter the following:
         
         curl http://localhost:8090/endpoints_status
         




### Getting the service configuration ID

If you set `rollout_strategy` to `managed` when you started ESP, and you need to find the configuration ID that an instance of ESP is using, near the end of the output from the `curl http://localhost:8090/endpoints_status` command, the output is similar to the following:
    
    
          "serviceConfigRollouts": {
              "rolloutId": "2017-08-09r27",
              "percentages": {
                   "2017-08-09r26": "100"
              }
          }
    

The value in the `rolloutId` is the service configuration ID that ESP is using. This configuration ID should match the latest deployed configuration. You can view the deployment history on the **Endpoints** > **Services** page in the Google Cloud console and view changes made to the service configuration. See [Comparing configuration files](https://docs.cloud.google.com/endpoints/docs/grpc/config-file-compare).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
