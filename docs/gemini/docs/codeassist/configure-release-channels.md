---
url: https://docs.cloud.google.com/gemini/docs/codeassist/configure-release-channels/
title: Configure Gemini Code Assist release channels \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:47.531547+00:00
---

# Configure Gemini Code Assist release channels  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/configure-release-channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Configure Gemini Code Assist release channels Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Gemini Code Assist release channels for a project by using the Google Cloud console or an API.

We release Gemini Code Assist features in different release channels. You can set each Google Cloud project to a single release channel depending on your chosen balance between feature availability and stability. Users in your organization who use Gemini Code Assist in their local IDE can use features and models based on the release channel configured for the project.

The following release channels are available:

  * **Generally Available.** The default release channel. Lets you use generally available models and features. Note that it is possible to access certain preview features without opting into the Preview channel, using alternative mechanisms of Preview sign-up. These features will be accessible within the GA channel, but are still covered under Pre-GA Offering Terms.

  * **Preview.** Lets you access certain preview features for Gemini Code Assist.

When you enable the Preview release channel on a project, you agree on behalf of the customer that **all** usage of Gemini Code Assist in that project is subject to the Pre-GA Offering Terms of the [Google Cloud Platform Specific Service Terms](https://cloud.google.com/terms/service-terms). Don't use this channel for projects and resources that aren't suitable for use with pre-GA offerings.




The following sections provide steps required to set or change your Gemini Code Assist release channel.

## Before you begin

  * Verify that your Google Cloud project is attached to a billing account. For more information, see [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#billing_project_linkage).



### Required roles

For the required permissions to create settings and bindings that control the release channel, ask your administrator to grant you the Gemini for Google Cloud Settings Admin (`roles/cloudaicompanion.settingsAdmin`) role on the project.

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `cloudaicompanion.releaseChannelSettings.create`
  * `cloudaicompanion.releaseChannelSettings.delete`
  * `cloudaicompanion.releaseChannelSettings.get`
  * `cloudaicompanion.releaseChannelSettings.list`
  * `cloudaicompanion.releaseChannelSettings.update`
  * `cloudaicompanion.dataSharingWithGoogleSettings.create`
  * Configure release channels using an API:
    * `cloudaicompanion.settingBindings.releaseChannelSettingsCreate`
    * `cloudaicompanion.settingBindings.releaseChannelSettingsDelete`
    * `cloudaicompanion.settingBindings.releaseChannelSettingsGet`
    * `cloudaicompanion.settingBindings.releaseChannelSettingsList`
    * `cloudaicompanion.settingBindings.releaseChannelSettingsUpdate`
    * `cloudaicompanion.settingBindings.releaseChannelSettingsUse`
  * Configure prompt and response sharing using an API:
    * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsCreate`
    * `cloudaicompanion.settingBindings.dataSharingWithGoogleSettingsUse`
  * View Gemini Code Assist administrator settings:
    * `cloudaicompanion.instances.queryEffectiveSetting`
    * `cloudaicompanion.instances.queryEffectiveSettingBindings`



## Configure Gemini Code Assist release channels

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Admin for Gemini** page.

[Go to Admin for Gemini](https://console.cloud.google.com/gemini-admin)

  2. Click **Settings** in the navigation menu.

  3. In the **Release channels for Gemini Code Assist in local IDEs** section, select the release channel that best suits your needs:

###  Preview 

     1. Select **Preview**.
     2. Review the Preview release channel details and Trusted Tester program terms, and then click **Save changes**.

###  Generally Available 

     1. Select **GA**.
     2. Click **Save changes**.




###  API 

  1. Create the release channel setting and a setting-specific value:

     1. Obtain an [authentication token](https://docs.cloud.google.com/docs/authentication/rest). You must be authenticated using gcloud CLI authentication to obtain it:
            
            TOKEN=$(gcloud auth print-access-token)
            

     2. Create the setting. These instructions use [`cURL`](http://curl.haxx.se/) to call API methods:
            
            curl -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' -d '{
                  "release_channel": "RELEASE_CHANNEL",
                } ' -X POST "https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT_NAME/locations/global/releaseChannelSettings?release_channel_setting_id=RC_SETTING_ID"
            

Replace the following:

        * `RELEASE_CHANNEL`: the release channel, either `EXPERIMENTAL` for Preview or `STABLE` for Generally Available.
        * `CONTAINER_PROJECT_NAME`: the project ID of the project where the binding resource is stored. This is the parent project of the binding.
        * `RC_SETTING_ID`: a unique setting name—for example, `rc1` for `Release Channel`.

The output shows the `releaseChannel` set to `RELEASE_CHANNEL`:
    
    {
      "name": "projects/CONTAINER_PROJECT_NAME
    /locations/global/releaseChannelSettings/RC_SETTING_ID",
      "createTime": "2025-01-23T15:22:49.717166932Z",
      "updateTime": "2025-01-23T15:22:49.717166932Z",
      "releaseChannel": RELEASE_CHANNEL
    }
    

     3. Create the release channel setting binding:
            
            curl \
              -H "Authorization: Bearer $TOKEN" \
              -H 'Content-Type: application/json' \
              -d '{
                  "target": "projects/TARGET_PROJECT_NAME",
                  "product": "GEMINI_CODE_ASSIST"
                }' \
              -X POST "https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT_NAME/locations/global/releaseChannelSettings/RC_SETTING_ID/settingBindings?setting_binding_id=RC_BINDING_ID"
            

Replace the following:

        * `TARGET_PROJECT_NAME`: the target project to which the binding should be bound. This is often the same as the container project. However, you can bind a setting to multiple projects so that the setting resource doesn't have to be duplicated.
        * `CONTAINER_PROJECT_NAME`: the project ID of the project where the binding resource is stored. This is the parent project of the binding.
        * `RC_SETTING_ID`: the same `RC_SETTING_ID` that you used when you created the setting, but appended with `b1`. For example, use `rc1b1` for `Release Channel`.
        * `RC_BINDING_ID`: a unique name for the settings binding—for example, `rc_binding`.

The output includes the operation metadata in the following format:
    
    {
      "name": "projects/CONTAINER_PROJECT_NAME/locations/global/operations/operation-RC_BINDING_OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.cloudaicompanion.v1.OperationMetadata",
        "createTime": "2025-01-23T15:27:50.076075570Z",
        "target": "projects/TARGET_PROJECT_NAME/locations/global/releaseChannelSettings/RC_SETTING_ID/settingBindings/RC_BINDING_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

     4. Optional: Check the status of the release channel setting binding creation:
            
            curl -H "Authorization: Bearer $TOKEN" \
            https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT_NAME/locations/global/operations/operation-RC_BINDING_OPERATION_ID
            

Replace the following:

        * `CONTAINER_PROJECT_NAME`: the project ID of the project where the binding resource is stored. This is the parent project of the binding.
        * `RC_BINDING_OPERATION_ID`: the release channel setting binding creation operation ID provided in the response in the previous step.
  2. Optional: Create the prompt and response sharing setting and a setting-specific value:

     1. Obtain the token:
            
            TOKEN=$(gcloud auth print-access-token)
            

     2. Create the setting:
            
            curl -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' -d '{
                "enable_preview_data_sharing": true,
              } ' -X POST "https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT_NAME/locations/global/dataSharingWithGoogleSettings?data_sharing_with_google_setting_id=DSWG_SETTING_ID"
            

Replace the following:

        * `CONTAINER_PROJECT_NAME`: the parent project ID
        * `DSWG_SETTING_ID`: a unique setting name—for example, `dswg1` for `Data Sharing with Google`

The output shows the `enablePreviewDataSharing` set to `true`:
    
    {
      "name": "projects/CONTAINER_PROJECT_NAME
    /locations/global/dataSharingWithGoogleSettings/DSWG_SETTING_ID",
      "createTime": "2025-01-23T15:22:49.717166932Z",
      "updateTime": "2025-01-23T15:22:49.717166932Z",
      "enablePreviewDataSharing": true
    }
    

     3. Create the prompt and response setting binding:
            
            curl \
              -H "Authorization: Bearer $TOKEN" \
              -H 'Content-Type: application/json' \
              -d '{
                  "target": "projects/TARGET_PROJECT_NAME",
                  "product": "GEMINI_CODE_ASSIST"
                }' \
              -X POST "https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT_NAME/locations/global/dataSharingWithGoogleSettings/DSWG_SETTING_ID/settingBindings?setting_binding_id=DSWG_BINDING_ID"
            

Replace the following:

        * `TARGET_PROJECT_NAME`: the target project to which the setting should be applied.
        * `CONTAINER_PROJECT_NAME`: the parent project ID.
        * `DSWG_SETTING_ID`: the same `DSWG_SETTING_ID` that you used when you created the setting, but appended with `b1`. For example, use `dswg1b1` for `Data Sharing with Google`.
        * `DSWG_BINDING_ID`: a unique name for the settings binding—for example, `dswg_binding`.

The output includes the operation metadata in the following format:
    
    {
    "name": "projects/CONTAINER_PROJECT_NAME/locations/global/operations/operation-DSWG_BINDING_OPERATION_ID",
    "metadata": {
      "@type": "type.googleapis.com/google.cloud.cloudaicompanion.v1.OperationMetadata",
      "createTime": "2025-01-23T15:27:50.076075570Z",
      "target": "projects/TARGET_PROJECT_NAME/locations/global/dataSharingWithGoogleSettings/DSWG_SETTING_ID/settingBindings/DSWG_BINDING_ID",
      "verb": "create",
      "requestedCancellation": false,
      "apiVersion": "v1"
    },
    "done": false
    }
    

     4. Optional: Check the status of the prompt and response setting binding creation:
            
            curl -H "Authorization: Bearer $TOKEN" \
            https://cloudaicompanion.googleapis.com/v1/projects/CONTAINER_PROJECT_NAME/locations/global/operations/operation-DSWG_BINDING_OPERATION_ID
            

Replace the following:

        * `CONTAINER_PROJECT_NAME`: the project ID of the project where the binding resource is stored. This is the parent project of the binding.
        * `DSWG_BINDING_OPERATION_ID`: the prompt and response setting binding creation operation ID provided in the response in the previous step.



## What's next

  * Learn about [Gemini Code Assist pricing](https://cloud.google.com/products/gemini/pricing).
  * [View other Gemini Code Assist administrator settings](https://docs.cloud.google.com/gemini/docs/admin-settings-console).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
