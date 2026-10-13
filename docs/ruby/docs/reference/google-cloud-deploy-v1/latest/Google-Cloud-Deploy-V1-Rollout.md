---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Rollout/
title: Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Rollout (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:04.530453+00:00
---

# Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Rollout (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Rollout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Rollout (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.1  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.0  1.0.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Google Cloud Deploy V1 API class Google::Cloud::Deploy::V1::Rollout.

A `Rollout` resource in the Cloud Deploy API.

A `Rollout` contains information around a specific deployment to a `Target`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #active_repair_automation_run
    
    
    def active_repair_automation_run() -> ::String

**Returns**

  * (::String) — Output only. The AutomationRun actively repairing the rollout. 



### #annotations
    
    
    def annotations() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. 



### #annotations=
    
    
    def annotations=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. 



### #approval_state
    
    
    def approval_state() -> ::Google::Cloud::Deploy::V1::Rollout::ApprovalState

**Returns**

  * ([::Google::Cloud::Deploy::V1::Rollout::ApprovalState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Rollout-ApprovalState)) — Output only. Approval state of the `Rollout`. 



### #approve_time
    
    
    def approve_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the `Rollout` was approved. 



### #controller_rollout
    
    
    def controller_rollout() -> ::String

**Returns**

  * (::String) — Output only. Name of the `ControllerRollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the `Rollout` was created. 



### #deploy_end_time
    
    
    def deploy_end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the `Rollout` finished deploying. 



### #deploy_failure_cause
    
    
    def deploy_failure_cause() -> ::Google::Cloud::Deploy::V1::Rollout::FailureCause

**Returns**

  * ([::Google::Cloud::Deploy::V1::Rollout::FailureCause](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Rollout-FailureCause)) — Output only. The reason this rollout failed. This will always be unspecified while the rollout is in progress. 



### #deploy_start_time
    
    
    def deploy_start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the `Rollout` started deploying. 



### #deploying_build
    
    
    def deploying_build() -> ::String

**Returns**

  * (::String) — Output only. The resource name of the Cloud Build `Build` object that is used to deploy the Rollout. Format is `projects/{project}/locations/{location}/builds/{build}`. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description of the `Rollout` for user purposes. Max length is 255 characters. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description of the `Rollout` for user purposes. Max length is 255 characters. 



**Returns**

  * (::String) — Optional. Description of the `Rollout` for user purposes. Max length is 255 characters. 



### #enqueue_time
    
    
    def enqueue_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the `Rollout` was enqueued. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



**Returns**

  * (::String) — This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



### #failure_reason
    
    
    def failure_reason() -> ::String

**Returns**

  * (::String) — Output only. Additional information about the rollout failure, if available. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
    * All characters must use UTF-8 encoding, and international characters are allowed.
    * Keys must start with a lowercase letter or international character.
    * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes. 




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
    * All characters must use UTF-8 encoding, and international characters are allowed.
    * Keys must start with a lowercase letter or international character.
    * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
    * All characters must use UTF-8 encoding, and international characters are allowed.
    * Keys must start with a lowercase letter or international character.
    * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes. 




### #metadata
    
    
    def metadata() -> ::Google::Cloud::Deploy::V1::Metadata

**Returns**

  * ([::Google::Cloud::Deploy::V1::Metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Metadata)) — Output only. Metadata contains information about the rollout. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. Name of the `Rollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. The `rollout` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. Name of the `Rollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. The `rollout` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`



**Returns**

  * (::String) — Identifier. Name of the `Rollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. The `rollout` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`



### #phases
    
    
    def phases() -> ::Array<::Google::Cloud::Deploy::V1::Phase>

**Returns**

  * (::Array<[::Google::Cloud::Deploy::V1::Phase](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Phase)>) — Output only. The phases that represent the workflows of this `Rollout`. 



### #rollback_of_rollout
    
    
    def rollback_of_rollout() -> ::String

**Returns**

  * (::String) — Output only. Name of the `Rollout` that is rolled back by this `Rollout`. Empty if this `Rollout` wasn't created as a rollback. 



### #rolled_back_by_rollouts
    
    
    def rolled_back_by_rollouts() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. Names of `Rollouts` that rolled back this `Rollout`. 



### #state
    
    
    def state() -> ::Google::Cloud::Deploy::V1::Rollout::State

**Returns**

  * ([::Google::Cloud::Deploy::V1::Rollout::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Rollout-State)) — Output only. Current state of the `Rollout`. 



### #target_id
    
    
    def target_id() -> ::String

**Returns**

  * (::String) — Required. The ID of Target to which this `Rollout` is deploying. 



### #target_id=
    
    
    def target_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID of Target to which this `Rollout` is deploying. 



**Returns**

  * (::String) — Required. The ID of Target to which this `Rollout` is deploying. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. Unique identifier of the `Rollout`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
