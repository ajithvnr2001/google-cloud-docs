---
url: https://docs.cloud.google.com/assured-workloads/docs/key-concepts/
title: Key concepts \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:48.073597+00:00
---

# Key concepts  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/key-concepts/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Key concepts

Assured Workloads provides Google Cloud users with the ability to [apply controls](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to a folder in support of regulatory, regional, or sovereign requirements. This page provides information about its key components.

## Assured Workloads folders

An Assured Workloads folder is the top-level regulatory boundary for your workloads. Each Assured Workloads folder is configured with (and actively enforces) controls that meet the selected [control package's](https://docs.cloud.google.com/assured-workloads/docs/control-packages) regulatory requirements. Assured Workloads folders are also the container for your resources that must adhere to those requirements, such as projects that contain your workloads. Assured Workloads folders and their resources are constantly [monitored](https://docs.cloud.google.com/assured-workloads/docs/monitor-folder) for adherence to compliance requirements.

For example, if you need to meet the regulatory requirements for Impact Level 4 (IL4), you would [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder) for IL4, and then create or [migrate](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload) projects and resources to that Assured Workloads folder. Inside the folder, those projects will be configured to enforce IL4's regulatory requirements, and you will be notified if any resources fall out of compliance.

To ensure that all of your organization's resources are compliant with a specific control package, you can create an Assured Workloads folder as the parent for all of your other folders, projects, and resources. By making the top-level folder an Assured Workloads folder, its controls will be inherited by all child resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). For more information, see [How to set compliance controls for your Google Cloud organization](https://cloud.google.com/blog/products/identity-security/how-to-set-compliance-controls-for-your-google-cloud-organization).

**Note:** Any Assured Workloads environment created before the introduction of Assured Workloads folders continues to be supported. Although it is not required, we recommend that you migrate to Assured Workloads folders if it is possible to do so.

## Assured Workloads key management project

Depending on the control package you select, Assured Workloads can also create a **key management project** inside the Assured Workloads folder to store your CMEK encryption keys. Having one project for keys and another for resources establishes [separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties) between security administrators and developers.

## What's next

  * Learn how to [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder).
  * Learn which [products are supported](https://docs.cloud.google.com/assured-workloads/docs/supported-products) for each control package.
  * Learn how to [migrate a workload](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
