---
url: https://docs.cloud.google.com/api-gateway/docs/api-hub-connect/
title: Connect API Gateway with API hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:22.066127+00:00
---

# Connect API Gateway with API hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/api-hub-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect API Gateway with API hub

This page describes how to connect API Gateway with Apigee API hub to allow you to view your APIs and centralize your API management.

## Overview

As an API Gateway administrator, to connect API Gateway with API hub you'll need to do the following steps: 

  1. Provision API hub
  2. Attach your API Gateway project to API hub



## Before you begin: Grant roles

Ensure that you have the appropriate Identity and Access Management (IAM) roles to connect API Gateway with API hub. 

In the project where you will provision API hub:

  * Grant roles for provisioning, as described in [Before you begin](https://docs.cloud.google.com/apigee/docs/apihub/provision) in the API hub provisioning steps.



In the API Gateway projects that you will attach to API hub:

  * Grant the [Cloud API hub Runtime Project Attachment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runTimeProjectAttachmentsEditor) (`roles/apihub.runTimeProjectAttachmentsEditor`) role to your principal account.
  * To attach your API Gateway project to API hub using the Google Cloud console, grant the [Browser](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#browser) (`roles/browser`) role to your principal account.



## Provision API hub

Before you can connect API Gateway with API hub, you'll need to provision API hub in your host project. A _host project_ is a Google Cloud project in your Google Cloud organization that you designate as the consumer project for all API hub resources. A single API hub instance can be provisioned per host project. 

To provide centralized discovery of APIs across all of your API Gateways, we recommend using one **dedicated host project** for the API hub instance and attaching multiple API Gateway projects, referred to as _runtime projects_ , to the API hub instance.

If an instance of API hub is already provisioned in your Google Cloud organization or folder, we recommend that you skip this step and attach your API Gateway project to the existing API hub instance.

To provision API hub in your host project, do one of the following:

  * In the Google Cloud console, go to the [API hub](https://console.cloud.google.com/apigee/api-hub) page, select the Google Cloud project to use as the host project, and click **Set up API hub**.

You can access this page from [API Gateway](https://console.cloud.google.com/api-gateway) pages as follows:  


    * Click **Get started** in the API hub banner at the top of any of the API Gateway pages
    * Click **Get started with API hub** at the top of the APIs page

Then follow the detailed provisioning steps described in [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision).

  * Use the [command line](https://docs.cloud.google.com/apigee/docs/apihub/provision-cli) or [Terraform](https://docs.cloud.google.com/apigee/docs/apihub/provision-terraform).


**Note that during provisioning:**

  * You choose the [hosting location](https://docs.cloud.google.com/apigee/docs/apihub/provision#step-hosting) where you want to persist the API Gateway API metadata.
  * You can choose to [encrypt](https://docs.cloud.google.com/apigee/docs/apihub/provision#step-encryption) the data stored in API hub. However, the API Gateway service is automatically [CMEK-compliant](https://docs.cloud.google.com/kms/docs/compatible-services#cmek_compliant).



## Attach your API Gateway project to API hub

Attach your API Gateway project to API hub.

### Google Cloud console

To attach an API Gateway project to API hub, do the following:

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Go to the **Project associations** tab.
  4. If your API Gateway project is not in the list of attached runtime projects, do the following: 
     1. Click **Attach runtime project**.  
This displays the **Select a resource** pane.
     2. Click the Google Cloud project where API Gateway is provisioned.
     3. In the **Project association settings** pane, select **API Gateway** and any other API assets you want to automatically import.
     4. Click **Save**.
  5. If your API Gateway project is already on the list of attached runtime projects, do the following: 
     1. Click **Edit settings** in the row associated with the API Gateway runtime project.
     2. In the **Project association settings** pane, select **API Gateway** and any other API assets you want to automatically import.
     3. Click **Save**.

To enable real-time data ingestion, API hub creates an API Gateway [plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/plugins) for the attached runtime project when you select to import API Gateway assets. You can view this plugin instance in the **Associated plugins** column on the **Project associations** page.

### REST

To attach your API Gateway project to API hub, use the [Create runtime project attachments](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.runtimeProjectAttachments/create) and [Create plugin instance](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.plugins.instances/create) APIs.

For example, to create the runtime project attachment:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT_ID/locations/HUB_LOCATION/runtimeProjectAttachments?runtimeProjectAttachmentId=RUNTIME_PROJECT_ID" \
      -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{"runtimeProject":"projects/RUNTIME_PROJECT_ID"}'
    

Replace the following:

  * HUB_PROJECT_ID: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * RUNTIME_PROJECT_ID: The name of your API Gateway runtime project.



If successful, an [RuntimeProjectAttachment](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.runtimeProjectAttachments#RuntimeProjectAttachment) JSON object is returned.

Then, to create the API Gateway plugin instance:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT_ID/locations/HUB_LOCATION/plugins/PLUGIN_TYPE/instances" \
      -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "displayName": "API Gateway Plugin Instance",
        "sourceProjectId": "RUNTIME_PROJECT_ID",
        "actions": [
          {
            "actionId": "sync-metadata"
          }
        ]
      }'
    

Replace the following:

  * HUB_PROJECT_ID: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * PLUGIN_TYPE: Type of plugin. Set to **system-api-gateway**.
  * RUNTIME_PROJECT_ID: The name of your API Gateway runtime project.



If successful, an [Operation](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.operations) JSON object is returned.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
