---
url: https://docs.cloud.google.com/chronicle/docs/detection/curated-detections/
title: Manage curated detections \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:06.058566+00:00
---

# Manage curated detections  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/curated-detections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage curated detections

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to use the curated detections pages.

For Google Security Operations customers, Google Cloud Threat Intelligence (GCTI) team is offering out-of-the-box threat analytics as part of Google Cloud Security Shared Fate model. As part of these curated detections, GCTI provides and manages a set of YARA-L rules to help customers identify threats to their enterprise. These GCTI managed rules:

  * Provide customers with immediately actionable intelligence which can be used against their ingested data.

  * Leverages Google's threat intelligence by providing customers with a way to use it within Google SecOps.




## Before you begin

For information about predefined threat detection policies, see the following:

  * [Overview of Cloud Threats category](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category)
  * [Overview of Chrome Enterprise Threats category](https://docs.cloud.google.com/chronicle/docs/detection/chrome-enterprise-threats-category)
  * [Overview of Windows Threats category](https://docs.cloud.google.com/chronicle/docs/detection/windows-threats-category)
  * [Overview of Linux Threats category](https://docs.cloud.google.com/chronicle/docs/detection/linux-threats-category)
  * [Overview of macOS Threats category](https://docs.cloud.google.com/chronicle/docs/detection/macos-threats-category)
  * [Overview of Risk Analytics for UEBA category](https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-ueba-category)
  * [Overview of Applied Threat Intelligence category](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections)



To verify that data required for each policy is in the correct format, see [Verify log data ingestion using test rules](https://docs.cloud.google.com/chronicle/docs/detection/verify-data-ingestion).

## Curated detections features

The following are some of the key curated detections features:

  * Curated Detection: curated detection created and managed by GCTI for Google SecOps customers.

  * Rule sets: Collection of rules managed by GCTI for Google SecOps customers. GCTI provides and maintains multiple rule sets. The customer has the option to enable or disable these rules within their Google SecOps account and to enable or disable alerts for these rules. New rules and rule sets will be periodically provided by GCTI as the threat landscape changes.

When Google releases new or updated curated content, the following default behaviors apply:

    * New rule sets (rule packs): Default to Disabled (Status is **Disabled** and Alerting is **Off**). However, rule sets under the Applied Threat Intelligence (ATI) categories are automatically enabled for Enterprise Plus instances.
    * New rules added to an existing rule set: Automatically inherit the parent rule set's current Status and Alerting configuration for their precision level (Precise or Broad).
    * Updated rules (new rule revisions): Retain their existing per-rule Status and Alerting configuration.



## Open the curated detections page and rule sets

To open the curated detections page, complete the following steps:

  1. Select **Rules** from the main menu.

  2. Click **Curated Detections** to open the rule sets view.




The Curated Detection page provides information about each of the rule sets active for your Google SecOps account including the following:

  * Last updated: Time GCTI last updated the rule set.

  * Enabled Rules: Indicates which of the Precise and Broad rules are enabled for each rule set. Precise rules find malicious threats with a high degree of confidence. Broad rules search for suspicious behavior that may be more common and produce more false positives. Both Precise and Broad rules might be available for a rule set.

  * Alerting: Indicates which of the Precise and Broad rules have alerting enabled for each rule set.

  * Mitre Tactics: Identifier of the Mitre ATT&CK® tactics covered by each rule set. Mitre ATT&CK® tactics represent the intent behind malicious behavior.

  * Mitre Techniques: Identifier of the Mitre ATT&CK® techniques covered by each rule set. Mitre ATT&CK® techniques represent specific actions of malicious behavior

**Note:** For more information about Mitre Tactics and Techniques, see the official MITRE ATT&CK page at <https://attack.mitre.org/>.



From this page, you can also enable or disable the rule and alerting for the rule. You can do this for either the broad or the precise rules.

## Open the curated detection dashboard

The curated detection dashboard displays information about each curated detection which has produced a detection against the log data in your Google SecOps account. Rules with detections are grouped by rule set.

To open the curated detection dashboard, complete the following steps:

  1. Select **Rules** from the main menu. The default tab is curated detections and the default view is rule sets.

  2. Click **Dashboard**.

![Curated Detections](https://docs.cloud.google.com/static/chronicle/images/rules-dash.png)

**Figure 2: Curated Detections dashboard**

  3. The Curated Detections dashboard displays each of the rule sets available to your Google SecOps account. Each display includes the following:

     * Chart tracking the current activity for each of the rules associated with a rule set.

     * Time of the last detection.

     * Status of each rule.

     * Severity of recent detections.

     * Whether alerting is enabled or disabled.

  4. You can edit the rule settings by clicking the menu icon more_vert or the rule set name.

  5. Click **Rule Sets** to switch back to the rule sets view. The rule sets view provides information about each rule set active for your Google SecOps account.




## View details about a rule set

You can modify the settings for any curated detection by clicking the menu icon more_vert for the rule set, and then selecting **View and edit rule settings**.

You enable or disable the rule set under the **Settings** section. The **Status** and **Alerting** toggles let you enable or disable the precise and broad rules in the rule set. You can also turn on or turn off alerting.

You can also view all of the exclusions configured for the rule set. You can edit the exclusions by clicking **View**. See [Configure rule exclusions](https://docs.cloud.google.com/chronicle/docs/detection/rule-exclusions) for more information.

![Rule settings](https://docs.cloud.google.com/static/chronicle/images/rule-settings.png)

**Figure 3: Rule Settings**

## Modification of all the rules in a rule set

The **Settings** section displays the settings for all rules in a rule set. You can modify the settings to create curated detections specific to your organizational usage and needs.

  * **Precise rules** : Find malicious behavior with a higher degree of confidence with fewer false positives due to the more specific nature of the rule.

  * **Broad rules** : Find behavior that could potentially be malicious or anomalous, but with typically more false positives due to the more general nature of the rule.

  * **Status** : Activate a rule's status as precise or broad by setting the corresponding **Status** option to **Enabled**.

  * **Alerting** : Enable alerting to receive detections created by corresponding precise or broad rules by setting the **Alerting** option to **On**.




## Configure rule exclusions

To manage the volume of alerts from GCTI curated detections, you can configure rule exclusions. For more information, see [Configure rule exclusions](https://docs.cloud.google.com/chronicle/docs/detection/rule-exclusions).

## View curated detections

You can view any of the curated detections in the Curated Detection view. This view lets you examine any of the detections associated with the rule and pivot to other views such as [Asset view](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-asset) from the Timeline.

To open the Curated Detection view, complete the following steps:

  1. Click **Dashboard**.

  2. Click the rule name link in the Rule column.


**Note:** Curated detections can only be edited by Google SecOps, so all of the normal rule editing options are missing.

## What's next

  * [Investigate a GCTI alert](https://docs.cloud.google.com/chronicle/docs/investigation/investigate-uppercase-alert)
  * [Tune alerts returned by rule sets in this category](https://docs.cloud.google.com/chronicle/docs/detection/use-curated-detections#tune-detections)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
