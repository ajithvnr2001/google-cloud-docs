---
url: https://docs.cloud.google.com/application-integration/docs/clone-integrations/
title: Clone integrations \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:18.401887+00:00
---

# Clone integrations  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/clone-integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Clone integrations

Cloning an integration creates a full copy of its original integration version. You can use cloning to create a new integration version within the same integration, or to create a completely new independent integration that is a full copy of the original integration version. 

## Clone within the same integration

To clone of an integration version within the same integration, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select the existing integration that you want to clone. 
  4. Click the **Versions** dropdown and select the version you want to clone.
  5. In the designer toolbar, click  more_vert  (Actions menu) and select **Clone integration**.
  6. Select **Create new version**. 

The **Create new version** pane appears.

  7. (Optional) Enter a name for the new clone version.
  8. Click **OK**.

A new clone of the integration version is created in the same integration.




## Clone as a new integration

To create a new independent integration that is a full copy of the original integration version, perform the following steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select an existing integration that you want to clone. 
  4. Click the **Versions** dropdown and select the version you want to clone.
  5. In the designer toolbar, click  more_vert  (Actions menu) and select **Clone integration**.
  6. Select **Create new integration from current version**. 

The **Create new integration** pane appears.

  7. Enter a name and a description for the clone integration.
  8. Select a **Region** for the clone integration from the list of [supported regions](https://docs.cloud.google.com/application-integration/docs/locations).
  9. Click **Create**. 

A new cloned integration is created in the selected region.




## Considerations

  * Cloning an integration doesn't clone the authentication profiles associated with that integration. You must manually create a copy of the associated authentication profiles in the same region as the cloned integration. For information about creating authentication profiles, see [Create authentication profiles in Application Integration](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile)
  * You can't have two integrations with the same name in the same region. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
