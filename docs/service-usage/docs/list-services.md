---
url: https://docs.cloud.google.com/service-usage/docs/list-services/
title: List services \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:36.140128+00:00
---

# List services  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/list-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Guides ](https://docs.cloud.google.com/service-usage/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# List services

This document describes how to list the APIs and services that are enabled or available in a Google Cloud project, folder, or organization. The list of available or enabled APIs and services can contain both public [Google Cloud services](https://cloud.google.com/terms/services), such as [Pub/Sub](https://docs.cloud.google.com/pubsub), as well as any APIs and services shared privately with you, such as services created using [Cloud Endpoints](https://docs.cloud.google.com/endpoints). For more information on the differences between public and private APIs and services, see [Public and private services](https://docs.cloud.google.com/service-usage/docs/public-vs-private).

To program against the Service Usage API, you can also use one of the [Service Usage client libraries](https://docs.cloud.google.com/service-usage/docs/libraries).

## Before you begin

To list the enabled and available APIs and services, you need:

  * A Google Cloud project. To learn how to create a Google Cloud project, see [Create projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * The correct [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) permissions. To learn about the IAM requirements for Service Usage, see [Access control with IAM](https://docs.cloud.google.com/service-usage/docs/access-control).
  * If you plan to use the Google Cloud CLI or REST API instructions on this page, you also need to [install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).



## List enabled services in an organization or folder

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To list the enabled services in an organization or folder, complete the following steps:

###  gcloud 

To list the enabled APIs and services for an organization or folder, use the [`gcloud beta services list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/list) command:
    
    
    gcloud beta services list RESOURCE_TYPE=RESOURCE_ID
    

Replace the following:

  * `RESOURCE_TYPE`: use `--organization` or `--folder` to list the enabled services for an organization or folder, respectively.

  * `RESOURCE_ID`: enter the ID of the organization or folder that you want to list enabled services for.




### REST API

To list enabled services for an organization or folder, call the [`consumerPolicies.get`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/consumerPolicies/get) method:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://serviceusage.googleapis.com/v2beta/RESOURCE_TYPE/RESOURCE_ID/consumerPolicies/default?filter=state:ENABLED"
    

Replace the following:

  * `RESOURCE_TYPE`: use `organizations` or `folders` to list the enabled services for an organization or folder, respectively.

  * `RESOURCE_ID`: enter the ID of the organization or folder that you want to list enabled services for.




If successful, the response body contains a [`ConsumerPolicy`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/consumerPolicies#ConsumerPolicy), which contains a list of enabled APIs:
    
    
    {
      "name": "organizations/organization-name/consumerPolicies/default",
      ...
      "enableRules": [
        {
        "services": [
          "services/apphub.googleapis.com",
          "services/appoptimize.googleapis.com",
          "services/artifactregistry.googleapis.com",
          ...
          ]
        }
      ]
    }
    

**Note:** To list which services are enabled across an organization, you can alternatively [use Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/listing-assets). Using Cloud Asset Inventory is useful if you want to [export a listing to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/export-bigquery) in a single RPC call or if you want to [monitor for state changes](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes).

## List enabled services in a project

To list the enabled services in a project, complete the following steps:

### Console

To list the enabled APIs and services in a project:

  1. In the Google Cloud console, go to the **APIs & Services** page.

[Go to APIs & Services](https://console.cloud.google.com/project/_/apis/dashboard)

  2. Select the Google Cloud project by doing one of the following:

     * Select a recent project from the available list.

     * Click **Select project** , find your project, and click the name of the project.

The **APIs & Services** page opens, listing the APIs enabled in your Google Cloud project.




###  gcloud 

To list the enabled APIs and services in your current project, use the [`gcloud services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command:
    
    
    gcloud services list
    

The output is similar to the following:
    
    
    NAME: analyticshub.googleapis.com
    TITLE: Analytics Hub API
    
    NAME: appoptimize.googleapis.com
    TITLE: App Optimize API
    
    NAME: artifactregistry.googleapis.com
    TITLE: Artifact Registry API
    
    NAME: bigquery.googleapis.com
    TITLE: BigQuery API
    ...
    

### REST API

To list enabled services for your project, call the [`services.list`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/list) method with the `state:ENABLED` filter:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://serviceusage.googleapis.com/v1/projects/PROJECT_ID/services?filter=state:ENABLED"
    

Replace `PROJECT_ID` with your Google Cloud project ID or number.

## List available services in a project

**Caution:** The list of available services is substantially larger than the list of enabled services. If applicable, use the previous instructions to list only enabled services in a project. Listing all services might take as long as 30 seconds due to the amount of data returned. We recommend that you save the list of all available services, as changes to this list are infrequent.

To list the available services in a project, complete the following steps. The set of available services rarely changes and can be cached for extended periods of time.

### Console

To list the APIs and services available to you in a project:

  1. In the Google Cloud console, go to the **API Library** page.

[Go to API Library](https://console.cloud.google.com/project/_/apis/library)

  2. Select the Google Cloud project by doing one of the following:

     * Select a recent project from the available list.

     * Click **Select project** , find your project, and click the name of the project.

The **API Library** page opens. You can search for or browse through available APIs.




###  gcloud 

To list the APIs and services available to you in your current project, use the [`gcloud services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command with the `--available` flag:
    
    
    gcloud services list --available
    

The results include any services that have already been enabled, as well as services that are available to be enabled for the current project. The output is similar to the following:
    
    
    NAME: places-backend.googleapis.com
    TITLE: Google Places API Web Service
    
    NAME: clouderrorreporting.googleapis.com
    TITLE: Stackdriver Error Reporting API
    
    NAME: analyticsreporting.googleapis.com
    TITLE: Google Analytics Reporting API
    
    NAME: youtube.googleapis.com
    TITLE: YouTube Data API v3
    ...
    

### REST API

To list available services for your project, call the [`services.list`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/list) method:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://serviceusage.googleapis.com/v1/projects/PROJECT_ID/services"
    

Replace `PROJECT_ID` with your Google Cloud project ID or number.

The result includes all public services, all services for which the calling user has the `servicemanagement.services.bind` permission, and all services that have already been enabled on the project.

You can filter the results to exclude the services that are enabled on the project by including the query parameter `?filter=state:DISABLED` as part of the request.

## What's next

  * [Enable and disable services](https://docs.cloud.google.com/service-usage/docs/enable-disable) in your Google Cloud project.

  * [Review quotas and system limits](https://docs.cloud.google.com/service-usage/docs/quotas).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
