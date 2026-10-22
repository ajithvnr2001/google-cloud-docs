---
url: https://docs.cloud.google.com/app-optimize/about-reports/
title: About cost and utilization reports \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:43.130594+00:00
---

# About cost and utilization reports  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/about-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Guides ](https://docs.cloud.google.com/app-optimize/overview)



Send feedback 

#  About cost and utilization reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

App Optimize API lets you define and generate reports to help you understand and manage your Google Cloud costs and resource usage.

## Overview

To retrieve cost and utilization data with App Optimize API, you first create a _report_ resource in a Google Cloud project of your choice. This resource acts as a persistent definition for the data you want to analyze.

The project that stores your report doesn't need to be the source of the report's data. You can create a report in one project that analyzes data from a different source project or from an App Hub application.

After you create a report, the API generates the requested data asynchronously. You then use the report's resource name to fetch the resulting dataset when the report is ready.

The workflow is therefore:

  1. You create a report specifying your criteria.
  2. The system processes this request asynchronously.
  3. When the operation is complete, you read the resulting data.



This document details the structure and configurable parameters of App Optimize API reports, including available scope, dimensions, metrics, and filtering options, and explains the format of the data returned.

For information about limitations for cost and utilization, see [Understand the data](https://docs.cloud.google.com/app-optimize/overview#understand-data).

## Define a report

To create a report, you define a `Report` resource with the following configuration parameters, which are described in the next subsections:

Parameter | Type | Description  
---|---|---  
`scopes` | Array | The project or App Hub application to analyze. You must provide exactly one scope element.  
`dimensions` | Array | The attributes to retrieve and group the data by, including time-based groupings.  
`metrics` | Array | The specific measurements to return.  
`filter` | String | A [Common Expression Language (CEL)](https://cel.dev/) expression to narrow down the data, including time ranges.  
  
### Scopes

The `scopes` field defines the set of resources App Optimize API will analyze. Although the field is an array, you must specify exactly one element, which can be either a project or an App Hub application:

  * `project`: a string representing a Google Cloud project. It must be formatted as:
        
        projects/PROJECT_ID
        

Replace `PROJECT_ID` with the ID of the Google Cloud project to analyze. For example, `projects/my-project-1`.

  * `application`: a string representing the full resource name of an App Hub application. It must be formatted as:
        
        projects/PROJECT_ID/locations/LOCATION/applications/APPLICATION_ID
        

Replace the following:

    * `PROJECT_ID`: the ID of the App Hub host project.
    * `LOCATION`: the region of the App Hub application, such as `us-central1`.
    * `APPLICATION_ID`: the ID of the App Hub application.

For example, `projects/my-host-proj/locations/us-central1/applications/my-app`.




Here are example `scopes` arrays in JSON for a report creation request, showing a single scope element:

  * Scoping by project:
        
        "scopes": [
          {
            "project": "projects/my-project-1"
          }
        ]
        

  * Scoping by application:
        
        "scopes": [
          {
            "application": "projects/my-host-proj/locations/us-central1/applications/my-app"
          }
        ]
        




### Dimensions

Dimensions determine how what data is returned and how the data is grouped. For example, if you select `project` and `product_display_name`, the output contains one row for every unique combination of project and product name values found in the data.

Here is a table of supported dimensions:

Dimension | Type | Description | Example value  
---|---|---|---  
`project` | STRING | The Google Cloud project ID. | `projects/my-project`  
`application` | STRING | The App Hub application. | `projects/my-project/locations/us-central1/applications/my-app`  
`service_or_workload` | STRING | The App Hub service or workload. | `projects/my-project/locations/us-central1/applications/my-app/services/my-service`  
`resource` | STRING | The full resource name. | `//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/vm-1`  
`resource_type` | STRING | The API resource type. | `compute.googleapis.com/Instance`  
`location` | STRING | The Google Cloud region or multi-region. | `us-east1`  
`sku` | STRING | The billing SKU ID. | `4496-8C0D-228F`  
`product_display_name` | STRING | The Google Cloud product name. | `Compute Engine`  
`month` | STRING | The year and month. | `2024-01`  
`day` | STRING | The year, month, and day. | `2024-01-10`  
`hour` | STRING | The year, month, day, and hour. | `2024-01-10T00`  
  
The `location` dimension represents the Google Cloud region or multi-region to which costs and usage are attributed. How this location is reported depends on the location settings of the resources in the report scope:

  * For resources deployed in a specific zone, such as `us-central1-a`, the costs and usage are aggregated and attributed to the parent region. In this example, the `location` dimension would show `us-central1`.
  * For resources deployed in a region, such as `us-central1`, the `location` dimension reflects that specific region.
  * For resources deployed or configured for a multi-region, such as `us`, the `location` dimension reflects that multi-region.



#### Time dimensions

To aggregate results by time, include at least one time dimension, such as `month`, `day`, or `hour`, in the `dimensions` list. Bear in mind that:

  * All time dimensions use Pacific Time and respect Daylight Saving Time (DST).
  * Formats follow ISO 8601.
  * If the time range in the `filter` does not perfectly align with the selected time dimension's granularity, the range is expanded to cover the full periods. For example, filtering for part of a day with `dimension: ["month"]` will include data for the entire month.



### Metrics

Metrics are the quantitative values you want to measure for each group defined by your dimensions.

#### Cost metrics

Cost metric | Type | Description  
---|---|---  
`cost` | RECORD | The monetary cost in the requested currency.  
`network_cost` | RECORD | Total networking cost, including data transfer and data processing.  
`network_cost_standard_internet` | RECORD | Total cost for [Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard_tier) data transfer.  
`network_cost_premium_internet` | RECORD | Total cost for [Premium Tier](https://docs.cloud.google.com/network-tiers/docs/overview#premium_tier) data transfer.  
`network_cost_inter_region` | RECORD | Total cost for inter-region data transfer.  
`network_cost_inter_zone` | RECORD | Total cost for inter-zone data transfer.  
`network_cost_load_balancing_inbound` | RECORD | Total cost for inbound data processing by [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).  
`network_cost_load_balancing_outbound` | RECORD | Total cost of outbound data processing by [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).  
`network_cost_interconnect_inbound` | RECORD | Total cost of inbound data transfer through [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).  
`network_cost_interconnect_outbound` | RECORD | Total cost of outbound data transfer through [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).  
`resource_cost` | RECORD | Total resource cost.  
  
#### Utilization metrics

Utilization metric | Type | Description  
---|---|---  
`cpu_mean_utilization` | FLOAT64 | Average CPU utilization (0.0 to 1.0).  
`cpu_p95_utilization` | FLOAT64 | 95th percentile CPU utilization (0.0 to 1.0).  
`cpu_usage_core_seconds` | INT64 | Total CPU work performed.  
`cpu_allocation_core_seconds` | INT64 | Total CPU capacity provisioned.  
`memory_mean_utilization` | FLOAT64 | Average memory utilization (0.0 to 1.0).  
`memory_p95_utilization` | FLOAT64 | 95th percentile memory utilization (0.0 to 1.0).  
`memory_usage_byte_seconds` | INT64 | Total memory used over time.  
`memory_allocation_byte_seconds` | INT64 | Total memory provisioned over time.  
  
#### Valid combinations

Not all dimensions can be combined with every metric in App Optimize API. The following table shows examples of valid dimension sets and the metrics you can use with them. The API will return an error if an invalid combination is requested; refer to that error for valid combinations.

Dimensions | Supports `cost` metric | Supports `cpu_mean_utilization` metric  
---|---|---  
`application`, `product_display_name` |  |   
`application` |  |   
`location`, `product_display_name`, `project`, `resource`, `resource_type`, `sku` |  |   
`location`, `product_display_name`, `project`, `resource`, `resource_type` |  |   
`location`, `product_display_name`, `project`, `service_or_workload` |  |   
`location`, `product_display_name`, `project`, `sku` |  |   
`product_display_name`, `project` |  |   
`product_display_name`, `resource_type` |  |   
`product_display_name`, `resource` |  |   
`product_display_name` |  |   
`project` |  |   
  
## Filters

Use the `filter` field to narrow down the data using a CEL string. You can build your filter expressions using any of the fields listed in the Dimensions table.

Filtering must conform to these constraints:

  * All string field predicates must use exact string matches. For example, `location == 'us-east1'`.
  * Multiple predicates referring to the same string field must be joined using the logical OR operator, `||`. For example, `location == 'us-east1' || location == 'us-west1'`.
  * All other predicates must be joined using the logical AND operator, `&&`.
  * A predicate on a time dimension, such as `day`, specifying the start time must use the greater-than-or-equal-to comparison, `>=`.
  * A predicate on a time dimension specifying the end time must use the less-than comparison, `<`.



### Time range

If the `filter` omits time dimensions (`month`, `day`, `hour`), the report defaults to a seven-day range ending at the previous Pacific Time midnight, respecting DST. The maximum date range is 90 days before the current date, and the start time must be within the 90-day time window.

For example, if the current Pacific Time is `2026-01-05T12:00:00`, the default range is `2025-12-29T00:00:00` to `2026-01-05T00:00:00` Pacific Time. The earliest start time for the time range is `2025-10-07T00:00:00`.

Cloud Run metrics are only available for six weeks before the current date.

### Example filters

Here are some examples of how you can structure your CEL filter strings:

  * To filter the report data for a specific resource type, use the `==` operator on the `resource_type` dimension:
        
        resource_type == 'compute.googleapis.com/Instance'
        

  * To include only data from a single location, filter on the `location` dimension:
        
        location == 'us-east1'
        

  * To include data from a specific list of locations, use the `||` operator to combine conditions on the `location` dimension:
        
        location == 'us-east1' || location == 'us-west1'
        

  * To get data within a specific time range using hourly granularity, you can filter on the `hour` dimension. This example includes data from the start of 2024-01-01 up to, but not including, 2024-02-01:
        
        hour >= timestamp('2024-01-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')
        

  * To filter for whole days, use the `day` dimension. Note that day boundaries are interpreted in Pacific Time, so specifying the offset is best practice. This example includes all data for 2024-03-15 and 2024-03-16:
        
        day >= timestamp('2024-03-15T00:00:00-07:00') && day < timestamp('2024-03-17T00:00:00-07:00')
        

  * Similarly, you can filter by calendar months using the `month` dimension, again being mindful of Pacific Time for the exact boundaries. This example includes all data for October and November 2025:
        
        month >= timestamp('2025-10-01T00:00:00-07:00') && month < timestamp('2025-12-01T00:00:00-08:00')
        

  * To get data from the last 72 hours, use the `now()` and `duration()` functions on the `hour` dimension:
        
        hour >= now() - duration('72h')
        

  * To get data from the last seven days, you can use `duration()` with the `hour` dimension:
        
        hour >= now() - duration('168h')
        

  * Filtering for a specific calendar month, like the previous one, requires calculating the start and end timestamps in your application code. You then insert those calculated timestamps into the CEL expression. Conceptually, it might look like this, filtering on the `day` dimension:
        
        day >= timestamp('START_OF_LAST_MONTH') && day < timestamp('START_OF_THIS_MONTH')
        

Replace the following:

    * `START_OF_LAST_MONTH`: the ISO 8601 timestamp string representing the very beginning of the previous month in the Pacific Time zone, such as `2025-12-01T00:00:00-08:00`.
    * `START_OF_THIS_MONTH`: the ISO 8601 timestamp string representing the very beginning of the current month in the Pacific Time zone, such as `2026-01-01T00:00:00-08:00`.

You need to calculate these exact timestamp strings in your application code, taking into account the current date, time zone (Pacific Time), and Daylight Saving Time transitions.

  * You can combine string and time filters using the `&&` operator. This example filters for two locations within a specific two-month period:
        
        (location == 'us-east1' || location == 'us-west1') && hour >= timestamp('2023-12-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')
        

  * Here's a more complex example combining `resource_type`, `project`, and a `day`-based time range:
        
        resource_type == 'compute.googleapis.com/Instance' && project == 'projects/my-project' && day >= timestamp('2025-01-01T00:00:00-08:00') && day < timestamp('2025-02-01T00:00:00-08:00')
        




## Report data structure

When you successfully [read a report](https://docs.cloud.google.com/app-optimize/read-report), the service returns the data as `columns` and `rows`.

### Columns

The `columns` array describes the schema of the data, in the order that each field appears in the `rows`. Each object in the `columns` array has a `name`, `type`, and sometimes nested `columns` if the type is `RECORD`.

  * Dimensions you requested appear as fields with type `STRING`.
  * Metrics you requested appear as fields with types like `INT64`, `FLOAT64`, or `RECORD` for complex types like `cost`.



For example, with the REST API, if you request `dimensions: ["application", "product_display_name"]` and `metrics: ["cost", "cpu_mean_utilization"]`, then App Optimize API in response generates a `columns` array like this:
    
    
    "columns": [
      {
        "name": "application",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "product_display_name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "cost",
        "type": "RECORD",
        "mode": "NULLABLE",
        "columns": [
          {
            "name": "currency_code",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "units",
            "type": "INT64",
            "mode": "NULLABLE"
          },
          {
            "name": "nanos",
            "type": "INT64",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "cpu_mean_utilization",
        "type": "FLOAT64",
        "mode": "NULLABLE"
      }
    ]
    

### Rows

The `rows` field contains the actual data. Each row is an array of values representing a single record. The order of values within each inner array corresponds directly to the order of the fields defined in the `columns` array.

Continuing the example where `application`, `product_display_name`, `cost`, and `cpu_mean_utilization` were requested from the REST API, a single row in the generated `rows` array might look like this:
    
    
    "rows": [
      [
        "//apphub.googleapis.com/projects/my-proj/locations/us-central1/applications/my-app",
        "Compute Engine",
        {
          "currency_code": "USD",
          "units": "12",
          "nanos": 750000000
        },
        0.65
      ],
      [
        "//apphub.googleapis.com/projects/my-proj/locations/us-east1/applications/another-app",
        "Cloud Storage",
        {
          "currency_code": "USD",
          "units": "5",
          "nanos": 200000000
        },
        0.15
      ]
    ]
    

The following table visualizes how the values within a single row array map to the schema defined in the `columns` array, using the index of the value in the row array:

Index within row | Corresponding column | Type | Example value  
---|---|---|---  
0 | `application` | STRING | `"//apphub.googleapis.com/.../applications/my-app"`  
1 | `product_display_name` | STRING | `"Cloud Storage"`  
2 | `cost` | RECORD | `{ "currency_code": "USD", "units": "10", ... }`  
3 | `cpu_mean_utilization` | FLOAT64 | `0.65`  
  
Each element in the `rows` list is an array where the order of values matches the order of field definitions in the `columns` array. Thus, the value at index `n` in any given row array corresponds to the column defined at index `n` in the `columns` array.

### Interpreting cost metrics

When a report includes the `cost` metric, the value is returned as a `RECORD` containing the following fields, based on the standard [google.type.Money](https://cloud.google.com/docs/reference/protobuf/latest/google.type#google.type.Money) type:

Field | Type | Description  
---|---|---  
`currency_code` | STRING | The three-letter ISO 4217 currency code, such as "USD".  
`units` | INT64 | The whole units of the amount.  
`nanos` | INT64 | The nano (10-9) units of the amount. Must be between -999,999,999 and +999,999,999 inclusive.  
  
To get the full monetary value, you combine the `units` and the `nanos` fields. The `nanos` field represents the fractional part of the currency value. For example:

  * If `currency_code` is "USD", `units` is `106`, and `nanos` is `321590000`: The value is 106 + (321,590,000 / 1,000,000,000) = 106.32159 USD.

  * If `currency_code` is "EUR", `units` is `5`, and `nanos` is `750000000`: The value is 5 + (750,000,000 / 1,000,000,000) = 5.75 EUR.




You would typically use a standard currency formatting library to display this value in a user-friendly format, including the appropriate currency symbol.

For more information on the data returned by the API and to understand its limitations, see [Understand the data](https://docs.cloud.google.com/app-optimize/overview#understand-data).

## Report expiry

Each report is automatically deleted from the App Optimize API service 24 hours after the report's creation. After this time, the report and its data cannot be retrieved through the API. To check a report's scheduled expiration time, obtain its [metadata](https://docs.cloud.google.com/app-optimize/get-report-metadata) and view the `expireTime` field.

## What's next

  * [Create a report](https://docs.cloud.google.com/app-optimize/create-report)
  * [List reports](https://docs.cloud.google.com/app-optimize/list-reports)
  * [Get a report's metadata](https://docs.cloud.google.com/app-optimize/get-report-metadata)
  * [Read a report's data](https://docs.cloud.google.com/app-optimize/read-report)
  * [Delete a report](https://docs.cloud.google.com/app-optimize/delete-report)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
