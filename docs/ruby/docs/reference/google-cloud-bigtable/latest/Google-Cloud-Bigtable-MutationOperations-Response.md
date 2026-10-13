---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-MutationOperations-Response/
title: Cloud Bigtable API - Class Google::Cloud::Bigtable::MutationOperations::Response (v2.13.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:11:21.582104+00:00
---

# Cloud Bigtable API - Class Google::Cloud::Bigtable::MutationOperations::Response (v2.13.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-MutationOperations-Response/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable API - Class Google::Cloud::Bigtable::MutationOperations::Response (v2.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.13.0 (latest)  2.12.3  2.11.1  2.10.2  2.9.1  2.8.0  2.7.1  2.6.5 

Reference documentation and code samples for the Cloud Bigtable API class Google::Cloud::Bigtable::MutationOperations::Response.

## MutationEntry::Response

Represents a response message from BigtableService.MutateRows.

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

### #The
    
    
    def The() -> Google::Cloud::Bigtable::Status

result of the request Entry identified by `index`. Depending on how requests are batched during execution, it is possible for one Entry to fail due to an error with another Entry. In the event that this occurs, the same error will be reported for both entries.

**Returns**

  * ([Google::Cloud::Bigtable::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Status)) — the current value of The 



### #The=
    
    
    def The=(value) -> Google::Cloud::Bigtable::Status

result of the request Entry identified by `index`. Depending on how requests are batched during execution, it is possible for one Entry to fail due to an error with another Entry. In the event that this occurs, the same error will be reported for both entries.

**Parameter**

  * **value** ([Google::Cloud::Bigtable::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Status)) — the newly set value 



**Returns**

  * ([Google::Cloud::Bigtable::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Status)) — the newly set value 



### #index
    
    
    def index() -> Integer

The index into the original request's `entries` list of the Entry for which a result is being reported.

**Returns**

  * (Integer) — the current value of index 



### #index=
    
    
    def index=(value) -> Integer

The index into the original request's `entries` list of the Entry for which a result is being reported.

**Parameter**

  * **value** (Integer) — the newly set value 



**Returns**

  * (Integer) — the newly set value 



### #status
    
    
    def status()

Returns the value of attribute status.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
