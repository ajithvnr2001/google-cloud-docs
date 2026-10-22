---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-curations/
title: Manage curations \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:24.507007+00:00
---

# Manage curations  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-curations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage curations Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to view, and manage custom curations in API hub. For information about creating a custom curation, see [Create custom curations](https://docs.cloud.google.com/apigee/docs/apihub/create-curations). 

## View custom curations

To view the list of custom curations in your project, perform the following steps: 

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Click the **Curations** tab and go to the **Manage curations** section to view the list of curations in your project as shown in the following image: 

![Image showing the custom curation.](https://docs.cloud.google.com/static/apigee/docs/apihub/images/custom-curation.png)![Image showing the custom curation.](https://docs.cloud.google.com/static/apigee/docs/apihub/images/custom-curation.png)




## Edit a custom curation

To edit a custom curation, perform the following steps: 

**Notes:**

  * You can't edit a custom curation if it is associated with a plugin instance. You must first remove the curation from the plugin instance before editing it.
  * Updating the fingerprint of a custom curation may result in duplicate entries in your project. You must manually delete any duplicate entries in such cases.



  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Click the **Curations** tab and go to the **Manage curations** section to view the list of curations in your project.
  4. Click the **Endpoint** URL of the curation that you want to edit. 

You are taken to the integration editor page for the custom curation in Application Integration. 

  5. In the Application Integration editor, make the required changes to your custom curation logic and click **Publish** to publish the updated integration. 

The curation is updated in API hub and the changes are reflected in the **Manage curations** section. 




## Delete a custom curation

To delete a custom curation, perform the following steps: **Note:** You can't delete a custom curation if it is associated with a plugin instance. You must first remove the curation from the plugin instance before deleting it. 

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Click the **Curations** tab and go to the **Manage curations** section to view the list of curations in your project.
  4. For the curation that you want to delete, click more_vert (Curation actions) and then select **Delete**.
  5. In the confirmation dialog, click **Delete** to confirm the deletion of the curation.



## What's next

  * Learn how to [edit the configuration of a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/manage-plugin-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
