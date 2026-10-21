---
url: https://docs.cloud.google.com/chronicle/docs/detection/mandiant-recommended/
title: Mandiant Recommended rules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:08:50.420307+00:00
---

# Mandiant Recommended rules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/mandiant-recommended/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mandiant Recommended rules

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

This guide helps security operations center (SOC) analysts and detection engineers to establish a high-fidelity threat detection baseline. It explains how Mandiant Recommended rules in Google Security Operations provide a curated threat detection baseline designed to identify threat actor behaviors while minimizing SOC alert fatigue.

## Common use cases

Common use cases for this workflow include the following:

### Automated threat detection baseline

**Objective:** Establish a curated threat detection baseline that identifies threat actor behaviors without manual rule-by-rule configuration.

**Value:** A core architectural strategy of the Mandiant Recommended baseline uses composite detections (multi-event and multi-detection correlations) alongside high-precision [Applied Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/detection/applied-threat-intel-overview) (ATI). Prioritizing multi-stage composite logic over noisy single-event alerts provides higher detection confidence by default and reduces initial rule-tuning requirements.

### Quota-free detection coverage

**Objective:** Maximize threat detection coverage across your environment without consuming custom rule capacity quotas.

**Value:** Mandiant Recommended rules don't count against your custom rule capacity quotas, which lets you maximize coverage without sacrificing capacity.

## Key terminology

  * **Mandiant Recommended rules:** Curated detection rules in Google Security Operations that identify threat actor behaviors while minimizing SOC alert fatigue.
  * **Composite detections:** Multi-event and multi-detection correlations that prioritize multi-stage composite logic over single-event alerts.
  * **Applied Threat Intelligence (ATI):** High-precision threat intelligence used alongside composite detections in the curated baseline.
  * **Tag subscription service:** A background service that automates rule deployment and lifecycle management for rules tagged with `google.mandiant.recommended`.



## Before you begin

To manage tag subscriptions, you must have the following IAM permissions:

  * `chronicle.tagSubscriptions.create`
  * `chronicle.tagSubscriptions.delete`
  * `chronicle.tagSubscriptions.get`
  * `chronicle.tagSubscriptions.list`
  * `chronicle.tagSubscriptions.update`



## Key concepts and rule tagging infrastructure

The Mandiant Recommended baseline uses the Google SecOps [Unified Rules dashboard](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/manage-unified-rules) and a background subscription service to automate deployment and lifecycle management.

### System and custom tags

Google SecOps automatically tags every detection rule in this curated baseline with the tag:

`google.mandiant.recommended`

This tag lets Google SecOps automatically identify, enable, and update recommended rules.

### Tag subscriptions

Instead of requiring manual rule-by-rule activation, you can subscribe to the tag by using the subscription service:

  * **Automatic synchronization** : Subscribing to the `google.mandiant.recommended` tag triggers the subscription service.
  * **LiveRules population** : The subscription service automatically populates and enables corresponding YARA-L rules with the recommended detection and alerting settings.



To manage tag subscriptions:

  1. Go to the **Rules & Detections** dashboard, select the **Overview** tab, and click **Manage tag subscriptions**.
  2. Locate the **Mandiant Recommended** tag and enable the subscription by setting the toggle to on. To unsubscribe, set the toggle to off.



When you subscribe to the **Mandiant Recommended** tag, all curated rules with that tag are automatically set to their recommended detection and alerting settings. If you need to override those settings, you can update each rule using the rule's **Overview** tab. A warning indicates that you changed settings from the Mandiant Recommended subscription baseline. You can use the curated rule exclusions feature as an alternative to changing rule settings. For more information, see [Suppress rule exclusions](https://docs.cloud.google.com/chronicle/docs/investigation/alert-suppression#suppress-rule-exclusions).

To view all differences between Mandiant Recommended configurations and your overrides, go to the **Overview** tab and click **View diff and align**. This opens an overview drawer that lets you reset your overrides back to the Mandiant Recommended defaults. This button only appears when the **Alignment** value is less than 100%.

### Curated saved view

Google SecOps adds a default pinned saved view called **Mandiant Recommended rules** to your Unified Rules dashboard. The view uses the following filter criteria: `(rule_owner:"*" AND archived=false) AND (tags:"google.mandiant.recommended")`.

For more information about searching rules, see [Search the rules list](https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/search-rules-list).

## Troubleshooting

This section provides information to resolve common issues and understand the behavior of recommended rules.

### Warning notifications for recommended rules

Disabling standard alerting on a Mandiant Recommended rule triggers a warning message rather than a hard restriction. Verify that your team maintains active coverage before disabling alerting on recommended rules.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
