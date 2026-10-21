---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-gcp-plugins/
title: Manage Google Cloud plugins \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:27:56.655280+00:00
---

# Manage Google Cloud plugins  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-gcp-plugins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage Google Cloud plugins Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

API hub provides built-in plugins to connect and ingest API data from supported Google Cloud services into API hub. These plugins use an _on-ramp model_ , where you don't need to create any plugins or plugin instances manually in API hub. Instead, you attach a Google Cloud runtime project to your API hub instance, and API hub automatically creates the required plugin instances for all supported services found in that project. 

**Note:** Plugin cards for these plugins are not displayed in the **API hub > Settings > Plugins** page.

## Supported Google Cloud plugins

The following table lists the currently supported Google Cloud plugins, and the ingested API data. 

Plugin | API data ingested  
---|---  
[Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) and [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/what-is-hybrid) | Proxy name, environment, organization, and deployment details.  
[API Gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway) | API Gateway APIs including gateway definitions and managed service endpoints.  
  
## Attach a runtime project to API hub

Attaching a runtime project to API hub establishes a _project association_ between the Google Cloud runtime project and your API hub instance (host project). This association enables API hub to automatically ingest API data from the project and keep them synchronized. 

### Before you begin

### Apigee/Apigee hybrid

To attach an Apigee or Apigee hybrid runtime project to API hub, ensure the following: 

  * Ensure that the data residency status (enabled or disabled) of the attached Apigee runtime project matches the data residency status of the Apigee organization associated with your API hub instance.
  * Grant the [Cloud API hub Runtime Project Attachment Editor (`roles/apihub.runTimeProjectAttachmentsEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runTimeProjectAttachmentsEditor) IAM role to your principal account.
  * Ensure that the API proxy is deployed to an environment in the Apigee runtime project.
  * Ensure that the OpenAPI specification is included as a resource in the API proxy.



### API Gateway

To attach an API Gateway runtime project to API hub, ensure the following: 

  * Ensure that the APIs are active and deployed in the API Gateway runtime project.
  * Grant the [Cloud API hub Runtime Project Attachment Editor (`roles/apihub.runTimeProjectAttachmentsEditor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runTimeProjectAttachmentsEditor) IAM role to your principal account.
  * Grant the [Browser](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#browser) (`roles/browser`) role to your principal account.



### Console

To attach an runtime project to API hub, do the following steps:

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Go to the **Project associations** tab and click **Attach runtime project**. This displays the **Select a resource** pane.
  4. Click the Google Cloud project where your runtime is provisioned. 
  5. In the **Project association settings** pane, do the following: 
     * To ingest Apigee or Apigee hybrid API data, select **Apigee X and Hybrid**.
     * To ingest Application Integration API data, select **Application Integration**.
     * To ingest API Gateway API data, select **API Gateway**.
     * To attach the runtime project to API hub without importing assets, clear all of the **Assets to automatically import** checkboxes.
  6. Click **Attach**. **Note:** API hub automatically creates a plugin instance for the associated runtime project if you choose to import assets. This plugin instance is displayed in the **Associated plugins** column on the **Project associations** page.



### REST

To attach a runtime project to API hub, use the [`create`](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.runtimeProjectAttachments/create) method.
    
    
    curl -X POST   
    -H "Authorization: Bearer $(gcloud auth print-access-token)"   
    -H "Content-Type: application/json"
      -d '{
        "runtime_project": "RUNTIME_PROJECT_ID"
      }'   "https://apihub.googleapis.com/v1/projects/HUB_PROJECT_ID/locations/LOCATION/runtimeProjectAttachments?runtime_project_attachment_id=RUNTIME_PROJECT_ID"

Replace the following:

  * HUB_PROJECT_ID: The project ID of your API hub host project.
  * LOCATION: The location of your API hub host project.
  * RUNTIME_PROJECT_ID: The Google Cloud project name or ID that you want to attach to API hub.



## Edit project association settings

You can edit the project association settings to update the API assets that are ingested into API hub.

### Console

To edit the project association settings, do the following steps:

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Go to the **Project associations** tab to view the list of attached projects.
  4. Click **Edit settings** for the desired project. 
  5. In the **Project association settings** pane, edit the **API assets to automatically import** checkbox selection.
  6. Click **Save** to apply your changes.



## Detach a runtime project from API hub

**Warning:** Detaching a runtime project from API hub also deletes all the associated plugin instances and registered APIs from API hub.

### Console

To detach a runtime project from API hub, do the following steps:

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Go to the **Project associations** tab to view the list of attached projects.
  4. Click **Detach project** for the project you want to detach. 

**Note:** Even though all the APIs of the detached project are removed from API hub, the attributes that were created for those APIs aren't deleted, and will still show up in API hub.

### REST

To detach a runtime project from API hub, use the [`delete`](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.runtimeProjectAttachments/delete) method.
    
    
    curl -X DELETE   -H "Authorization: Bearer $(gcloud auth print-access-token)"
    "https://apihub.googleapis.com/v1/projects/HUB_PROJECT_ID/locations/LOCATION/runtimeProjectAttachments/RUNTIME_PROJECT_ID"

Replace the following:

  * HUB_PROJECT_ID: The project ID of your API hub host project.
  * LOCATION: The location of your API hub host project.
  * RUNTIME_PROJECT_ID: The Google Cloud project name or ID that you want to detach from API hub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
