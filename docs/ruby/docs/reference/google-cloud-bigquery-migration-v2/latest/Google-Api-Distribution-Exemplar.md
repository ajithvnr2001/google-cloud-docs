---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-Exemplar/
title: BigQuery Migration V2 API - Class Google::Api::Distribution::Exemplar (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:54.217505+00:00
---

# BigQuery Migration V2 API - Class Google::Api::Distribution::Exemplar (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution-Exemplar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Api::Distribution::Exemplar (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Api::Distribution::Exemplar.

Exemplars are example points that may be used to annotate aggregated distribution values. They are metadata that gives information about a particular value added to a Distribution bucket, such as a trace ID that was active when a value was added. They may contain further information, such as a example values and timestamps, origin, etc.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #attachments
    
    
    def attachments() -> ::Array<::Google::Protobuf::Any>

**Returns**

  * (::Array<[::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Any)>) — Contextual information about the example value. Examples are:

Trace: type.googleapis.com/google.monitoring.v3.SpanContext

Literal string: type.googleapis.com/google.protobuf.StringValue

Labels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabels

There may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system. 




### #attachments=
    
    
    def attachments=(value) -> ::Array<::Google::Protobuf::Any>

**Parameter**

  * **value** (::Array<[::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Any)>) — Contextual information about the example value. Examples are:

Trace: type.googleapis.com/google.monitoring.v3.SpanContext

Literal string: type.googleapis.com/google.protobuf.StringValue

Labels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabels

There may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system. 




**Returns**

  * (::Array<[::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Any)>) — Contextual information about the example value. Examples are:

Trace: type.googleapis.com/google.monitoring.v3.SpanContext

Literal string: type.googleapis.com/google.protobuf.StringValue

Labels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabels

There may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system. 




### #timestamp
    
    
    def timestamp() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Timestamp)) — The observation (sampling) time of the above value. 



### #timestamp=
    
    
    def timestamp=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Timestamp)) — The observation (sampling) time of the above value. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Timestamp)) — The observation (sampling) time of the above value. 



### #value
    
    
    def value() -> ::Float

**Returns**

  * (::Float) — Value of the exemplar point. This value determines to which bucket the exemplar belongs. 



### #value=
    
    
    def value=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Value of the exemplar point. This value determines to which bucket the exemplar belongs. 



**Returns**

  * (::Float) — Value of the exemplar point. This value determines to which bucket the exemplar belongs. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
