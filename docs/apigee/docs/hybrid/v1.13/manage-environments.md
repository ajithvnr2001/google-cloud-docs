---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/manage-environments/
title: Manage environments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:03:00.316179+00:00
---

# Manage environments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/manage-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage environments Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/manage-environments.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/manage-environments.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/manage-environments.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/manage-environments.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/manage-environments.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/manage-environments.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/manage-environments.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/manage-environments.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/manage-environments.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/manage-environments.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/manage-environments.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/manage-environments.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/manage-environments.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/manage-environments.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/manage-environments.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/manage-environments.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/manage-environments.html)



**More Information**  
For more information, see:

  * [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview)



You can manage your environments with a combination of the [Google Cloud console](https://console.cloud.google.com) and the hybrid runtime configuration file. This section describes how to create a new environment, edit an environment's details, and delete an existing environment with Google Cloud. You must then update your overrides.yaml on the runtime plane to complete the creation or deletion of an environment.

**NOTE:** Do not create any new environments until you have installed the hybrid runtime on your cluster as described in [Part 2: Runtime quickstart](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-before-begin).

## Create a new environment in the UI

To create a new environment, you must do the following (in this order):

  1. Create a new environment in the Google Cloud console. 

**AND**

  2. Provision the new environment in your overrides file.

**NOTE:** After you create a new environment in the UI, there can be a several minute delay before you can provision it in the runtime.

You can create up to 75 environments per organization.

**To create a new environment:**

  1. Create the new environment as described in [Creating environments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#create). 

There can be a several minute delay before the new environment is provisioned.

Even when provisioning is done, you have one more step to perform. You must still add the environment to the runtime's overrides.yaml file.

  2. On the Kubernetes administration machine, add the new environment to the runtime's overrides file, as described in [How to add multiple environments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/environment-create#how-to-add-multiple-environments). 



## Edit an existing environment in the UI

You can change the following properties of an existing environment in the UI:

  * Display name
  * Description



To edit an existing environment, see [Editing environments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#edit).

## Delete an existing environment

To delete an existing environment, you must do the following (in this order):

  1. Delete the environment in the UI, as described in this section 

**AND**

  2. Delete the environment from the runtime, as described in [Deleting environments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/environment-delete).



**To delete an existing environment:**

  1. Delete the environment in the Apigee UI using the instructions in [Deleting environments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#delete). 

The environment's card in the UI displays a "Pending Deletion" label while Apigee deletes the environment.

There can be a several minute delay before the deletion is completed.

**NOTE:** You're not quite done. You must still delete the environment from the runtime's `overrides.yaml` file.
  2. Delete the environment from the runtime's `overrides.yaml` file, as described in [Deleting environments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/environment-delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
