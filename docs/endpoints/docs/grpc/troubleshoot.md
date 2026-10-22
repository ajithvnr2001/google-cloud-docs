---
url: https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot/
title: Troubleshooting overview \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:15.242445+00:00
---

# Troubleshooting overview  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Troubleshooting overview Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

This page provides general troubleshooting information and provides links to other pages for additional information.

## Errors when deploying the Cloud Endpoints configuration

If you got an error message from the `gcloud endpoints services deploy` command, see [Troubleshooting Endpoints configuration deployment](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-config-deployment) for information on troubleshooting the error.

## Errors when deploying your API backend

The deployment of your API and the Extensible Service Proxy (ESP) to a Google Cloud backend is platform dependent. See the following troubleshooting guides for more information: 

  * [Troubleshooting proxy deployment on Compute Engine](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gce-deployment)

  * [Troubleshooting proxy deployment on GKE](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-gke-deployment)




## Response errors

When you send a request to your API and receive an error response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-response-errors) for information on troubleshooting the error.

## Checking required services

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

## Checking required permissions

The instance running Extensible Service Proxy requires permissions to call [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started) and [ServiceControl](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started).

  * For ESP deployed on Cloud Run, see [Building a new ESPv2 image in Cloud Run tutorial](https://docs.cloud.google.com/endpoints/docs/openapi/set-up-cloud-run-espv2#configure_esp) for details.

  * For ESP deployed on Compute Engine, see [Checking required permissions in Compute Engine tutorial](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-compute-engine-docker#checking_required_permissions) for details.

  * For ESP deployed on GKE, see [Checking required permissions in GKE tutorial](https://docs.cloud.google.com/endpoints/docs/openapi/get-started-kubernetes-engine#checking_required_permissions) for details.




## Checking debug information

Running the Google Cloud CLI with debug verbosity helps with debugging.
    
    
    gcloud --verbosity=debug COMMAND
    

This command makes the Google Cloud CLI print a verbose log of the error. Depending on the command being run, the output can include request and response information from the server.

## Enabling a service

You can check whether a service is enabled using `gcloud`.
    
    
    gcloud services list
    

To display configuration for a particular service, use the following command:
    
    
    gcloud endpoints services describe SERVICE_NAME
    

## Proxy OAuth fails yet requests pass

Make sure there is an `authentication` section that has your OAuth definition in your gRPC API configuration file. An example configuration file is available in the [Bookstore sample on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config_auth.yaml).

## What's next

  * [Monitoring your API](https://docs.cloud.google.com/endpoints/docs/grpc/monitoring-your-api)
  * [Tracing your API](https://docs.cloud.google.com/endpoints/docs/grpc/tracing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
