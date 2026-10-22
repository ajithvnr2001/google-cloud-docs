---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/default-audience/
title: Managing the default visibility for specific portal resources \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:30.083093+00:00
---

# Managing the default visibility for specific portal resources  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/default-audience/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing the default visibility for specific portal resources Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

To manage the default visibility for specific portal resources, you must have [enrolled in the Preview release of the audience management feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#enroll).

Manage the default visibility of pages and API products in the Apigee console. When creating resources in the Apigee management console, the default visibility will be populated by default. You will have the opportunity to modify the visibility before saving (in the case of Catalog Items) or publishing (in the case of Pages).

**Note:** Default visibility settings won't apply when creating resources directly through the API.

In addition, you can modify the visibility of an existing portal resource, as described in the following sections:

  * [Manage the visibility of a page in your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages#visibility)
  * [Manage the visibility of an API in your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#visibility)



To manage the default visibility for specific portal resources:

  1. In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click the row of the portal for which you want to set default visibility.

  3. Click **Audiences** in the side navigation.

  4. Click the **Default visibility** tab.

  5. Click **Edit**.

  6. Select one of the following values: 

     * **Public (visible to anyone)** to allow all users to view the page.
     * **Authenticated users** to allow only registered users to view the page.
     * **Selected audiences** to select the specific audiences that you want to be able to view the page. See [ Manage the audiences for your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience). 
**Note:** If you select **Authenticated users** or **Selected audiences** , the portal resources will not be indexed by search engines.
  7. Click **Apply**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
