---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/auto-extraction/
title: Auto-extraction overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:34.712445+00:00
---

# Auto-extraction overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/auto-extraction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Auto-extraction overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document provides an overview of how data is automatically extracted to enhance the ability to ingest, process, and analyze data.

Google Security Operations uses [prebuilt parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers) to extract and structure log data using the Unified Data Model (UDM) schema. Managing and maintaining these parsers can be challenging due to several limitations: incomplete data extraction, the growing number of parsers to manage, and the requirement for frequent updates as log formats evolve.

To address these challenges, you can use the auto extraction feature. This feature automatically extracts key-value pairs from JSON-formatted and XML-formatted logs ingested into Google SecOps. It also supports Syslog-formatted logs that include a JSON message. This extracted data is stored in a UDM, map-type field called `extracted`. You can then use this data within UDM search queries, [Native Dashboards](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards), and YARA-L rules.

As a best practice, the UDM searches using extracted fields must include `metadata.log_type` in their query to improve search query performance.

The benefit of auto extraction is reduced reliance on parsers, ensuring that data remains available, even when a parser is not present or fails to parse a log.

## Parse and extract data from the raw log

  1. **Parsing** : Google SecOps attempts to parse logs using a parser specific to the log type, if available. If no specific parser exists, or if parsing fails, Google SecOps uses a general parser to extract basic information like ingested timestamp, log type, and metadata labels.

  2. **Data Extraction** : Auto extraction is not enabled by default. Opt-in and select the specific fields (data points) you want to extract from the logs.

  3. **Event Enrichment** : Google SecOps combines the parsed data and any custom-formatted fields to create enriched events, providing more context and detail.

  4. **Downstream Data Transfer** : These enriched events are then sent to other systems for further analysis and processing.


**Note:** Auto-extraction behavior depends on whether a parser is available for the log type:

  * **When there is a parser:** Default auto-extraction does not occur. You must explicitly opt-in to the specific fields needed, as explained in the Work with extractors section.
  * **When there is no parser:** Auto-extraction kicks in automatically and extracts the first 100 fields.



## Work with extractors

Extractors let you extract fields from all supported log sources, and are designed to optimize log management. By using extractors, you can reduce event size, enhance parsing efficiency, and gain better control over data extraction. This is especially useful for managing new log types or minimizing processing time. 

You can create extractors using the **SIEM Settings** menu or by performing a raw log search.

### Create extractors

  1. Go to the **Extract Additional Fields** pane using either of the following methods:

     * Click **SIEM Settings** > **Parsers** , and do the following: 
       1. In the **PARSERS** table that appears, identify a parser (log source) and click more_vert **Menu** > **Extend Parser** > **Extract Additional Fields**.
     * Use [Raw Log Scan](https://docs.cloud.google.com/chronicle/docs/investigation/search-raw-logs) and do the following: 
       1. Select the required log sources (parsers) from the **Log Sources** menu.
       2. From the raw log results, select a log source to open the **EVENT DATA** pane.
       3. In the **EVENT DATA** pane, click **Manage Parser** > **Extend Parser** > **Extract Additional Fields**.
     * Use [UDM search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#access_search) and do the following: 
       1. On the **EVENTS** tab in the UDM search results, select a log source to view the **Event Viewer** pane.
       2. On the **Raw Log** tab, click **Manage Parser** > **Extend Parser** > **Extract Additional Fields**.
  2. On the **Select Extractors** tab in the **Extract Additional fields** pane, select the required raw log fields. By default, you can select up to 100 fields. If no additional fields are available for extraction, a warning notice displays.

Click the **Reference Raw Log** tab to view the raw log data and preview the UDM output. 

  3. Click **Save**.




The newly created extractor is labeled as `EXTRACTOR`. Extracted fields are displayed in the UDM output as`extracted.field{"fieldName"}`.

### View extractor details

  1. Go to the extractor row in the **PARSERS** table and click more_vert **Menu** > **Extend Parser** > **View Extension**.
  2. On the **VIEW CUSTOM PARSERS** page, click the **Extensions and Extracted Fields** tab.



This tab displays information on parser extensions and extractor fields. You can modify or remove fields and preview the parser output from the **VIEW CUSTOM PARSERS** page.

### Limitations

  * If a batch UDM event size exceeds 8.2 MB, the raw logs and all the extracted fields are dropped.
  * If a single UDM event exceeds 500 KB, the extracted fields are dropped.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
