---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-BasicYarnAutoscalingConfig/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::BasicYarnAutoscalingConfig (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:59.908358+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::BasicYarnAutoscalingConfig (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-BasicYarnAutoscalingConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::BasicYarnAutoscalingConfig (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::BasicYarnAutoscalingConfig.

Basic autoscaling configurations for YARN.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #graceful_decommission_timeout
    
    
    def graceful_decommission_timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Protobuf-Duration)) — Required. Timeout for YARN graceful decommissioning of Node Managers. Specifies the duration to wait for jobs to complete before forcefully removing workers (and potentially interrupting jobs). Only applicable to downscaling operations.

Bounds: [0s, 1d]. 




### #graceful_decommission_timeout=
    
    
    def graceful_decommission_timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Protobuf-Duration)) — Required. Timeout for YARN graceful decommissioning of Node Managers. Specifies the duration to wait for jobs to complete before forcefully removing workers (and potentially interrupting jobs). Only applicable to downscaling operations.

Bounds: [0s, 1d]. 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Protobuf-Duration)) — Required. Timeout for YARN graceful decommissioning of Node Managers. Specifies the duration to wait for jobs to complete before forcefully removing workers (and potentially interrupting jobs). Only applicable to downscaling operations.

Bounds: [0s, 1d]. 




### #scale_down_factor
    
    
    def scale_down_factor() -> ::Float

**Returns**

  * (::Float) — Required. Fraction of average YARN pending memory in the last cooldown period for which to remove workers. A scale-down factor of 1 will result in scaling down so that there is no available memory remaining after the update (more aggressive scaling). A scale-down factor of 0 disables removing workers, which can be beneficial for autoscaling a single job. See [How autoscaling works](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling#how_autoscaling_works) for more information.

Bounds: [0.0, 1.0]. 




### #scale_down_factor=
    
    
    def scale_down_factor=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Required. Fraction of average YARN pending memory in the last cooldown period for which to remove workers. A scale-down factor of 1 will result in scaling down so that there is no available memory remaining after the update (more aggressive scaling). A scale-down factor of 0 disables removing workers, which can be beneficial for autoscaling a single job. See [How autoscaling works](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling#how_autoscaling_works) for more information.

Bounds: [0.0, 1.0]. 




**Returns**

  * (::Float) — Required. Fraction of average YARN pending memory in the last cooldown period for which to remove workers. A scale-down factor of 1 will result in scaling down so that there is no available memory remaining after the update (more aggressive scaling). A scale-down factor of 0 disables removing workers, which can be beneficial for autoscaling a single job. See [How autoscaling works](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling#how_autoscaling_works) for more information.

Bounds: [0.0, 1.0]. 




### #scale_down_min_worker_fraction
    
    
    def scale_down_min_worker_fraction() -> ::Float

**Returns**

  * (::Float) — Optional. Minimum scale-down threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2 worker scale-down for the cluster to scale. A threshold of 0 means the autoscaler will scale down on any recommended change.

Bounds: [0.0, 1.0]. Default: 0.0. 




### #scale_down_min_worker_fraction=
    
    
    def scale_down_min_worker_fraction=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Optional. Minimum scale-down threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2 worker scale-down for the cluster to scale. A threshold of 0 means the autoscaler will scale down on any recommended change.

Bounds: [0.0, 1.0]. Default: 0.0. 




**Returns**

  * (::Float) — Optional. Minimum scale-down threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2 worker scale-down for the cluster to scale. A threshold of 0 means the autoscaler will scale down on any recommended change.

Bounds: [0.0, 1.0]. Default: 0.0. 




### #scale_up_factor
    
    
    def scale_up_factor() -> ::Float

**Returns**

  * (::Float) — Required. Fraction of average YARN pending memory in the last cooldown period for which to add workers. A scale-up factor of 1.0 will result in scaling up so that there is no pending memory remaining after the update (more aggressive scaling). A scale-up factor closer to 0 will result in a smaller magnitude of scaling up (less aggressive scaling). See [How autoscaling works](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling#how_autoscaling_works) for more information.

Bounds: [0.0, 1.0]. 




### #scale_up_factor=
    
    
    def scale_up_factor=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Required. Fraction of average YARN pending memory in the last cooldown period for which to add workers. A scale-up factor of 1.0 will result in scaling up so that there is no pending memory remaining after the update (more aggressive scaling). A scale-up factor closer to 0 will result in a smaller magnitude of scaling up (less aggressive scaling). See [How autoscaling works](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling#how_autoscaling_works) for more information.

Bounds: [0.0, 1.0]. 




**Returns**

  * (::Float) — Required. Fraction of average YARN pending memory in the last cooldown period for which to add workers. A scale-up factor of 1.0 will result in scaling up so that there is no pending memory remaining after the update (more aggressive scaling). A scale-up factor closer to 0 will result in a smaller magnitude of scaling up (less aggressive scaling). See [How autoscaling works](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling#how_autoscaling_works) for more information.

Bounds: [0.0, 1.0]. 




### #scale_up_min_worker_fraction
    
    
    def scale_up_min_worker_fraction() -> ::Float

**Returns**

  * (::Float) — Optional. Minimum scale-up threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2-worker scale-up for the cluster to scale. A threshold of 0 means the autoscaler will scale up on any recommended change.

Bounds: [0.0, 1.0]. Default: 0.0. 




### #scale_up_min_worker_fraction=
    
    
    def scale_up_min_worker_fraction=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Optional. Minimum scale-up threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2-worker scale-up for the cluster to scale. A threshold of 0 means the autoscaler will scale up on any recommended change.

Bounds: [0.0, 1.0]. Default: 0.0. 




**Returns**

  * (::Float) — Optional. Minimum scale-up threshold as a fraction of total cluster size before scaling occurs. For example, in a 20-worker cluster, a threshold of 0.1 means the autoscaler must recommend at least a 2-worker scale-up for the cluster to scale. A threshold of 0 means the autoscaler will scale up on any recommended change.

Bounds: [0.0, 1.0]. Default: 0.0. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
