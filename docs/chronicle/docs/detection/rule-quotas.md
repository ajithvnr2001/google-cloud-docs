---
url: https://docs.cloud.google.com/chronicle/docs/detection/rule-quotas/
title: Understand rule quotas \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:29:36.402407+00:00
---

# Understand rule quotas  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/rule-quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand rule quotas

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Google Security Operations enforces capacity limits on detection rules to ensure consistent system performance and query speed.

Rule capacity is managed through the following two categories:

  * **Custom rules** : Rules written and managed by your team.

  * **Curated detections** : Rules written and managed by Google.




## Custom rule quotas by package

Custom rules are subject to performance quotas based on your Google SecOps package.

The following table lists the rule quotas for each package:

Package | Total rules quota | Multi-event rules quota  
---|---|---  
**Standard** | 1,000 | 75  
**Enterprise** | 2,000 | 200  
**Enterprise Plus** | 3,500 | 400  
  
## Track custom rule quota

Custom rules are subject to strict performance quotas based on their complexity.

To track custom rule quota, do the following:

  1. In Google SecOps, go to **Detection > Rules & Detections**.

  2. Select the **Rules Dashboard** tab.

  3. Click **Rules Capacity**. The capacity details popover displays the following quotas:

     * **Multiple Event Rules Quota** : Number of enabled multi-event rules versus the maximum allowed.
     * **Total Rules Quota** : Total number of enabled rules versus the maximum allowed.

Quota type  |  Description  |  What counts toward the quota  |  Total rules quota  |  The maximum number of enabled rules allowed in the environment.  |  All active rules: Single-event and multi-event.   
---|---|---  
Multi-event rules quota  |  A restricted subset of the total quota reserved for multi-event rules.  |  Only multi-event rules: Rules that correlate multiple events over time, use joins, or perform [windowed aggregations](https://docs.cloud.google.com/chronicle/docs/yara-l/match-syntax#supported_time_windows) (for example, rules with a match section).   
  
  * [Single-event rules](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#single-event-rule) count only toward the total active quota.

  * [Multi-event rules](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#multiple-event-rule) consume capacity from **both** the total active and multi-event quotas simultaneously.




Multi-event rules consume significantly more resources than single event rules. You might have available space in your _total_ quota but be blocked from enabling a new rule if you have exhausted your _multi-event_ quota.

## Curated detections capacity

Curated detections (also called Google SecOps Rules) are rule sets created by Google Threat Intelligence (GTI).

For Enterprise and Enterprise Plus customers, license entitlements are explicitly sized to accommodate the entire library of curated rule sets. You can activate all curated rule sets simultaneously without risking performance trade-offs or hitting a capacity ceiling.

While the dashboard provides **Capacity** or **Weight** metrics, these figures are informational, and not hard limits. If a limit warning triggers, verify your license package configuration.

### How curated capacity is calculated

Curated capacity is not based on the number of rules, but on the sum of weights assigned to each enabled rule set. The default capacity is 150.

  * **Weight** : The weight of a rule set is based on its complexity and the volume of events it processes. More complex rule sets or those processing more events have a higher weight.

  * **Consumption** : When any rules (Precise, Broad, or both) are enabled for a rule set, the rule set's full capacity weight is counted toward the total usage.




### View curated capacity details

To view the curated detections capacity and usage:

  1. In Google SecOps, go to **Detection > Rules & Detections > Curated Detections**.

  2. Select the **Rule Sets** tab. The **Capacity** column displays the weight for each rule set.

  3. Click the **Curated Detections Capacity** status button to view the total capacity usage for the account.




### Enable curated rule sets

If your package supports it, you can enable rules across curated rule sets:

  1. In Google SecOps, go to **Detection > Rules & Detections > Curated Detections**.

  2. In the **Rule Sets** tab, select the checkboxes for the rule sets you want to enable.

  3. In the bulk action menu, select **Enable All Selected**.

  4. Confirm your capacity usage by clicking **Curated Detections Capacity** , or go to **Detection > Rules & Detections**, select the **Rules Dashboard** tab, and click **Rules Capacity**.




## Optimize system performance

This section outlines optimization strategies to maximize your rule capacity and system performance.

### Modularize complex logic

Create lightweight, single-event rules to flag atomic behaviors. That is, avoid writing massive multi-event rules that attempt to detect every stage of an attack from raw logs.

  1. Detect signals with single-event rules

     * Create single-event rules for individual behaviors (for example, `User Login Failed`, `Process Launched`).

     * **Impact** : Consumes the total active quota (abundant) and runs in near real-time.

  2. Correlate alerts with composite or multi-event rule

     * Write a composite rule which uses the detections generated in step 1 as input.

     * **Impact** : Consumes multi-event quota (expensive).

     * **Benefit** : You use the multi-event quota once for the logic, rather than reprocessing raw logs multiple times for different scenarios.




### Create an efficient rule design

  * **Prioritize single-event logic** : If a detection can be done with a single log line (for example, "User visited a known bad domain"), write it as a single-event rule to save your multi-event quota for correlations. Avoid using a match window.

  * **Use reference lists** : Instead of _N_ rules for _N_ indicators, use a single rule that references a reference list (for example, `target.ip in %suspicious_ips`). This consumes only one unit of rule quota.

  * **Perform regular audits:** Regularly audit paused or disabled rules. While they don't count toward active quota, archiving them keeps the environment clean.




### Use case: Detect lateral movement through brute force

**Scenario:** Detect an attacker who attempts to brute force their way into a server through Risk Data Platform (RDP) and immediately executes a suspicious administrative tool (like PsExec) to move laterally.

**Step 1: Detect signals with single-event rules**

Create two lightweight rules that run on the abundant total active quota. These generate detections.

  * **Rule A (brute force signal):**

    * **Logic** :

      * Check for `auth.status = FAILURE`.

      * Group login events.

      * Trigger if more than 5 failed attempts in 1 minute.

    * **Input** : Raw UDM events.

    * **Output** : A detection alert named `Possible_RDP_Brute_Force`.

    * **Cost** : Low (uses total active quota).

  * **Rule B (suspicious tool signal)** :

    * **Logic** : Trigger if the process is `psexec.exe`.

    * **Input** : Raw UDM events.

    * **Output** : A detection alert named `PsExec_Usage`.

    * **Cost:** Low (uses total active quota).




**Step 2: Correlate alerts with composite rule**

Write one composite rule that looks at the detections generated in step 1, not the raw logs.

  * **Rule C** :

    * **Logic** : Look for `Possible_RDP_Brute_Force AND PsExec_Usage` occurring on the same `principal.hostname` within 10 minutes.

    * **Input** : Detections from rules A and B.

    * **Cost** : High (uses multi-event quota) but only processes the few alerts generated in step 1.




This tiered approach optimizes for both performance and cost-efficiency by decoupling initial signal generation from complex correlation logic. By filtering billions of raw UDM events into high-fidelity detections using single-event rules, you reduce the data volume processed by the multi-event engine.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
