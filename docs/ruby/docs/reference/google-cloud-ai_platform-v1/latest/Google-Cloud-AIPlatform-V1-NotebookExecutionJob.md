---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::NotebookExecutionJob (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:26.893568+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::NotebookExecutionJob (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::NotebookExecutionJob (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::NotebookExecutionJob.

NotebookExecutionJob represents an instance of a notebook execution.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when this NotebookExecutionJob was created. 



### #custom_environment_spec
    
    
    def custom_environment_spec() -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::CustomEnvironmentSpec

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::CustomEnvironmentSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-CustomEnvironmentSpec)) — The custom compute configuration for an execution job.

Note: The following fields are mutually exclusive: `custom_environment_spec`, `notebook_runtime_template_resource_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #custom_environment_spec=
    
    
    def custom_environment_spec=(value) -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::CustomEnvironmentSpec

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::CustomEnvironmentSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-CustomEnvironmentSpec)) — The custom compute configuration for an execution job.

Note: The following fields are mutually exclusive: `custom_environment_spec`, `notebook_runtime_template_resource_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::CustomEnvironmentSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-CustomEnvironmentSpec)) — The custom compute configuration for an execution job.

Note: The following fields are mutually exclusive: `custom_environment_spec`, `notebook_runtime_template_resource_name`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dataform_repository_source
    
    
    def dataform_repository_source() -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DataformRepositorySource

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DataformRepositorySource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-DataformRepositorySource)) — The Dataform Repository pointing to a single file notebook repository.

Note: The following fields are mutually exclusive: `dataform_repository_source`, `gcs_notebook_source`, `direct_notebook_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dataform_repository_source=
    
    
    def dataform_repository_source=(value) -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DataformRepositorySource

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DataformRepositorySource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-DataformRepositorySource)) — The Dataform Repository pointing to a single file notebook repository.

Note: The following fields are mutually exclusive: `dataform_repository_source`, `gcs_notebook_source`, `direct_notebook_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DataformRepositorySource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-DataformRepositorySource)) — The Dataform Repository pointing to a single file notebook repository.

Note: The following fields are mutually exclusive: `dataform_repository_source`, `gcs_notebook_source`, `direct_notebook_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #direct_notebook_source
    
    
    def direct_notebook_source() -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DirectNotebookSource

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DirectNotebookSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-DirectNotebookSource)) — The contents of an input notebook file.

Note: The following fields are mutually exclusive: `direct_notebook_source`, `dataform_repository_source`, `gcs_notebook_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #direct_notebook_source=
    
    
    def direct_notebook_source=(value) -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DirectNotebookSource

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DirectNotebookSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-DirectNotebookSource)) — The contents of an input notebook file.

Note: The following fields are mutually exclusive: `direct_notebook_source`, `dataform_repository_source`, `gcs_notebook_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::DirectNotebookSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-DirectNotebookSource)) — The contents of an input notebook file.

Note: The following fields are mutually exclusive: `direct_notebook_source`, `dataform_repository_source`, `gcs_notebook_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — The display name of the NotebookExecutionJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The display name of the NotebookExecutionJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. 



**Returns**

  * (::String) — The display name of the NotebookExecutionJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. 



### #encryption_spec
    
    
    def encryption_spec() -> ::Google::Cloud::AIPlatform::V1::EncryptionSpec

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::EncryptionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EncryptionSpec)) — Customer-managed encryption key spec for the notebook execution job. This field is auto-populated if the [NotebookRuntimeTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookRuntimeTemplate "Google::Cloud::AIPlatform::V1::NotebookRuntimeTemplate \(class\)") has an encryption spec. 



### #encryption_spec=
    
    
    def encryption_spec=(value) -> ::Google::Cloud::AIPlatform::V1::EncryptionSpec

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::EncryptionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EncryptionSpec)) — Customer-managed encryption key spec for the notebook execution job. This field is auto-populated if the [NotebookRuntimeTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookRuntimeTemplate "Google::Cloud::AIPlatform::V1::NotebookRuntimeTemplate \(class\)") has an encryption spec. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::EncryptionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EncryptionSpec)) — Customer-managed encryption key spec for the notebook execution job. This field is auto-populated if the [NotebookRuntimeTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookRuntimeTemplate "Google::Cloud::AIPlatform::V1::NotebookRuntimeTemplate \(class\)") has an encryption spec. 



### #execution_timeout
    
    
    def execution_timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Duration)) — Max running time of the execution job in seconds (default 86400s / 24 hrs). 



### #execution_timeout=
    
    
    def execution_timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Duration)) — Max running time of the execution job in seconds (default 86400s / 24 hrs). 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Duration)) — Max running time of the execution job in seconds (default 86400s / 24 hrs). 



### #execution_user
    
    
    def execution_user() -> ::String

**Returns**

  * (::String) — The user email to run the execution as. Only supported by Colab runtimes.

Note: The following fields are mutually exclusive: `execution_user`, `service_account`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #execution_user=
    
    
    def execution_user=(value) -> ::String

**Parameter**

  * **value** (::String) — The user email to run the execution as. Only supported by Colab runtimes.

Note: The following fields are mutually exclusive: `execution_user`, `service_account`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The user email to run the execution as. Only supported by Colab runtimes.

Note: The following fields are mutually exclusive: `execution_user`, `service_account`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_notebook_source
    
    
    def gcs_notebook_source() -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::GcsNotebookSource

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::GcsNotebookSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-GcsNotebookSource)) — The Cloud Storage url pointing to the ipynb file. Format: `gs://bucket/notebook_file.ipynb`

Note: The following fields are mutually exclusive: `gcs_notebook_source`, `dataform_repository_source`, `direct_notebook_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_notebook_source=
    
    
    def gcs_notebook_source=(value) -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::GcsNotebookSource

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::GcsNotebookSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-GcsNotebookSource)) — The Cloud Storage url pointing to the ipynb file. Format: `gs://bucket/notebook_file.ipynb`

Note: The following fields are mutually exclusive: `gcs_notebook_source`, `dataform_repository_source`, `direct_notebook_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::GcsNotebookSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-GcsNotebookSource)) — The Cloud Storage url pointing to the ipynb file. Format: `gs://bucket/notebook_file.ipynb`

Note: The following fields are mutually exclusive: `gcs_notebook_source`, `dataform_repository_source`, `direct_notebook_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_output_uri
    
    
    def gcs_output_uri() -> ::String

**Returns**

  * (::String) — The Cloud Storage location to upload the result to. Format: `gs://bucket-name`



### #gcs_output_uri=
    
    
    def gcs_output_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The Cloud Storage location to upload the result to. Format: `gs://bucket-name`



**Returns**

  * (::String) — The Cloud Storage location to upload the result to. Format: `gs://bucket-name`



### #job_state
    
    
    def job_state() -> ::Google::Cloud::AIPlatform::V1::JobState

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::JobState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-JobState)) — Output only. The state of the NotebookExecutionJob. 



### #kernel_name
    
    
    def kernel_name() -> ::String

**Returns**

  * (::String) — The name of the kernel to use during notebook execution. If unset, the default kernel is used. 



### #kernel_name=
    
    
    def kernel_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the kernel to use during notebook execution. If unset, the default kernel is used. 



**Returns**

  * (::String) — The name of the kernel to use during notebook execution. If unset, the default kernel is used. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The labels with user-defined metadata to organize NotebookExecutionJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. 




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — The labels with user-defined metadata to organize NotebookExecutionJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The labels with user-defined metadata to organize NotebookExecutionJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource name of this NotebookExecutionJob. Format: `projects/{project_id}/locations/{location}/notebookExecutionJobs/{job_id}`



### #notebook_runtime_template_resource_name
    
    
    def notebook_runtime_template_resource_name() -> ::String

**Returns**

  * (::String) — The NotebookRuntimeTemplate to source compute configuration from.

Note: The following fields are mutually exclusive: `notebook_runtime_template_resource_name`, `custom_environment_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #notebook_runtime_template_resource_name=
    
    
    def notebook_runtime_template_resource_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The NotebookRuntimeTemplate to source compute configuration from.

Note: The following fields are mutually exclusive: `notebook_runtime_template_resource_name`, `custom_environment_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The NotebookRuntimeTemplate to source compute configuration from.

Note: The following fields are mutually exclusive: `notebook_runtime_template_resource_name`, `custom_environment_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #schedule_resource_name
    
    
    def schedule_resource_name() -> ::String

**Returns**

  * (::String) — The Schedule resource name if this job is triggered by one. Format: `projects/{project_id}/locations/{location}/schedules/{schedule_id}`



### #schedule_resource_name=
    
    
    def schedule_resource_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The Schedule resource name if this job is triggered by one. Format: `projects/{project_id}/locations/{location}/schedules/{schedule_id}`



**Returns**

  * (::String) — The Schedule resource name if this job is triggered by one. Format: `projects/{project_id}/locations/{location}/schedules/{schedule_id}`



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — The service account to run the execution as.

Note: The following fields are mutually exclusive: `service_account`, `execution_user`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #service_account=
    
    
    def service_account=(value) -> ::String

**Parameter**

  * **value** (::String) — The service account to run the execution as.

Note: The following fields are mutually exclusive: `service_account`, `execution_user`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The service account to run the execution as.

Note: The following fields are mutually exclusive: `service_account`, `execution_user`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #status
    
    
    def status() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Rpc-Status)) — Output only. Populated when the NotebookExecutionJob is completed. When there is an error during notebook execution, the error details are populated. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when this NotebookExecutionJob was most recently updated. 



### #workbench_runtime
    
    
    def workbench_runtime() -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::WorkbenchRuntime

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::WorkbenchRuntime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-WorkbenchRuntime)) — The Workbench runtime configuration to use for the notebook execution. 



### #workbench_runtime=
    
    
    def workbench_runtime=(value) -> ::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::WorkbenchRuntime

**Parameter**

  * **value** ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::WorkbenchRuntime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-WorkbenchRuntime)) — The Workbench runtime configuration to use for the notebook execution. 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::NotebookExecutionJob::WorkbenchRuntime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookExecutionJob-WorkbenchRuntime)) — The Workbench runtime configuration to use for the notebook execution. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
