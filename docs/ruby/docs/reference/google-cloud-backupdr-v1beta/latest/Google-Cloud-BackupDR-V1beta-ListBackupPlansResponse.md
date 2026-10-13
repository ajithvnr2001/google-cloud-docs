---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-ListBackupPlansResponse/
title: Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::ListBackupPlansResponse (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:45.299535+00:00
---

# Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::ListBackupPlansResponse (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-ListBackupPlansResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::ListBackupPlansResponse (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Backup and DR Service V1BETA API class Google::Cloud::BackupDR::V1beta::ListBackupPlansResponse.

The response message for getting a list of `BackupPlan`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_plans
    
    
    def backup_plans() -> ::Array<::Google::Cloud::BackupDR::V1beta::BackupPlan>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1beta::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-BackupPlan)>) — The list of `BackupPlans` in the project for the specified location.

If the `{location}` value in the request is "-", the response contains a list of resources from all locations. In case any location is unreachable, the response will only return backup plans in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations. BackupPlan 




### #backup_plans=
    
    
    def backup_plans=(value) -> ::Array<::Google::Cloud::BackupDR::V1beta::BackupPlan>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1beta::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-BackupPlan)>) — The list of `BackupPlans` in the project for the specified location.

If the `{location}` value in the request is "-", the response contains a list of resources from all locations. In case any location is unreachable, the response will only return backup plans in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations. BackupPlan 




**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1beta::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-BackupPlan)>) — The list of `BackupPlans` in the project for the specified location.

If the `{location}` value in the request is "-", the response contains a list of resources from all locations. In case any location is unreachable, the response will only return backup plans in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations. BackupPlan 




### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token which may be sent as [page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-ListBackupPlansRequest#Google__Cloud__BackupDR__V1beta__ListBackupPlansRequest_page_token_instance_ "Google::Cloud::BackupDR::V1beta::ListBackupPlansRequest#page_token \(method\)") in a subsequent `ListBackupPlans` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token which may be sent as [page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-ListBackupPlansRequest#Google__Cloud__BackupDR__V1beta__ListBackupPlansRequest_page_token_instance_ "Google::Cloud::BackupDR::V1beta::ListBackupPlansRequest#page_token \(method\)") in a subsequent `ListBackupPlans` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. 



**Returns**

  * (::String) — A token which may be sent as [page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-ListBackupPlansRequest#Google__Cloud__BackupDR__V1beta__ListBackupPlansRequest_page_token_instance_ "Google::Cloud::BackupDR::V1beta::ListBackupPlansRequest#page_token \(method\)") in a subsequent `ListBackupPlans` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Locations that could not be reached. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Locations that could not be reached. 



**Returns**

  * (::Array<::String>) — Locations that could not be reached. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
