---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Status/
title: Cloud Bigtable API - Class Google::Cloud::Bigtable::Status (v2.13.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:55.055097+00:00
---

# Cloud Bigtable API - Class Google::Cloud::Bigtable::Status (v2.13.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable API - Class Google::Cloud::Bigtable::Status (v2.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.13.0 (latest)  2.12.3  2.11.1  2.10.2  2.9.1  2.8.0  2.7.1  2.6.5 

Reference documentation and code samples for the Cloud Bigtable API class Google::Cloud::Bigtable::Status.

## Status

Represents a logical error model from the Bigtable service, containing an error code, an error message, and optional error details.

## Inherits

  * Object 



## Example
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    
    table = bigtable.table "my-instance", "my-table"
    
    entries = []
    entries << table.new_mutation_entry("row-1").set_cell("cf1", "field1", "XYZ")
    entries << table.new_mutation_entry("row-2").set_cell("cf1", "field1", "ABC")
    responses = table.mutate_rows entries
    
    responses.each do |response|
      puts response.status.description
    end

## Methods 

### #code
    
    
    def code() -> Integer

The status code, which should be an enum value of [google.rpc.Code](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto).

**Returns**

  * (Integer) — the current value of code 



### #code=
    
    
    def code=(value) -> Integer

The status code, which should be an enum value of [google.rpc.Code](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto).

**Parameter**

  * **value** (Integer) — the newly set value 



**Returns**

  * (Integer) — the newly set value 



### #description
    
    
    def description() -> String

The human-readable description for the status code, which should be an enum value of [google.rpc.Code](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto). For example, `INVALID_ARGUMENT`.

**Returns**

  * (String) — the current value of description 



### #description=
    
    
    def description=(value) -> String

The human-readable description for the status code, which should be an enum value of [google.rpc.Code](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto). For example, `INVALID_ARGUMENT`.

**Parameter**

  * **value** (String) — the newly set value 



**Returns**

  * (String) — the newly set value 



### #details
    
    
    def details() -> Array<String>

A list of messages that carry the error details.

**Returns**

  * (Array<String>) — the current value of details 



### #details=
    
    
    def details=(value) -> Array<String>

A list of messages that carry the error details.

**Parameter**

  * **value** (Array<String>) — the newly set value 



**Returns**

  * (Array<String>) — the newly set value 



### #message
    
    
    def message() -> String

A developer-facing error message, which should be in English.

**Returns**

  * (String) — the current value of message 



### #message=
    
    
    def message=(value) -> String

A developer-facing error message, which should be in English.

**Parameter**

  * **value** (String) — the newly set value 



**Returns**

  * (String) — the newly set value 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
