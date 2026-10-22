---
url: https://docs.cloud.google.com/cloud-assist/configure-grounding/
title: Configure grounding for Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:30.542901+00:00
---

# Configure grounding for Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/configure-grounding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Configure grounding for Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

[Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview) lets you connect Gemini Cloud Assist to external web sources through Vertex AI, delivering more accurate, up-to-date responses. This document describes how to configure grounding in the Google Cloud console or with an API.

Available grounding types:

  * **[Grounding with Google Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-search) (Recommended)**: Instructs Gemini Cloud Assist to use Google Search for the most comprehensive and up-to-date responses. Note that certain offerings like Data Residency, Access Transparency, and Customer-Managed Encryption Keys (CMEK) are not supported with this option.

  * **[Web Grounding for Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/web-grounding-enterprise)** : Leverages a restricted subset of web content. While this might lead to lower quality responses compared to Grounding with Google Search, it's the preferred option for highly-regulated industries that require strict data residency compliance, such as finance, healthcare, and the public sector.




By default, Gemini Cloud Assist uses Grounding with Google Search to improve the quality of its responses to your prompts. The use of Grounding with Google Search involves special data handling for your prompts and responses, as described in the [Google Cloud Service terms](https://cloud.google.com/terms/service-terms).

## Before you begin

  1. Verify your Google Cloud project is attached to a billing account.

  2. [Verify that Gemini Cloud Assist is set up for your Google Cloud project](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

  3. To get the required permissions for configuring grounding for Gemini Cloud Assist, ask your administrator to [grant](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role) you the [**Gemini for Google Cloud Settings Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.settingsAdmin) (`roles/cloudaicompanion.settingsAdmin`) Identity and Access Management (IAM) role on your project. This predefined role contains the permissions required to manage Gemini Cloud Assist administrator settings.

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

     * `cloudaicompanion.geminiGcpEnablementSettings.create`
     * `cloudaicompanion.geminiGcpEnablementSettings.update`
     * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsCreate`
     * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsUse`
       * If you are using direct API requests, this permission is required specifically for the `TARGET_PROJECT`. 

The following are additional permissions that are required if you are using the Google Cloud console:

     * `cloudaicompanion.instances.queryEffectiveSetting`
     * `cloudaicompanion.instances.queryEffectiveSettingBindings`
     * `cloudaicompanion.geminiGcpEnablementSettings.get`
     * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsGet`
     * `cloudaicompanion.settingBindings.geminiGcpEnablementSettingsUpdate`




You might be able to get these permissions with other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Configure grounding for Gemini Cloud Assist

Select one of the following options:

###  Console 

  1. Open the Google Cloud console.

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. In any page of the Google Cloud console, click spark **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens.

  3. Click **More actions** (more_vert), and then click **Cloud Assist Settings** from the drop-down menu.

The **Manage Gemini Cloud Assist** settings panel opens.

  4. Select the grounding option that you want to use.

  5. Click **Save**.




###  API 

To configure grounding for Gemini Cloud Assist using the API, you create a `geminiGcpEnablementSettings` resource that defines the grounding type, using the [`geminiGcpEnablementSettings.create`](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings/create) method. Then, you apply the setting using the associated [`settingBindings.create`](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings.settingBindings/create) method to bind the setting to a project.

  1. Create the setting and a setting-specific value:

     1. Obtain an [authentication token](https://docs.cloud.google.com/docs/authentication/rest):
            
            TOKEN=$(gcloud auth print-access-token)
            

For more information on authentication, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest).

     2. Run the following command to create the setting:
            
            curl -X POST \
              -H "Authorization: Bearer $TOKEN" \
              -H 'Content-Type: application/json' \
              -d '{
                "webGroundingType": "GROUNDING_TYPE"
                }' \
              "https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT/locations/global/geminiGcpEnablementSettings?geminiGcpEnablementSettingId=GROUNDING_SETTING_ID"
            

Replace the following:

        * `CONTAINER_PROJECT`: The project ID of the project that stores the setting data.
        * `GROUNDING_TYPE`: The grounding type, which is either `GROUNDING_WITH_GOOGLE_SEARCH` or `WEB_GROUNDING_FOR_ENTERPRISE`.
        * `GROUNDING_SETTING_ID`: A unique name to identify this particular setting data, such as `gt1`.

If the command succeeds, it returns a response body that shows the `webGroundingType` set to your selection:
    
    {
      "name": "projects/CONTAINER_PROJECT/locations/global/geminiGcpEnablementSettings/GROUNDING_SETTING_ID",
      "createTime": "2025-01-23T15:22:49.717166932Z",
      "updateTime": "2025-01-23T15:22:49.717166932Z",
      "webGroundingType": "GROUNDING_TYPE"
    }
    

  2. Create the setting binding:
         
         curl -X POST \
             -H "Authorization: Bearer $TOKEN" \
             -H 'Content-Type: application/json' \
             -d '{
               "target": "projects/TARGET_PROJECT",
               "product": "GEMINI_CLOUD_ASSIST"
               }' \
             "https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT/locations/global/geminiGcpEnablementSettings/GROUNDING_SETTING_ID/settingBindings?settingBindingId=GROUNDING_BINDING_ID"
         

Replace the following:

     * `TARGET_PROJECT`: The project ID of the project to which the setting should be applied. Typically, the target project and the container project are the same.
     * `CONTAINER_PROJECT`: The project ID of the project that stores the setting data.
     * `GROUNDING_SETTING_ID`: The `GROUNDING_SETTING_ID` that you specified when you created the setting.
     * `GROUNDING_BINDING_ID`: A unique ID to identify this particular setting binding resource, such as `b1`.

If the command succeeds, it returns the operation metadata in the following format:
    
    {
      "name": "projects/CONTAINER_PROJECT/locations/global/operations/operation-1737646069712-62c6140bb04bb-49261230-43701daf",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.v1.OperationMetadata",
        "createTime": "2025-01-23T15:27:50.076075570Z",
        "target": "projects/TARGET_PROJECT/locations/global/geminiGcpEnablementSettings/GROUNDING_SETTING_ID/settingBindings/GROUNDING_BINDING_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    




## What's next

  * [View other Gemini Cloud Assist administrator settings](https://docs.cloud.google.com/cloud-assist/admin-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
