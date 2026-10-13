---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-LogEntrySourceLocation/
title: Service Control API V1 API - Class Google::Cloud::ServiceControl::V1::LogEntrySourceLocation (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:44.693402+00:00
---

# Service Control API V1 API - Class Google::Cloud::ServiceControl::V1::LogEntrySourceLocation (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Cloud-ServiceControl-V1-LogEntrySourceLocation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Control API V1 API - Class Google::Cloud::ServiceControl::V1::LogEntrySourceLocation (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.1  0.6.0  0.5.0  0.4.6 

Reference documentation and code samples for the Service Control API V1 API class Google::Cloud::ServiceControl::V1::LogEntrySourceLocation.

Additional information about the source code location that produced the log entry.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #file
    
    
    def file() -> ::String

**Returns**

  * (::String) — Optional. Source file name. Depending on the runtime environment, this might be a simple name or a fully-qualified name. 



### #file=
    
    
    def file=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Source file name. Depending on the runtime environment, this might be a simple name or a fully-qualified name. 



**Returns**

  * (::String) — Optional. Source file name. Depending on the runtime environment, this might be a simple name or a fully-qualified name. 



### #function
    
    
    def function() -> ::String

**Returns**

  * (::String) — Optional. Human-readable name of the function or method being invoked, with optional context such as the class or package name. This information may be used in contexts such as the logs viewer, where a file and line number are less meaningful. The format can vary by language. For example: `qual.if.ied.Class.method` (Java), `dir/package.func` (Go), `function` (Python). 



### #function=
    
    
    def function=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Human-readable name of the function or method being invoked, with optional context such as the class or package name. This information may be used in contexts such as the logs viewer, where a file and line number are less meaningful. The format can vary by language. For example: `qual.if.ied.Class.method` (Java), `dir/package.func` (Go), `function` (Python). 



**Returns**

  * (::String) — Optional. Human-readable name of the function or method being invoked, with optional context such as the class or package name. This information may be used in contexts such as the logs viewer, where a file and line number are less meaningful. The format can vary by language. For example: `qual.if.ied.Class.method` (Java), `dir/package.func` (Go), `function` (Python). 



### #line
    
    
    def line() -> ::Integer

**Returns**

  * (::Integer) — Optional. Line within the source file. 1-based; 0 indicates no line number available. 



### #line=
    
    
    def line=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Line within the source file. 1-based; 0 indicates no line number available. 



**Returns**

  * (::Integer) — Optional. Line within the source file. 1-based; 0 indicates no line number available. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
