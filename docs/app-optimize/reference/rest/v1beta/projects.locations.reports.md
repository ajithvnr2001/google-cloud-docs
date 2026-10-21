---
url: https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports
title: REST Resource: projects.locations.reports \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:14.257689+00:00
---

# REST Resource: projects.locations.reports  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  REST Resource: projects.locations.reports Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Report
    * JSON representation
  * Scope
    * JSON representation
  * Methods



## Resource: Report

A configuration that defines the parameters for the data represented by a report.

JSON representation  
---  
      
    
    {
      "name": string,
      "dimensions": [
        string
      ],
      "metrics": [
        string
      ],
      "scopes": [
        {
          object ([Scope](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports#Scope))
        }
      ],
      "filter": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "expireTime": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of this report.  
`dimensions[]` |  `string` Required. A list of dimensions to include in the report. Supported values:

  * `project`
  * `application`
  * `service_or_workload`
  * `resource`
  * `resourceType`
  * `location`
  * `product_display_name`
  * `sku`
  * `month`
  * `day`
  * `hour`

To aggregate results by time, specify at least one time dimension (`month`, `day`, or `hour`). All time dimensions use Pacific Time, respect Daylight Saving Time (DST), and follow these ISO 8601 formats:

  * `month`: `YYYY-MM` (e.g., `2024-01`)
  * `day`: `YYYY-MM-DD` (e.g., `2024-01-10`)
  * `hour`: `YYYY-MM-DDTHH` (e.g., `2024-01-10T00`)

If the time range filter does not align with the selected time dimension, the range is expanded to encompass the full period of the finest-grained time dimension.For example, if the filter is `2026-01-10` through `2026-01-12` and the `month` dimension is selected, the effective time range expands to include all of January (`2026-01-01` to `2026-02-01`).  
`metrics[]` |  `string` Required. A list of metrics to include in the report. Supported values:

  * `cost`
  * `resourceCost`
  * `network_cost`
  * `network_cost_standard_internet`
  * `network_cost_premium_internet`
  * `network_cost_inter_region`
  * `network_cost_inter_zone`
  * `network_cost_load_balancing_inbound`
  * `network_cost_load_balancing_outbound`
  * `network_cost_interconnect_inbound`
  * `network_cost_interconnect_outbound`
  * `cpu_mean_utilization`
  * `cpu_usage_core_seconds`
  * `cpu_allocation_core_seconds`
  * `cpu_p95_utilization`
  * `memory_mean_utilization`
  * `memory_usage_byte_seconds`
  * `memory_allocation_byte_seconds`
  * `memory_p95_utilization`

  
`scopes[]` |  `object (`[Scope](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports#Scope)`)` Optional. The resource containers for which to fetch data. Default is the project specified in the report's parent.No more than one scope is supported.  
`filter` |  `string` Optional. A Common Expression Language (CEL) expression used to filter the data for the report.Predicates may refer to any dimension. Filtering must conform to these constraints:

  * All string field predicates must use exact string matches.
  * Multiple predicates referring to the same string field must be joined using the logical OR operator ('||').
  * All other predicates must be joined using the logical AND operator (`&&`).
  * A predicate on a time dimension (e.g., `day`) specifying the start time must use a greater-than-or-equal-to comparison (`>=`).
  * A predicate on a time dimension specifying the end time must use a less-than comparison (`<`).

Examples:

  1. Filter by a specific resource type: `"resourceType == 'compute.googleapis.com/Instance'"`
  2. Filter data points that fall within a specific absolute time interval: `"hour >= timestamp('2024-01-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')"`
  3. Filter data points that fall within the past 72 hours: `"hour >= now - duration('72h')"`
  4. Combine string predicate with time interval predicate: `"(location == 'us-east1' || location == 'us-west1') && hour >= timestamp('2023-12-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')"`

If the filter omits time dimensions (`month`, `day`, `hour`), the report defaults to a 7-day range ending at the previous Pacific Time midnight, with Daylight Saving Time (DST) applied.For example, if the current Pacific Time is `2026-01-05T12:00:00`, the default range is `2025-12-29T00:00:00` to `2026-01-05T00:00:00` Pacific time.  
Defines this report's expiration time. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp in UTC of when this report expires. Once the report expires, it will no longer be accessible and the report's underlying data will be deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
End of mutually exclusive fields.  
  
## Scope

Specifies the report scope.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "project": string,
      "application": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`project` |  `string` Required. A Google Cloud Platform project to fetch data from.Format: `"projects/{project}"`.  
`application` |  `string` Required. An App Hub Application to fetch data from.Format: `"projects/{project}/locations/{location}/applications/{application}"`.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/create)`

|  Creates a new report.  
  
### `[delete](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/delete)`

|  Deletes the specified report.  
  
### `[get](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/get)`

|  Retrieves the details of a report configuration.  
  
### `[list](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/list)`

|  Lists reports within a given project.  
  
### `[read](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/read)`

|  Reads data within a specified report.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
