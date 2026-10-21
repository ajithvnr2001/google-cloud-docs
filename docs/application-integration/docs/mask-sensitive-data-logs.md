---
url: https://docs.cloud.google.com/application-integration/docs/mask-sensitive-data-logs/
title: Mask sensitive data in logs \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:53.058185+00:00
---

# Mask sensitive data in logs  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/mask-sensitive-data-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mask sensitive data in logs

**Preview — Mask sensitive data in logs**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes masking sensitive data in integration execution logs.

## About data masking

Application Integration generates log messages for each integration execution. These logs can contain information that is used to determine the status of each integration step, or to troubleshoot failed integrations, tasks, or events. However, if you have enabled [local logging](https://docs.cloud.google.com/application-integration/docs/local-logging) or [Cloud Logging](https://docs.cloud.google.com/application-integration/docs/cloud-logging), all data variables and fields are included in the log output of the execution log or Cloud Logging respectively. These logs can also include sensitive or personally identifiable information (PII) that you don't want to be visible in the log output. With Application Integration, you can mask sensitive data in the log output so that this information is not visible when you review the logs.

## What masking doesn't do

Masking reduces the exposure of sensitive values in log output only. Masking a variable does **not** :

  * Encrypt the variable value, or change how it is stored.
  * Hide the value in the integration editor. Anyone who can edit the integration can see the value, including a default value set on a masked variable.
  * Redact the value when you [download or export](https://docs.cloud.google.com/application-integration/docs/upload-download-integrations) an integration. Values, including masked ones, are written to the exported file in plain text.
  * Redact config variable values when you share an integration as a template. Values are carried into the template in plain text unless you clear them in the review step.

**Caution:** Masking is not a substitute for a secret store. Variables, config or otherwise, aren't designed to store credentials. Don't store passwords, API keys, or tokens in them. Use an [authentication profile](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles) or the [Secret Manager access task](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-secretmanager-access-task) instead.

## Benefits

Masking sensitive data in logs provides the following benefits:

  * Improve customer security and privacy
  * Comply with data privacy regulations



## Supported data types

You can mask variables for all supported data types in Application Integration.

## Mask sensitive data in logs

To mask sensitive data in logs for a project, you must enable masking for all of the following resources:

  * [Project by enabling masking for all regions in that project](https://docs.cloud.google.com/application-integration/docs/enable-new-region#edit-region)
  * [Integration](https://docs.cloud.google.com/application-integration/docs/view-integration-details)
  * [Variables](https://docs.cloud.google.com/application-integration/docs/variables#create-a-variable)



_Project-level_ masking control signifies the highest tier of the masking hierarchy, subsequently followed by _integration_ and _variables_. Authorization for project-level masking is established by using a flag at the region level. To enable project-level masking, enable masking for all regions within your projects. In your project, if you have enabled masking for the integration and the variable, but disabled masking for the region that contains the integration, then the masking functionality doesn't work. Similarly, if integration masking is disabled, variable masking for that integration doesn't work even if you have enabled masking at the region level.

Suppose, you have a project that contains a region with multiple integrations. You want to disable masking for specific integration. In such a case, you can enable masking for the region and disable it for the specific integration that doesn't require masking. Based on your business needs, for your project, you can enable masking at the region, integration, and the variable level. On the other hand, if a project has multiple regions and you have enabled masking for only one region, then end-to-end masking will work only for that region and all integrations built within that region.

### Masking format

Variables are masked in the fixed masking format. For example, the following format shows a masked variable of type string and length 12: `Masked String of length 12`

You can search for masked variables with the `/Masked.*\./` regular expression. You can use the following regular expressions to filter specific types of masked variables:

  * String: `Masked String.*\.`
  * Integer: `Masked Int.*\.`
  * Boolean: `Masked Bool.*\.`



The fixed masking format is efficient for large strings. Both Cloud Logging and integration execution logs mask variables in the same format.

## Example use case

Suppose, your customers' sales data contains sensitive information such as, contact information, order history, pricing agreements, customer payments, etc. By enabling masking at different hierarchical levels, you can protect your data log visibility:

  * To protect customer sales in the production environment, enable masking for your project for all regions associated with that project.
  * To protect specific sections such as customer's payment details, enable masking for the intgeration that contains the payment flow. 
  * To protect specific details such as customer's account number, enable masking for the variable that contains the account number.



For data protection, you must mask all sensitive information. If any level is left unmasked, it could lead to a potential point of unauthorized access. 

## Pricing

There's no additional cost for masking variables. For information about pricing, see [Application Integration pricing](https://docs.cloud.google.com/application-integration/pricing).

## Limitation

  * Application Integration doesn't support masking data in nested fields.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
