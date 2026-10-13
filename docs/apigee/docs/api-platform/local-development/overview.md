---
url: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview/
title: Overview of local development with Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:57.652180+00:00
---

# Overview of local development with Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Overview of local development with Apigee Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can develop and test your Apigee APIs and API proxies in a local environment using Cloud Code. Cloud Code is an extension that integrates your Apigee API development, testing, and deployment into the [Visual Studio Code (VS Code) IDE](https://code.visualstudio.com/), including verifying the functionality through unit and manual testing using the Apigee Emulator (local runtime).

During **local development** , use Apigee in Cloud Code to develop your API proxies and verify the functionality through unit and manual testing using the Apigee Emulator (local runtime). 

During **archive deployment** , deploy to Apigee for integration testing and release, leveraging an archive that contains the complete environment and API proxy configuration.

**Preview — Archive deployment**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Benefits of local development with Apigee

The benefits of local development with Apigee include:

  * Quickly iterate through build and test cycles without impact to other dependent applications
  * Access and manage APIs in your API hub catalog, including publishing new APIs to API hub
  * Create and run repeatable unit tests that verify that the code is producing the intended outcome
  * Identify the set of changes that are deployed as part of a release
  * Track who made changes to a specific deployment



## Prevented actions with archive deployment

To support local development, you must [enable archive deployment](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/manage-archive-deployments#enable-archive-deployment) for an environment in your Apigee organization. When you enable archive deployment in an Apigee environment, you will be **prevented from performing certain actions within the environment** to prevent conflicts with local development. For complete details, see [Summary of prevented actions with archive deployment](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#archive-prevented-actions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
