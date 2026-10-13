---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-DeleteBackupVaultRequest/
title: Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::DeleteBackupVaultRequest (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:09.259406+00:00
---

# Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::DeleteBackupVaultRequest (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-DeleteBackupVaultRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::DeleteBackupVaultRequest (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Backup and DR Service V1BETA API class Google::Cloud::BackupDR::V1beta::DeleteBackupVaultRequest.

Message for deleting a BackupVault.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allow_missing
    
    
    def allow_missing() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If true and the BackupVault is not found, the request will succeed but no action will be taken. 



### #allow_missing=
    
    
    def allow_missing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If true and the BackupVault is not found, the request will succeed but no action will be taken. 



**Returns**

  * (::Boolean) — Optional. If true and the BackupVault is not found, the request will succeed but no action will be taken. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — The current etag of the backup vault. If an etag is provided and does not match the current etag of the connection, deletion will be blocked. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — The current etag of the backup vault. If an etag is provided and does not match the current etag of the connection, deletion will be blocked. 



**Returns**

  * (::String) — The current etag of the backup vault. If an etag is provided and does not match the current etag of the connection, deletion will be blocked. 



### #force
    
    
    def force() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true, any data source from this backup vault will also be deleted. 



### #force=
    
    
    def force=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true, any data source from this backup vault will also be deleted. 



**Returns**

  * (::Boolean) — Optional. If set to true, any data source from this backup vault will also be deleted. 



### #ignore_backup_plan_references
    
    
    def ignore_backup_plan_references() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true, backupvault deletion will proceed even if there are backup plans referencing the backupvault. The default is 'false'. 



### #ignore_backup_plan_references=
    
    
    def ignore_backup_plan_references=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true, backupvault deletion will proceed even if there are backup plans referencing the backupvault. The default is 'false'. 



**Returns**

  * (::Boolean) — Optional. If set to true, backupvault deletion will proceed even if there are backup plans referencing the backupvault. The default is 'false'. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Name of the resource. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the resource. 



**Returns**

  * (::String) — Required. Name of the resource. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is 'false'. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is 'false'. 



**Returns**

  * (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is 'false'. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
