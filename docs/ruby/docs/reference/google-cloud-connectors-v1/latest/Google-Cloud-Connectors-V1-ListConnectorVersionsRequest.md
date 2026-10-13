---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListConnectorVersionsRequest/
title: Connectors V1 API - Class Google::Cloud::Connectors::V1::ListConnectorVersionsRequest (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:03.224883+00:00
---

# Connectors V1 API - Class Google::Cloud::Connectors::V1::ListConnectorVersionsRequest (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ListConnectorVersionsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Connectors V1 API - Class Google::Cloud::Connectors::V1::ListConnectorVersionsRequest (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Connectors V1 API class Google::Cloud::Connectors::V1::ListConnectorVersionsRequest.

Request message for Connectors.ListConnectorVersions.

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

  * (::Integer) — Page size. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Page size. 



**Returns**

  * (::Integer) — Page size. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Page token. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Page token. 



**Returns**

  * (::String) — Page token. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Parent resource of the connectors, of the form: `projects/*/locations/*/providers/*/connectors/*` Only global location is supported for ConnectorVersion resource. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Parent resource of the connectors, of the form: `projects/*/locations/*/providers/*/connectors/*` Only global location is supported for ConnectorVersion resource. 



**Returns**

  * (::String) — Required. Parent resource of the connectors, of the form: `projects/*/locations/*/providers/*/connectors/*` Only global location is supported for ConnectorVersion resource. 



### #view
    
    
    def view() -> ::Google::Cloud::Connectors::V1::ConnectorVersionView

**Returns**

  * ([::Google::Cloud::Connectors::V1::ConnectorVersionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectorVersionView)) — Specifies which fields of the ConnectorVersion are returned in the response. Defaults to `BASIC` view. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::Connectors::V1::ConnectorVersionView

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::ConnectorVersionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectorVersionView)) — Specifies which fields of the ConnectorVersion are returned in the response. Defaults to `BASIC` view. 



**Returns**

  * ([::Google::Cloud::Connectors::V1::ConnectorVersionView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectorVersionView)) — Specifies which fields of the ConnectorVersion are returned in the response. Defaults to `BASIC` view. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
