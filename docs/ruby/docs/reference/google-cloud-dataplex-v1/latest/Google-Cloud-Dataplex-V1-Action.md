---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Action (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:49.378865+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Action (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Action (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::Action.

Action represents an issue requiring administrator action for resolution.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #asset
    
    
    def asset() -> ::String

**Returns**

  * (::String) — Output only. The relative resource name of the asset, of the form: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}`. 



### #category
    
    
    def category() -> ::Google::Cloud::Dataplex::V1::Action::Category

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::Category](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-Category)) — The category of issue associated with the action. 



### #category=
    
    
    def category=(value) -> ::Google::Cloud::Dataplex::V1::Action::Category

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Action::Category](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-Category)) — The category of issue associated with the action. 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::Category](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-Category)) — The category of issue associated with the action. 



### #data_locations
    
    
    def data_locations() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The list of data locations associated with this action. Cloud Storage locations are represented as URI paths(E.g. `gs://bucket/table1/year=2020/month=Jan/`). BigQuery locations refer to resource names(E.g. `bigquery.googleapis.com/projects/project-id/datasets/dataset-id`). 



### #data_locations=
    
    
    def data_locations=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The list of data locations associated with this action. Cloud Storage locations are represented as URI paths(E.g. `gs://bucket/table1/year=2020/month=Jan/`). BigQuery locations refer to resource names(E.g. `bigquery.googleapis.com/projects/project-id/datasets/dataset-id`). 



**Returns**

  * (::Array<::String>) — The list of data locations associated with this action. Cloud Storage locations are represented as URI paths(E.g. `gs://bucket/table1/year=2020/month=Jan/`). BigQuery locations refer to resource names(E.g. `bigquery.googleapis.com/projects/project-id/datasets/dataset-id`). 



### #detect_time
    
    
    def detect_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Timestamp)) — The time that the issue was detected. 



### #detect_time=
    
    
    def detect_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Timestamp)) — The time that the issue was detected. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Timestamp)) — The time that the issue was detected. 



### #failed_security_policy_apply
    
    
    def failed_security_policy_apply() -> ::Google::Cloud::Dataplex::V1::Action::FailedSecurityPolicyApply

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::FailedSecurityPolicyApply](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-FailedSecurityPolicyApply)) — Details for issues related to applying security policy.

Note: The following fields are mutually exclusive: `failed_security_policy_apply`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #failed_security_policy_apply=
    
    
    def failed_security_policy_apply=(value) -> ::Google::Cloud::Dataplex::V1::Action::FailedSecurityPolicyApply

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Action::FailedSecurityPolicyApply](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-FailedSecurityPolicyApply)) — Details for issues related to applying security policy.

Note: The following fields are mutually exclusive: `failed_security_policy_apply`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::FailedSecurityPolicyApply](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-FailedSecurityPolicyApply)) — Details for issues related to applying security policy.

Note: The following fields are mutually exclusive: `failed_security_policy_apply`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #incompatible_data_schema
    
    
    def incompatible_data_schema() -> ::Google::Cloud::Dataplex::V1::Action::IncompatibleDataSchema

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::IncompatibleDataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-IncompatibleDataSchema)) — Details for issues related to incompatible schemas detected within data.

Note: The following fields are mutually exclusive: `incompatible_data_schema`, `invalid_data_format`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #incompatible_data_schema=
    
    
    def incompatible_data_schema=(value) -> ::Google::Cloud::Dataplex::V1::Action::IncompatibleDataSchema

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Action::IncompatibleDataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-IncompatibleDataSchema)) — Details for issues related to incompatible schemas detected within data.

Note: The following fields are mutually exclusive: `incompatible_data_schema`, `invalid_data_format`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::IncompatibleDataSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-IncompatibleDataSchema)) — Details for issues related to incompatible schemas detected within data.

Note: The following fields are mutually exclusive: `incompatible_data_schema`, `invalid_data_format`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #invalid_data_format
    
    
    def invalid_data_format() -> ::Google::Cloud::Dataplex::V1::Action::InvalidDataFormat

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::InvalidDataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-InvalidDataFormat)) — Details for issues related to invalid or unsupported data formats.

Note: The following fields are mutually exclusive: `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #invalid_data_format=
    
    
    def invalid_data_format=(value) -> ::Google::Cloud::Dataplex::V1::Action::InvalidDataFormat

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Action::InvalidDataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-InvalidDataFormat)) — Details for issues related to invalid or unsupported data formats.

Note: The following fields are mutually exclusive: `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::InvalidDataFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-InvalidDataFormat)) — Details for issues related to invalid or unsupported data formats.

Note: The following fields are mutually exclusive: `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #invalid_data_organization
    
    
    def invalid_data_organization() -> ::Google::Cloud::Dataplex::V1::Action::InvalidDataOrganization

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::InvalidDataOrganization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-InvalidDataOrganization)) — Details for issues related to invalid data arrangement.

Note: The following fields are mutually exclusive: `invalid_data_organization`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #invalid_data_organization=
    
    
    def invalid_data_organization=(value) -> ::Google::Cloud::Dataplex::V1::Action::InvalidDataOrganization

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Action::InvalidDataOrganization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-InvalidDataOrganization)) — Details for issues related to invalid data arrangement.

Note: The following fields are mutually exclusive: `invalid_data_organization`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::InvalidDataOrganization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-InvalidDataOrganization)) — Details for issues related to invalid data arrangement.

Note: The following fields are mutually exclusive: `invalid_data_organization`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #invalid_data_partition
    
    
    def invalid_data_partition() -> ::Google::Cloud::Dataplex::V1::Action::InvalidDataPartition

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::InvalidDataPartition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-InvalidDataPartition)) — Details for issues related to invalid or unsupported data partition structure.

Note: The following fields are mutually exclusive: `invalid_data_partition`, `invalid_data_format`, `incompatible_data_schema`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #invalid_data_partition=
    
    
    def invalid_data_partition=(value) -> ::Google::Cloud::Dataplex::V1::Action::InvalidDataPartition

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Action::InvalidDataPartition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-InvalidDataPartition)) — Details for issues related to invalid or unsupported data partition structure.

Note: The following fields are mutually exclusive: `invalid_data_partition`, `invalid_data_format`, `incompatible_data_schema`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::InvalidDataPartition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-InvalidDataPartition)) — Details for issues related to invalid or unsupported data partition structure.

Note: The following fields are mutually exclusive: `invalid_data_partition`, `invalid_data_format`, `incompatible_data_schema`, `missing_data`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #issue
    
    
    def issue() -> ::String

**Returns**

  * (::String) — Detailed description of the issue requiring action. 



### #issue=
    
    
    def issue=(value) -> ::String

**Parameter**

  * **value** (::String) — Detailed description of the issue requiring action. 



**Returns**

  * (::String) — Detailed description of the issue requiring action. 



### #lake
    
    
    def lake() -> ::String

**Returns**

  * (::String) — Output only. The relative resource name of the lake, of the form: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`. 



### #missing_data
    
    
    def missing_data() -> ::Google::Cloud::Dataplex::V1::Action::MissingData

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::MissingData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-MissingData)) — Details for issues related to absence of data within managed resources.

Note: The following fields are mutually exclusive: `missing_data`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #missing_data=
    
    
    def missing_data=(value) -> ::Google::Cloud::Dataplex::V1::Action::MissingData

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Action::MissingData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-MissingData)) — Details for issues related to absence of data within managed resources.

Note: The following fields are mutually exclusive: `missing_data`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::MissingData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-MissingData)) — Details for issues related to absence of data within managed resources.

Note: The following fields are mutually exclusive: `missing_data`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_resource`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #missing_resource
    
    
    def missing_resource() -> ::Google::Cloud::Dataplex::V1::Action::MissingResource

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::MissingResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-MissingResource)) — Details for issues related to absence of a managed resource.

Note: The following fields are mutually exclusive: `missing_resource`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #missing_resource=
    
    
    def missing_resource=(value) -> ::Google::Cloud::Dataplex::V1::Action::MissingResource

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Action::MissingResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-MissingResource)) — Details for issues related to absence of a managed resource.

Note: The following fields are mutually exclusive: `missing_resource`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::MissingResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-MissingResource)) — Details for issues related to absence of a managed resource.

Note: The following fields are mutually exclusive: `missing_resource`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `unauthorized_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The relative resource name of the action, of the form: `projects/{project}/locations/{location}/lakes/{lake}/actions/{action}` `projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/actions/{action}` `projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/assets/{asset}/actions/{action}`. 



### #unauthorized_resource
    
    
    def unauthorized_resource() -> ::Google::Cloud::Dataplex::V1::Action::UnauthorizedResource

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::UnauthorizedResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-UnauthorizedResource)) — Details for issues related to lack of permissions to access data resources.

Note: The following fields are mutually exclusive: `unauthorized_resource`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #unauthorized_resource=
    
    
    def unauthorized_resource=(value) -> ::Google::Cloud::Dataplex::V1::Action::UnauthorizedResource

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::Action::UnauthorizedResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-UnauthorizedResource)) — Details for issues related to lack of permissions to access data resources.

Note: The following fields are mutually exclusive: `unauthorized_resource`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataplex::V1::Action::UnauthorizedResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Action-UnauthorizedResource)) — Details for issues related to lack of permissions to access data resources.

Note: The following fields are mutually exclusive: `unauthorized_resource`, `invalid_data_format`, `incompatible_data_schema`, `invalid_data_partition`, `missing_data`, `missing_resource`, `failed_security_policy_apply`, `invalid_data_organization`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — Output only. The relative resource name of the zone, of the form: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
