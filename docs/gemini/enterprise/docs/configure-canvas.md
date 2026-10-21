---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-canvas/
title: Configure Canvas \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:58:24.963947+00:00
---

# Configure Canvas  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-canvas/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure Canvas Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how administrators can set up and configure Canvas in Gemini Enterprise for their users.

Canvas is generally available in the global, US, and EU regions. It is available for users of Gemini Enterprise Business edition, Standard and Plus editions.

## Before you begin

Canvas is disabled by default. You can review and test Canvas before you choose to enable it for users.

To enable Canvas for your users, complete the following setup:

  * Turn on the feature toggle
  * Add Canvas permissions to a custom IAM role



### Turn on Canvas on the Gemini Enterprise app

For users to access the Canvas feature, a Gemini Enterprise administrator must turn on the **Enable canvas** toggle in the web app feature management settings. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

### Add Canvas permissions to a custom IAM role

Ensure users have the required permissions for Canvas:

  * **Predefined roles** : Users accessing Gemini Enterprise with standard roles like `roles/discoveryengine.user` don't need to make any changes, as the necessary permissions are included in the predefined roles.

  * **Custom roles** : For users accessing Gemini Enterprise using custom IAM roles, you must add the `immersiveArtifacts` permissions to the custom role. Without these permissions, users can't use Canvas. Canvas requires the following permissions:

    * `discoveryengine.immersiveArtifacts.create`
    * `discoveryengine.immersiveArtifacts.delete`
    * `discoveryengine.immersiveArtifacts.export`
    * `discoveryengine.immersiveArtifacts.get`
    * `discoveryengine.immersiveArtifacts.list`
    * `discoveryengine.immersiveArtifacts.navigate`
    * `discoveryengine.immersiveArtifacts.update`

Because the permissions required for Canvas are in preview, you can't add them using the Google Cloud console. Instead, use the gcloud CLI. For example, to add these permissions to an existing project-level custom role, run the following command:
    
    gcloud iam roles update ROLE_ID \
      --project=PROJECT_ID \
      --add-permissions=discoveryengine.immersiveArtifacts.create,discoveryengine.immersiveArtifacts.delete,discoveryengine.immersiveArtifacts.export,discoveryengine.immersiveArtifacts.get,discoveryengine.immersiveArtifacts.list,discoveryengine.immersiveArtifacts.navigate,discoveryengine.immersiveArtifacts.update
    

**Note:** Because these permissions are in preview, you see an expected warning from gcloud CLI stating that these permissions are in the `alpha` launch stage and might be unstable for use in custom roles. This warning is expected and doesn't prevent the permissions from being applied.

For more information about managing Gemini Enterprise IAM roles, see [Access control with IAM](https://docs.cloud.google.com/gemini/enterprise/docs/access-control).




## Limitations

Canvas isn't supported on the mobile app. It is only available on the web app.

## Quota consumption

Canvas queries and regular Gemini Enterprise app chat queries are counted in the same way and share the same quota.

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

  * Your project reached its monthly spend cap.
  * Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 



This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
