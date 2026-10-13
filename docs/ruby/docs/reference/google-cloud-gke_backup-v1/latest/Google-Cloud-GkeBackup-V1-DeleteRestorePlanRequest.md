---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteRestorePlanRequest/
title: Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::DeleteRestorePlanRequest (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:18.600126+00:00
---

# Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::DeleteRestorePlanRequest (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteRestorePlanRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::DeleteRestorePlanRequest (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Backup for GKE V1 API class Google::Cloud::GkeBackup::V1::DeleteRestorePlanRequest.

Request message for DeleteRestorePlan.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Optional. If provided, this value must match the current value of the target RestorePlan's [etag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan#Google__Cloud__GkeBackup__V1__RestorePlan_etag_instance_ "Google::Cloud::GkeBackup::V1::RestorePlan#etag \(method\)") field or the request is rejected. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. If provided, this value must match the current value of the target RestorePlan's [etag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan#Google__Cloud__GkeBackup__V1__RestorePlan_etag_instance_ "Google::Cloud::GkeBackup::V1::RestorePlan#etag \(method\)") field or the request is rejected. 



**Returns**

  * (::String) — Optional. If provided, this value must match the current value of the target RestorePlan's [etag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan#Google__Cloud__GkeBackup__V1__RestorePlan_etag_instance_ "Google::Cloud::GkeBackup::V1::RestorePlan#etag \(method\)") field or the request is rejected. 



### #force
    
    
    def force() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true, any Restores below this RestorePlan will also be deleted. Otherwise, the request will only succeed if the RestorePlan has no Restores. 



### #force=
    
    
    def force=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true, any Restores below this RestorePlan will also be deleted. Otherwise, the request will only succeed if the RestorePlan has no Restores. 



**Returns**

  * (::Boolean) — Optional. If set to true, any Restores below this RestorePlan will also be deleted. Otherwise, the request will only succeed if the RestorePlan has no Restores. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Fully qualified RestorePlan name. Format: `projects/*/locations/*/restorePlans/*`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Fully qualified RestorePlan name. Format: `projects/*/locations/*/restorePlans/*`



**Returns**

  * (::String) — Required. Fully qualified RestorePlan name. Format: `projects/*/locations/*/restorePlans/*`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-12 UTC."],[],[]] 
