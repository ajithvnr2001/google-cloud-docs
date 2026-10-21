---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy/
title: Overview of content policies \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:09.972670+00:00
---

# Overview of content policies  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Overview of content policies Stay organized with collections  Save and categorize content based on your preferences. 

A Sensitive Data Protection _content policy_ is a reusable resource that you can use to evaluate content and determine whether to allow or block it based on its sensitivity. You can use content policies to integrate real-time data protection checks directly into your workflows.

In contrast to other Sensitive Data Protection inspection operations, such as a [`content.inspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect) call or an [inspection job](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers), a content policy doesn't return a list of findings. Instead, a content policy returns a single `ALLOW` or `BLOCK` verdict. The client application can then act on the verdict by allowing or blocking the content.

To create and manage content policies, see [Create and manage content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies).

## Benefits and use cases

Content policies let you act immediately on inspection results by producing a verdict rather than a list of findings. Example use cases include the following:

  * Automatically block chatbot responses or file uploads that contain sensitive information, such as credit card numbers or personally identifiable information (PII).
  * Integrate Sensitive Data Protection content policies with Gemini Enterprise to prevent it from using content that contains sensitive data. For more information, see [Protect sensitive data in sources](https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data).
  * Get immediate, synchronous verdicts on content to enforce organizational data policies.
  * Get a verdict on whether to allow certain types of data in an AI model training dataset.



## Parts of a content policy

Each content policy includes the following:

  * **Inspection configuration** : Defines what sensitive data to scan for using [built-in](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) or [custom](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes) infoType detectors.
  * **List of policy rules** : An ordered list of rules. Each rule specifies conditions and an action (verdict). Sensitive Data Protection evaluates the rules in order; the first matching rule determines the verdict (`ALLOW` or `BLOCK`).
  * **Default actions** : Actions to take if Sensitive Data Protection can't scan a file or if the content is successfully scanned but matches no rules.
  * **Logging configuration** : Optional. Configuration to record the outcomes of policy evaluations to external systems, such as a BigQuery table. For information about the schema of the exported logs, see [`ContentPolicyActionLog`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentPolicyActionLog).



## Limits

For information about the maximum file sizes that Sensitive Data Protection can scan, see [Content policy limits](https://docs.cloud.google.com/sensitive-data-protection/limits#content-policy-limits). In your [content policy configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies#create-content-policy), you can specify the verdict that Sensitive Data Protection assigns to files that are too large.

## What's next

  * Learn how to [create and manage content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies).

  * If you administer Gemini Enterprise, apply the content policy to a Gemini Enterprise data store or app. For information, see [Protect sensitive data in sources](https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
