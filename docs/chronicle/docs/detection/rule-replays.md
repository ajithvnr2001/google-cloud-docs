---
url: https://docs.cloud.google.com/chronicle/docs/detection/rule-replays/
title: Understand rule replays and MTTD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:44.562038+00:00
---

# Understand rule replays and MTTD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/rule-replays/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand rule replays and MTTD

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how **rule replays** (also called **cleanup runs** or **true-up runs**) handle late-arriving data and context updates, and how these replays affect the Mean Time to Detect (MTTD) metrics.

## Rule replays

Google Security Operations processes large volumes of security data. To ensure accurate detections for rules that depend on contextual or correlated data, the rule engine automatically runs a **rule replay** process.

The rule replay process handles these categories of rules:

  * **[Single-event rules](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays#single-event-rules):** These rules are replayed when the UDM enrichment process updates a previously evaluated event. For exceptions regarding rules with data tables, see Late arriving data scenarios later in this document.

  * **Windowed Single-event (WSE) rules and Single-event rules with data tables:** These rules have a distinct scheduling mechanism for handling late-arriving data, different from both standard single-event and multi-event rules.

  * **[Multi-event rules](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays#multi-event-rules):** These rules execute on a schedule, processing blocks of event time. They repeatedly re-evaluate the same time block at different intervals to capture late enrichment updates, such as matching user or asset context data or an Indicator of Compromise (IOC). The exact timings depend on the schedule configuration.




### Rule replay triggers

The system re-evaluates (re-runs) rules to ensure it catches detections, even if data arrives or updates after the initial rule execution. This _late arriving data_ includes the following categories:

  * **Late arriving source events:** The raw log or UDM event itself arrives in Google SecOps significantly later than the event's actual timestamp.
  * **Late arriving enrichment data:** Contextual data (for example, user, asset, threat intelligence) related to an event becomes available, or the system updates it, after it first processed the event. This often occurs because enrichment pipelines, such as the [entity context graph (ECG)](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph), process data in batches or depend on external data sources.
  * **Retroactive UDM enrichment updates:** Late-arriving source data (like DHCP records updating hostnames) triggers changes to UDM event fields. Rules using [aliased fields (enriched fields)](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment) in their detection logic, such as `$udm.event.principal.hostname`, can trigger replays when source data is delayed. This late arrival retroactively updates those field values.



The system triggers rule replays differently depending on the rule type and the nature of the late data. The goal is to balance detection timeliness with data completeness.

### How the system handles late arriving data by rule type

The rule type and its configuration determine the time window within which late-arriving data can trigger a rule re-evaluation.

  * **Single-event rules (without match windows or data tables):**

    * **Late source events:** Generally, these rules process an event regardless of how old its timestamp is when it arrives in the system. The system doesn't impose a strict cut-off window for the initial processing of late source events.
    * **Late enrichment:** If enrichment data for a previously evaluated event arrives or an update occurs, the system re-evaluates these single-event rules against the event with the new context. This can happen hours or even days after the initial event.
  * **Windowed-single-event (WSE) rules and single-event rules with data tables:**

    * These rules do _not_ follow the same late data handling as other single-event rules or the true-up schedules of multi-event rules.
    * They have the following behavior: 
      * **Cut-off:** These rules don't process events ingested 7 days or more after the event timestamp.
      * **Late-Arriving Data ( <7d):** The system processes events arriving less than 7 days late, but with potentially higher latency.
      * **Late-arriving source events** : WSE rules won't process events if the data arrives in Google SecOps 7 days or more after the event timestamp.
      * **Context Updates:** If context for an event arrives late or if an event is retroactively enriched, the system automatically re-evaluates rules against the enriched event. This rule replay can trigger new detections, even if the initial evaluation didn't result in a detection.
      * **Late enrichment** : If a UDM event is updated due to enrichment (which can occur up to 7 days after ingestion), the system re-evaluates these rules against the updated event. However, unlike other rule types, updates to data table content don't trigger an automatic re-evaluation of past events for these rules.
      * **Lookback window:** These rules use a lookback window of approximately 7 days to re-evaluate events. If enrichment data arrives for an event that falls within this 7-day window, the rule will be re-evaluated.
  * **Multi-event rules:**

    * Multi-event rules run on a schedule and re-evaluate time blocks to account for late data. The rule's schedule determines the effective cut-off window: 
      * **Primary run:** The system runs the first evaluation at the event time plus any configured settlement delay (for example, T + 1 hour).
      * **True-up run 1:** The system runs the first true-up run approximately 4 hours after the primary run. This allows the system to include late-arriving events.
      * **True-up run 2 (Conditional):** If you turn on **Ensure enrichment completeness** , the system runs a final true-up run approximately 30 hours after the primary run. This extends the window for the system to process late-arriving data and context enrichments up to approximately 30 hours.
      * **Cut-off implications:** The final true-up run dictates the effective cut-off for including late data. This typically occurs around 4 hours after the primary run (or around 30 hours after the primary run if you enable **Ensure enrichment completeness**). Events or enrichments arriving after the final true-up run for a given time window won't be processed by this rule for that window.
**Note:** These windows are typical, but various system factors and processing delays can influence the exact timing. These times are provided as approximations. For more information on run schedules, see [Understand rule run scheduling](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency) and [Configure customized schedules for rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule).



### Examples of late arriving data scenarios

  * **Scenario 1: Late source event - Single-event rule**

    * Google SecOps ingests an event with a timestamp from 3 days ago. A standard single-event rule processes this event as new data.
  * **Scenario 2: Late enrichment - Single-event rule**

    * The system processed a login event yesterday. Today, it ingests and enriches new information for the user involved (for example, a department change). The system re-evaluates the single-event rule against the login event with the updated user context.
  * **Scenario 3: Late source event - Multi-event rule (default 4-hour true-up)**

    * An event arrives 3 hours after its event timestamp for a multi-event rule scheduled with default settings. The event missed the initial primary run (T + 1h), but the system processes it during the 4-hour true-up run.
  * **Scenario 4: Late source event - Multi-event rule (without enrichment completeness)**

    * You configure a multi-event rule with a primary run offset of 1 hour without enabling **Ensure enrichment completeness**. An event arrives 6 hours after its timestamp.
    * This event misses the primary run (T + 1h) and the first _true-up run_ (T + 4h). The system won't process this event for that time window because it arrived after the final true-up run.
  * **Scenario 5: Late enrichment - Multi-event rule (with enrichment completeness)**

    * A multi-event rule has a 1-hour offset and you enable **Ensure enrichment completeness**. Enrichment data for an event arrives 28 hours after the event timestamp.
    * The system re-evaluates the rule using this late enrichment during the second true-up run at approximately T + 31h.
  * **Scenario 6: Late source event - Multi-event rule with match window**

    * A multi-event rule has a 48-hour `match` window and a schedule with **Ensure enrichment completeness** enabled (final true-up around T + 30h). An event arrives 36 hours after its timestamp. This event won't be processed because it arrived after the final true-up run, even though the event time is within the rule's match window relative to other events. The cut-off is based on arrival time relative to the true-up schedule, not just the match window.
  * **Scenario 7: Late source event - Windowed-single-event rule**

    * If a source event with a timestamp from 8 days ago arrives late, it might fall outside of the 7-day lookback window for WSE rules, and it might not be processed.



### Impact on timing metrics

When a detection results from a rule replay, the system uses the following terminology:

  * The alert's **Detection window** or **Event timestamp** refers to the time of the original malicious activity.
  * The **Created time** is the time the system creates the detection, which can be much later, sometimes hours or days later.
  * **Detection latency** is the time difference between the **Event timestamp** and the detection's **Created time**.



### Timeline delta and MTTD

The time elapsed between the initial event timestamp and the creation of a detection directly impacts your MTTD calculation.

Pipeline / schedule stage | Evaluation timing | Impact on MTTD measurement  
---|---|---  
**Single-event rule (Streaming)** | Continuous (<5 minutes after arrival) | Real-time detections represent true platform speed with minimal impact on MTTD.  
**Multi-event rule (Primary Run)** | 1 to 2 hours after arrival (plus configured settlement delay) | Includes the unavoidable batch buffering window required to aggregate multi-event correlation states.  
**Multi-event rule (True-up runs)** | 4 hours or 30 hours after primary run | A secondary (replay) run that incorporates late enrichment data causes this time to appear late or delayed relative to the Event timestamp. This delta negatively affects the MTTD calculation.  
  
## Best practices for measuring MTTD

MTTD quantifies the time from initial compromise to the effective detection of the threat. When you analyze detections triggered by rule replays, apply the following best practices to maintain accurate MTTD metrics.

Google SecOps provides several user-queryable metrics to measure MTTD accurately. For more information about these metrics, see [Sample YARA-L 2.0 queries for Dashboards page](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard).

A lightbulb icon in the **Detection Type** column identifies detections generated from event data arriving more than 30 minutes late, automated true-up runs, reprocessing pipelines, or retrohunts. This icon also appears on the **Alerts** page in Google SecOps.

### Prioritize real-time detection systems

For the fastest detections, use single-event rules. These rules run in near-real time, typically with a delay of less than 5 minutes. This also supports more comprehensive use of [Composite detections](https://docs.cloud.google.com/chronicle/docs/detection/composite-detections#optimize-composite-detections).

### Account for rule replay in multi-event rules

Multi-event rules inherently incur higher latency due to their scheduled [run frequency](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency). When you measure MTTD for detections from multi-event rules, recognize that automated rule replays increase coverage and accuracy. These replays often catch threats requiring late context, which increases the reported latency for those detections.

  * **For critical, time-sensitive alerting:** Use single-event rules or multi-event rules with the shortest practical run frequencies. Reducing the match window doesn't directly affect latency, but it can increase efficiency by setting the minimum delay.

  * **For complex, long-duration correlation (UEBA, multi-stage attacks):** These rules rely on extensive contextual joins or reference lists, which might update asynchronously. They can experience high latency with late-arriving contextual or event data, but they offer the benefit of higher fidelity detection rather than absolute speed.




### Optimize rules to reduce reliance on late enrichment

To optimize for detection speed and minimize the impact of retroactive enrichment runs, consider using **non-aliased fields** (fields that downstream enrichment pipelines don't process) in your rule logic where possible.

## What's next

To explore related scheduling concepts and configuration workflows, see the following documents:

  * [Understand rule run scheduling](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency): Learn how Google SecOps maps rule configurations to continuous streaming and scheduled batch query engines.
  * [Configure customized schedules for rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule): Customize run frequencies, settlement delays, and true-up enrichment completeness for multi-event rules.
  * [Understand rule detection delays](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays): Diagnose and resolve expected and unpredicted delays across ingestion and processing pipelines.
  * [Manage rules using the Rules editor](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules): Create, edit, and manage custom detection rules in Google SecOps.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
