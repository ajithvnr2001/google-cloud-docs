---
url: https://docs.cloud.google.com/security-command-center/docs/model-armor-agentspace-integration/
title: Integrate Model Armor with Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:43:14.713095+00:00
---

# Integrate Model Armor with Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/model-armor-agentspace-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Integrate Model Armor with Gemini Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

Integrating Model Armor with [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs) lets you screen user prompts to and responses from your AI agents, mitigating risks such as prompt injection, harmful content, and sensitive data leakage. After the integration is set up, it applies to all user interactions.

## Before you begin

Create a Model Armor template and ensure that it is in the same Google Cloud project as Gemini Enterprise. The location of the template and the Gemini Enterprise instance must match. For more information about supported locations, see [Model Armor locations](https://docs.cloud.google.com/model-armor/locations) and [Gemini Enterprise locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations).

### Required roles

Before you integrate Model Armor with Gemini Enterprise, ensure that you have the required role.

To get the permissions that you need to create and manage Model Armor templates, ask your administrator to grant you the [Model Armor Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/modelarmor#modelarmor.admin) (`roles/modelarmor.admin`) IAM role on Model Armor templates. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable the integration

To enable Gemini Enterprise with Model Armor, your security administrator creates policies in Model Armor and your Gemini Enterprise administrator applies these policies to the Gemini Enterprise instance.

  1. [Create a Model Armor template](https://docs.cloud.google.com/model-armor/manage-templates).
  2. [Enable and configure Model Armor in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor).



## Limitations and considerations

Consider the following limitations and considerations when integrating Model Armor with Gemini Enterprise:

  * **De-identification and masking** : When Model Armor uses a Sensitive Data Protection template for scanning prompts or responses, Model Armor checks if the content matches the infoType detector criteria defined in the template. Although Sensitive Data Protection supports de-identification based on the template configuration, Model Armor doesn't pass de-identified or masked data back to Gemini Enterprise. If the content triggers any infoType detectors from Sensitive Data Protection and the enforcement type is `INSPECT_AND_BLOCK`, Gemini Enterprise blocks the request or response rather than de-identifying it.
  * **Document and image screening** : In addition to text prompts, the integration supports [documents](https://docs.cloud.google.com/model-armor/overview#ma-support-screening-pdfs) (such as PDFs) and images. The integration screens the following files only when you upload them to the [Gemini Enterprise assistant](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat#upload_and_chat_about_files):

    * Images that you upload directly.
    * Images contained inside other files and documents that you upload directly.

If a file or an image inside a document violates your configured policies, the entire file or document is discarded and excluded from the request.

  * **Screened agents and interactions** : Screening applies to the Gemini Enterprise assistant, employee-made agents (created in the Gemini Enterprise app using the Workflow Builder), and Google-made agents. Interactions with custom agents from your organization (such as ADK, A2A, and Dialogflow) are not screened.

  * **Token limits and quotas** : There are no token limits when you use Model Armor with Gemini Enterprise. However, the total throughput of Model Armor evaluations is governed by [Gemini Enterprise system quotas](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages) and [Model Armor API rate limits](https://docs.cloud.google.com/model-armor/quotas#quotas).

  * **Service Level Agreement (SLA)** : Gemini Enterprise provides a [Service Level Agreement](https://cloud.google.com/terms/gemini/enterprise/sla). When Gemini Enterprise is configured to use Model Armor, blocked queries don't count as SLA violations, regardless of whether the **fail-open** or **fail-closed** mode is used.

  * **Compliance** : Both Gemini Enterprise and Model Armor offer various compliance certifications. When used together, the effective compliance certifications are the common subset of both products. Review the compliance certifications for both products to ensure that they meet your regulatory requirements.




## How it works

After the integration is configured, Gemini Enterprise routes user inputs and assistant outputs through the Model Armor API for screening using the selected templates. The Gemini Enterprise authenticates to Model Armor using the service agent. Model Armor responds based on the filter configuration defined in the template, which Gemini Enterprise acts upon by either blocking the request or response or allowing it.

For example, Gemini Enterprise might detect a request containing personally identifiable information and route it to Model Armor for screening. If the Model Armor template is configured to block personally identifiable information (PII), it tells Gemini Enterprise to block the request.

## Logging

Model Armor generates platform logs for sanitization requests and their responses in Cloud Logging. You need the Private Logs Viewer (`roles/logging.privateLogViewer`) IAM role to view the Model Armor audit logs. For more information about the auto-generated audit logs, see [Model Armor audit logging](https://docs.cloud.google.com/model-armor/audit-logging-model-armor).

To log the sanitize operations, set the `templateMetadata.logSanitizeOperations` field to `true`. For more information, see [Configure logging in templates](https://docs.cloud.google.com/model-armor/configure-logging#configure-logging-templates).

## What's next

  * [Enable Model Armor in Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor)
  * [Correlate Model Armor logs with Gemini Enterprise logs](https://docs.cloud.google.com/gemini/enterprise/docs/correlate-model-armor-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
