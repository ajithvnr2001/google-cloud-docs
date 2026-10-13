---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-StandardSql-Field/
title: BigQuery API - Class Google::Cloud::Bigquery::StandardSql::Field (v1.64.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:04.167462+00:00
---

# BigQuery API - Class Google::Cloud::Bigquery::StandardSql::Field (v1.64.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-StandardSql-Field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery API - Class Google::Cloud::Bigquery::StandardSql::Field (v1.64.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.64.0 (latest)  1.63.1  1.62.0  1.61.1  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.1  1.51.1  1.50.0  1.49.1  1.48.1  1.47.0  1.46.1  1.45.0  1.44.2  1.43.1  1.42.0  1.41.0  1.40.0  1.39.0  1.38.1 

Reference documentation and code samples for the BigQuery API class Google::Cloud::Bigquery::StandardSql::Field.

A field or a column. See [Routine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-Routine "Google::Cloud::Bigquery::Routine \(class\)") and [Argument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-Argument "Google::Cloud::Bigquery::Argument \(class\)").

## Inherits

  * Object 



## Example
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    dataset = bigquery.dataset "my_dataset"
    routine = dataset.create_routine "my_routine" do |r|
      r.routine_type = "SCALAR_FUNCTION"
      r.language = :SQL
      r.body = "(SELECT SUM(IF(elem.name = \"foo\",elem.val,null)) FROM UNNEST(arr) AS elem)"
      r.arguments = [
        Google::Cloud::Bigquery::Argument.new(
          name: "arr",
          argument_kind: "FIXED_TYPE",
          data_type: Google::Cloud::Bigquery::StandardSql::DataType.new(
            type_kind: "ARRAY",
            array_element_type: Google::Cloud::Bigquery::StandardSql::DataType.new(
              type_kind: "STRUCT",
              struct_type: Google::Cloud::Bigquery::StandardSql::StructType.new(
                fields: [
                  Google::Cloud::Bigquery::StandardSql::Field.new(
                    name: "name",
                    type: Google::Cloud::Bigquery::StandardSql::DataType.new(type_kind: "STRING")
                  ),
                  Google::Cloud::Bigquery::StandardSql::Field.new(
                    name: "val",
                    type: Google::Cloud::Bigquery::StandardSql::DataType.new(type_kind: "INT64")
                  )
                ]
              )
            )
          )
        )
      ]
    end

## Methods 

### #initialize
    
    
    def initialize(name, type) -> Field

Creates a new, immutable StandardSql::Field object.

**Overloads**
    
    
    def initialize(name, type) -> Field

Creates a new, immutable StandardSql::Field object. 

**Parameters**

  * **name** (String) — The name of the field. Optional. Can be absent for struct fields. 
  * **type** ([StandardSql::DataType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-StandardSql-DataType), String) — The type of the field. Optional. Absent if not explicitly specified (e.g., `CREATE FUNCTION` statement can omit the return type; in this case the output parameter does not have this "type" field). 



**Returns**

  * ([Field](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-StandardSql-Field)) — a new instance of Field 



### #name
    
    
    def name() -> String, nil

The name of the field. Optional. Can be absent for struct fields.

**Returns**

  * (String, nil) 



### #type
    
    
    def type() -> DataType, nil

The type of the field. Optional. Absent if not explicitly specified (e.g., `CREATE FUNCTION` statement can omit the return type; in this case the output parameter does not have this "type" field).

**Returns**

  * ([DataType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-StandardSql-DataType), nil) — The type of the field. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
