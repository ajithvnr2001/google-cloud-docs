---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-CreateManagementServerRequest/
title: Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::CreateManagementServerRequest (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:12.771209+00:00
---

# Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::CreateManagementServerRequest (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-CreateManagementServerRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::CreateManagementServerRequest (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Backup and DR Service V1BETA API class Google::Cloud::BackupDR::V1beta::CreateManagementServerRequest.

Request message for creating a management server instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #management_server
    
    
    def management_server() -> ::Google::Cloud::BackupDR::V1beta::ManagementServer

**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-ManagementServer)) — Required. A [management server resource][google.cloud.backupdr.v1.ManagementServer] 



### #management_server=
    
    
    def management_server=(value) -> ::Google::Cloud::BackupDR::V1beta::ManagementServer

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1beta::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-ManagementServer)) — Required. A [management server resource][google.cloud.backupdr.v1.ManagementServer] 



**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-ManagementServer)) — Required. A [management server resource][google.cloud.backupdr.v1.ManagementServer] 



### #management_server_id
    
    
    def management_server_id() -> ::String

**Returns**

  * (::String) — Required. The name of the management server to create. The name must be unique for the specified project and location. 



### #management_server_id=
    
    
    def management_server_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the management server to create. The name must be unique for the specified project and location. 



**Returns**

  * (::String) — Required. The name of the management server to create. The name must be unique for the specified project and location. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The management server project and location in the format 'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR locations map to Google Cloud regions, for example **us-central1**. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The management server project and location in the format 'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR locations map to Google Cloud regions, for example **us-central1**. 



**Returns**

  * (::String) — Required. The management server project and location in the format 'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR locations map to Google Cloud regions, for example **us-central1**. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
