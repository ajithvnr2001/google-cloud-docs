---
url: https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule/
title: Configure customized schedules for rules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:58.902832+00:00
---

# Configure customized schedules for rules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure customized schedules for rules

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for security analysts, engineers, and platform administrators to configure and manage how Google Security Operations schedules rule executions. It explains how to adjust run frequency, configure settlement delays, and manage true-up timelines for custom multi-event rules.

By following the process described in this document, you gain precise control over detection latency and data integrity. Successful completion ensures that your detections are both timely and accurate, reducing false negatives caused by ingestion delays and ensuring consistent security operations.

Customizable schedules provide transparency and control over how multi-event rules run in Google Security Operations. Some multi-event rules may require a buffer period to aggregate data accurately; this method lets you define that period rather than relying on system defaults.

**Caution:** When this feature is enabled, the system labels all existing multi-event rule schedules as "legacy". You can migrate your legacy schedules for custom rules to the new customizable system. Once you migrate the rule schedule to the new system, you can't revert it to a legacy schedule.

## Common use cases

Customizable schedules let you tune execution parameters to match specific operational goals:

  * **Short-window correlation** : Run multi-event rules with match windows under 60 minutes on a **10-minute** frequency (rather than waiting for the default 1-hour interval) to detect time-sensitive threats like brute-force attacks more quickly.
  * **Compensating for ingestion latency** : Configure a settlement delay (_T_ \+ offset) for log sources with known delivery delays, ensuring the primary execution includes all expected events.
  * **Ensuring context completeness** : Enable the **Ensure enrichment completeness** toggle for non-critical compliance and forensic rules that require full entity and asset metadata resolution before final evaluation.



## Key terminology

  * **Primary run (_T_ \+ offset)**: The initial execution of the rule logic on incoming data. The settlement delay represents the offset added to account for late-arriving data.
  * **Settlement delay** : The buffer period added to the primary run to allow late-arriving logs to process before rule evaluation begins.
  * **True-up run** : A background re-evaluation of the same time window to capture logs or enrichment data that arrived after the primary run.
  * **Enrichment** : External metadata (like asset tags or user aliases) added to logs during processing.



## Before you begin

Before you attempt to modify or automate your rule schedules, make sure that your environment and account meet the necessary security and system requirements. When you validate these prerequisites, it helps prevent deployment errors and makes sure that your detection logic aligns with your organization's Identity and Access Management policies.

  * **Permissions** : To modify rule schedules, you must have the following IAM permissions:

    * `chronicle.ruleDeployments.update` for API usage for individual schedule updates.

    * `chronicle.rules.modifyRules` for batch API updates and UI usage.

If you use [predefined IAM roles](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#predefined-roles), such as Chronicle API Admin (`roles/chronicle.admin`) or Chronicle API Editor (`roles/chronicle.editor`), these permissions are included automatically.

  * **Environment check** :

    * **Rule type** : Customizable schedules apply only to multi-event rules. Single-event rules (including standard, windowed, and reference-based rules) evaluate in near-real time and cannot be customized. Curated rules use fixed system schedules and are excluded.
    * **`match` window**: Multi-event rules with a `match` window greater than 48 hours execute at an automatically assigned frequency of `match_window / 10` and cannot be customized.
    * **Migration** : Migrating a legacy schedule to a customizable schedule is a one-way process and cannot be reverted.



## Configure the schedule for a multi-event rule

To configure the schedule for a multi-event rule, follow these steps:

  1. In Google SecOps, go to **Detection** > **Rules & Detections**.
  2. Click **Rules Dashboard**.
  3. Locate your rule in the rules table, click **More** more_vert, and select **Run schedule**.
  4. On the **Rule schedule** tab, configure the **Primary Run** section: 
     1. In the **Set Frequency** list, select how often the rule runs (for example, **Every 10 min** or **Every 1 Hour**).
     2. (Optional) To account for late-arriving data, turn on the **Settlement delay** toggle.
     3. In the **Delay** field, enter the delay value and select the time unit (**Minutes** or **Hours**) from the **Unit** menu.
  5. In the **True-up run** section, (optional) turn on the **Ensure enrichment completeness** toggle. 
     * **Anticipated failure** : Alerts may appear significantly later than the event timestamp if external context sources take time to process.
     * **Corrective step** : Only use this for non-critical compliance and forensic rules where context fidelity is prioritized over immediate alerting speed.
  6. Review the run timeline under **Primary Run** and **True-up run** : 
     * **Primary Run:** The system executes the rule logic after the settlement delay you specify for late-arriving data.
     * **True-up run 1:** The system automatically re-scans the window 4 hours after the primary run to capture missed or late data. If you turn on **Ensure enrichment completeness** , this run also waits for associated enrichment data to process.
     * **True-up run 2:** Appears only when you turn on **Ensure enrichment completeness**. The system performs a final scan 30 hours after the primary run to provide maximum data fidelity.
  7. Click **Save**.



## Troubleshooting

Investigate scheduling issues by reviewing the evaluation timing and rule configuration. While the platform automates most scheduling tasks, certain settings or data delays can impact when detections appear.

### Detections only appear in true-up runs

If a detection doesn't appear during the primary run (_T_), but appears in a true-up run (_T_ \+ 4h or _T_ \+ 30h), check the following:

  * **Ingestion latency:** Check if the log source has a delay. If logs arrive 15 minutes after the event occurs, a 10-minute first-run schedule will miss them. The true-up runs capture these late arrivals.
  * **Context enrichment:** Confirm if the rule relies on external metadata, such as asset tags or user aliases. If the enrichment process takes longer than the primary run window, the detection only surfaces after the system completes the enrichment in a later true-up run.



### Customizable options are missing

If the **Rule schedule** tab doesn't show customization options or the menu is grayed out:

  * **Check the rule type:** Customizable schedules apply only to multi-event rules. Single-event rules (including standard, windowed, and reference-based rules) evaluate in near-real time and don't support custom schedules.
  * **Verify the`match` window:** Multi-event rules with a `match` window greater than 48 hours execute at an automatically assigned frequency of `match_window / 10` and cannot be customized.
  * **Identify curated rules:** You can't modify the schedule for curated rules. If you inspect a curated rule, the UI displays the message: `Multi-event curated rules use a legacy schedule`.



### Unexpected delay in first-run alerts

If a detection arrives later than the scheduled interval:

  * **Initialization period:** New or recently modified rules require a one-hour initialization period. Detections don't surface until the platform completes this initial setup and begins the first scheduled cycle.
  * **Enrichment wait times:** If you turn on the **Ensure enrichment completeness** toggle, the system may dynamically adjust timing to wait for data enrichment processes to finish. While this process prevents missed detections, it can cause the initial detection to arrive later than the exact _T_ timestamp.



### MTTD measurements seem high

The MTTD measurements include the buffering period required for data completeness.

  * **Review the buffer** : For a one-hour schedule, the system evaluates events one to two hours after they arrive.
  * **Optimize for speed** : If you require lower latency, configure the rule to a **10-minute** schedule (for match windows under 60 minutes), or convert the detection logic into a single-event rule running in near-real time if event aggregation is not required.



### Limitations

  * **Multi-event rules only** : This feature is unavailable for single-event rules. Single-event rules (including standard, windowed, and reference-based rules) evaluate in near-real time.
  * **Custom rules only** : Curated rules use fixed schedules that you can't modify. If you view a curated rule, the system displays the message: `Multi-event curated rules use a legacy schedule`. If you view a legacy custom rule, the system displays: `Your Multi-Event rule uses a legacy schedule`.



### Error remediation

Error | Issue | Fix  
---|---|---  
**Missing options** | Rule schedule tab is grayed out or options are missing. | Verify the rule is a multi-event custom rule and the match window is 48 hours or less. Curated rules and single-event rules cannot be customized.  
**Unsupported intervals** | Cannot select near-real-time streaming. | Multi-event rules requiring correlation across events or rules using aggregations (such as `count` or `sum`) require the scheduled batch query engine.  
**Delayed alerts** | Detections arrive later than the scheduled interval. | Check if the **Ensure enrichment completeness** toggle is on; the system may be waiting for metadata processing.  
**Only true-up alerts** | Detections never appear in the primary run (_T_). | Verify log ingestion latency. If logs arrive 15 minutes late but your settlement delay is 10 minutes, increase the settlement delay.  
  
### Validation and testing

To verify your schedule is working as intended, follow these steps:

  1. In Google SecOps, go to **Detection** > **Rules & Detections** and select **Rules Dashboard**.
  2. Select your rule and view the **Detections** tab.
  3. Check the **Detection Type** column and filter by lightbulb to verify whether true-up runs are catching data that the primary run missed, then adjust your settlement delay accordingly.



## What's next

To explore related scheduling concepts and configuration workflows, see the following documents:

  * [Understand rule run scheduling](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency): Learn how Google SecOps maps rule configurations to continuous streaming and scheduled batch query engines.
  * [Understand rule replays and MTTD](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays): Learn how automated true-up runs handle late-arriving data and context updates to impact Mean Time to Detect (MTTD) metrics.
  * [Understand rule detection delays](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays): Diagnose and resolve expected and unpredicted delays across ingestion and processing pipelines.
  * [Manage rules using the Rules editor](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules): Create, edit, and manage custom detection rules in Google SecOps.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
