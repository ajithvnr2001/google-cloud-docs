---
url: https://docs.cloud.google.com/workstations/docs/service-accounts/
title: Cloud Workstations service accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:07.629419+00:00
---

# Cloud Workstations service accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Cloud Workstations service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the service accounts created and managed by Cloud Workstations. Cloud Workstations creates two service accounts:

  * Cloud Workstations Service Agent
  * Cloud Workstations VM Default Service Account



Google owns these accounts, but they are specific to your project. They are deleted only when you delete your project. You might encounter service disruptions if you change the permissions granted to these service accounts.

### Cloud Workstations Service Agent

The Cloud Workstations Service Agent uses the following email format:
    
    
    service-PROJECT_NUMBER@gcp-sa-workstations.iam.gserviceaccount.com

This service agent allows Cloud Workstations to perform service duties on your project. By default, this service agent is automatically granted the Workstations Service Agent (`roles/workstations.serviceAgent`) IAM role on your project.

Revoking or changing the permissions for this service agent prevents Cloud Workstations from accessing the compute and network resources that back your workstations. To avoid service disruptions, don't modify the service agent's permissions.

### Cloud Workstations VM Default Service Account

Workstations are hosted on Compute Engine instances. When you create a workstation, you can specify a service account to attach to the underlying Compute Engine instance. If you don't specify a service account, the Cloud Workstations VM Default Service Account for your project is used.

The Cloud Workstations VM Default Service Account uses the following email format:
    
    
    service-PROJECT_NUMBER@gcp-sa-workstations**vm**.iam.gserviceaccount.com

Using the Cloud Workstations VM Default Service Account has the following limitations:

  * [Cloud Workstations container output logging](https://docs.cloud.google.com/workstations/docs/container-output-logging) is not supported.
  * [Impersonating a service account](https://docs.cloud.google.com/workstations/docs/authentication#impersonate-a-service-account) is not supported.
  * You cannot use `ssh` to connect to the VM assigned to the workstations that use this configuration.



To avoid these limitations, you can specify a service account on your workstation configuration. For more information, see [Customize the environment](https://docs.cloud.google.com/workstations/docs/create-configuration#customize_environment).

## What's next

  * [Authenticate and setup API access within a workstation](https://docs.cloud.google.com/workstations/docs/authentication).
  * [Access control with IAM](https://docs.cloud.google.com/workstations/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
