---
url: https://docs.cloud.google.com/fault-injection-testing/run-experiment/
title: Run an experiment \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:02:08.860629+00:00
---

# Run an experiment  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/run-experiment/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Run an experiment Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to run an experiment in Fault Injection Testing.

Running an experiment involves using an existing template to create an experiment. The experiment does a dry run where it automatically verifies the target resources and permissions needed. Once the experiment is ready, you can proceed with the fault injection.

**Note:** You cannot start a new experiment if an active [exclusion window](https://docs.cloud.google.com/fault-injection-testing/exclusion-windows) covers the target region of your experiment. Any attempts to start an experiment during an active exclusion window will be blocked.

Before proceeding, you must have the `roles/faulttesting.operator` role.

To run an experiment:

  1. Select **Experiment templates** from the left-hand navigation and choose a template. 
     * (Optional) Enter a custom name for this experiment. If you don't enter an experiment name, it will use the auto-generated one. Example: "template_name_Sep_3_2025".
     * (Optional) Enter a description for this experiment.
  2. Select **Start Experiment**.

A details page showing the progress of the experiment appears, and the dry run of the experiment starts.

When the dry run completes:

     * The target resources appear on the page.
     * The status indicates **Prepared** , meaning that you can start the fault injection. If an experiment is left in the **Prepared** state for more than 10 days, it is automatically canceled.
  3. Select **Start injection**. The fault injection starts on the target resources, and you can see the progress.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
