---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Longrunning-OperationInfo/
title: Retail V2 API - Class Google::Longrunning::OperationInfo (v2.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:50.972995+00:00
---

# Retail V2 API - Class Google::Longrunning::OperationInfo (v2.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Longrunning-OperationInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Retail V2 API - Class Google::Longrunning::OperationInfo (v2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.0 (latest)  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.0  1.0.1  0.21.0  0.20.0  0.19.0  0.18.2  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Retail V2 API class Google::Longrunning::OperationInfo.

A message representing the message types used by a long-running operation.

Example:
    
    
    rpc Export(ExportRequest) returns (google.longrunning.Operation) {
      option (google.longrunning.operation_info) = {
        response_type: "ExportResponse"
        metadata_type: "ExportMetadata"
      };
    }
    

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #metadata_type
    
    
    def metadata_type() -> ::String

**Returns**

  * (::String) — Required. The message name of the metadata type for this long-running operation.

If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).

Note: Altering this value constitutes a breaking change. 




### #metadata_type=
    
    
    def metadata_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The message name of the metadata type for this long-running operation.

If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).

Note: Altering this value constitutes a breaking change. 




**Returns**

  * (::String) — Required. The message name of the metadata type for this long-running operation.

If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).

Note: Altering this value constitutes a breaking change. 




### #response_type
    
    
    def response_type() -> ::String

**Returns**

  * (::String) — Required. The message name of the primary return type for this long-running operation. This type will be used to deserialize the LRO's response.

If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).

Note: Altering this value constitutes a breaking change. 




### #response_type=
    
    
    def response_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The message name of the primary return type for this long-running operation. This type will be used to deserialize the LRO's response.

If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).

Note: Altering this value constitutes a breaking change. 




**Returns**

  * (::String) — Required. The message name of the primary return type for this long-running operation. This type will be used to deserialize the LRO's response.

If the response is in a different package from the rpc, a fully-qualified message name must be used (e.g. `google.protobuf.Struct`).

Note: Altering this value constitutes a breaking change. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
