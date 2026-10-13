---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-RevisionTemplate/
title: Cloud Run V2 API - Class Google::Cloud::Run::V2::RevisionTemplate (v0.29.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:47.828076+00:00
---

# Cloud Run V2 API - Class Google::Cloud::Run::V2::RevisionTemplate (v0.29.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-RevisionTemplate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Run V2 API - Class Google::Cloud::Run::V2::RevisionTemplate (v0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.1  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.1  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Run V2 API class Google::Cloud::Run::V2::RevisionTemplate.

RevisionTemplate describes the data a revision should have when created from a template.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotations
    
    
    def annotations() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

Cloud Run API v2 does not support annotations with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected. All system annotations in v1 now have a corresponding field in v2 RevisionTemplate.

This field follows Kubernetes annotations' namespacing, limits, and rules. 




### #annotations=
    
    
    def annotations=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

Cloud Run API v2 does not support annotations with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected. All system annotations in v1 now have a corresponding field in v2 RevisionTemplate.

This field follows Kubernetes annotations' namespacing, limits, and rules. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

Cloud Run API v2 does not support annotations with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected. All system annotations in v1 now have a corresponding field in v2 RevisionTemplate.

This field follows Kubernetes annotations' namespacing, limits, and rules. 




### #containers
    
    
    def containers() -> ::Array<::Google::Cloud::Run::V2::Container>

**Returns**

  * (::Array<[::Google::Cloud::Run::V2::Container](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Container)>) — Holds the single container that defines the unit of execution for this Revision. 



### #containers=
    
    
    def containers=(value) -> ::Array<::Google::Cloud::Run::V2::Container>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Run::V2::Container](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Container)>) — Holds the single container that defines the unit of execution for this Revision. 



**Returns**

  * (::Array<[::Google::Cloud::Run::V2::Container](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Container)>) — Holds the single container that defines the unit of execution for this Revision. 



### #encryption_key
    
    
    def encryption_key() -> ::String

**Returns**

  * (::String) — A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek 



### #encryption_key=
    
    
    def encryption_key=(value) -> ::String

**Parameter**

  * **value** (::String) — A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek 



**Returns**

  * (::String) — A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek 



### #encryption_key_revocation_action
    
    
    def encryption_key_revocation_action() -> ::Google::Cloud::Run::V2::EncryptionKeyRevocationAction

**Returns**

  * ([::Google::Cloud::Run::V2::EncryptionKeyRevocationAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-EncryptionKeyRevocationAction)) — Optional. The action to take if the encryption key is revoked. 



### #encryption_key_revocation_action=
    
    
    def encryption_key_revocation_action=(value) -> ::Google::Cloud::Run::V2::EncryptionKeyRevocationAction

**Parameter**

  * **value** ([::Google::Cloud::Run::V2::EncryptionKeyRevocationAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-EncryptionKeyRevocationAction)) — Optional. The action to take if the encryption key is revoked. 



**Returns**

  * ([::Google::Cloud::Run::V2::EncryptionKeyRevocationAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-EncryptionKeyRevocationAction)) — Optional. The action to take if the encryption key is revoked. 



### #encryption_key_shutdown_duration
    
    
    def encryption_key_shutdown_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Protobuf-Duration)) — Optional. If encryption_key_revocation_action is SHUTDOWN, the duration before shutting down all instances. The minimum increment is 1 hour. 



### #encryption_key_shutdown_duration=
    
    
    def encryption_key_shutdown_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Protobuf-Duration)) — Optional. If encryption_key_revocation_action is SHUTDOWN, the duration before shutting down all instances. The minimum increment is 1 hour. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Protobuf-Duration)) — Optional. If encryption_key_revocation_action is SHUTDOWN, the duration before shutting down all instances. The minimum increment is 1 hour. 



### #execution_environment
    
    
    def execution_environment() -> ::Google::Cloud::Run::V2::ExecutionEnvironment

**Returns**

  * ([::Google::Cloud::Run::V2::ExecutionEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ExecutionEnvironment)) — Optional. The sandbox environment to host this Revision. 



### #execution_environment=
    
    
    def execution_environment=(value) -> ::Google::Cloud::Run::V2::ExecutionEnvironment

**Parameter**

  * **value** ([::Google::Cloud::Run::V2::ExecutionEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ExecutionEnvironment)) — Optional. The sandbox environment to host this Revision. 



**Returns**

  * ([::Google::Cloud::Run::V2::ExecutionEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ExecutionEnvironment)) — Optional. The sandbox environment to host this Revision. 



### #gpu_zonal_redundancy_disabled
    
    
    def gpu_zonal_redundancy_disabled() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. True if GPU zonal redundancy is disabled on this revision. 



### #gpu_zonal_redundancy_disabled=
    
    
    def gpu_zonal_redundancy_disabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. True if GPU zonal redundancy is disabled on this revision. 



**Returns**

  * (::Boolean) — Optional. True if GPU zonal redundancy is disabled on this revision. 



### #health_check_disabled
    
    
    def health_check_disabled() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Disables health checking containers during deployment. 



### #health_check_disabled=
    
    
    def health_check_disabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Disables health checking containers during deployment. 



**Returns**

  * (::Boolean) — Optional. Disables health checking containers during deployment. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels.

Cloud Run API v2 does not support labels with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected. All system labels in v1 now have a corresponding field in v2 RevisionTemplate. 




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels.

Cloud Run API v2 does not support labels with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected. All system labels in v1 now have a corresponding field in v2 RevisionTemplate. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels.

Cloud Run API v2 does not support labels with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected. All system labels in v1 now have a corresponding field in v2 RevisionTemplate. 




### #max_instance_request_concurrency
    
    
    def max_instance_request_concurrency() -> ::Integer

**Returns**

  * (::Integer) — Optional. Sets the maximum number of requests that each serving instance can receive. If not specified or 0, concurrency defaults to 80 when requested `CPU >= 1` and defaults to 1 when requested `CPU < 1`. 



### #max_instance_request_concurrency=
    
    
    def max_instance_request_concurrency=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Sets the maximum number of requests that each serving instance can receive. If not specified or 0, concurrency defaults to 80 when requested `CPU >= 1` and defaults to 1 when requested `CPU < 1`. 



**Returns**

  * (::Integer) — Optional. Sets the maximum number of requests that each serving instance can receive. If not specified or 0, concurrency defaults to 80 when requested `CPU >= 1` and defaults to 1 when requested `CPU < 1`. 



### #node_selector
    
    
    def node_selector() -> ::Google::Cloud::Run::V2::NodeSelector

**Returns**

  * ([::Google::Cloud::Run::V2::NodeSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-NodeSelector)) — Optional. The node selector for the revision template. 



### #node_selector=
    
    
    def node_selector=(value) -> ::Google::Cloud::Run::V2::NodeSelector

**Parameter**

  * **value** ([::Google::Cloud::Run::V2::NodeSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-NodeSelector)) — Optional. The node selector for the revision template. 



**Returns**

  * ([::Google::Cloud::Run::V2::NodeSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-NodeSelector)) — Optional. The node selector for the revision template. 



### #revision
    
    
    def revision() -> ::String

**Returns**

  * (::String) — Optional. The unique name for the revision. If this field is omitted, it will be automatically generated based on the Service name. 



### #revision=
    
    
    def revision=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The unique name for the revision. If this field is omitted, it will be automatically generated based on the Service name. 



**Returns**

  * (::String) — Optional. The unique name for the revision. If this field is omitted, it will be automatically generated based on the Service name. 



### #scaling
    
    
    def scaling() -> ::Google::Cloud::Run::V2::RevisionScaling

**Returns**

  * ([::Google::Cloud::Run::V2::RevisionScaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-RevisionScaling)) — Optional. Scaling settings for this Revision. 



### #scaling=
    
    
    def scaling=(value) -> ::Google::Cloud::Run::V2::RevisionScaling

**Parameter**

  * **value** ([::Google::Cloud::Run::V2::RevisionScaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-RevisionScaling)) — Optional. Scaling settings for this Revision. 



**Returns**

  * ([::Google::Cloud::Run::V2::RevisionScaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-RevisionScaling)) — Optional. Scaling settings for this Revision. 



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — Optional. Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. If not provided, the revision will use the project's default service account. 



### #service_account=
    
    
    def service_account=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. If not provided, the revision will use the project's default service account. 



**Returns**

  * (::String) — Optional. Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. If not provided, the revision will use the project's default service account. 



### #service_mesh
    
    
    def service_mesh() -> ::Google::Cloud::Run::V2::ServiceMesh

**Returns**

  * ([::Google::Cloud::Run::V2::ServiceMesh](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ServiceMesh)) — Optional. Enables service mesh connectivity. 



### #service_mesh=
    
    
    def service_mesh=(value) -> ::Google::Cloud::Run::V2::ServiceMesh

**Parameter**

  * **value** ([::Google::Cloud::Run::V2::ServiceMesh](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ServiceMesh)) — Optional. Enables service mesh connectivity. 



**Returns**

  * ([::Google::Cloud::Run::V2::ServiceMesh](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ServiceMesh)) — Optional. Enables service mesh connectivity. 



### #session_affinity
    
    
    def session_affinity() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Enable session affinity. 



### #session_affinity=
    
    
    def session_affinity=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Enable session affinity. 



**Returns**

  * (::Boolean) — Optional. Enable session affinity. 



### #timeout
    
    
    def timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Protobuf-Duration)) — Optional. Max allowed time for an instance to respond to a request. 



### #timeout=
    
    
    def timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Protobuf-Duration)) — Optional. Max allowed time for an instance to respond to a request. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Protobuf-Duration)) — Optional. Max allowed time for an instance to respond to a request. 



### #volumes
    
    
    def volumes() -> ::Array<::Google::Cloud::Run::V2::Volume>

**Returns**

  * (::Array<[::Google::Cloud::Run::V2::Volume](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Volume)>) — Optional. A list of Volumes to make available to containers. 



### #volumes=
    
    
    def volumes=(value) -> ::Array<::Google::Cloud::Run::V2::Volume>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Run::V2::Volume](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Volume)>) — Optional. A list of Volumes to make available to containers. 



**Returns**

  * (::Array<[::Google::Cloud::Run::V2::Volume](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Volume)>) — Optional. A list of Volumes to make available to containers. 



### #vpc_access
    
    
    def vpc_access() -> ::Google::Cloud::Run::V2::VpcAccess

**Returns**

  * ([::Google::Cloud::Run::V2::VpcAccess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-VpcAccess)) — Optional. VPC Access configuration to use for this Revision. For more information, visit https://cloud.google.com/run/docs/configuring/connecting-vpc. 



### #vpc_access=
    
    
    def vpc_access=(value) -> ::Google::Cloud::Run::V2::VpcAccess

**Parameter**

  * **value** ([::Google::Cloud::Run::V2::VpcAccess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-VpcAccess)) — Optional. VPC Access configuration to use for this Revision. For more information, visit https://cloud.google.com/run/docs/configuring/connecting-vpc. 



**Returns**

  * ([::Google::Cloud::Run::V2::VpcAccess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-VpcAccess)) — Optional. VPC Access configuration to use for this Revision. For more information, visit https://cloud.google.com/run/docs/configuring/connecting-vpc. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
