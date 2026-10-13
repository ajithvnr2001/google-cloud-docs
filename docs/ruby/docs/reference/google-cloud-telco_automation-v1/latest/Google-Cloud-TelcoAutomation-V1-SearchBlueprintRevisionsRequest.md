---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-SearchBlueprintRevisionsRequest/
title: Telco Automation V1 API - Class Google::Cloud::TelcoAutomation::V1::SearchBlueprintRevisionsRequest (v2.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:07.301556+00:00
---

# Telco Automation V1 API - Class Google::Cloud::TelcoAutomation::V1::SearchBlueprintRevisionsRequest (v2.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-telco_automation-v1/latest/Google-Cloud-TelcoAutomation-V1-SearchBlueprintRevisionsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Telco Automation V1 API - Class Google::Cloud::TelcoAutomation::V1::SearchBlueprintRevisionsRequest (v2.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.1 (latest)  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Telco Automation V1 API class Google::Cloud::TelcoAutomation::V1::SearchBlueprintRevisionsRequest.

Request object for `SearchBlueprintRevisions`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of blueprints revisions to return per page. max page size = 100, default page size = 20. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of blueprints revisions to return per page. max page size = 100, default page size = 20. 



**Returns**

  * (::Integer) — Optional. The maximum number of blueprints revisions to return per page. max page size = 100, default page size = 20. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. The page token, received from a previous search call. It can be provided to retrieve the subsequent page. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The page token, received from a previous search call. It can be provided to retrieve the subsequent page. 



**Returns**

  * (::String) — Optional. The page token, received from a previous search call. It can be provided to retrieve the subsequent page. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The name of parent orchestration cluster resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}". 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of parent orchestration cluster resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}". 



**Returns**

  * (::String) — Required. The name of parent orchestration cluster resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}". 



### #query
    
    
    def query() -> ::String

**Returns**

  * (::String) — 

Required. Supported queries:

    1. "" : Lists all revisions across all blueprints.
    2. "latest=true" : Lists latest revisions across all blueprints.
    3. "name={name}" : Lists all revisions of blueprint with name {name}.
    4. "name={name} latest=true": Lists latest revision of blueprint with name {name}



### #query=
    
    
    def query=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. Supported queries:

    1. "" : Lists all revisions across all blueprints.
    2. "latest=true" : Lists latest revisions across all blueprints.
    3. "name={name}" : Lists all revisions of blueprint with name {name}.
    4. "name={name} latest=true": Lists latest revision of blueprint with name {name}



**Returns**

  * (::String) — 

Required. Supported queries:

    1. "" : Lists all revisions across all blueprints.
    2. "latest=true" : Lists latest revisions across all blueprints.
    3. "name={name}" : Lists all revisions of blueprint with name {name}.
    4. "name={name} latest=true": Lists latest revision of blueprint with name {name}



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
