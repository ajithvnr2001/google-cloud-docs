---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/overview-of-aliasing-and-enrichment/
title: Data enrichment and aliasing overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:31.069890+00:00
---

# Data enrichment and aliasing overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/overview-of-aliasing-and-enrichment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Data enrichment and aliasing overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document provides an overview of how Google Security Operations enriches raw logs after converting them to normalized Unified Data Model (UDM) events. Google SecOps provides different enrichment capabilities during ingestion and search.

## Enrichment during ingestion

  * [**UDM enrichment**](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment): Merges normalized data from context sources into UDM event sources to create a single enriched UDM event. These pipelines operate in near-real time and re-enrichment pipelines handle late-arriving data.
  * [**Aliasing service**](https://docs.cloud.google.com/chronicle/docs/event-processing/aliasing-overview): Keeps track of users and assets over time, merging multiple UDM Enrichment using aliasing to add context to a UDM indicator or event. 



## Enrichment during search

  * [**Entity Context Graph (ECG)**](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph): Combines customer log data, asset information, user identity, and multiple sources of threat intelligence to construct both timed and timeless entities and computed attributes (for example, prevalence, first seen, or last seen).
  * [**Data tables**](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables): Act as lookup tables with defined columns. The data is stored in rows that are joined at query time with your UDM events. You can define the data in data tables and manage their lifecycle.



Aliasing, UDM enrichment, and ECG are derived from your parsed security data.

For more information on sources that can provide context data, see the following topics:

  * [Ingest data using the entity data model](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities)
  * [Key UDM fields](https://docs.cloud.google.com/chronicle/docs/reference/important-udm-fields#key_udm_fields): Search for **aliasing** to view the important UDM fields.



## Viewing events

View events in the [Event Viewer's](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#event-viewer) **Event Fields** tab. This tab displays UDM event fields in a hierarchical tree structure, labeled **Selected**. Each UDM field is labeled with an icon indicating whether the field contains enriched or unenriched data. The icon labels are the following:

  * **U** : Unenriched fields pull values directly from the original raw log during the normalization process.
  * **E** : Enriched fields contain values that Google SecOps generates to provide additional context about artifacts in your environment.



Enriched fields show all associated sources to help you with validation, troubleshooting, auditing, and compliance. You also filter fields by their enrichment source to refine your view.

## Supported aliasing and UDM enrichment capabilities

Google SecOps supports aliasing and enrichment for the following:

  * Assets
  * Users
  * Processes
  * File hash metadata (VirusTotal)
  * Geographic locations
  * Cloud resources



## Supported ECG capabilities

Google SecOps supports the following ECG-related enrichments for search:

  * Prevalence
  * First seen and last seen
  * WHOIS data
  * VirusTotal relationship data
  * Tor exit node IP addresses
  * Google Threat Intelligence IOCs
  * Safe Browsing Threat lists



Enrichment during ingestion and search help you balance the trade-off between latency and accuracy for detections, searches, and dashboards. UDM enrichment and aliasing simplify the user experience by writing enrichments directly to UDM events. ECG and data tables provide flexibility and can be applied to specific use cases.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
