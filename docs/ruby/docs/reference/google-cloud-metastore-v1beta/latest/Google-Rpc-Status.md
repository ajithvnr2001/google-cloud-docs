---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Rpc-Status/
title: Dataproc Metastore V1beta API - Class Google::Rpc::Status (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:26.619333+00:00
---

# Dataproc Metastore V1beta API - Class Google::Rpc::Status (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Rpc-Status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataproc Metastore V1beta API - Class Google::Rpc::Status (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.0  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.2  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Dataproc Metastore V1beta API class Google::Rpc::Status.

The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details.

You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #code
    
    
    def code() -> ::Integer

**Returns**

  * (::Integer) — The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code]. 



### #code=
    
    
    def code=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code]. 



**Returns**

  * (::Integer) — The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code]. 



### #details
    
    
    def details() -> ::Array<::Google::Protobuf::Any>

**Returns**

  * (::Array<[::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Protobuf-Any)>) — A list of messages that carry the error details. There is a common set of message types for APIs to use. 



### #details=
    
    
    def details=(value) -> ::Array<::Google::Protobuf::Any>

**Parameter**

  * **value** (::Array<[::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Protobuf-Any)>) — A list of messages that carry the error details. There is a common set of message types for APIs to use. 



**Returns**

  * (::Array<[::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Protobuf-Any)>) — A list of messages that carry the error details. There is a common set of message types for APIs to use. 



### #message
    
    
    def message() -> ::String

**Returns**

  * (::String) — A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Rpc-Status#Google__Rpc__Status_details_instance_ "Google::Rpc::Status#details \(method\)") field, or localized by the client. 



### #message=
    
    
    def message=(value) -> ::String

**Parameter**

  * **value** (::String) — A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Rpc-Status#Google__Rpc__Status_details_instance_ "Google::Rpc::Status#details \(method\)") field, or localized by the client. 



**Returns**

  * (::String) — A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Rpc-Status#Google__Rpc__Status_details_instance_ "Google::Rpc::Status#details \(method\)") field, or localized by the client. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
