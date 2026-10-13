---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeBackupsResponse/
title: Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::ListVolumeBackupsResponse (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:14.074405+00:00
---

# Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::ListVolumeBackupsResponse (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeBackupsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::ListVolumeBackupsResponse (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Backup for GKE V1 API class Google::Cloud::GkeBackup::V1::ListVolumeBackupsResponse.

Response message for ListVolumeBackups.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token which may be sent as [page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeBackupsRequest#Google__Cloud__GkeBackup__V1__ListVolumeBackupsRequest_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListVolumeBackupsRequest#page_token \(method\)") in a subsequent `ListVolumeBackups` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token which may be sent as [page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeBackupsRequest#Google__Cloud__GkeBackup__V1__ListVolumeBackupsRequest_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListVolumeBackupsRequest#page_token \(method\)") in a subsequent `ListVolumeBackups` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. 



**Returns**

  * (::String) — A token which may be sent as [page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeBackupsRequest#Google__Cloud__GkeBackup__V1__ListVolumeBackupsRequest_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListVolumeBackupsRequest#page_token \(method\)") in a subsequent `ListVolumeBackups` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. 



### #volume_backups
    
    
    def volume_backups() -> ::Array<::Google::Cloud::GkeBackup::V1::VolumeBackup>

**Returns**

  * (::Array<[::Google::Cloud::GkeBackup::V1::VolumeBackup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeBackup)>) — The list of VolumeBackups matching the given criteria. 



### #volume_backups=
    
    
    def volume_backups=(value) -> ::Array<::Google::Cloud::GkeBackup::V1::VolumeBackup>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GkeBackup::V1::VolumeBackup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeBackup)>) — The list of VolumeBackups matching the given criteria. 



**Returns**

  * (::Array<[::Google::Cloud::GkeBackup::V1::VolumeBackup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeBackup)>) — The list of VolumeBackups matching the given criteria. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-12 UTC."],[],[]] 
