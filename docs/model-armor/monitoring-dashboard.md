---
url: https://docs.cloud.google.com/model-armor/monitoring-dashboard/
title: View the monitoring dashboard \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:21.058787+00:00
---

# View the monitoring dashboard  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/monitoring-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  View the monitoring dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Model Armor screens the prompts and responses for your AI applications. The monitoring dashboard provides you with the data, metrics, and visualizations generated from this screening process. Use these insights to understand how Model Armor protects your AI applications and identifies attempted prompt injections or other malicious activities.

## Before you begin

[Enable Model Armor](https://docs.cloud.google.com/model-armor/manage-templates#enable-apis).

### Required role

To get the permissions that you need to access the monitoring dashboard, ask your administrator to grant you the [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to access the monitoring dashboard. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to access the monitoring dashboard:

  * `monitoring.monitoredResourceDescriptors.list`
  * `monitoring.metricDescriptors.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View the monitoring dashboard

  1. In the Google Cloud console, go to the **Model Armor** page.

[Go to Model Armor](https://console.cloud.google.com/security/modelarmor)

  2. Verify that you are viewing the project that you activated Model Armor on.

  3. Go to the **Monitoring** tab.




## Monitor Model Armor usage and performance

To monitor Model Armor usage and performance in detail, you can use the specific metric types available within Cloud Monitoring. The following metric types are available:

  * `modelarmor.googleapis.com/template/request_count`: SanitizeAPI request count
  * `modelarmor.googleapis.com/template/pi_jb_request_count`: Prompt injection and jailbreak filter count
  * `modelarmor.googleapis.com/template/rai_request_count`: Responsible AI filter count
  * `modelarmor.googleapis.com/template/sdp_request_count`: Sensitive Data Protection filter count
  * `modelarmor.googleapis.com/template/malicious_uri_request_count`: Malicious URI filter count
  * `modelarmor.googleapis.com/template/used_token_count`: Used token count



For more information, see [Model Armor metric types](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-modelarmor).

## View the number of flagged or blocked interactions

On the monitoring dashboard, view the number of interactions, including flagged and blocked interactions. The monitoring dashboard displays the following metrics:

  * **Total interactions** : The total number of prompts and responses that are analyzed by Model Armor.
  * **Interactions flagged** : The number of interactions that violated a configured policy in your Model Armor template or floor settings.
  * **Interactions blocked** : The number of interactions blocked if you configured Model Armor in the [`INSPECT_AND_BLOCK`](https://docs.cloud.google.com/model-armor/manage-templates#templates-metadata) mode. These blocked interactions violated floor settings or templates. 

**Note:** When Model Armor is configured in `INSPECT_ONLY` mode, violations are logged, but requests proceed to the model. In this mode, you can check what actions Model Armor might take, and because requests aren't blocked, you can also check if the model refused the request independently. Check the `SanitizeOperationLogEntry` records in Cloud Logging and not just the response body. 

## Monitor content security violations

In the **Violations over time** chart, monitor the number of detected violations over time.

The violations detected are categorized into the following areas:

  * **Prompt injections and jailbreaks** : Content violations indicating the presence of prompts that contain malicious commands or jailbreak attempts. For more information, see [Prompt injection and jailbreak detection](https://docs.cloud.google.com/model-armor/overview#ma-prompt-injection). 
  * **Malicious URL** : Content violations indicating the presence of malicious URLs. For more information, see [Malicious URL detection](https://docs.cloud.google.com/model-armor/overview#ma-malicious-url-detection). 
  * **Responsible AI** : Content violations that are detected by safety filters, such as harassment and hate speech. For a complete list of responsible AI categories, see [Responsible AI safety filter](https://docs.cloud.google.com/model-armor/overview#ma-responsible-ai-safety-categories).
  * **Sensitive data** : Content violations involving the presence of [sensitive information types](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) or [custom information types](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes) that you define. For more information, see [Sensitive Data Protection](https://docs.cloud.google.com/model-armor/overview#ma-sensitive-data-prot). 



For more information about these detectors, see [Model Armor filters](https://docs.cloud.google.com/model-armor/overview#ma-filters).

## Apply filters to views

When you apply these filters on the monitoring dashboard, all the views on the monitoring dashboard are filtered based on the criteria that you select:

  * **Templates/Floor settings** : Filter views based on the associated template or floor settings.
  * **Integration points** : Filter views based on Model Armor integrations.
  * **Locations** : Filter views based on where an interaction was processed.
  * **Input types** : Filter views based on the type of input evaluated: prompt or response.



## Inspect related logs

To explore log entries related to the data on the monitoring dashboard, enable logging in your [templates](https://docs.cloud.google.com/model-armor/configure-logging#configure-logging-templates) or [floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings#configure-floor-settings). You must have the [required IAM roles to view logs](https://docs.cloud.google.com/logging/docs/audit#roles).

To inspect the logs for the selected period, on the monitoring dashboard, click more_vert **More chart options > Inspect related logs**. 

## Download violations data to a PNG or CSV file

To download violations data to a PNG or CSV file, follow these steps:

  1. In the **Violations over time** view on the monitoring dashboard, select the period for which you want to download data.
  2. Click more_vert **More chart options > Download**.
  3. Click **Download PNG** or **Download CSV** to download the data in your preferred format.



## What's next

  * Learn about [Model Armor audit logging](https://docs.cloud.google.com/model-armor/audit-logging-model-armor).
  * [Configure logging for Model Armor](https://docs.cloud.google.com/model-armor/configure-logging)
  * [Troubleshoot Model Armor issues](https://docs.cloud.google.com/model-armor/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
