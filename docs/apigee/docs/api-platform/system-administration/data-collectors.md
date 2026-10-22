---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/data-collectors/
title: Managing Data Collectors \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:39.622488+00:00
---

# Managing Data Collectors  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/data-collectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing Data Collectors Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

A [ data collector](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest#rest-resource:-v1.organizations.datacollectors) resource enables you to collect a wide variety of custom data from API traffic. Once you have created a data collector, you specify the data you want to gather using the [DataCapture](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) policy. The data collector is like a shopping cart, and the DataCapture policy is a shopping list for the data you want to capture. 

**Note:** If you use a data collector in multiple policies, the captured data will be overwritten by the last policy that executes. 

For a list of the quantities related to API traffic that you can capture using the data collector resource, see [Metrics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference).

## Creating a data collector

You can create a data collector resource in the Apigee UI or with the Apigee API:

### Apigee UI

To create a data collector resource using Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Management > Data Collectors** page.

[Go to Data Collectors](https://console.cloud.google.com/apigee/datacollectors)

  2. In the **Data Collectors** view, click **Create**.
  3. In the **Add data collector** dialog, enter the following information: 
     * **Name** : A name for the data collector. **Note:** The name for a data collector must begin with `dc_`.**Warning:** Do _not_ create two data collectors whose names differ only by case, such as `dc_my_data` and `dc_My_Data`, as then exporting data will result in a "duplicate column names" error.
     * **Type** : The type of the data to be collected (`Integer`, `String`, and so on).
     * **Description** : An informal description of the data to be collected, possibly including the reason for collecting it. This is for the benefit of other API developers who may be involved in analyzing the data.
  4. Click **Add**.



To edit or delete a data collector, click the three dots at the end of its row under **Actions** , and select either **Edit** or **Delete**.

### Apigee API

You can create a [ data collector](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors) resource using the Apigee API. For example:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -X POST -H "content-type:application/json" \
      -d '
    {
      "name": "dc_data_collector",
      "description": "Collects data for analysis.",
      "type": "STRING",
    }' \
      "https://apigee.googleapis.com/v1/organizations/ORG/datacollectors"

where ORG is the name of the organization. This creates a resource named `dc_data_collector`, which you can use in the [DataCapture](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy) policy.

**Notes:**

  * The name of the data collector resource must begin with the prefix `dc_`. 
  * If you use a data collector in multiple DataCapture policies, the captured data will be overwritten by the last policy that executes.

**Warning:** Do _not_ create two data collectors whose names differ only by case, such as `dc_my_data` and `dc_My_Data`, as then exporting data will result in a "duplicate column names" error.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
