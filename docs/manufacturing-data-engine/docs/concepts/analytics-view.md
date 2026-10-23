---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/analytics-view/
title: Analytics views \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:14.306732+00:00
---

# Analytics views  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/analytics-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Analytics views

Manufacturing Data Engine (MDE) Analytics views is a powerful feature designed to streamline data analysis and reporting within your MDE environment. By automatically generating BigQuery views that consolidate type-specific data, metadata, and associated dimensions, MDE simplifies the creation of comprehensive queries and dashboards.

## Concepts

An Analytics view is a prebuilt BigQuery view tailored to a specific type version within your MDE environment. This view acts as a unified data source, seamlessly joining the type table (your core fact table) with all relevant metadata buckets (your dimensions) associated with that type version.

This consolidation simplifies querying by eliminating the need for manual joins across multiple tables. Analytics views also flatten metadata instances and data fields based on predefined JSON schemas.

## How Analytics views work

  1. **Automatic creation:** MDE automatically creates a dedicated Analytics view within the `mde_analytics` dataset for each unique type version. Views for new type versions are always updated in-place.

  2. **Metadata flattening:** The view query intelligently flattens the JSON metadata instances (dimension members) associated with the type. Each field within the JSON schema of the metadata bucket version associated with the type version is mapped to a corresponding BigQuery field, adhering to the following well-defined type mapping:

     * String -> String
     * Array -> JSON
     * Object -> JSON
     * Number -> Float64
     * Integer -> Int64
     * Boolean -> Bool
     * null -> null



The resulting BigQuery fields are always prefixed with the metadata bucket name.

  1. **Nested JSON Handling:** Nested JSON fields are converted into BigQuery fields by concatenating their path elements with underscores. For example, `{"location":{"city":"Düsseldorf"}}` becomes `location_city`.

  2. **"Data" Field Flattening:** The view extends flattening to the JSON "data" field for non-numeric types based on the schema defined for the type, ensuring comprehensive data accessibility. Flattening is performed only when a schema for the "data" field is defined. For more details about data field schemas, see [data field](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/type#data_field).

  3. **Field Naming and Conflicts:** In case of a naming conflict, fields derived from metadata buckets are prefixed with the bucket name.




## View Schema

The final view schema encompasses a rich set of fields:

  * **All fields from the underlying type table:** Your core manufacturing data.
  * **All flattened fields from each metadata instance:** Detailed contextual information about your records.
  * **All flattened fields from the "data" field (non-numeric):** Additional data points specific to the type.



## Benefits of Analytics views

The following are the benefits of Analytics views:

  * **Simplified Querying:** Eliminate complex joins by querying a single view for comprehensive data.
  * **Accelerated Analysis:** Spend less time on data preparation and more time on extracting insights.
  * **Standardized Structure:** Consistent schema across type versions facilitates standardized reporting.
  * **Automation:** MDE handles view creation and maintenance, avoiding you from manual tasks.



## Getting started

Analytics views are ready to use as soon as you start working with types in MDE. You can explore the automatically generated views in your Google Cloud project with the following steps:

  1. Select BigQuery.
  2. Click **Studio** on the left panel.
  3. Select the `mde_analytics` dataset on the BigQuery explorer window.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
