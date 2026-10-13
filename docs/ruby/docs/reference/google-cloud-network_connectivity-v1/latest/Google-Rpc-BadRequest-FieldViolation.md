---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Rpc-BadRequest-FieldViolation/
title: Network Connectivity V1 API - Class Google::Rpc::BadRequest::FieldViolation (v1.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:40.507283+00:00
---

# Network Connectivity V1 API - Class Google::Rpc::BadRequest::FieldViolation (v1.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Rpc-BadRequest-FieldViolation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1 API - Class Google::Rpc::BadRequest::FieldViolation (v1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Network Connectivity V1 API class Google::Rpc::BadRequest::FieldViolation.

A message type used to describe a single bad request field.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — A description of why the request element is bad. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — A description of why the request element is bad. 



**Returns**

  * (::String) — A description of why the request element is bad. 



### #field
    
    
    def field() -> ::String

**Returns**

  * (::String) — 

A path that leads to a field in the request body. The value will be a sequence of dot-separated identifiers that identify a protocol buffer field.

Consider the following:
        
        message CreateContactRequest {
          message EmailAddress {
            enum Type {
              TYPE_UNSPECIFIED = 0;
              HOME = 1;
              WORK = 2;
            }
        
            optional string email = 1;
            repeated EmailType type = 2;
          }
        
          string full_name = 1;
          repeated EmailAddress email_addresses = 2;
        }
        

In this example, in proto `field` could take one of the following values:

    * `full_name` for a violation in the `full_name` value
    * `email_addresses[0].email` for a violation in the `email` field of the first `email_addresses` message
    * `email_addresses[2].type[1]` for a violation in the second `type` value in the third `email_addresses` message.

In JSON, the same values are represented as:

    * `fullName` for a violation in the `fullName` value
    * `emailAddresses[0].email` for a violation in the `email` field of the first `emailAddresses` message
    * `emailAddresses[2].type[1]` for a violation in the second `type` value in the third `emailAddresses` message.



### #field=
    
    
    def field=(value) -> ::String

**Parameter**

  * **value** (::String) — 

A path that leads to a field in the request body. The value will be a sequence of dot-separated identifiers that identify a protocol buffer field.

Consider the following:
        
        message CreateContactRequest {
          message EmailAddress {
            enum Type {
              TYPE_UNSPECIFIED = 0;
              HOME = 1;
              WORK = 2;
            }
        
            optional string email = 1;
            repeated EmailType type = 2;
          }
        
          string full_name = 1;
          repeated EmailAddress email_addresses = 2;
        }
        

In this example, in proto `field` could take one of the following values:

    * `full_name` for a violation in the `full_name` value
    * `email_addresses[0].email` for a violation in the `email` field of the first `email_addresses` message
    * `email_addresses[2].type[1]` for a violation in the second `type` value in the third `email_addresses` message.

In JSON, the same values are represented as:

    * `fullName` for a violation in the `fullName` value
    * `emailAddresses[0].email` for a violation in the `email` field of the first `emailAddresses` message
    * `emailAddresses[2].type[1]` for a violation in the second `type` value in the third `emailAddresses` message.



**Returns**

  * (::String) — 

A path that leads to a field in the request body. The value will be a sequence of dot-separated identifiers that identify a protocol buffer field.

Consider the following:
        
        message CreateContactRequest {
          message EmailAddress {
            enum Type {
              TYPE_UNSPECIFIED = 0;
              HOME = 1;
              WORK = 2;
            }
        
            optional string email = 1;
            repeated EmailType type = 2;
          }
        
          string full_name = 1;
          repeated EmailAddress email_addresses = 2;
        }
        

In this example, in proto `field` could take one of the following values:

    * `full_name` for a violation in the `full_name` value
    * `email_addresses[0].email` for a violation in the `email` field of the first `email_addresses` message
    * `email_addresses[2].type[1]` for a violation in the second `type` value in the third `email_addresses` message.

In JSON, the same values are represented as:

    * `fullName` for a violation in the `fullName` value
    * `emailAddresses[0].email` for a violation in the `email` field of the first `emailAddresses` message
    * `emailAddresses[2].type[1]` for a violation in the second `type` value in the third `emailAddresses` message.



### #localized_message
    
    
    def localized_message() -> ::Google::Rpc::LocalizedMessage

**Returns**

  * ([::Google::Rpc::LocalizedMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Rpc-LocalizedMessage)) — Provides a localized error message for field-level errors that is safe to return to the API consumer. 



### #localized_message=
    
    
    def localized_message=(value) -> ::Google::Rpc::LocalizedMessage

**Parameter**

  * **value** ([::Google::Rpc::LocalizedMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Rpc-LocalizedMessage)) — Provides a localized error message for field-level errors that is safe to return to the API consumer. 



**Returns**

  * ([::Google::Rpc::LocalizedMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Rpc-LocalizedMessage)) — Provides a localized error message for field-level errors that is safe to return to the API consumer. 



### #reason
    
    
    def reason() -> ::String

**Returns**

  * (::String) — The reason of the field-level error. This is a constant value that identifies the proximate cause of the field-level error. It should uniquely identify the type of the FieldViolation within the scope of the google.rpc.ErrorInfo.domain. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE. 



### #reason=
    
    
    def reason=(value) -> ::String

**Parameter**

  * **value** (::String) — The reason of the field-level error. This is a constant value that identifies the proximate cause of the field-level error. It should uniquely identify the type of the FieldViolation within the scope of the google.rpc.ErrorInfo.domain. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE. 



**Returns**

  * (::String) — The reason of the field-level error. This is a constant value that identifies the proximate cause of the field-level error. It should uniquely identify the type of the FieldViolation within the scope of the google.rpc.ErrorInfo.domain. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
