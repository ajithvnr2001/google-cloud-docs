---
url: https://docs.cloud.google.com/apigee/docs/apihub/configure-api-observation/
title: Configure API observations in API hub \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:44.801591+00:00
---

# Configure API observations in API hub  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/configure-api-observation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure API observations in API hub Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

**Preview — API observations in API hub**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure API observations in API hub for Apigee runtime projects. 

## Before you begin

  * API observations is part of the Advanced API Security add-on. To ingest the Apigee API Observation assets, you must first activate this add-on by enabling Shadow API Discovery from the [Shadow APIs](https://console.cloud.google.com/apigee/api-hub) page. 
  * Assign the required [ IAM roles and permissions](https://docs.cloud.google.com/apigee/docs/apihub/api-observation-overview#iam-roles-permissions) to your principal account. 
  * Ensure that you have [created observation jobs](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery#create-observation-jobs) in Apigee for API hub to ingest this data. 



## Configure API observations in API hub for new Apigee runtime projects

To configure API observations in API hub for Apigee runtime projects, do the following: 

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Go to the **Project associations** tab and click **Attach runtime project**. This displays the **Select a resource** pane.
  4. Click the Google Cloud project where the Apigee instance is installed. 
  5. In the **Project association settings** pane, select the **Apigee API Observation** checkbox. 

![Apigee API Observation checkbox](https://docs.cloud.google.com/static/apigee/docs/apihub/images/api-observation-checkbox.png)

Apigee API Observation discovers and imports Shadow APIs using observation jobs. Ensure that you have [created observation jobs](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery#create-observation-jobs) in Apigee for API hub to ingest this data. 

**Important:** Apigee API Observation is part of the Advanced API Security add-on. To ingest the Apigee API Observation assets, you must first activate this add-on by enabling Shadow API Discovery from the [Shadow APIs](https://console.cloud.google.com/apigee/api-hub) page. 
  6. Click **Attach**. 

The **Project associations** page is updated with the Apigee runtime project and the **Associated plugins** column is updated with a new **Apigee API Observation** plugin instance. 




## Configure API observations in API hub for existing Apigee runtime projects

For existing Apigee runtime projects that are associated with API hub, you can edit the project association settings to ingest data from Apigee API Observation: 

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Go to the **Project associations** tab to view the list of attached projects.
  4. Click **Edit settings** for the desired project. 
  5. In the **Project association settings** pane, select the **Apigee API Observation** checkbox.
  6. Click **Save** to apply your changes. 

The **Project associations** page is updated with the Apigee runtime project and the **Associated plugins** column is updated with a new **Apigee API Observation** plugin instance. 




## Considerations

The following considerations apply when configuring API observations in API hub: 

  * The refresh rate for the **API observations** page in API hub is 30 minutes. This might cause a slight delay in the appearance or update of any newly observed APIs in API hub. 
  * API observations in API hub currently only supports Apigee runtime projects.
  * Custom tags assigned in Apigee runtime projects are not directly transferred or supported within API hub.



## What's next

  * Learn how to [manage API observations in API hub](https://docs.cloud.google.com/apigee/docs/apihub/manage-api-observation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
