---
url: https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency/
title: Understand rule run scheduling \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:25.265871+00:00
---

# Understand rule run scheduling  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand rule run scheduling

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document is for security analysts, engineers, and platform administrators who want to understand and manage how Google Security Operations schedules rule executions. It explains how rule configurations determine processing frequency, how the system balances near-real-time streaming with scheduled batch processing, and how background runs handle late-arriving logs and context enrichment.

## Common use cases

Choosing or understanding the right schedule depends on threat severity and logic complexity:

  * **High-priority alerting** : Detect critical threats in near-real time for single-event matches that require no additional event correlation, reducing attacker dwell time.
  * **Complex correlation and reporting** : Use scheduled intervals (such as 10 minutes or 1 hour) for multi-event rules that calculate counts, sums, or sliding match windows. Scheduled intervals ensure that the system ingests and enriches related logs before execution, improving alert accuracy for compliance and trend analysis.



## Key terminology

  * **Deterministic frequency** : The baseline execution interval the system assigns automatically based on your rule's match window and rule type.
  * **Primary run (_T_ \+ offset)**: The initial execution of the detection logic against an event time block. The settlement delay represents the offset added to account for late-arriving data.
  * **Settlement delay** : The buffer period added to the primary run to allow late-arriving logs to process before rule evaluation begins.
  * **True-up runs (rule replays)** : Automated background executions that re-evaluate previously processed time windows to capture logs or enrichment data that arrived after the primary run.
  * **Enrichment** : The process of adding context to a log (such as asset metadata, user identity, or threat intelligence indicators) during pipeline processing.
  * **Detection delay** : The total elapsed time between the event timestamp and the creation of a detection.



## Before you begin

Confirm your environment meets the following requirements:

  * **Permissions** : You must have the Chronicle API Admin (`roles/chronicle.admin`) or Chronicle API Editor (`roles/chronicle.editor`) IAM role to modify rule schedules, or the Chronicle API Viewer (`roles/chronicle.viewer`) role to inspect schedules in the Rules Dashboard.
  * **Environment check** : Make sure your logs are mapped to the **Unified Data Model (UDM)** to support scheduled interval aggregations.



## How rule scheduling works

Google SecOps balances near-real-time detection latency with platform stability across thousands of rules. The platform uses two primary execution models:

  1. **Streaming engine** : Evaluates standard and windowed single-event rules (even with match windows greater than 48 hours) continuously in near-real time (typically within 5 minutes of ingestion). Late-arriving events and retroactive enrichments are evaluated continuously during standard execution.
  2. **Scheduled query engine** : Evaluates complex single-event rules (with reference lists or data tables) in near-real time, and multi-event rules in batched blocks of event time (such as 10-minute or 1-hour intervals, or `match_window / 10` for windows greater than 48 hours). Multi-event rules require a time window to aggregate and correlate events across sources.



### Default schedule configuration

When you enable a rule, Google SecOps automatically determines the default execution frequency based on your rule's logic and match window:

Rule type and window size | Execution frequency | Evaluation timing | True-up runs  
---|---|---|---  
**Single-event rule** (standard or windowed) | **Real-time** | Shortly after arrival (<5 minutes) | **No.** Evaluates late and enriched data continuously in standard execution.  
**Single-event rule** (with reference lists or data tables) | **Near-real time** | Shortly after arrival (<5 minutes) | **No.** Evaluates late and enriched data continuously during standard query execution.  
**Multi-event rule** (`window <= 48h`) | **Every 1 Hour** (or **Every 10 min** customizable for windows < 1h) | 1 to 2 hours after arrival | **Yes.** Includes an automated 4h true-up run and an optional 30h true-up run.  
**Multi-event rule** (`window > 48h`) | **`match_window / 10`** (for example, every 1d for a 10d match window) | Varies based on match window (`match_window / 10`) | **No.** Evaluates late and enriched data during subsequent overlapping runs.  
  
## Automatic true-up runs

To prevent missed detections caused by ingestion latency or late-arriving enrichment metadata (such as asset tags or user aliases), the system automatically performs background true-up runs for multi-event rules (`window <= 48h`):

  1. **Initial run** : Executed as quickly as possible based on the scheduled interval to expose immediate threats.
  2. **First true-up run (4h)** : Re-evaluates the time block approximately 4 hours after the initial run to capture late-arriving logs. This stage does not wait for full data enrichment.
  3. **Second true-up run (30h)** : (Optional) Executed approximately 30 hours after the initial run once all additional context and data enrichment pipelines reach completion.

**Note:** Multi-event rules with match windows greater than 48 hours don't perform true-up runs because their execution frequency (`match_window / 10`) continuously evaluates overlapping time windows.

For more information on true-up behavior and scenarios, see [Understand rule replays and MTTD](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays).

## Customizable schedules

For custom multi-event rules with match window <=48h, Google SecOps lets you customize schedule parameters rather than relying entirely on system defaults:

  * **Frequency selection** : Choose run frequencies such as **Every 10 min** (for match windows under 60 minutes) or **Every 1 Hour**.
  * **Settlement delay** : Add a buffer delay (_T_ \+ offset) to accommodate known log source ingestion latency.
  * **Enrichment completeness** : Extend true-up processing to 30 hours to ensure all external metadata joins are complete before final evaluation.

**Note:** Single-event rules (including standard, windowed, and reference-based rules) evaluate in near-real time and don't support scheduled intervals. Curated rules use fixed system schedules that cannot be modified. Multi-event rules with a match window greater than 48 hours execute at a frequency of `match_window / 10` and cannot be customized.

For full configuration steps, see [Configure customized schedules for rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule).

## Schedule visibility in the Rules Dashboard

The **Rules Dashboard** displays the assigned execution schedule for each active rule in the **Rule schedule** column. Inactive rules don't display an active schedule until enabled.

To modify the run frequency, add settlement delays, or adjust enrichment wait times for a custom multi-event rule, see [Configure customized schedules for rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule).

## Detection source indicators

In the **Alerts** page and **Rules Dashboard** , the **Detection Type** column indicates whether a detection originated from an initial execution or an automated background run:

  * **No icon** : The detection was generated during the primary run (_T_) or using the continuous streaming engine.
  * **lightbulb icon** lightbulb: The detection originated from event data arriving more than 30 minutes late, automated true-up runs, reprocessing pipelines, or retrohunts.



## Latency and troubleshooting considerations

Rule run frequency directly impacts the speed of your detections. Keep the following behaviors in mind when designing and monitoring rules:

  * **Hourly schedules** : Run every hour using the most recent data available; no extra buffer is applied by default.
  * **Match windows greater than 48 hours** : The system executes these rules at a rate of `match_window / 10` and does not do any true-up runs.
  * **Discrepancies between runs** : A detection that does not trigger on the first run might trigger during a true-up run if log ingestion was delayed or if context enrichment (such as entity graph resolution) completed after the initial evaluation.
  * **Missing customization options** : Single-event rules evaluate in near-real time and don't support interval customization. Curated rules follow fixed system schedules. Custom multi-event rules with a match window greater than 48 hours execute at a frequency of `match_window / 10` and cannot be customized.
  * **Unsupported intervals** : If you cannot select near-real-time execution, your rule is a multi-event rule requiring event correlation across time or includes aggregations (such as `count` or `sum`), which require the scheduled batch query engine.



For in-depth troubleshooting steps, see [Understand rule detection delays](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays).

## What's next

To explore related scheduling concepts and configuration workflows, see the following documents:

  * [Configure customized schedules for rules](https://docs.cloud.google.com/chronicle/docs/detection/set-customized-schedule): Customize run frequencies, settlement delays, and true-up enrichment completeness for multi-event rules.
  * [Understand rule replays and MTTD](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays): Learn how automated true-up runs handle late-arriving data and context updates to impact Mean Time to Detect (MTTD) metrics.
  * [Understand rule detection delays](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays): Diagnose and resolve expected and unpredicted delays across ingestion and processing pipelines.
  * [Manage rules using the Rules editor](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules): Create, edit, and manage custom detection rules in Google SecOps.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
