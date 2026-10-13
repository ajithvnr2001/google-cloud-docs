---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-ProcessOpenLineageRunEventResponse/
title: Data Lineage V1 API - Class Google::Cloud::DataCatalog::Lineage::V1::ProcessOpenLineageRunEventResponse (v0.16.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:10.326282+00:00
---

# Data Lineage V1 API - Class Google::Cloud::DataCatalog::Lineage::V1::ProcessOpenLineageRunEventResponse (v0.16.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-ProcessOpenLineageRunEventResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Lineage V1 API - Class Google::Cloud::DataCatalog::Lineage::V1::ProcessOpenLineageRunEventResponse (v0.16.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.1 (latest)  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.0  0.10.1  0.9.1  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Data Lineage V1 API class Google::Cloud::DataCatalog::Lineage::V1::ProcessOpenLineageRunEventResponse.

Response message for [ProcessOpenLineageRunEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-Lineage-Client#Google__Cloud__DataCatalog__Lineage__V1__Lineage__Client_process_open_lineage_run_event_instance_ "Google::Cloud::DataCatalog::Lineage::V1::Lineage::Client#process_open_lineage_run_event \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #lineage_events
    
    
    def lineage_events() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Created lineage event names. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}/lineageEvents/{lineage_event}`. 



### #lineage_events=
    
    
    def lineage_events=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Created lineage event names. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}/lineageEvents/{lineage_event}`. 



**Returns**

  * (::Array<::String>) — Created lineage event names. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}/lineageEvents/{lineage_event}`. 



### #process
    
    
    def process() -> ::String

**Returns**

  * (::String) — Created process name. Format: `projects/{project}/locations/{location}/processes/{process}`. 



### #process=
    
    
    def process=(value) -> ::String

**Parameter**

  * **value** (::String) — Created process name. Format: `projects/{project}/locations/{location}/processes/{process}`. 



**Returns**

  * (::String) — Created process name. Format: `projects/{project}/locations/{location}/processes/{process}`. 



### #run
    
    
    def run() -> ::String

**Returns**

  * (::String) — Created run name. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}`. 



### #run=
    
    
    def run=(value) -> ::String

**Parameter**

  * **value** (::String) — Created run name. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}`. 



**Returns**

  * (::String) — Created run name. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
