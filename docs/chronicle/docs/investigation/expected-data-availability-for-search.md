---
url: https://docs.cloud.google.com/chronicle/docs/investigation/expected-data-availability-for-search/
title: Understand data availability for search \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:19.659914+00:00
---

# Understand data availability for search  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/expected-data-availability-for-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand data availability for search

Supported in:

Google SecOps 

This document details the data ingestion lifecycle, including end-to-end data flow and latency, and how these factors impact the availability of recently ingested data for querying and analysis.

## Ingest and process data in Google SecOps

This section describes how Google SecOps ingests, processes, and analyzes security data.

### Data ingestion

The [data ingestion](https://docs.cloud.google.com/chronicle/docs/secops/secops-ingestion) pipeline begins by collecting your raw security data from sources such as:

  * Security logs from your internal systems
  * Data stored in Cloud Storage
  * Your Security Operations Center (SOC) and other internal systems



Google SecOps brings this data to the platform using one of its secure ingestion methods. 

The primary ingestion methods are:

  * **Direct Google Cloud ingestion**

Google SecOps uses [direct Google Cloud ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs#option-1-direct-ingestion) to automatically pull in logs and telemetry data from your organization's Google Cloud, including Cloud Logging, Cloud Asset Inventory metadata, and Security Command Center Premium findings.

  * **Ingestion APIs**

Send data directly to Google SecOps using its public REST [Ingestion APIs](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api). You use this method for custom integrations or to send data as either unstructured logs or pre-formatted Unified Data Model (UDM) events.

  * **Bindplane agent**

You can deploy the versatile [Bindplane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent) in your environment (on-premises or other clouds) to collect logs from a wide variety of sources and forward them to Google SecOps.

  * **Data feeds**

In Google SecOps, you configure [data feeds](https://docs.cloud.google.com/chronicle/docs/administration/feed-management-overview) to pull logs from third-party sources, such as specific third-party cloud storage buckets (like Amazon S3) or third-party APIs (like Okta or Microsoft 365).




### Normalization and data enrichment

Once data arrives in Google SecOps, the platform processes it through the following stages:

  1. **Parsing and normalization**

A parser first processes raw log data to validate, extract, and transform the data from its original format into the standardized [UDM](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview). [Parsing and normalization](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions) lets you analyze disparate data sources (for example, firewall logs, endpoint data, cloud logs) using a single, consistent schema. The original raw log remains stored alongside the UDM event.

  2. **Indexing**

After normalization, Google SecOps indexes the UDM data to deliver fast query speeds across massive datasets, making the UDM events searchable.

  3. **UDM Aliasing and enrichment**

     * Google SecOps performs [UDM aliasing and enrichment](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment) to enrich UDM events with valuable context, by identifying and adding context data and indicators for log entities. For example, it connects a user's `login name` to their various `IP addresses`, `hostnames`, and `MAC addresses`.
     * **Geolocation:** Google SecOps enriches IP addresses with [geolocation](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment#ip-geolocation-enrichment) data.
  4. **ECG enrichment**

     * Google SecOps performs [ECG aliasing](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph#merging-ecg) which merges context from multiple sources (such as IdPs, CMDBs, and threat intelligence), to build a consolidated entity profile in the [entity context graph](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph).

     * **Threat intelligence:** Google SecOps automatically compares event data against Google's vast threat intelligence, including sources like [Google Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph#ingest-google-threat-intelligence-data) and [Safe Browsing](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph#enrich-entities-with-information-from-safe-browsing-threat-lists), to identify known malicious threats, like `domains`, `IP addresses`, and `file hashes`.

     * **WHOIS:** Google SecOps enriches domain names with their public registration [WHOIS](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph#enrich-entities-with-whois-data) information.




### Data availability for analysis

After being processed and enriched, UDM data is immediately available for analysis:

  * **Real-time detection**

The **Detection Engine** automatically runs [Live Rule](https://docs.cloud.google.com/chronicle/docs/detection/run-rule-live-data)-enabled custom and Google-built rules against live incoming data to identify threats and generate alerts.

  * **Search and investigation**

An analyst can use the Search methods to search across all this normalized and enriched data. For example, using [UDM search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) to pivot between related entities (like a `user`, to their `asset`, to a malicious `domain`), and investigate alerts.




## Search methods

Google SecOps provides several distinct methods for searching your data, each serving a different purpose.

### UDM search

[UDM search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) is the **primary and fastest** search method, used for most investigations.

  * **What it searches:** It queries the normalized and indexed UDM events. Because all data is parsed into this standard format, you can write one query to find the same activity (like a login) across all your different products (for example, Windows, Okta, Linux).
  * **How it works:** You use a specific syntax to query fields, operators, and values.
  * **Example:** `principal.hostname = "win-server" AND target.ip = "10.1.2.3"`

Results are typically available within 2–15 minutes of ingestion.




### Raw log search

Use [Raw log search](https://docs.cloud.google.com/chronicle/docs/investigation/search-raw-logs) to find something in the original, unparsed log message that may not have been mapped to a UDM field. This search method is optimized for high-velocity hunts, typically returning results in under 2 seconds for specific indicators such as file hashes or IP addresses.

  * **What it searches:** It scans the original, raw text of the logs _before_ they were parsed and normalized. This is useful for finding specific strings, command-line arguments, or other artifacts that aren't indexed UDM fields.
  * **How it works:** You use the `raw =` prefix. It can be slower than UDM search because it doesn't search indexed fields.
  * **Example (String):** `raw = "PsExec.exe"`
  * **Example (Regex):** `raw = /admin\$/`



### Stats search

Use [Stats search](https://docs.cloud.google.com/chronicle/docs/investigation/statistics-aggregations-in-udm-search) for long-term trending that aggregates millions of rows of data. Because the platform must perform statistical analysis and grouping, expect longer load times for these queries.

### Natural language search (Gemini)

[Natural language search (Gemini)](https://docs.cloud.google.com/chronicle/docs/investigation/generate-udm-search-queries-gemini#nl-to-udm) lets you use plain English to ask questions, which Gemini then translates into a formal UDM query.

  * **What it searches:** It provides a conversational interface to query UDM data.
  * **How it works:** You type a question, and Gemini generates the underlying UDM search query for you, which you can then run or refine.
  * **Example:** "Show me all failed logins from user 'bob' in the last 24 hours"



### SOAR search

[SOAR search](https://docs.cloud.google.com/chronicle/docs/soar/investigate/search/working-with-search-screen) is specific to **SOAR** components. You use it to manage security incidents, not to hunt in logs.

  * **What it searches:** It searches for **Cases** and **Entities** (like users, assets, IP addresses) within the SOAR platform.
  * **How it works:** You can use free-text or field-based filters to find cases by, for example, their ID, alert name, status, and assigned user.
  * **Example:** Search for `CaseIds:180` or `AlertName:Brute Force`



## Data ingestion pipeline to search availability

End-to-end data availability is the total time between when an event occurs and when it's available for search or rule execution in Google SecOps. This latency is the sum of the following two components:

  1. **Source-side availability delay:** The time between when an event occurs and when the source system makes the log data available for ingestion. This delay depends on the source system's architecture, processing, batching, and API publication schedules. Google SecOps cannot influence this delay. Examples include delays when a system writes logs to a storage bucket or publishes them to an API endpoint.

  2. **Google SecOps processing time:** The time Google SecOps requires to process the data after receiving it. This duration includes internal pipeline stages such as ingestion, parsing, normalization, indexing, and enrichment.




You must consider both components when troubleshooting data visibility timelines.

### Delays originating from the data source

The following factors can influence the source-side availability delay:

  * **Batch processing:** Some systems generate logs in batches at set intervals (for example, hourly).
  * **API latency:** The source API can have inherent delays in making new events queryable.
  * **Event creation and publication time:** An event timestamp in a log might be much earlier than the timestamp when the log is finalized and becomes available for collection.
  * **Throttling:** Source-side API rate limits can slow data retrieval.
  * **Initial backfill:** Serving and ingesting large volumes of historical data takes time.



These delays vary by data source and log type. For more details on ingestion methods, see [Data ingestion overview](https://docs.cloud.google.com/chronicle/docs/secops/secops-ingestion). The [Feed management API reference](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api) describes specific considerations for log types such as Microsoft Graph, SentinelOne, Okta, and CrowdStrike.

### Google SecOps processing time

The system processes newly ingested data through several steps. The duration of these steps determines when newly ingested data becomes available for querying and analysis.

The following table breaks down the processing steps for newly ingested data by search method. Newly ingested data becomes searchable after these steps are complete.

Search method | Data being searched | Processing steps contributing to availability time  
---|---|---  
  
  * **[UDM search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)**
  * **[Natural language search (Gemini)](https://docs.cloud.google.com/chronicle/docs/investigation/generate-udm-search-queries-gemini#nl-to-udm)**

| Normalized and enriched UDM events | 

  1. **Ingestion:** Log arrives at the Google SecOps ingestion point.
  2. **Parsing:** The raw log is identified and processed by its specific parser.
  3. **Normalization:** Data is extracted and mapped to the UDM schema.
  4. **Indexing (UDM):** The normalized UDM record is indexed for fast, structured search.
  5. **Enrichment:** Context (threat intelligence, geolocation, user or asset data) is added.

  
**[Raw log search](https://docs.cloud.google.com/chronicle/docs/investigation/search-raw-logs)** | Original, unparsed log text | 

  1. **Ingestion:** Log arrives at the Google SecOps ingestion point.

  
**[Detection Engine (Rules)](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules)** | Normalized events | 

  1. **UDM event availability:** Same steps as listed for UDM search.
  2. **Detection evaluation:** The Rules Engine evaluates logs in "micro-batches," typically firing detections within 5–10 minutes of event arrival.

  
**[SOAR search](https://docs.cloud.google.com/chronicle/docs/soar/investigate/search/working-with-search-screen)** | Cases and entities |  This is a different lifecycle, as it searches for _alerts and cases_ , not logs. The time is based on: 

  1. **UDM event availability:** Uses the same processing steps listed for "UDM search".
  2. **[Detection](https://docs.cloud.google.com/chronicle/docs/detection/detection-delays#detect-rules):** A Detection Engine rule must match the UDM event(s).
  3. **Alert generation:** The system creates a formal alert from the detection.
  4. **Case creation:** The SOAR platform ingests the alert and creates a case.

  
  
## Example data flow

The following example demonstrates how Google SecOps ingests, processes, enhances, and analyzes your security data, making it available for searches and further analysis.

**Example of data processing steps**

  1. Retrieves security data from cloud services like Amazon S3 or from the Google Cloud. Google SecOps encrypts this data in transit.
  2. Separates and stores your encrypted security data in your account. Access is limited to you and a small number of Google personnel for product support, development, and maintenance.
  3. Parses and validates raw security data, making it easier to process and view.
  4. Normalizes and indexes the data for quick searches.
  5. Stores the parsed and indexed data within your account.
  6. Enriches with context data. 
  7. Offers secure access for users to search and review their security data.
  8. Compares your security data with the Google Threat Intelligence malware database to identify matches. In a Google SecOps event view, such as the Asset view, click **VT Context** to see Google Threat Intelligence information. Google SecOps doesn't share your security data with Google Threat Intelligence.



![Flow and processing of data to Google SecOps ](https://docs.cloud.google.com/chronicle/images/data-flow.svg)

### Examples of the expected time until Search availability

The expected time until the newly ingested data becomes available for Search is the sum of the flow durations along the data flow.

For example, a typical average time for data availability in UDM search is approximately 5 minutes and 30 seconds from when the data is sent to the Google SecOps ingestion service.

Data flow step | Description | Flow duration  
---|---|---  
**Cloud Storage** to **Raw logs** | Ingests raw logs from Cloud Storage. | Less than 30 seconds  
**Security logs** to **Data forwarding service** | Transmits security logs from internal systems to the platform. | N/A  
**Data forwarding service** to **Raw logs** | Sends raw security data received from various sources to the ingestion pipeline. | Less than 30 seconds  
**Raw logs** to **Parse and validate** | Parses and validates raw logs into the UDM format. | Less than 3 minutes  
**Parse and validate** to **Index** | Indexes the parsed UDM data for fast searching. | N/A  
**Index** to **Parsed customer data** | Makes the indexed data available as parsed customer data for analysis. | Less than 2 minutes  
  
## Troubleshooting

This section provides troubleshooting guidance.

### Latency and limits

Processing and visualization delays within the Google SecOps platform are subject to the following architectural limits after Google SecOps receives the data:

  * **Search visibility:** 2 to 15 minutes after ingestion.
  * **Rule execution:** 5 to 10 minutes after event arrival.

**Note:** For search ranges greater than 30 days, recently ingested events may take longer to appear. For near-real-time results, select a time range of 30 days or less.**Note:** These times start after Google SecOps receives the data. End-to-end data availability also depends on delays originating from the data source that occur before the data enters the Google SecOps pipeline.**Caution:** If a change doesn't immediately appear in the UI, it doesn't necessarily indicate a sync failure. If the event occurred less than 15 minutes ago for search or 10 minutes ago for rules, the data is likely still in the standard processing pipeline. The delay doesn't indicate a system failure.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
