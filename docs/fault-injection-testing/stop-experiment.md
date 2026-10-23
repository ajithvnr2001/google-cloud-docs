---
url: https://docs.cloud.google.com/fault-injection-testing/stop-experiment/
title: Stop and revert an experiment \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:17.916129+00:00
---

# Stop and revert an experiment  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/stop-experiment/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Stop and revert an experiment Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to stop and revert fault injection experiments in progress.

Before proceeding, you must have the `roles/faulttesting.operator` role.

## Stop and revert an experiment

To stop an experiment:

  1. Select **Experiments** in the left-hand navigation.
  2. Select an experiment.
  3. Select **Stop and Revert**.
  4. Confirm that you want to stop and revert the experiment.



**IMPORTANT** : For the Failover Cloud SQL fault, the experiment will move your primary SQL instance to a different zone. High availability will be restored, but the primary instance won't automatically return to its original zone. To restore your original topology, you can manually fail back later or run another experiment on the same instance.

## Stop and revert all running experiments

Before proceeding, you must have permissions to update experiments.

You can stop all experiments at once. In order to be stopped, the fault injection must be in progress or complete. If there are ten experiments and two can't be stopped for some reason, the remaining eight experiments will be stopped. A list of the experiments being acted upon will be displayed before you Stop all the experiments, and a second list will be displayed showing what experiments were stopped.

  1. Press the **Stop all experiments** button from the top of either the **Overview** page or the **Experiments** page.
  2. Select **Stop all**.
  3. Confirm that you want to stop all the experiments.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
