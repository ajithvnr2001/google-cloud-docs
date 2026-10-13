---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationRun/
title: Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::AutomationRun (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:21.871073+00:00
---

# Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::AutomationRun (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationRun/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::AutomationRun (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.1  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.0  1.0.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Google Cloud Deploy V1 API class Google::Cloud::Deploy::V1::AutomationRun.

An `AutomationRun` resource in the Cloud Deploy API.

An `AutomationRun` represents an execution instance of an automation rule.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #advance_rollout_operation
    
    
    def advance_rollout_operation() -> ::Google::Cloud::Deploy::V1::AdvanceRolloutOperation

**Returns**

  * ([::Google::Cloud::Deploy::V1::AdvanceRolloutOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AdvanceRolloutOperation)) — Output only. Advances a rollout to the next phase.

Note: The following fields are mutually exclusive: `advance_rollout_operation`, `promote_release_operation`, `repair_rollout_operation`, `timed_promote_release_operation`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #automation_id
    
    
    def automation_id() -> ::String

**Returns**

  * (::String) — Output only. The ID of the automation that initiated the operation. 



### #automation_snapshot
    
    
    def automation_snapshot() -> ::Google::Cloud::Deploy::V1::Automation

**Returns**

  * ([::Google::Cloud::Deploy::V1::Automation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Automation)) — Output only. Snapshot of the Automation taken at AutomationRun creation time. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the `AutomationRun` was created. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Output only. The weak etag of the `AutomationRun` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



### #expire_time
    
    
    def expire_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time the `AutomationRun` expires. An `AutomationRun` expires after 14 days from its creation date. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Name of the `AutomationRun`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automationRuns/{automation_run}`. 



### #policy_violation
    
    
    def policy_violation() -> ::Google::Cloud::Deploy::V1::PolicyViolation

**Returns**

  * ([::Google::Cloud::Deploy::V1::PolicyViolation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-PolicyViolation)) — Output only. Contains information about what policies prevented the `AutomationRun` from proceeding. 



### #promote_release_operation
    
    
    def promote_release_operation() -> ::Google::Cloud::Deploy::V1::PromoteReleaseOperation

**Returns**

  * ([::Google::Cloud::Deploy::V1::PromoteReleaseOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-PromoteReleaseOperation)) — Output only. Promotes a release to a specified 'Target'.

Note: The following fields are mutually exclusive: `promote_release_operation`, `advance_rollout_operation`, `repair_rollout_operation`, `timed_promote_release_operation`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #repair_rollout_operation
    
    
    def repair_rollout_operation() -> ::Google::Cloud::Deploy::V1::RepairRolloutOperation

**Returns**

  * ([::Google::Cloud::Deploy::V1::RepairRolloutOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-RepairRolloutOperation)) — Output only. Repairs a failed 'Rollout'.

Note: The following fields are mutually exclusive: `repair_rollout_operation`, `promote_release_operation`, `advance_rollout_operation`, `timed_promote_release_operation`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #rule_id
    
    
    def rule_id() -> ::String

**Returns**

  * (::String) — Output only. The ID of the automation rule that initiated the operation. 



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — Output only. Email address of the user-managed IAM service account that performs the operations against Cloud Deploy resources. 



### #state
    
    
    def state() -> ::Google::Cloud::Deploy::V1::AutomationRun::State

**Returns**

  * ([::Google::Cloud::Deploy::V1::AutomationRun::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationRun-State)) — Output only. Current state of the `AutomationRun`. 



### #state_description
    
    
    def state_description() -> ::String

**Returns**

  * (::String) — Output only. Explains the current state of the `AutomationRun`. Present only when an explanation is needed. 



### #target_id
    
    
    def target_id() -> ::String

**Returns**

  * (::String) — Output only. The ID of the source target that initiates the `AutomationRun`. The value of this field is the last segment of a target name. 



### #timed_promote_release_operation
    
    
    def timed_promote_release_operation() -> ::Google::Cloud::Deploy::V1::TimedPromoteReleaseOperation

**Returns**

  * ([::Google::Cloud::Deploy::V1::TimedPromoteReleaseOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-TimedPromoteReleaseOperation)) — Output only. Promotes a release to a specified 'Target' as defined in a Timed Promote Release rule.

Note: The following fields are mutually exclusive: `timed_promote_release_operation`, `promote_release_operation`, `advance_rollout_operation`, `repair_rollout_operation`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the automationRun was updated. 



### #wait_until_time
    
    
    def wait_until_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Earliest time the `AutomationRun` will attempt to resume. Wait-time is configured by `wait` in automation rule. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
