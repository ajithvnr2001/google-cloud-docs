---
url: https://docs.cloud.google.com/chronicle/docs/detection/mandiant-hunt-category/
title: Mandiant Hunting rules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:04:44.456544+00:00
---

# Mandiant Hunting rules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/mandiant-hunt-category/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mandiant Hunting rules

Supported in:

Google SecOps 

**Warning:** These rules are not designed to be run in alerting mode. Google recommends setting **Alerting** to **Off**.

This document provides an overview of the Mandiant Hunting Rule sets, the required data sources, and the configuration options for tuning the alerts they generate in the Google Security Operations platform. 

Mandiant Hunting Rules identify security-relevant events for cloud and endpoint data. These rules are developed in coordination with the Mandiant Threat Defense team and provide a baseline for threat hunting operations. Detections from these rules can be used in composite rules. This category includes the following rule sets:

  * **Cloud Identification rules** : Logic derived from Mandiant Threat Defense investigation and response to cloud incidents across the globe. These rules are designed to detect security-relevant cloud events and are designed for use by correlation rules in the cloud composite rule set.

  * **Endpoint Identification rules** : Logic derived from Mandiant Threat Defense investigation and response to incidents across the globe. These rules are designed to detect security-relevant endpoint events and are designed for use by correlation rules in the endpoint composite rule set.




## Supported devices and log types

These rules primarily rely on Cloud Audit Logs logs, endpoint detection and response logs, and network proxy logs. Google SecOps Unified Data Model (UDM) automatically normalizes these log sources. 

For a list of all Google SecOps supported data sources, see [Supported default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

The following categories outline the most important log sources required for the curated composite content to function effectively:

### Endpoint identification rule log sources

  * [Linux threats](https://docs.cloud.google.com/chronicle/docs/detection/linux-threats-category#supported_devices_and_log_types)
  * [macOS threats](https://docs.cloud.google.com/chronicle/docs/detection/macos-threats-category#supported_devices_and_log_types)
  * [Windows threats](https://docs.cloud.google.com/chronicle/docs/detection/windows-threats-category#supported_devices_and_log_types)



### Google Cloud identification rule log sources

  * [Google Cloud threats](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#log-types)
  * [AWS](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#aws-log-types)
  * [Microsoft Azure](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#azure-supported-devices)
  * [Microsoft Office 365](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#supported_devices_and_required_log_types_for_office_365)
  * [Okta](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#supported_devices_and_required_log_types_for_okta)



### Google Cloud and endpoint rule log sources

  * [Applied Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections#supported_devices_and_log_types)
  * [Chrome Enterprise Premium threats](https://docs.cloud.google.com/chronicle/docs/detection/chrome-enterprise-threats-category#supported_devices_and_log_types)
  * [Risk Analytics for UEBA](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-ueba-category#required_data_needed_by_risk_analytics_for_ueba_category)



For a complete list of the available curated detections, see [Use curated detections](https://docs.cloud.google.com/chronicle/docs/detection/curated-detections). Contact your Google SecOps representative if you need to enable the detection sources using a different mechanism.

Google SecOps provides default parsers that parse and normalize raw logs to create UDM records with data required by composite and curated detection rule sets. For a list of all Google SecOps supported data sources, see [Supported log types and default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers).

## Modify rules in a rule set

You can customize the behavior of rules within a rule set to meet your organization's needs. Adjust how each rule operates by selecting one of the following detection modes, and configure whether the rules generate alerts:

  * **Broad:** detects potentially malicious or anomalous behavior, but may produce more false positives due to the general nature of the rule.
  * **Precise:** detects specific malicious or anomalous behavior. 



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
