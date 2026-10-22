---
url: https://docs.cloud.google.com/chronicle/docs/detection/timestamp-definitions/
title: Timestamp definitions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:30.774344+00:00
---

# Timestamp definitions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/timestamp-definitions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Timestamp definitions

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains common timestamps for events and detections. For more information about timestamps, see [Date function](https://docs.cloud.google.com/chronicle/docs/reference/parser-syntax#date_function).

The following timestamps are related to events:

  * **Event timestamp** : Time when an event occurred and is stored in the `metadata.event_timestamp` UDM field. Rules and UDM searches use the `metadata.event_timestamp` field for queries.
  * **Collected timestamp** : Time when an event was collected by the local collection infrastructure, such as the forwarder, and started transit to Google Security Operations. This is stored in the `metadata.collected_timestamp` UDM field. Collection and transport delays between local collectors and Google Security Operations affect when logs arrive, but don't represent ingestion latency.
  * **Ingested timestamp** : Time when an event was received and ingested by Google Security Operations. This is stored in the `metadata.ingested_timestamp` UDM field. Even if a log arrives hours after its `metadata.event_timestamp` or `metadata.collected_timestamp` due to forwarding or network transit delays, Google Security Operations typically ingests and indexes the log shortly after arrival.

**Note:** A large difference between `metadata.event_timestamp` (or `metadata.collected_timestamp`) and `metadata.ingested_timestamp` indicates local collection or forwarding delay before the log reaches Google Security Operations. For example, if a log arrives five hours after the event occurred, that five-hour gap represents collection and transport delay outside of Google Security Operations, not ingestion latency. Once Google Security Operations receives the log (`metadata.ingested_timestamp`), ingestion typically finishes within seconds. Ingestion latency refers only to the time between when Google Security Operations receives the event and when the data becomes searchable or available for detection rules.

## Indexing and data availability timestamps

In addition to the event, collection, and ingestion timestamps, understanding when data becomes fully searchable and usable within Google Security Operations is crucial. This involves the indexing process, which makes ingested logs and UDM events available for various analysis and detection features.

The following section outlines data availability in relation to the indexing process:

  * **Raw Log Search Availability:** Raw logs become available for searching using the Raw log search feature very quickly after ingestion. This search method directly scans the original, unparsed log text for your query. Expected availability for raw log searching is often within seconds to a few minutes after the log arrives at the Google SecOps ingestion point.

  * **UDM Search Availability:** After raw logs are ingested, they go through parsing and normalization to be converted into Unified Data Model (UDM) events. Subsequently, these UDM events undergo indexing. The indexed UDM data is required for a UDM search and becomes available for querying typically within 2–15 minutes after the initial ingestion. A more precise average time is around 5 minutes from when data is sent to the Google SecOps ingestion service.

  * **Detection Rule Availability:** UDM events are used by the Detection Engine. For real-time and scheduled rules to evaluate against new data, the UDM events must be parsed, normalized, and indexed. Rule execution typically occurs within 5–10 minutes after the event arrives at the Google SecOps ingestion point, depending on the rule type and scheduling.




**Detecting Delays:**

When diagnosing perceived latency, distinguish between collection latency and ingestion latency:

  * **Collection latency (transport delay):** Compare `metadata.event_timestamp` or `metadata.collected_timestamp` with `metadata.ingested_timestamp`. A large gap indicates delays occurring in the local log source, forwarder, or network path before reaching Google SecOps.
  * **Ingestion and indexing latency:** Monitor the time difference between `metadata.ingested_timestamp` (when Google SecOps received the event) and when the event becomes queryable using UDM Search or available for rule execution.



While specific indexing completion timestamps are not directly exposed as UDM fields, the documented availability times for UDM Search and Detection Engine provide a guide to the indexing latency. Significant deviations from the expected 2–15 minute window after `metadata.ingested_timestamp` could indicate processing delays.

The following timestamps are stored with detections:

  * **Detection window** : For rules with a [`match` section](https://docs.cloud.google.com/chronicle/docs/yara-l/match-syntax), a detection is created over the time range, called the _detection window_. The event timestamps for events that triggered the detection are within the detection window.
  * **Detection timestamp** : For rules with a `match` section, the detection timestamp is the end time of the detection window. Otherwise, the detection timestamp is the `metadata.event_timestamp` of the event that generated the detection.
  * **Detection created timestamp** : Date and time the detection was created by detection engine.



## Where timestamps appear in the application

The following sections define where you can view these timestamps in the UI.

### UDM Event viewer

To open the **UDM Event** view, do the following:

  1. Perform a UDM Search.
  2. In the **Events** tab, select an event to open the [Event viewer](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#event-viewer)
  3. The **UDM event** pane displays the following data:

     * Event timestamp is stored in the `metadata.event_timestamp` UDM field (1).
     * Ingested timestamp is stored in the `metadata.ingested_timestamp` UDM field (2).

![UDM Event view](https://docs.cloud.google.com/chronicle/images/detection/udm-view-timestamp.png)




### Detections panel

To open the **Detections** view, do the following:

  1. Open **Detections** > **Rules & Detections**, and then click the **Dashboard** button.
  2. Click the rule name link under the **Rule name** column. The **Detections** panel appears and displays the following:

     * Detection timestamp appears in rows that identify a detection (1).
     * Event timestamp appears in rows that identify events (2).

![Detections view](https://docs.cloud.google.com/chronicle/images/detection/detection-view-timestamp.png)




### Alert view

To open the **Alert** view, do the following:

  1. Open **Detections** > **Alerts & IOCs**.
  2. Under the **Alerts** tab, click the alert name link in the **Name** column.
  3. Click the **Overview** tab to display the following:

     * Alert (or Detection) created timestamp appears in the **Alert Details** pane > **Created** field (1).
     * Detection window appears in the **Detection Summary** pane > **Detection window** field (2).
     * Detection timestamp appears is in the **Detection Summary** pane > **Alerts detected at** field (3).

![Alert view](https://docs.cloud.google.com/chronicle/images/detection/alert-view-timestamp.png)




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
