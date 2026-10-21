---
url: https://docs.cloud.google.com/service-infrastructure/docs/manage-services/
title: Managing Service Lifecycles \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:31.476334+00:00
---

# Managing Service Lifecycles  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/manage-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Managing Service Lifecycles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage the lifecycles of [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) using the Google Cloud CLI [`gcloud endpoints services`](https://cloud.google.com/sdk/gcloud/reference/endpoints/services) commands.

For advanced use cases, you can use the Service Management API to manage services programmatically. For more information, see [Getting Started with the Service Management API](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started)

## Introduction

A [managed service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services) is a simple resource that logically represents a service integrated with Service Infrastructure, such as Gmail API and Spanner API. A managed service itself has only two immutable properties, a _service name_ and a _producer project_ , but the implementation of a managed service can provide a wide range of functionality. For example, [Cloud Storage API](https://docs.cloud.google.com/storage/docs) provides planet-scale object storage for millions of developers and enterprises.

A managed service has a set of [service consumers](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.consumers), a history of immutable [service configurations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs), and a history of immutable [service rollouts](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts). The service configurations referenced by the latest service rollout represents the current state of the service, which covers all aspects of the service, from the display name to metrics definitions to rate limits. For the specification, see [`google.api.Service`](https://github.com/googleapis/googleapis/blob/master/google/api/service.proto#L73).

We will describe how to create and manage your service lifecycles in this page. For more information about the service management, see [How-to Guides](https://docs.cloud.google.com/service-infrastructure/docs/how-to).

## Creating a service

To create a service, you need to complete the following steps.

  1. Install and initialize [gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize) on your computer.

  2. Create a dedicated producer project to host your service. A dedicated project provides the best security and isolation for your service. It also allows you to transfer the ownership of your service to another team or even another company.

  3. Enable the Service Management API and Service Control API for your project.

  4. Enable Cloud Billing for your project. To integrate your service with Service Infrastructure, you will depend on several paid Google Cloud products, including the Service Control API, Cloud Logging API, and Cloud Monitoring API.

  5. Prepare a simple service configuration yaml file for your service as follows:
         
         # Filename: endpointsapis.yaml
         type: google.api.Service
         config_version: 3
         # Update the next line to use your own service name.
         name: endpointsapis.appspot.com
         # Update the next line to use your own producer project id.
         producer_project_id: endpointsapis
         

  6. Run `gcloud` command to create your service by deploying a blank service configuration:
         
         gcloud endpoints services deploy endpointsapis.yaml
         




The service creation process takes about a minute. After that, you should be able to see your service listed on the [Endpoints](https://console.cloud.google.com/endpoints?project=_) page in the Google Cloud console.

## Listing services

To list services in a project, you can use the following command:
    
    
    gcloud endpoints services list --project endpointsapis
    

## Describing a service

To describe a service and its configuration, you can use the following command:
    
    
    gcloud endpoints services describe endpointsapis.appspot.com
    

## Deleting a service

If you no longer need a service, you can delete it using the following command:
    
    
    gcloud endpoints services delete endpointsapis.appspot.com
    

NOTE: Every service has a mandatory 30-day deletion retention.

## Undeleting a service

You can undelete a service within its retention window using the following command:
    
    
    gcloud endpoints services undelete endpointsapis.appspot.com
    

## Next steps

The Service Management API uses a declarative model for service management. After the service is created, you need to push immutable service configurations and service rollouts to reach the desired state of your service. Your service configurations are used to configure Google Cloud infrastructure services to support your service, including Cloud Billing, Cloud Logging, Cloud Monitoring, and Identity and Access Management.

For more information about service configurations, see [Managing Service Configurations](https://docs.cloud.google.com/service-infrastructure/docs/manage-config). For more information about service rollouts, see [Managing Service Rollouts](https://docs.cloud.google.com/service-infrastructure/docs/rollout).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
