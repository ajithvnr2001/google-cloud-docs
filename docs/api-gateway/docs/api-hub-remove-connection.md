---
url: https://docs.cloud.google.com/api-gateway/docs/api-hub-remove-connection/
title: Remove an API Gateway connection from API hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:19.975203+00:00
---

# Remove an API Gateway connection from API hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/api-hub-remove-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Remove an API Gateway connection from API hub

This page describes how to remove an API Gateway connection from API hub.

## Overview

To remove an API Gateway connection from API hub, do one of the following:

  * Remove API Gateway assets from API hub without detaching the runtime project
  * Detach the runtime project from API hub

**Important** : When you remove an API Gateway connection from API hub, the API Gateway plugin instance and all ingested data will be deleted from API hub. 

## Remove API Gateway assets from API hub without detaching the runtime project

Remove API Gateway assets from API hub without detaching the runtime project as described below.

### Google Cloud console

To remove API Gateway assets from the runtime project association settings, do the following:

  1. In the Google Cloud console, select your host project. 
  2. Go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  3. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  4. Go to the **Project associations** tab.
  5. Click **Edit settings** associated with the API Gateway project.
  6. In the **Project association settings** pane, deselect **API Gateway Plugin** and any other API assets you want to automatically import. 
  7. Click **Save**.



### REST

To remove API Gateway assets from the runtime project, use the [delete plugin instance](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.plugins.instances/delete) API.

For example:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT_ID/locations/HUB_LOCATION/plugins/PLUGIN_TYPE/instances/PLUGIN_INSTANCE_ID" \
      -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)"
    

Replace the following:

  * HUB_PROJECT_ID: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * PLUGIN_TYPE: Type of plugin. Set to **system-api-gateway**.
  * PLUGIN_INSTANCE_ID: ID of the API Gateway plugin instance. Use the [list plugin instances](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.plugins.instances/list) API to get the plugin instance ID.



If successful, an [Operation](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.operations) JSON object is returned.

## Detach the API Gateway project from API hub

Detach the runtime project from API hub as described below.

### Google Cloud console

To detach the API Gateway project from API hub, do the following:

  1. In the Google Cloud console, select your host project.
  2. Go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  3. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  4. Go to the **Project associations** tab. 
  5. Click **Detach runtime project** associated with the API Gateway project.
  6. Click **Confirm**.



### REST

To detach the runtime project from API hub, use the [delete runtime project attachments](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.runtimeProjectAttachments/delete) API.

For example:
    
    
    curl 'https://apihub.googleapis.com/v1/projects/HUB_PROJECT_ID/locations/HUB_LOCATION/runtimeProjectAttachments/RUNTIME_PROJECT_ID' \
      -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)"
    

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * RUNTIME_PROJECT_ID: ID of the runtime project. Use the [list runtime project attachments](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.runtimeProjectAttachments/list) API to get the runtime project ID.



If successful, an empty JSON object is returned.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
