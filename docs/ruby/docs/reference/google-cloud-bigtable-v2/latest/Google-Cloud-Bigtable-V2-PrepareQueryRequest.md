---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-PrepareQueryRequest/
title: Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::PrepareQueryRequest (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:07.263054+00:00
---

# Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::PrepareQueryRequest (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-PrepareQueryRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::PrepareQueryRequest (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Cloud Bigtable V2 API class Google::Cloud::Bigtable::V2::PrepareQueryRequest.

Request message for Bigtable.PrepareQuery

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_profile_id
    
    
    def app_profile_id() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used. 



### #app_profile_id=
    
    
    def app_profile_id=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used. 



### #instance_name
    
    
    def instance_name() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`



### #instance_name=
    
    
    def instance_name=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`



### #param_types
    
    
    def param_types() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Bigtable::V2::Type}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Bigtable::V2::Type}) — Required. `param_types` is a map of parameter identifier strings to their `Type`s.

In query string, a parameter placeholder consists of the `@` character followed by the parameter name (for example, `@firstName`) in the query string.

For example, if param_types["firstName"] = Bytes then `@firstName` will be a query parameter of type Bytes. The specific `Value` to be used for the query execution must be sent in `ExecuteQueryRequest` in the `params` map. 




### #param_types=
    
    
    def param_types=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Bigtable::V2::Type}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Bigtable::V2::Type}) — Required. `param_types` is a map of parameter identifier strings to their `Type`s.

In query string, a parameter placeholder consists of the `@` character followed by the parameter name (for example, `@firstName`) in the query string.

For example, if param_types["firstName"] = Bytes then `@firstName` will be a query parameter of type Bytes. The specific `Value` to be used for the query execution must be sent in `ExecuteQueryRequest` in the `params` map. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Bigtable::V2::Type}) — Required. `param_types` is a map of parameter identifier strings to their `Type`s.

In query string, a parameter placeholder consists of the `@` character followed by the parameter name (for example, `@firstName`) in the query string.

For example, if param_types["firstName"] = Bytes then `@firstName` will be a query parameter of type Bytes. The specific `Value` to be used for the query execution must be sent in `ExecuteQueryRequest` in the `params` map. 




### #proto_format
    
    
    def proto_format() -> ::Google::Cloud::Bigtable::V2::ProtoFormat

**Returns**

  * ([::Google::Cloud::Bigtable::V2::ProtoFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ProtoFormat)) — Protocol buffer format as described by ProtoSchema and ProtoRows messages. 



### #proto_format=
    
    
    def proto_format=(value) -> ::Google::Cloud::Bigtable::V2::ProtoFormat

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::V2::ProtoFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ProtoFormat)) — Protocol buffer format as described by ProtoSchema and ProtoRows messages. 



**Returns**

  * ([::Google::Cloud::Bigtable::V2::ProtoFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ProtoFormat)) — Protocol buffer format as described by ProtoSchema and ProtoRows messages. 



### #query
    
    
    def query() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Required. The query string. 



### #query=
    
    
    def query=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Required. The query string. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Required. The query string. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
