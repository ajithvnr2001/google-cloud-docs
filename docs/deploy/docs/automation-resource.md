---
url: https://docs.cloud.google.com/deploy/docs/automation-resource/
title: About the automation resource \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:00.324783+00:00
---

# About the automation resource  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/automation-resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  About the automation resource Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the Cloud Deploy resources used to execute [automations](https://docs.cloud.google.com/deploy/docs/automation).

You can configure Cloud Deploy to automatically perform certain delivery pipeline tasks, such as promote a release or advance a rollout to a given phase. These automations rely on two Cloud Deploy resources:

  * The `Automation` itself

  * The `AutomationRun`




These resources are described in this document.

## The `Automation` resource

An `Automation` is a Cloud Deploy resource that defines how to automate one or more delivery pipeline tasks. The `Automation` associates one or more target resources with one or more automation `rules`.

The `Automation` resource includes the following:

  * A reference to the target (or targets) against which to perform the automation (the `selector`).

  * An automation rule that determines how to do the automation.

  * Metadata, such as `description`, `annotations`, and `labels`.

  * A `suspended` property.

  * The service account to use to perform the automation. The service account is required, and it must have the [necessary permissions](https://docs.cloud.google.com/deploy/docs/automation#roles_and_permissions_required) to perform the automation. Automation doesn't assume a default service account.




The `Automation` resource is a child resource of the [delivery pipeline](https://docs.cloud.google.com/deploy/docs/architecture#resources); if you [delete a delivery pipeline](https://docs.cloud.google.com/deploy/docs/delete-pipeline), all automations that are children of that pipeline are also deleted.

The [configuration file schema](https://docs.cloud.google.com/deploy/docs/config-files#automation_definitions) describes how to configure the `Automation`.

## The `AutomationRun` resource

An `AutomationRun` represents an execution of an [automation rule](https://docs.cloud.google.com/deploy/docs/automation-rules).

## The automation service account

The service account you use to invoke an automation can be the [default service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account) or another service account. However, even if you're using the default service account, you must specify it, using the `serviceAccount` property in the `Automation` configuration.

The automation service account must have `iam.serviceAccount.actAs` permission on the [applicable execution service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account). Also, if the automation service account isn't in the same project as the delivery pipeline, the Cloud Deploy [service agent](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#service_agent) must have `iam.serviceAccount.actAs` on the automation service account.

### Required permissions on the automation service account

Whether you specify the default or a non-default service account for an automation, the service account must have the following permissions:

  * Permission to `actAs` the [execution service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account).

  * [Permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#permissions) to perform the operations that are being automated. See the [automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules) for specific permission requirements.




## What's next

  * Try the [quickstart: Automate release creation and rollout advancement](https://docs.cloud.google.com/deploy/docs/deploy-app-automation).

  * Read about [automation rules](https://docs.cloud.google.com/deploy/docs/automation-rules).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
