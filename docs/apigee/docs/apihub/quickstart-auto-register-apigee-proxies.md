---
url: https://docs.cloud.google.com/apigee/docs/apihub/quickstart-auto-register-apigee-proxies/
title: Auto-register Apigee proxies \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:12.823455+00:00
---

# Auto-register Apigee proxies  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/quickstart-auto-register-apigee-proxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Auto-register Apigee proxies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This quickstart shows you how to register Apigee proxies in API hub.

## Before you begin

You must have completed the API hub provisioning steps. See [Provision API hub](https://docs.cloud.google.com/apigee/docs/apihub/provision). 

## Auto-register Apigee proxies

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **Settings > Project associations**.
  3. Click **Attach runtime project**. This displays the **Select a resource** pane.
  4. Click the required project. If there aren't any errors, the project gets attached to API hub, and will be listed in the **Project associations** page. However, the actual process of registering the proxies will start after the next run of the scheduler which runs once every six hours.

**Note:** For a project to be attached as a runtime project, the project shouldn't have API hub installed in it, and the project shouldn't be a part of other runtime projects for another host project.

## Next

  * [Settings overview](https://docs.cloud.google.com/apigee/docs/apihub/settings-overview)
  * [Manage API resources](https://docs.cloud.google.com/apigee/docs/apihub/manage-apis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
