---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Api-ResourceReference/
title: Google Cloud Deploy V1 API - Class Google::Api::ResourceReference (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:15.670951+00:00
---

# Google Cloud Deploy V1 API - Class Google::Api::ResourceReference (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Api-ResourceReference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Deploy V1 API - Class Google::Api::ResourceReference (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.1  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.0  1.0.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Google Cloud Deploy V1 API class Google::Api::ResourceReference.

Defines a proto annotation that describes a string field that refers to an API resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #child_type
    
    
    def child_type() -> ::String

**Returns**

  * (::String) — 

The resource type of a child collection that the annotated field references. This is useful for annotating the `parent` field that doesn't have a fixed resource type.

Example:
        
        message ListLogEntriesRequest {
          string parent = 1 [(google.api.resource_reference) = {
            child_type: "logging.googleapis.com/LogEntry"
          };
        }
        




### #child_type=
    
    
    def child_type=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The resource type of a child collection that the annotated field references. This is useful for annotating the `parent` field that doesn't have a fixed resource type.

Example:
        
        message ListLogEntriesRequest {
          string parent = 1 [(google.api.resource_reference) = {
            child_type: "logging.googleapis.com/LogEntry"
          };
        }
        




**Returns**

  * (::String) — 

The resource type of a child collection that the annotated field references. This is useful for annotating the `parent` field that doesn't have a fixed resource type.

Example:
        
        message ListLogEntriesRequest {
          string parent = 1 [(google.api.resource_reference) = {
            child_type: "logging.googleapis.com/LogEntry"
          };
        }
        




### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — 

The resource type that the annotated field references.

Example:
        
        message Subscription {
          string topic = 2 [(google.api.resource_reference) = {
            type: "pubsub.googleapis.com/Topic"
          }];
        }
        

Occasionally, a field may reference an arbitrary resource. In this case, APIs use the special value * in their resource reference.

Example:
        
        message GetIamPolicyRequest {
          string resource = 2 [(google.api.resource_reference) = {
            type: "*"
          }];
        }
        




### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The resource type that the annotated field references.

Example:
        
        message Subscription {
          string topic = 2 [(google.api.resource_reference) = {
            type: "pubsub.googleapis.com/Topic"
          }];
        }
        

Occasionally, a field may reference an arbitrary resource. In this case, APIs use the special value * in their resource reference.

Example:
        
        message GetIamPolicyRequest {
          string resource = 2 [(google.api.resource_reference) = {
            type: "*"
          }];
        }
        




**Returns**

  * (::String) — 

The resource type that the annotated field references.

Example:
        
        message Subscription {
          string topic = 2 [(google.api.resource_reference) = {
            type: "pubsub.googleapis.com/Topic"
          }];
        }
        

Occasionally, a field may reference an arbitrary resource. In this case, APIs use the special value * in their resource reference.

Example:
        
        message GetIamPolicyRequest {
          string resource = 2 [(google.api.resource_reference) = {
            type: "*"
          }];
        }
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
