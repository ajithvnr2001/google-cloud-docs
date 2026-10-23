---
url: https://docs.cloud.google.com/workflows/docs/security-best-practices/
title: Security best practices \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:01.902474+00:00
---

# Security best practices  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/security-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Security best practices Stay organized with collections  Save and categorize content based on your preferences. 

Workflows provides several [security features](https://docs.cloud.google.com/workflows/docs/security-overview) that you can use. This page describes some security best practices to keep in mind when using Workflows to avoid unintentionally exposing your resources to vulnerabilities.

  * [Follow general networking and security best practices](https://docs.cloud.google.com/architecture/framework/security).

  * [Create a new service account](https://docs.cloud.google.com/workflows/docs/authentication) and grant it only the Identity and Access Management (IAM) roles that contain the minimum permissions required by your workflow. You should not use the default service account since it is automatically granted the highly privileged Editor basic role which includes a large number of permissions.

  * [Create your workflow using Terraform](https://docs.cloud.google.com/workflows/docs/create-workflow-terraform) so that you can store your environment's configuration as code in a repository.

  * [Use customer-managed encryption keys](https://docs.cloud.google.com/workflows/docs/use-cmek) so that your workflow and associated data at rest are protected using an encryption key that only you can access.

  * [Set up a service perimeter with VPC Service Controls](https://docs.cloud.google.com/workflows/docs/use-vpc-service-controls) to mitigate data exfiltration risks.

  * [Use Secret Manager to secure and store sensitive data](https://docs.cloud.google.com/workflows/docs/use-secret-manager) such as API keys, passwords, and certificates. You can use a Workflows connector to access Secret Manager within a workflow and simplify the integration for you.

  * [Use Cloud Tasks to manage delivery rates](https://docs.cloud.google.com/workflows/docs/create-http-task) and [use Cloud Scheduler to execute workflows on a recurring schedule](https://docs.cloud.google.com/workflows/docs/schedule-workflow). By automating and parameterizing the deployment and execution of your workflows, you ensure that you can repeatedly and consistently run your services, and also eliminate inconsistencies between environments such as testing, staging, and production. Note that Workflows doesn't ensure exactly-once processing of duplicate requests from Cloud Tasks.




## What's next

  * [Google Cloud security best practices center](https://docs.cloud.google.com/security/best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
