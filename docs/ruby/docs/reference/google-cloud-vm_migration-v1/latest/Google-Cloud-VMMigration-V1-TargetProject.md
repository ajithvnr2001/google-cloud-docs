---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-TargetProject/
title: Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::TargetProject (v2.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:58.549121+00:00
---

# Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::TargetProject (v2.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-TargetProject/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::TargetProject (v2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.1  2.0.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Migrate for Compute Engine V1 API class Google::Cloud::VMMigration::V1::TargetProject.

TargetProject message represents a target Compute Engine project for a migration or a clone.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time this target project resource was created (not related to when the Compute Engine project it points to was created). 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — The target project's description. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — The target project's description. 



**Returns**

  * (::String) — The target project's description. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The name of the target project. 



### #project
    
    
    def project() -> ::String

**Returns**

  * (::String) — Required. The target project ID (number) or project name. 



### #project=
    
    
    def project=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The target project ID (number) or project name. 



**Returns**

  * (::String) — Required. The target project ID (number) or project name. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Protobuf-Timestamp)) — Output only. The last time the target project resource was updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
