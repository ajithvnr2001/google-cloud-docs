---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-BatchCreateInstancesMetadata/
title: AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::BatchCreateInstancesMetadata (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:40.062872+00:00
---

# AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::BatchCreateInstancesMetadata (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-BatchCreateInstancesMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::BatchCreateInstancesMetadata (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.1  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1ALPHA API class Google::Cloud::AlloyDB::V1alpha::BatchCreateInstancesMetadata.

Message for metadata that is specific to BatchCreateInstances API. NEXT_ID: 3

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #instance_statuses
    
    
    def instance_statuses() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::AlloyDB::V1alpha::BatchCreateInstanceStatus}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::AlloyDB::V1alpha::BatchCreateInstanceStatus}) — A map representing state of the instances involved in the BatchCreateInstances operation during the operation execution. The instance state will be in STATE_UNSPECIFIED state if the instance has not yet been picked up for processing. The key of the map is the name of the instance resource. For the format, see the comment on the Instance.name field. 



### #instance_statuses=
    
    
    def instance_statuses=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::AlloyDB::V1alpha::BatchCreateInstanceStatus}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::AlloyDB::V1alpha::BatchCreateInstanceStatus}) — A map representing state of the instances involved in the BatchCreateInstances operation during the operation execution. The instance state will be in STATE_UNSPECIFIED state if the instance has not yet been picked up for processing. The key of the map is the name of the instance resource. For the format, see the comment on the Instance.name field. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::AlloyDB::V1alpha::BatchCreateInstanceStatus}) — A map representing state of the instances involved in the BatchCreateInstances operation during the operation execution. The instance state will be in STATE_UNSPECIFIED state if the instance has not yet been picked up for processing. The key of the map is the name of the instance resource. For the format, see the comment on the Instance.name field. 



### #instance_targets
    
    
    def instance_targets() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The instances being created in the API call. Each string in this list is the server defined resource path for target instances in the request and for the format of each string, see the comment on the Instance.name field. 



### #instance_targets=
    
    
    def instance_targets=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The instances being created in the API call. Each string in this list is the server defined resource path for target instances in the request and for the format of each string, see the comment on the Instance.name field. 



**Returns**

  * (::Array<::String>) — The instances being created in the API call. Each string in this list is the server defined resource path for target instances in the request and for the format of each string, see the comment on the Instance.name field. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
