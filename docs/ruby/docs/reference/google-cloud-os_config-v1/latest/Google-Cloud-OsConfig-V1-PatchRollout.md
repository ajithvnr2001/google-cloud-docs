---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-PatchRollout/
title: Cloud OS Config V1 API - Class Google::Cloud::OsConfig::V1::PatchRollout (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:44.091291+00:00
---

# Cloud OS Config V1 API - Class Google::Cloud::OsConfig::V1::PatchRollout (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-PatchRollout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud OS Config V1 API - Class Google::Cloud::OsConfig::V1::PatchRollout (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1 

Reference documentation and code samples for the Cloud OS Config V1 API class Google::Cloud::OsConfig::V1::PatchRollout.

Patch rollout configuration specifications. Contains details on the concurrency control when applying patch(es) to all targeted VMs.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #disruption_budget
    
    
    def disruption_budget() -> ::Google::Cloud::OsConfig::V1::FixedOrPercent

**Returns**

  * ([::Google::Cloud::OsConfig::V1::FixedOrPercent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-FixedOrPercent)) — The maximum number (or percentage) of VMs per zone to disrupt at any given moment. The number of VMs calculated from multiplying the percentage by the total number of VMs in a zone is rounded up.

During patching, a VM is considered disrupted from the time the agent is notified to begin until patching has completed. This disruption time includes the time to complete reboot and any post-patch steps.

A VM contributes to the disruption budget if its patching operation fails either when applying the patches, running pre or post patch steps, or if it fails to respond with a success notification before timing out. VMs that are not running or do not have an active agent do not count toward this disruption budget.

For zone-by-zone rollouts, if the disruption budget in a zone is exceeded, the patch job stops, because continuing to the next zone requires completion of the patch process in the previous zone.

For example, if the disruption budget has a fixed value of `10`, and 8 VMs fail to patch in the current zone, the patch job continues to patch 2 VMs at a time until the zone is completed. When that zone is completed successfully, patching begins with 10 VMs at a time in the next zone. If 10 VMs in the next zone fail to patch, the patch job stops. 




### #disruption_budget=
    
    
    def disruption_budget=(value) -> ::Google::Cloud::OsConfig::V1::FixedOrPercent

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::FixedOrPercent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-FixedOrPercent)) — The maximum number (or percentage) of VMs per zone to disrupt at any given moment. The number of VMs calculated from multiplying the percentage by the total number of VMs in a zone is rounded up.

During patching, a VM is considered disrupted from the time the agent is notified to begin until patching has completed. This disruption time includes the time to complete reboot and any post-patch steps.

A VM contributes to the disruption budget if its patching operation fails either when applying the patches, running pre or post patch steps, or if it fails to respond with a success notification before timing out. VMs that are not running or do not have an active agent do not count toward this disruption budget.

For zone-by-zone rollouts, if the disruption budget in a zone is exceeded, the patch job stops, because continuing to the next zone requires completion of the patch process in the previous zone.

For example, if the disruption budget has a fixed value of `10`, and 8 VMs fail to patch in the current zone, the patch job continues to patch 2 VMs at a time until the zone is completed. When that zone is completed successfully, patching begins with 10 VMs at a time in the next zone. If 10 VMs in the next zone fail to patch, the patch job stops. 




**Returns**

  * ([::Google::Cloud::OsConfig::V1::FixedOrPercent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-FixedOrPercent)) — The maximum number (or percentage) of VMs per zone to disrupt at any given moment. The number of VMs calculated from multiplying the percentage by the total number of VMs in a zone is rounded up.

During patching, a VM is considered disrupted from the time the agent is notified to begin until patching has completed. This disruption time includes the time to complete reboot and any post-patch steps.

A VM contributes to the disruption budget if its patching operation fails either when applying the patches, running pre or post patch steps, or if it fails to respond with a success notification before timing out. VMs that are not running or do not have an active agent do not count toward this disruption budget.

For zone-by-zone rollouts, if the disruption budget in a zone is exceeded, the patch job stops, because continuing to the next zone requires completion of the patch process in the previous zone.

For example, if the disruption budget has a fixed value of `10`, and 8 VMs fail to patch in the current zone, the patch job continues to patch 2 VMs at a time until the zone is completed. When that zone is completed successfully, patching begins with 10 VMs at a time in the next zone. If 10 VMs in the next zone fail to patch, the patch job stops. 




### #mode
    
    
    def mode() -> ::Google::Cloud::OsConfig::V1::PatchRollout::Mode

**Returns**

  * ([::Google::Cloud::OsConfig::V1::PatchRollout::Mode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-PatchRollout-Mode)) — Mode of the patch rollout. 



### #mode=
    
    
    def mode=(value) -> ::Google::Cloud::OsConfig::V1::PatchRollout::Mode

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1::PatchRollout::Mode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-PatchRollout-Mode)) — Mode of the patch rollout. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1::PatchRollout::Mode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1/latest/Google-Cloud-OsConfig-V1-PatchRollout-Mode)) — Mode of the patch rollout. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
