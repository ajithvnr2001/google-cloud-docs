---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-GcsReportLogMessage/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::GcsReportLogMessage (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:02.566401+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::GcsReportLogMessage (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-GcsReportLogMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::GcsReportLogMessage (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::GcsReportLogMessage.

A record in the aggregate CSV report for a migration workflow

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #action
    
    
    def action() -> ::String

**Returns**

  * (::String) — Category of the error/warning. Example: SyntaxError 



### #action=
    
    
    def action=(value) -> ::String

**Parameter**

  * **value** (::String) — Category of the error/warning. Example: SyntaxError 



**Returns**

  * (::String) — Category of the error/warning. Example: SyntaxError 



### #category
    
    
    def category() -> ::String

**Returns**

  * (::String) — Category of the error/warning. Example: SyntaxError 



### #category=
    
    
    def category=(value) -> ::String

**Parameter**

  * **value** (::String) — Category of the error/warning. Example: SyntaxError 



**Returns**

  * (::String) — Category of the error/warning. Example: SyntaxError 



### #effect
    
    
    def effect() -> ::String

**Returns**

  * (::String) — Effect of the error/warning. Example: COMPATIBILITY 



### #effect=
    
    
    def effect=(value) -> ::String

**Parameter**

  * **value** (::String) — Effect of the error/warning. Example: COMPATIBILITY 



**Returns**

  * (::String) — Effect of the error/warning. Example: COMPATIBILITY 



### #file_path
    
    
    def file_path() -> ::String

**Returns**

  * (::String) — The file path in which the error occurred 



### #file_path=
    
    
    def file_path=(value) -> ::String

**Parameter**

  * **value** (::String) — The file path in which the error occurred 



**Returns**

  * (::String) — The file path in which the error occurred 



### #filename
    
    
    def filename() -> ::String

**Returns**

  * (::String) — The file name in which the error occurred 



### #filename=
    
    
    def filename=(value) -> ::String

**Parameter**

  * **value** (::String) — The file name in which the error occurred 



**Returns**

  * (::String) — The file name in which the error occurred 



### #message
    
    
    def message() -> ::String

**Returns**

  * (::String) — Detailed message of the record. 



### #message=
    
    
    def message=(value) -> ::String

**Parameter**

  * **value** (::String) — Detailed message of the record. 



**Returns**

  * (::String) — Detailed message of the record. 



### #object_name
    
    
    def object_name() -> ::String

**Returns**

  * (::String) — Name of the affected object in the log message. 



### #object_name=
    
    
    def object_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the affected object in the log message. 



**Returns**

  * (::String) — Name of the affected object in the log message. 



### #script_context
    
    
    def script_context() -> ::String

**Returns**

  * (::String) — The script context (obfuscated) in which the error occurred 



### #script_context=
    
    
    def script_context=(value) -> ::String

**Parameter**

  * **value** (::String) — The script context (obfuscated) in which the error occurred 



**Returns**

  * (::String) — The script context (obfuscated) in which the error occurred 



### #severity
    
    
    def severity() -> ::String

**Returns**

  * (::String) — Severity of the translation record. 



### #severity=
    
    
    def severity=(value) -> ::String

**Parameter**

  * **value** (::String) — Severity of the translation record. 



**Returns**

  * (::String) — Severity of the translation record. 



### #source_script_column
    
    
    def source_script_column() -> ::Integer

**Returns**

  * (::Integer) — Specifies the column from the source texts where the error occurred. (0 based, -1 for messages without column location) example: 6 



### #source_script_column=
    
    
    def source_script_column=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Specifies the column from the source texts where the error occurred. (0 based, -1 for messages without column location) example: 6 



**Returns**

  * (::Integer) — Specifies the column from the source texts where the error occurred. (0 based, -1 for messages without column location) example: 6 



### #source_script_line
    
    
    def source_script_line() -> ::Integer

**Returns**

  * (::Integer) — Specifies the row from the source text where the error occurred (0 based, -1 for messages without line location). Example: 2 



### #source_script_line=
    
    
    def source_script_line=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Specifies the row from the source text where the error occurred (0 based, -1 for messages without line location). Example: 2 



**Returns**

  * (::Integer) — Specifies the row from the source text where the error occurred (0 based, -1 for messages without line location). Example: 2 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
