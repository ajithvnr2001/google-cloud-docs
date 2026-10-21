---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-accelerators/
title: Manage accelerators \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:34.151191+00:00
---

# Manage accelerators  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-accelerators/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage accelerators Stay organized with collections  Save and categorize content based on your preferences. 

In Cloud Data Fusion environments running in version 6.3 and above, you can use add-ons, called accelerators, that incorporate special features in your pipeline jobs. For example, you can add Replication to existing jobs.

You can add accelerators to new and existing instances.

## Before you begin

Your instance needs to run in a Cloud Data Fusion environment version 6.3 or above. To upgrade, see [Upgrading instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).

## Add an accelerator to a new instance

To add an accelerator to a new instance, see [Creating a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).

## Manage accelerators in an existing instance

You can add, disable, or remove an accelerator in an instance.

  1. Go to the instance details: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. Click **Instances** , and then click the instance's name to go to the **Instance details** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the **Accelerators** section, you can add, disable, or remove accelerators.


**Note:** Making any change to accelerators forces a restart of the instance.

### Disable or remove accelerators

  * An accelerator must be disabled before it can be removed.
  * If you disable an accelerator, all services and pipelines associated with the accelerator are stopped. The schedules are ignored. The accelerator no longer appears in your Cloud Data Fusion environment. You can enable it again, if needed, and the schedules will resume. All data related to the accelerator is retained.
  * If you remove an accelerator from your instance, all services and pipelines associated with the accelerator are deleted. They cannot be recovered. If a pipeline runs on a schedule or trigger, the run fails.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
