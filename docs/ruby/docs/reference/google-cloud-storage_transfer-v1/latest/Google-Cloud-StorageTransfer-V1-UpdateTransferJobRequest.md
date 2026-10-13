---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-UpdateTransferJobRequest/
title: Storage Transfer Service V1 API - Class Google::Cloud::StorageTransfer::V1::UpdateTransferJobRequest (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:48.480128+00:00
---

# Storage Transfer Service V1 API - Class Google::Cloud::StorageTransfer::V1::UpdateTransferJobRequest (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-UpdateTransferJobRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Storage Transfer Service V1 API - Class Google::Cloud::StorageTransfer::V1::UpdateTransferJobRequest (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Storage Transfer Service V1 API class Google::Cloud::StorageTransfer::V1::UpdateTransferJobRequest.

Request passed to UpdateTransferJob.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #job_name
    
    
    def job_name() -> ::String

**Returns**

  * (::String) — Required. The name of job to update. 



### #job_name=
    
    
    def job_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of job to update. 



**Returns**

  * (::String) — Required. The name of job to update. 



### #project_id
    
    
    def project_id() -> ::String

**Returns**

  * (::String) — Required. The ID of the Google Cloud project that owns the job. 



### #project_id=
    
    
    def project_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID of the Google Cloud project that owns the job. 



**Returns**

  * (::String) — Required. The ID of the Google Cloud project that owns the job. 



### #transfer_job
    
    
    def transfer_job() -> ::Google::Cloud::StorageTransfer::V1::TransferJob

**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)) — Required. The job to update. `transferJob` is expected to specify one or more of five fields: [description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_description_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#description \(method\)"), [transfer_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_transfer_spec_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#transfer_spec \(method\)"), [notification_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_notification_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#notification_config \(method\)"), [logging_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_logging_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#logging_config \(method\)"), and [status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_status_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#status \(method\)"). An `UpdateTransferJobRequest` that specifies other fields are rejected with the error [INVALID_ARGUMENT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Rpc-Code#Google__Rpc__Code__INVALID_ARGUMENT "Google::Rpc::Code::INVALID_ARGUMENT \(constant\)"). Updating a job status to [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)") requires `storagetransfer.jobs.delete` permission. 



### #transfer_job=
    
    
    def transfer_job=(value) -> ::Google::Cloud::StorageTransfer::V1::TransferJob

**Parameter**

  * **value** ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)) — Required. The job to update. `transferJob` is expected to specify one or more of five fields: [description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_description_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#description \(method\)"), [transfer_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_transfer_spec_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#transfer_spec \(method\)"), [notification_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_notification_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#notification_config \(method\)"), [logging_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_logging_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#logging_config \(method\)"), and [status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_status_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#status \(method\)"). An `UpdateTransferJobRequest` that specifies other fields are rejected with the error [INVALID_ARGUMENT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Rpc-Code#Google__Rpc__Code__INVALID_ARGUMENT "Google::Rpc::Code::INVALID_ARGUMENT \(constant\)"). Updating a job status to [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)") requires `storagetransfer.jobs.delete` permission. 



**Returns**

  * ([::Google::Cloud::StorageTransfer::V1::TransferJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob)) — Required. The job to update. `transferJob` is expected to specify one or more of five fields: [description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_description_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#description \(method\)"), [transfer_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_transfer_spec_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#transfer_spec \(method\)"), [notification_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_notification_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#notification_config \(method\)"), [logging_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_logging_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#logging_config \(method\)"), and [status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_status_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#status \(method\)"). An `UpdateTransferJobRequest` that specifies other fields are rejected with the error [INVALID_ARGUMENT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Rpc-Code#Google__Rpc__Code__INVALID_ARGUMENT "Google::Rpc::Code::INVALID_ARGUMENT \(constant\)"). Updating a job status to [DELETED](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob-Status#Google__Cloud__StorageTransfer__V1__TransferJob__Status__DELETED "Google::Cloud::StorageTransfer::V1::TransferJob::Status::DELETED \(constant\)") requires `storagetransfer.jobs.delete` permission. 



### #update_transfer_job_field_mask
    
    
    def update_transfer_job_field_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-FieldMask)) — The field mask of the fields in `transferJob` that are to be updated in this request. Fields in `transferJob` that can be updated are: [description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_description_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#description \(method\)"), [transfer_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_transfer_spec_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#transfer_spec \(method\)"), [notification_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_notification_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#notification_config \(method\)"), [logging_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_logging_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#logging_config \(method\)"), and [status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_status_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#status \(method\)"). To update the `transfer_spec` of the job, a complete transfer specification must be provided. An incomplete specification missing any required fields is rejected with the error [INVALID_ARGUMENT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Rpc-Code#Google__Rpc__Code__INVALID_ARGUMENT "Google::Rpc::Code::INVALID_ARGUMENT \(constant\)"). 



### #update_transfer_job_field_mask=
    
    
    def update_transfer_job_field_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-FieldMask)) — The field mask of the fields in `transferJob` that are to be updated in this request. Fields in `transferJob` that can be updated are: [description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_description_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#description \(method\)"), [transfer_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_transfer_spec_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#transfer_spec \(method\)"), [notification_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_notification_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#notification_config \(method\)"), [logging_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_logging_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#logging_config \(method\)"), and [status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_status_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#status \(method\)"). To update the `transfer_spec` of the job, a complete transfer specification must be provided. An incomplete specification missing any required fields is rejected with the error [INVALID_ARGUMENT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Rpc-Code#Google__Rpc__Code__INVALID_ARGUMENT "Google::Rpc::Code::INVALID_ARGUMENT \(constant\)"). 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Protobuf-FieldMask)) — The field mask of the fields in `transferJob` that are to be updated in this request. Fields in `transferJob` that can be updated are: [description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_description_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#description \(method\)"), [transfer_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_transfer_spec_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#transfer_spec \(method\)"), [notification_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_notification_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#notification_config \(method\)"), [logging_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_logging_config_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#logging_config \(method\)"), and [status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Cloud-StorageTransfer-V1-TransferJob#Google__Cloud__StorageTransfer__V1__TransferJob_status_instance_ "Google::Cloud::StorageTransfer::V1::TransferJob#status \(method\)"). To update the `transfer_spec` of the job, a complete transfer specification must be provided. An incomplete specification missing any required fields is rejected with the error [INVALID_ARGUMENT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_transfer-v1/latest/Google-Rpc-Code#Google__Rpc__Code__INVALID_ARGUMENT "Google::Rpc::Code::INVALID_ARGUMENT \(constant\)"). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
