---
url: https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/
title: Monitor experiment progress \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:56.530412+00:00
---

# Monitor experiment progress  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/monitor-experiment/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Monitor experiment progress Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to see the current status of an experiment.

Before proceeding, you must have the following:

  * Viewer permissions for the resources affected by the experiment.
  * The `roles/faulttesting.operator` role.



To monitor progress for an experiment:

  1. Go to the Fault Injection Testing **Overview** page.
  2. Select **Experiments** at the left-hand navigation.



The experiment can be in one of the following states:

  * **Preparing**. The dry run is in progress and the experiment is being prepared.
  * **Prepared**. The dry run is complete, and you can start the injection on request.
  * **Injecting**. Fault injection is in progress.
  * **Injected**. Fault injection has been completed on the target resources, and the experiment keeps running for the set duration.
  * **Reverting**. Reverting the faults from the target resources.
  * **Failed**. The fault injection was not successful.
  * **Completed**. The experiment is concluded, which can mean one of the following: 
    * The experiment completed all the expected steps.
    * The experiment was canceled prematurely.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
