---
url: https://docs.cloud.google.com/chronicle/docs/detection/detection-delays/
title: Understand rule detection delays \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:32.973157+00:00
---

# Understand rule detection delays  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/detection-delays/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand rule detection delays

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains rule detection delays in Google Security Operations, identifies contributing factors across ingestion and processing pipelines, outlines structured troubleshooting approaches, and provides techniques to reduce detection latency.

## Detection rules overview

Detection rules examine normalized raw logs—both regular and entity Universal Data Model (UDM) events—to generate security detections according to rule specifications. Entity UDM events typically contain [context information](https://docs.cloud.google.com/chronicle/docs/detection/context-aware-analytics) such as user or asset metadata. Detection rules can also evaluate previously generated detections to produce composite alerts.

## Expected and unpredicted delays

Detection latency varies based on rule logic, data dependencies, and system processing cycles. Delays are categorized into two types:

  * **Expected delays** : Delays resulting from structural factors, such as the ingestion process, rule type, run frequency, detection generation method, match window duration, and known system limits. You can minimize expected delays by tuning detection rule configurations and scheduling parameters.
  * **Unpredicted delays** : Delays caused by external or dynamic pipeline conditions, including log delivery bottlenecks from data sources, transient processing latency within Google SecOps services, delayed context availability, and UDM re-enrichment cycles.



## Detection generation methods

Google SecOps generates rule detections through the following execution pipelines:

  * **Streaming engine** : A high-speed pipeline that evaluates standard and windowed single-event rules continuously in near-real time (typically within 5 minutes of ingestion). Late-arriving events and retroactive enrichments are evaluated continuously during standard execution.
  * **Query engine** : Evaluates rules that require time-based event correlation across multiple events or external data joins: 
    * **Complex single-event rules** : Includes single-event rules that query reference lists or data tables.
    * **Multi-event rules** : Queries data in batched blocks of event time (such as 10-minute or 1-hour intervals, or `match_window / 10` for windows greater than 48 hours) based on configured schedules.
  * **Rules run against historical data** : Evaluates rules retroactively against historical logs through retrohunts. Detections surface after the historical scan completes.
  * **Re-enrichment of UDM events** : Re-evaluates previously processed time blocks when new context or updated entity data is added to historical events.



## Factors contributing to rule detection delays

The speed at which detections appear depends on rule complexity, scheduling intervals, data ingestion latency, and context enrichment pipelines.

### Rule types and complexity

Detection rules fall into several categories with differing latency profiles:

#### Single-event rules

[Single-event rules](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#single-event-query) execute in near-real time on the continuous streaming engine and offer the lowest detection latency. These rules evaluate individual events without joining external datasets, data tables, or multi-event match windows.

**Note:** You can apply alert suppression to single-event rules using the [suppression_window option](https://docs.cloud.google.com/chronicle/docs/yara-l/options-syntax#suppression).

#### Complex single-event rules

These rules evaluate single events but incorporate additional data dependencies:

  * **Windowed single-event rules** : Single-event rules that include a `match` section (for example, evaluating if a single event matches a condition over a time window). These rules evaluate in near-real time on the continuous streaming engine as data is ingested.
  * **Reference single-event rules** : Single-event rules that compare event attributes against reference lists or data tables.



#### Multiple-event rules

[Multiple-event rules](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples#multi-event-queries) correlate two or more UDM event conditions over a specified match window and execute on scheduled batch intervals.

  * **Standard multi-event rules** : Aggregate multiple events across time windows and execute on 10-minute or 1-hour intervals (or `match_window / 10` for windows greater than 48 hours).
  * **Context-aware rules** : Correlate event data with UDM entity events (such as `user_context` or `asset_context`) using [context-aware analytics](https://docs.cloud.google.com/chronicle/docs/detection/context-aware-analytics#writing_rules_for_context-aware_analytics). Because context-aware rules rely on multiple data feeds, they are more sensitive to ingestion timing. For more information, see [Use context-enriched data in rules](https://docs.cloud.google.com/chronicle/docs/detection/use-enriched-data-in-rules).



### Rule run frequency

The configured execution frequency determines how often the query engine evaluates event time blocks:

  * **Near-real time** : Continuous evaluation for single-event rules (standard and windowed).
  * **10-minute frequency** : Available for multi-event rules with match windows under 60 minutes.
  * **1-hour frequency** : Default interval for multi-event rules with match windows of 48 hours or less.
  * **`match_window / 10` frequency**: Automatically assigned for multi-event rules with match windows greater than 48 hours (for example, running every 10 hours for a 100-hour match window, or every 24 hours for a 10-day window).



### Match window duration

For multi-event rules, the match window duration defines the observation period required to aggregate events. Detections cannot surface until the full time window has elapsed.

### Log ingestion delay

Ingestion delay is the elapsed time between when an event occurs at the source and when Google SecOps receives and parses the log.

If an event arrives after the initial scheduled evaluation for that time block, it misses the first run. The system captures late-arriving data in subsequent automated background runs (true-up runs), which occur approximately 4 hours (and optionally 30 hours with enrichment completeness) after the primary run.

  * **Example** : A rule correlates Event A (event time 9:03 AM) and Event B (event time 9:05 AM) within a 30-minute window. If Event A arrives at 10:05 AM (one hour late), it misses the initial execution for the 9:00–9:30 AM block. The system re-evaluates the block during a subsequent true-up run approximately 4 hours after the primary run (around 2:00 PM), generating the detection approximately 5 hours after the event occurred.



### Time zone discrepancies

Google SecOps interprets log timestamps as UTC by default. If a log source omits an explicit time zone offset, the system treats the timestamp as UTC, which can cause the log to appear late-arriving even if received immediately.

  * **Example** : An event occurs at 10:00 AM Eastern Time (15:00 UTC) and arrives at Google SecOps at 15:05 UTC without time zone metadata. The system interprets the timestamp as 10:00 UTC, creating a perceived 5-hour ingestion delay that postpones rule evaluation to a background true-up run.



**Workarounds** : To resolve time zone discrepancies:

  * Configure the log source to include explicit UTC time zone offsets in event timestamps.
  * Contact [Support](https://docs.cloud.google.com/chronicle/docs/getting-support) to set a time zone override for the specific ingestion feed.
  * Use a BindPlane processor to normalize log body timestamps to UTC before ingestion. For more information, see [Modifying log body timestamps using BindPlane](https://docs.bindplane.com/how-to-guides/modifying-log-body-timestamps).



### Contextual joins and data enrichment

Google SecOps enriches UDM events by adding identity, asset, and threat metadata from secondary sources. Delays in context availability can extend detection timing.

#### Aliasing and enrichment mechanics

Aliasing and enrichment correlate raw indicators with organizational context:

  * **Aliasing** : Identifies and links different identifiers for the same entity across data sources (such as mapping an IP address from DHCP logs to a MAC address and hostname like `alex-macbook`, or mapping a user ID to an employee job title).
  * **Enrichment** : Populates normalized UDM event fields with the aliased context (such as populating `$udm.event.principal.hostname` when only an IP address is present in the raw event).



Supported enrichment types include assets, users, processes, file hash metadata, geographic locations, and cloud resources. For more information, see [UDM enrichment and aliasing overview](https://docs.cloud.google.com/chronicle/docs/event-processing/overview-of-aliasing-and-enrichment).

#### Re-enrichment of UDM events

The system continuously updates historical events as context sources evolve:

  * **Underlying data changes** : Historical events can be updated for up to 24 hours after ingestion as new context data arrives.
  * **Enrichment system updates** : When entity metadata, IP geolocation, or VirusTotal threat intelligence updates, the rules engine re-evaluates historical blocks (typically during scheduled true-up runs or reprocessing) to generate detections with updated context.
  * **Delayed context data** : If context data (such as a hostname) arrives a day after the event log, the system re-enriches the UDM event, and subsequent true-up runs evaluate the enriched record.
  * **Context modifications** : If an enrichment update changes an event attribute (such as updating an IP geolocation from `USA` to `Canada`), rules that match the updated value trigger detections during subsequent re-evaluations.



#### Entity Context Graph (ECG) processing

The [Entity Context Graph (ECG)](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph) correlates Indicators of Compromise (IOCs) and enterprise asset graph data. Because the ECG pipeline relies on batch processing (which can take 30 hours or up to several days depending on data volume), rules referencing `graph.entity` fields generate detections after graph relationships are fully computed.

### Historical rule runs and retrohunts

Running a rule against historical data generates detections only after the retrohunt scan completes across the selected time range.

  * **Retroactive enrichment workflow** : 
    1. An event arrives at 1:00 PM with `ip_address = 10.0.0.5` (hostname unknown).
    2. At 2:30 PM, a DHCP log arrives linking `10.0.0.5` to `workstation-123`.
    3. The aliasing pipeline updates the historical 1:00 PM event with `principal.hostname = workstation-123`.
    4. Subsequent rule replays evaluate the enriched hostname and surface detections that were not triggered during the initial run.



### Reference lists

Rules that query reference lists evaluate against the latest list version at execution time. Updating a reference list can cause scheduled rules to produce detections retroactively against previously ingested logs.

### Non-existence rules

To prevent false positives, the system introduces a minimum one-hour buffer before evaluating rules that check for [non-existence conditions](https://docs.cloud.google.com/chronicle/docs/yara-l/condition-syntax#bounded-and-unbounded-conditions) (such as `!$e` or `#e=0`), ensuring all related logs have time to arrive.

### Data processing and true-up limitations

Keep the following system behaviors in mind when assessing detection latency:

  * **Enrichment processing** : Context enrichment can update historical UDM events up to 24 hours after initial ingestion.
  * **True-up cycles** : Multi-event rules automatically re-execute approximately 4 hours (and optionally 30 hours) after the primary run to capture late-arriving data. For more information, see [Understand rule replays and MTTD](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays).
  * **Detection limits** : For platform capacity and throttling boundaries, see [Understand detection limits](https://docs.cloud.google.com/chronicle/docs/detection/detection-limits).



## Troubleshoot rule detection delays

To diagnose why a rule generated a delayed detection, examine the following heuristics and pipeline stages in the Google SecOps console:

  * **Review rule metadata and schedule** : In the **Rules Dashboard** , check the **Rule Name** , **Rule Type** , and **Rule schedule** columns to identify the rule's execution engine and baseline evaluation frequency.
  * **Compare Event time against Ingested time** : Locate the detection on the **Detections** tab and compare the event timestamp with the ingestion timestamp. If the gap between event time and ingested time exceeds 30 minutes, the latency was caused by log delivery delays at the source or during collection. Detections generated from event data arriving more than 30 minutes late, automated true-up runs, reprocessing pipelines, or retrohunts display a lightbulb icon in the **Detection Type** column.
  * **Review context source dependencies** : Check if the rule references `principal` enrichment, UDM aliasing, or `graph.entity` fields. Context pipelines process asynchronously and may surface detections during subsequent true-up runs.
  * **Verify frequency and match window compatibility** : Confirm that the configured run frequency matches the match window size (for example, ensuring a rule with a 15-minute match window is scheduled for 10 minutes or 1 hour).
  * **Check for data feed interruptions** : Review ingestion logs and feed management dashboards for ingestion delays or transient source outages.



## Tips to shorten detection delays

To minimize detection delays across your environment, apply the following optimization techniques:

  * **Optimize rule run frequency** : 
    * Use **Near-real time** for single-event rules (standard and windowed).
    * Configure a **10-minute** schedule for multi-event rules with match windows under 60 minutes.
    * Use **1 hour** for rules with match windows between 1 and 48 hours where rapid alerting is needed.
  * **Tune match window durations** : Set match windows to the minimum duration necessary to capture the correlated threat behavior.
  * **Eliminate log delivery bottlenecks** : Ensure forwarders and collectors send event data immediately to prevent logs from missing the initial execution window.
  * **Validate time zone configurations** : Ensure log sources provide explicit UTC offsets to prevent 5+ hour perceived ingestion delays.
  * **Audit context and non-existence conditions** : Use context-enriched fields and non-existence conditions (`!$e`) only when required by detection logic, as these introduce intentional buffering periods.



## What's next

To explore related scheduling concepts and configuration workflows, see the following documents:

  * [Understand rule run scheduling](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency): Learn how Google SecOps maps rule configurations to continuous streaming and scheduled batch query engines.
  * [Configure customized schedules for rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule): Customize run frequencies, settlement delays, and true-up enrichment completeness for multi-event rules.
  * [Understand rule replays and MTTD](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays): Learn how automated true-up runs handle late-arriving data and context updates to impact Mean Time to Detect (MTTD) metrics.
  * [Manage rules using the Rules editor](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules): Create, edit, and manage custom detection rules in Google SecOps.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
