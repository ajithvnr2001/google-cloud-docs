---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/resources/bigquery-schema-changes/
title: BigQuery schema changes \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:17:32.577791+00:00
---

# BigQuery schema changes  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/resources/bigquery-schema-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/manufacturing-data-engine/docs/release-notes)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BigQuery schema changes

This guide shows any updates on data schema changes when releasing new Manufacturing Data Engine (MDE) versions.

## Changes from versions 1.2 to 1.3

Some BigQuery table schema changes from v1.2 to v1.3 are **not** backwards-compatible. The following table describes these changes.

### Record tables

All records in MDE v1.2 were stored in one of three archetype tables. In MDE v1.3, records are stored in tables per Type (_record tables_) where each Type is tied to a specific Archetype. The following table is an overview of the key changes in field names:

Nr | Archetype | Field name in v1.3 record table | Data type v1.3 | Field name in v1.2 archetype table  
---|---|---|---|---  
1 | All | id | string | id  
2 | All | tag_name | string | tagName  
3 | All | type_version | integer | N/A  
4 | All | embedded_metadata | JSON | payloadQualifier  
5 | All | cloud_metadata_ref | JSON | N/A  
6 | All | materialized_cloud_metadata | JSON | N/A  
8 | All | ingest_timestamp | timestamp | ingestTimestamp  
9 | All | source_message_id | string | messageId  
10 | DDS, CDS | data | JSON | payload  
11 | NDS | value | numeric | payload  
12 | DDS, NDS | event_timestamp | timestamp | eventTimestamp  
13 | CDS | event_timestamp_start | timestamp | eventTimestampStart  
14 | CDS | event_timestamp_end | timestamp | eventTimestampEnd  
15 | CDS | duration | integer | duration  
16 | NDS-C, DDS-C, CDS-C* | cluster_column_1 | string | N/A  
17 | NDS-C, DDS-C, CDS-C* | cluster_column_2 | string | N/A  
18 | NDS-C, DDS-C, CDS-C* | cluster_column_3 | string | N/A  
19 | NDS-C, DDS-C, CDS-C* | cluster_column_4 | string | N/A  
20 | All | N/A | N/A | uptime  
21 | All | N/A | N/A | downtime  
22 | All | N/A | N/A | currentState  
23 | All | N/A | N/A | previousState  
24 | All | N/A | N/A | payloadKV  
25 | All | N/A | N/A | edgeTagName  
26 | All | N/A | N/A | payloadQualifierKV  
27 | All | N/A | N/A | metadataKV  
28 | All | N/A | N/A | metadataKV  
  
Archetype references:

  * **NDS-C** : Numeric Data Series Clustered Archetype.
  * **DDS-C** : Discrete Data Series Clustered Archetype.
  * **CDS-C** : Continuous Data Series Clustered Archetype.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
