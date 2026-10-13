---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-OperationMetadata/
title: Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::OperationMetadata (v0.19.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:38.564025+00:00
---

# Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::OperationMetadata (v0.19.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-OperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::OperationMetadata (v0.19.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.1  0.13.1  0.12.0  0.11.1  0.10.2  0.9.0  0.8.0  0.7.0  0.6.1  0.5.5 

Reference documentation and code samples for the Cloud AutoML V1beta1 API class Google::Cloud::AutoML::V1beta1::OperationMetadata.

Metadata used across all long running operations returned by AutoML API.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #batch_predict_details
    
    
    def batch_predict_details() -> ::Google::Cloud::AutoML::V1beta1::BatchPredictOperationMetadata

**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::BatchPredictOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-BatchPredictOperationMetadata)) — Details of BatchPredict operation.

Note: The following fields are mutually exclusive: `batch_predict_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #batch_predict_details=
    
    
    def batch_predict_details=(value) -> ::Google::Cloud::AutoML::V1beta1::BatchPredictOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1beta1::BatchPredictOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-BatchPredictOperationMetadata)) — Details of BatchPredict operation.

Note: The following fields are mutually exclusive: `batch_predict_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::BatchPredictOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-BatchPredictOperationMetadata)) — Details of BatchPredict operation.

Note: The following fields are mutually exclusive: `batch_predict_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_model_details
    
    
    def create_model_details() -> ::Google::Cloud::AutoML::V1beta1::CreateModelOperationMetadata

**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::CreateModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-CreateModelOperationMetadata)) — Details of CreateModel operation.

Note: The following fields are mutually exclusive: `create_model_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_model_details=
    
    
    def create_model_details=(value) -> ::Google::Cloud::AutoML::V1beta1::CreateModelOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1beta1::CreateModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-CreateModelOperationMetadata)) — Details of CreateModel operation.

Note: The following fields are mutually exclusive: `create_model_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::CreateModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-CreateModelOperationMetadata)) — Details of CreateModel operation.

Note: The following fields are mutually exclusive: `create_model_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the operation was created. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the operation was created. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the operation was created. 



### #delete_details
    
    
    def delete_details() -> ::Google::Cloud::AutoML::V1beta1::DeleteOperationMetadata

**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::DeleteOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-DeleteOperationMetadata)) — Details of a Delete operation.

Note: The following fields are mutually exclusive: `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #delete_details=
    
    
    def delete_details=(value) -> ::Google::Cloud::AutoML::V1beta1::DeleteOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1beta1::DeleteOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-DeleteOperationMetadata)) — Details of a Delete operation.

Note: The following fields are mutually exclusive: `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::DeleteOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-DeleteOperationMetadata)) — Details of a Delete operation.

Note: The following fields are mutually exclusive: `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #deploy_model_details
    
    
    def deploy_model_details() -> ::Google::Cloud::AutoML::V1beta1::DeployModelOperationMetadata

**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::DeployModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-DeployModelOperationMetadata)) — Details of a DeployModel operation.

Note: The following fields are mutually exclusive: `deploy_model_details`, `delete_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #deploy_model_details=
    
    
    def deploy_model_details=(value) -> ::Google::Cloud::AutoML::V1beta1::DeployModelOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1beta1::DeployModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-DeployModelOperationMetadata)) — Details of a DeployModel operation.

Note: The following fields are mutually exclusive: `deploy_model_details`, `delete_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::DeployModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-DeployModelOperationMetadata)) — Details of a DeployModel operation.

Note: The following fields are mutually exclusive: `deploy_model_details`, `delete_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #export_data_details
    
    
    def export_data_details() -> ::Google::Cloud::AutoML::V1beta1::ExportDataOperationMetadata

**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::ExportDataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportDataOperationMetadata)) — Details of ExportData operation.

Note: The following fields are mutually exclusive: `export_data_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #export_data_details=
    
    
    def export_data_details=(value) -> ::Google::Cloud::AutoML::V1beta1::ExportDataOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1beta1::ExportDataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportDataOperationMetadata)) — Details of ExportData operation.

Note: The following fields are mutually exclusive: `export_data_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::ExportDataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportDataOperationMetadata)) — Details of ExportData operation.

Note: The following fields are mutually exclusive: `export_data_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #export_evaluated_examples_details
    
    
    def export_evaluated_examples_details() -> ::Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOperationMetadata

**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportEvaluatedExamplesOperationMetadata)) — Details of ExportEvaluatedExamples operation.

Note: The following fields are mutually exclusive: `export_evaluated_examples_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #export_evaluated_examples_details=
    
    
    def export_evaluated_examples_details=(value) -> ::Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportEvaluatedExamplesOperationMetadata)) — Details of ExportEvaluatedExamples operation.

Note: The following fields are mutually exclusive: `export_evaluated_examples_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportEvaluatedExamplesOperationMetadata)) — Details of ExportEvaluatedExamples operation.

Note: The following fields are mutually exclusive: `export_evaluated_examples_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #export_model_details
    
    
    def export_model_details() -> ::Google::Cloud::AutoML::V1beta1::ExportModelOperationMetadata

**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::ExportModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportModelOperationMetadata)) — Details of ExportModel operation.

Note: The following fields are mutually exclusive: `export_model_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #export_model_details=
    
    
    def export_model_details=(value) -> ::Google::Cloud::AutoML::V1beta1::ExportModelOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1beta1::ExportModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportModelOperationMetadata)) — Details of ExportModel operation.

Note: The following fields are mutually exclusive: `export_model_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::ExportModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportModelOperationMetadata)) — Details of ExportModel operation.

Note: The following fields are mutually exclusive: `export_model_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #import_data_details
    
    
    def import_data_details() -> ::Google::Cloud::AutoML::V1beta1::ImportDataOperationMetadata

**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::ImportDataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ImportDataOperationMetadata)) — Details of ImportData operation.

Note: The following fields are mutually exclusive: `import_data_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #import_data_details=
    
    
    def import_data_details=(value) -> ::Google::Cloud::AutoML::V1beta1::ImportDataOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1beta1::ImportDataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ImportDataOperationMetadata)) — Details of ImportData operation.

Note: The following fields are mutually exclusive: `import_data_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::ImportDataOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ImportDataOperationMetadata)) — Details of ImportData operation.

Note: The following fields are mutually exclusive: `import_data_details`, `delete_details`, `deploy_model_details`, `undeploy_model_details`, `create_model_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #partial_failures
    
    
    def partial_failures() -> ::Array<::Google::Rpc::Status>

**Returns**

  * (::Array<[::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Rpc-Status)>) — Output only. Partial failures encountered. E.g. single files that couldn't be read. This field should never exceed 20 entries. Status details field will contain standard GCP error details. 



### #partial_failures=
    
    
    def partial_failures=(value) -> ::Array<::Google::Rpc::Status>

**Parameter**

  * **value** (::Array<[::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Rpc-Status)>) — Output only. Partial failures encountered. E.g. single files that couldn't be read. This field should never exceed 20 entries. Status details field will contain standard GCP error details. 



**Returns**

  * (::Array<[::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Rpc-Status)>) — Output only. Partial failures encountered. E.g. single files that couldn't be read. This field should never exceed 20 entries. Status details field will contain standard GCP error details. 



### #progress_percent
    
    
    def progress_percent() -> ::Integer

**Returns**

  * (::Integer) — Output only. Progress of operation. Range: [0, 100]. Not used currently. 



### #progress_percent=
    
    
    def progress_percent=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. Progress of operation. Range: [0, 100]. Not used currently. 



**Returns**

  * (::Integer) — Output only. Progress of operation. Range: [0, 100]. Not used currently. 



### #undeploy_model_details
    
    
    def undeploy_model_details() -> ::Google::Cloud::AutoML::V1beta1::UndeployModelOperationMetadata

**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::UndeployModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-UndeployModelOperationMetadata)) — Details of an UndeployModel operation.

Note: The following fields are mutually exclusive: `undeploy_model_details`, `delete_details`, `deploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #undeploy_model_details=
    
    
    def undeploy_model_details=(value) -> ::Google::Cloud::AutoML::V1beta1::UndeployModelOperationMetadata

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1beta1::UndeployModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-UndeployModelOperationMetadata)) — Details of an UndeployModel operation.

Note: The following fields are mutually exclusive: `undeploy_model_details`, `delete_details`, `deploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AutoML::V1beta1::UndeployModelOperationMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-UndeployModelOperationMetadata)) — Details of an UndeployModel operation.

Note: The following fields are mutually exclusive: `undeploy_model_details`, `delete_details`, `deploy_model_details`, `create_model_details`, `import_data_details`, `batch_predict_details`, `export_data_details`, `export_model_details`, `export_evaluated_examples_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the operation was updated for the last time. 



### #update_time=
    
    
    def update_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the operation was updated for the last time. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the operation was updated for the last time. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
