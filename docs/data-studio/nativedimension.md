---
url: https://docs.cloud.google.com/data-studio/nativedimension/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:02.350546+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/nativedimension/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# NATIVE_DIMENSION

Returns the result of a BigQuery SQL expression as evaluated by the underlying dataset.

The `NATIVE_DIMENSION` function lets you write SQL directly into a Data Studio field. This is useful for functions that are not included in the [function list](https://docs.cloud.google.com/data-studio/function-list), but that your database supports.

**Note:** Native functions are disabled by default. See the **Enabling native functions** section in this article for instructions on how to enable native functions.

## Enabling native functions

Native functions are disabled by default and are managed at the data source level.

If you are an owner of a BigQuery data source, you can enable native functions for the data source by following these steps:

  1. In Data Studio, [edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. In the top right of the data source editor, click **Native functions**.
  3. In the **Native functions** dialog, select **On**.
  4. Click **Save**.



If you disable native functions, no users can create fields using native functions. Additionally, any existing charts that reference fields with native functions will display an error.

## Sample usage

```NATIVE_DIMENSION("JSON_VALUE('{"name": "Dana"}','$.name')","STRING")```

## Syntax

```NATIVE_DIMENSION( expression, type )```

### Parameters

`expression` \- An expression to be evaluated by the underlying dataset. This can be any valid BigQuery SQL that would go into a single column of a SELECT statement. The expression cannot include any aggregations.

`type` \- A data type literal. See the following section for the types that this function supports.

###  NATIVE_DIMENSION  types

You can select from the following types:

Type  |  Expected data  |  Report examples   
---|---|---  
` STRING ` |  Zero or more letters, numbers, characters, or symbols.  |  ` A1B2C3 `  
` BOOL ` |  A logical value.  |  ` true ` ` false `  
` DOUBLE ` |  A floating point number.  |  ` 1,234.56 `  
` INT64 ` |  An integer.  |  ` 1,234 `  
` DATE ` |  A calendar date.  |  ` 2020-09-21 `  
` DATETIME ` |  A calendar date with time.  |  ` 2020-09-21 12:35 PM `  
` GEOGRAPHY ` |  A collection of points and polygons that correspond to the [ BigQuery geography data type ](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#geography_type).  Only the BigQuery functions ` POINT ` and ` POLYGON ` are supported.  |  ` POINT(32 210)` ` POLYGON((0 0, 2 2, 2 0, 0 0), (2 2, 3 4, 2 4, 2 2)) `  
  
If your expression returns a timestamp data type, such as BigQuery's [`TIMESTAMP`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp_type) type, use the [`CAST`](https://docs.cloud.google.com/data-studio/cast) function to cast it to a `DATETIME` type. For example:

`NATIVE_DIMENSION("CAST({ expression } AS DATETIME)", "DATETIME")`

**Important:** Data Studio will return an error if your expression returns an unsupported data type, such as `ARRAY`, `STRUCT`, or `JSON`.

## NATIVE_DIMENSION examples

### JSON functions in SQL

Assume that your data includes a **users_ages_json** field whose values are formatted as JSON payloads. An example row value of this field might look like the following example:

```{"name": "Jakob", "age": "26"}```

Use the ```NATIVE_DIMENSION``` function to retrieve the age from **users_ages_json** , using BigQuery's ``[`JSON_VALUE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#json_value)`` function:

```NATIVE_DIMENSION("JSON_VALUE(user_ages_json, '$.age')","INT64")```

For this example row value, the ```NATIVE_DIMENSION``` function would return the age `26` as an integer.

## Limits of NATIVE_DIMENSION

### Who can use native functions

If native functions are enabled, owners and editors of the data source can create fields with native functions on the data source.

Viewers of the data source can use fields with native functions in charts. However, viewers cannot create new fields using native functions, nor can they edit any fields using native functions.

### Aggregate fields

You cannot include any aggregated fields in the `expression` parameter.

### Window functions

You cannot include any [window functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls) in the `expression` parameter.

### Blends

You cannot create a field with the ```NATIVE_DIMENSION``` function on a [blended data source](https://docs.cloud.google.com/data-studio/how-blends-work).

However, you can create a field with this function prior to blending and then use that field in a blend.

### TIMESTAMP data types

If your expression returns a timestamp data type, such as BigQuery's ``[`TIMESTAMP`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp_type)`` type, use the ``[`CAST`](https://docs.cloud.google.com/data-studio/cast)`` function to cast it to a **DATETIME** type. For example:

```NATIVE_DIMENSION("CAST({expression} AS DATETIME)", "DATETIME")```

## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)
  * [`CAST` function](https://docs.cloud.google.com/data-studio/cast)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
