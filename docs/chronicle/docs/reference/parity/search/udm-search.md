---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/udm-search/
title: UdmSearch parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:04.675647+00:00
---

# UdmSearch parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/udm-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# UdmSearch parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Search API (**`UdmSearch`**) to the modern Chronicle API (**`UdmSearch`**).

## Protocol and mapping overview

Feature | Legacy API (`UdmSearch`) | Modern Chronicle API (`UdmSearch`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/events.udmSearch`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `UdmSearchRequest` scopes queries under target instance environments and introduces support for SQL syntax dialects.

Legacy field (`UdmSearchRequest`) | Modern field (`UdmSearchRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** Scopes the search query under target instance environments: `projects/{project}/locations/{location}/instances/{instance}`.  
`query` | `query` | `string` | **Parity mapped:** Boolean structured query string (for example, `metadata.event_type = "NETWORK_CONNECTION"`). Note: Proto tag number changed from 1 to 2.  
`time_range` | `time_range` | `Interval` | **Parity mapped:** Required time interval `[start_time, end_time)`. Note: Proto tag number changed from 2 to 3. Rename to `timeRange` in JSON.  
`limit` | `limit` | `int32` | **Parity mapped:** Maximum returned results (coerced to 10k max). Note: Proto tag number changed from 3 to 4.  
— | `query_dialect` | `enum` | **New parameter:** Selects query syntax dialect (`QueryDialect` enum: `YL2` or `SQL`). Defaults to `YL2`. Rename to `queryDialect` in JSON.  
— | `simulated_data_visibility` | `enum` | **New parameter:** Controls whether simulated or test telemetry data is included in results (`SimulatedDataVisibility`). Rename to `simulatedDataVisibility` in JSON.  
  
* * *

## Response payload field-by-field parity

Both APIs return matched event arrays and truncation reporting flags, with the modern response adding support for SQL statistics tables.

Legacy field (`UdmSearchResponse`) | Modern field (`UdmSearchResponse` message) | Field type | Parity and migration notes  
---|---|---|---  
`events` | `events` | `repeated Event` | **Parity mapped:** Array of matched UDM events. As established under `GetEvent` guide, the modern `Event.name` property formats event IDs as URL-encoded Base64.  
`more_data_available` | `more_data_available` | `bool` | **Parity mapped:** Flag indicating result truncation when matches exceed limit. Rename to `moreDataAvailable` in JSON.  
— | `stats_data` | `StatsData` | **New field:** Returns tabular statistical columns and rows when the query is executed as an aggregation or statistical SQL query. Rename to `statsData` in JSON.  
  
### Nested StatsData property mappings

The fields mapping inside statistical data structures is as follows:

Legacy field | Modern field (`StatsData` message) | Field type | Parity and migration notes  
---|---|---|---  
— | `columns` | `repeated StatsColumn` | **New field:** Describes the header schema and data types of returned statistical columns.  
— | `rows` | `repeated StatsRow` | **New field:** Tabular rows containing repeated `StatsColumnValue` items matching column schemas.  
  
* * *

## Key differences

  * **Service consolidation:**
    * Legacy UDM searching was housed under `SearchService` (`UdmSearch`).
    * Modern Chronicle API standardizes this under `EventService` (`UdmSearch`), isolating event lookups from general search tooling.
  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **SQL query and statistics support:**
    * The modern Chronicle API introduces `query_dialect` (`SQL`), enabling analytical group-by aggregation queries whose tabular outputs are returned using `stats_data`.
  * **Proto tag number shifts:**
    * Within protobuf formatting, tag numbers shifted by +1 across request fields (`query` moved from tag 1 to 2; `time_range` from tag 2 to 3; `limit` from tag 3 to 4).
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/events.udmSearch`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
