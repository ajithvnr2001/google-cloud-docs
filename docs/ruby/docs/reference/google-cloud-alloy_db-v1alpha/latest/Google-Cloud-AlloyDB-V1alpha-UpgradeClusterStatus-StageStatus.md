---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterStatus-StageStatus/
title: AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::StageStatus (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:48.456023+00:00
---

# AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::StageStatus (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterStatus-StageStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::StageStatus (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.1  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1ALPHA API class Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::StageStatus.

Status of an upgrade stage.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #read_pool_instances_upgrade
    
    
    def read_pool_instances_upgrade() -> ::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::ReadPoolInstancesUpgradeStageStatus

**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::ReadPoolInstancesUpgradeStageStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterStatus-ReadPoolInstancesUpgradeStageStatus)) — Read pool instances upgrade metadata. 



### #read_pool_instances_upgrade=
    
    
    def read_pool_instances_upgrade=(value) -> ::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::ReadPoolInstancesUpgradeStageStatus

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::ReadPoolInstancesUpgradeStageStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterStatus-ReadPoolInstancesUpgradeStageStatus)) — Read pool instances upgrade metadata. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::ReadPoolInstancesUpgradeStageStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterStatus-ReadPoolInstancesUpgradeStageStatus)) — Read pool instances upgrade metadata. 



### #schedule
    
    
    def schedule() -> ::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::StageStatus::StageSchedule

**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterStatus::StageStatus::StageSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterStatus-StageStatus-StageSchedule)) — Output only. Timing information for the stage execution. 



### #stage
    
    
    def stage() -> ::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Stage

**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Stage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterResponse-Stage)) — Upgrade stage. 



### #stage=
    
    
    def stage=(value) -> ::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Stage

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Stage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterResponse-Stage)) — Upgrade stage. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Stage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterResponse-Stage)) — Upgrade stage. 



### #state
    
    
    def state() -> ::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Status

**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterResponse-Status)) — State of this stage. 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Status

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterResponse-Status)) — State of this stage. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::UpgradeClusterResponse::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-UpgradeClusterResponse-Status)) — State of this stage. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
