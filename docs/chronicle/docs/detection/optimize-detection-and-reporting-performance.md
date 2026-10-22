---
url: https://docs.cloud.google.com/chronicle/docs/detection/optimize-detection-and-reporting-performance/
title: Optimize rule performance \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:25.200717+00:00
---

# Optimize rule performance  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/optimize-detection-and-reporting-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Optimize rule performance

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to optimize detection and reporting performance.

## Total detection latency

For a security operations center (SOC), the total mean time to detect (MTTD) is the sum of time delays across the security pipeline. To accurately measure and reduce MTTD, you need to track three primary components:

  * Log-ingestion latency (log creation to data ingestion)
  * Rule-processing latency (data ingestion to detection creation)
  * Case-acknowledgement latency (detection creation to analyst assignment)



## Log-ingestion latency (log creation to data ingestion)

Log-ingestion latency is the time elapsed between when the security event occurred on the source system (`metadata.event_timestamp`) and when the log was successfully ingested and parsed in Google Security Operations (`metadata.ingested_time`).

Contributing factors:

  * Collector or forwarder issues (for example, backlogs or network throttling).
  * Log source parsing issues (for example, delays in UDM normalization).



To reduce log-ingestion latency, do the following: 

  * Monitor log-source health and optimize collector or forwarder configurations. 
  * To monitor the delta, in YARA-L or Data Lake, compare UDM timestamps—`metadata.ingested_timestamp` versus `metadata.event_timestamp`.



## Rule-processing latency (data ingestion to detection creation)

Rule-processing latency is the time elapsed between data ingestion and when the detection engine successfully creates an alert (`detection.creation_time`). This component is heavily affected by your YARA-L rule configuration.

Contributing factors:

  * **Rule run frequency:** Near-real time (lowest latency), 10 minutes, 1 hour, or `match_window / 10` (for match windows greater than 48 hours). For more information, see [Understand rule run scheduling](https://docs.cloud.google.com/chronicle/docs/detection/rule-execution-frequency).
  * **Rule type and complexity:** multi-event rules require a match window to fully process them, which imposes inherent latency. Composite rules that rely on other non-real-time detections also introduce delays. For more information, see [Composite detections](https://docs.cloud.google.com/chronicle/docs/detection/composite-detections).



To reduce rule-processing latency, do the following:

  * Use single-event rules running in near real-time where possible. 
  * For multi-event rules, set the smallest possible window size.



For more information, [Sample YARA-L 2.0 queries for Dashboards](https://docs.cloud.google.com/chronicle/docs/reference/sample-yaral-for-native-dashboard).

### YARA-L rule to monitor rule-processing latency

The following YARA-L rule identifies instances where the delta between the time a log was ingested and the time the detection was created exceeds a specific threshold. Use the rule to identify performance bottlenecks in your detection pipeline. 

Deploy this rule in your test environment to baseline your log sources.

You can export these outcomes to a dashboard to visualize latency trends across different log types.

The rule compares the `metadata.event_timestamp` (when the activity happened) against the `metadata.ingested_time` (when Google SecOps received the log). 
    
    
    rule rule_processing_latency_monitor {
      meta:
        author = "SecOps Engineering"
        description = "Alerts when the gap between ingestion and detection creation is greater than 15 minutes."
        severity = "Low"
    
      events:
        $event.metadata.event_timestamp.seconds = $event_ts
        $event.metadata.ingested_time.seconds = $ingest_ts
        
        // Calculate the delta in seconds
        $latency_delta = $ingest_ts - $event_ts
    
        // Threshold: 900 seconds (15 minutes)
        $latency_delta > 900
    
      match:
        $event.metadata.log_type over 1h
    
      outcome:
        $max_latency = max($latency_delta)
        $log_source = array_distinct($event.metadata.log_type)
    
      condition:
        $event
    }
    

## Case-acknowledgement latency (detection creation to analyst assignment)

This section is not relevant for customers who use the Google SecOps SIEM standalone platform.

Case-acknowledgement latency is the time elapsed between the detection that creates an alert and the alert being acknowledged by an analyst for triage in the SOAR component.

The _mean time to acknowledge_ (MTTA) metric specifically tracks the efficiency of the SOC team in responding to a generated alert.

**Note:** In certain SOAR advanced reports, such as in the **[Performance Analysis - Handling Times](https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-reports/using-looker-explores-in-soar-reports#perf-handling-times)** dashboard, _MTTD_ quantifies the average time from case creation until the case is assigned to a user, which is closer in meaning to mean time to _acknowledge_ (MTTA). (The standard definition for MTTD refers to the time from the initial event to the creation of the detection.) 

  * To reduce case-acknowledgement latency, optimize alert routing, tuning, and automation (for example, using playbooks for auto-assignment or enrichment) to quickly move the alert to the triage stage. 



## What's next

  * To learn about how _rule replays_ (also called _cleanup runs_) manage late-arriving data and context updates, and how this affects the MTTD metrics, see [Understand rule replays and MTTD](https://docs.cloud.google.com/chronicle/docs/detection/rule-replays).
  * To learn more about rule detection delays in Google SecOps, contributing factors, troubleshooting, and techniques to reduce delays, see [Understand rule detection delays](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
