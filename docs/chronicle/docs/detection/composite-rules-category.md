---
url: https://docs.cloud.google.com/chronicle/docs/detection/composite-rules-category/
title: Composite rules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:59:53.914946+00:00
---

# Composite rules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/composite-rules-category/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Composite rules

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document provides an overview of the composite rule sets, the required data sources, and the configuration options for tuning the alerts they generate. These rule sets provide higher-fidelity alerting. They establish severity, confidence, risk, and priority levels across all Google Security Operations-enabled detection content for Google Cloud and endpoint environments.

## Describe rule sets

The Composite Rules category includes the following rule sets:

  * Endpoint composite rules
  * Cloud composite rules
  * ATI composite rules



## Understand endpoint composite rules

These rules correlate findings from multiple detection rules that relate to the same endpoint over a defined time period. Confidence and risk levels are determined by specific characteristics of those detections.

## Understand Cloud composite rules

These rules correlate findings from multiple detection rules associated with the same Google Cloud account or Google Cloud resource over a defined time period. Confidence and risk levels are based on specific characteristics of those detections.

## Understand ATI composite rules

ATI composite rules detect multiple unique Applied Threat Intelligence detections from the same campaign, malware variant, or threat actor to provide additional environmental context of any potential threat. This helps you focus on clusters of activity to assist with prioritization. To ensure these rules produce alerts, you must enable Applied Threat Intelligence rule packs, such as "Active Breach", "High", or "Medium".

## Supported devices and log types

These rules primarily rely on Cloud Audit Logs, endpoint detection and response logs, and network proxy logs. Google SecOps UDM automatically normalizes these log sources. The following categories outline the most important log sources required for the curated composite content to function effectively:

**Endpoint composite rule log sources**

  * [Linux threats](https://docs.cloud.google.com/chronicle/docs/detection/linux-threats-category#supported_devices_and_log_types)
  * [MacOS threats](https://docs.cloud.google.com/chronicle/docs/detection/macos-threats-category#supported_devices_and_log_types)
  * [Windows threats](https://docs.cloud.google.com/chronicle/docs/detection/windows-threats-category#supported_devices_and_log_types)



**Google Cloud composite rule log sources**

  * [Google Cloud](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#log-types)
  * [AWS](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#aws-log-types)
  * [Azure](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#azure-supported-devices)
  * [Office365](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#supported_devices_and_required_log_types_for_office_365)
  * [Okta](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#supported_devices_and_required_log_types_for_okta)



**Google Cloud and endpoint rule log sources**

  * [Applied Threat Intelligence (ATI)](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections#supported_devices_and_log_types)
  * [Chrome Enterprise Threats](https://docs.cloud.google.com/chronicle/docs/detection/chrome-enterprise-threats-category#supported_devices_and_log_types)
  * [Risk Analytics for UEBA](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-ueba-category#required_data_needed_by_risk_analytics_for_ueba_category)



For a complete list of the available curated detections, see [Use curated detections](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections). Contact your Google SecOps representative if you need to enable the detection sources using a different mechanism.

Google SecOps provides default parsers that parse and normalize raw logs to create UDM records with data required by composite and curated detection rule sets. For a list of all Google SecOps supported data sources, see [Supported default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## Modify rules in a rule set

You can customize the behavior of rules within a rule set to meet your organization's needs. Adjust how each rule operates by selecting one of the following detection modes, and configure whether the rules generate alerts.

  * **Broad:** detects potentially malicious or anomalous behavior, but may produce more false positives due to the general nature of the rule.



To modify the settings, do the following:

  1. From the rules list, select the checkbox next to each rule that you want to modify.

  2. Configure the **Status** and **Alerting** settings for the rules as follows:

     * **Status:** applies the mode (**Precise** or **Broad**) to the selected rule. Set to `Enabled` to activate the rule's status to the mode.

     * **Alerting:** controls whether the rule generates an alert on the **Alerts** page. Set to **On** to enable alerts.




## Tune alerts from rule sets

You can reduce the number of alerts generated by a composite rule by using [rule exclusions](https://docs.cloud.google.com/chronicle/docs/detection/rule-exclusions).

A rule exclusion specifies criteria that prevent certain events from being evaluated by a rule or rule set. Use exclusions to reduce detection volume. See [Configure rule exclusions](https://docs.cloud.google.com/chronicle/docs/detection/rule-exclusions) for more information.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
