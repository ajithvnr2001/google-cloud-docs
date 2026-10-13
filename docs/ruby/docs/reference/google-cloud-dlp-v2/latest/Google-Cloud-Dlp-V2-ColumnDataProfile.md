---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile/
title: Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::ColumnDataProfile (v1.19.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:02.105869+00:00
---

# Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::ColumnDataProfile (v1.19.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::ColumnDataProfile (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.1  1.17.0  1.16.1  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.2  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1 

Reference documentation and code samples for the Cloud Data Loss Prevention (DLP) V2 API class Google::Cloud::Dlp::V2::ColumnDataProfile.

The profile for a scanned column within a table.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #column
    
    
    def column() -> ::String

**Returns**

  * (::String) — The name of the column. 



### #column=
    
    
    def column=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the column. 



**Returns**

  * (::String) — The name of the column. 



### #column_info_type
    
    
    def column_info_type() -> ::Google::Cloud::Dlp::V2::InfoTypeSummary

**Returns**

  * ([::Google::Cloud::Dlp::V2::InfoTypeSummary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-InfoTypeSummary)) — If it's been determined this column can be identified as a single type, this will be set. Otherwise the column either has unidentifiable content or mixed types. 



### #column_info_type=
    
    
    def column_info_type=(value) -> ::Google::Cloud::Dlp::V2::InfoTypeSummary

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::InfoTypeSummary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-InfoTypeSummary)) — If it's been determined this column can be identified as a single type, this will be set. Otherwise the column either has unidentifiable content or mixed types. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::InfoTypeSummary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-InfoTypeSummary)) — If it's been determined this column can be identified as a single type, this will be set. Otherwise the column either has unidentifiable content or mixed types. 



### #column_type
    
    
    def column_type() -> ::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnDataType

**Returns**

  * ([::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnDataType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile-ColumnDataType)) — The data type of a given column. 



### #column_type=
    
    
    def column_type=(value) -> ::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnDataType

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnDataType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile-ColumnDataType)) — The data type of a given column. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnDataType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile-ColumnDataType)) — The data type of a given column. 



### #data_risk_level
    
    
    def data_risk_level() -> ::Google::Cloud::Dlp::V2::DataRiskLevel

**Returns**

  * ([::Google::Cloud::Dlp::V2::DataRiskLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DataRiskLevel)) — The data risk level for this column. 



### #data_risk_level=
    
    
    def data_risk_level=(value) -> ::Google::Cloud::Dlp::V2::DataRiskLevel

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::DataRiskLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DataRiskLevel)) — The data risk level for this column. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::DataRiskLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-DataRiskLevel)) — The data risk level for this column. 



### #dataset_id
    
    
    def dataset_id() -> ::String

**Returns**

  * (::String) — The BigQuery dataset ID, if the resource profiled is a BigQuery table. 



### #dataset_id=
    
    
    def dataset_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The BigQuery dataset ID, if the resource profiled is a BigQuery table. 



**Returns**

  * (::String) — The BigQuery dataset ID, if the resource profiled is a BigQuery table. 



### #dataset_location
    
    
    def dataset_location() -> ::String

**Returns**

  * (::String) — If supported, the location where the dataset's data is stored. See https://docs.cloud.google.com/bigquery/docs/locations for supported BigQuery locations. 



### #dataset_location=
    
    
    def dataset_location=(value) -> ::String

**Parameter**

  * **value** (::String) — If supported, the location where the dataset's data is stored. See https://docs.cloud.google.com/bigquery/docs/locations for supported BigQuery locations. 



**Returns**

  * (::String) — If supported, the location where the dataset's data is stored. See https://docs.cloud.google.com/bigquery/docs/locations for supported BigQuery locations. 



### #dataset_project_id
    
    
    def dataset_project_id() -> ::String

**Returns**

  * (::String) — The Google Cloud project ID that owns the profiled resource. 



### #dataset_project_id=
    
    
    def dataset_project_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The Google Cloud project ID that owns the profiled resource. 



**Returns**

  * (::String) — The Google Cloud project ID that owns the profiled resource. 



### #estimated_null_percentage
    
    
    def estimated_null_percentage() -> ::Google::Cloud::Dlp::V2::NullPercentageLevel

**Returns**

  * ([::Google::Cloud::Dlp::V2::NullPercentageLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-NullPercentageLevel)) — Approximate percentage of entries being null in the column. 



### #estimated_null_percentage=
    
    
    def estimated_null_percentage=(value) -> ::Google::Cloud::Dlp::V2::NullPercentageLevel

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::NullPercentageLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-NullPercentageLevel)) — Approximate percentage of entries being null in the column. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::NullPercentageLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-NullPercentageLevel)) — Approximate percentage of entries being null in the column. 



### #estimated_uniqueness_score
    
    
    def estimated_uniqueness_score() -> ::Google::Cloud::Dlp::V2::UniquenessScoreLevel

**Returns**

  * ([::Google::Cloud::Dlp::V2::UniquenessScoreLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-UniquenessScoreLevel)) — Approximate uniqueness of the column. 



### #estimated_uniqueness_score=
    
    
    def estimated_uniqueness_score=(value) -> ::Google::Cloud::Dlp::V2::UniquenessScoreLevel

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::UniquenessScoreLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-UniquenessScoreLevel)) — Approximate uniqueness of the column. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::UniquenessScoreLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-UniquenessScoreLevel)) — Approximate uniqueness of the column. 



### #free_text_score
    
    
    def free_text_score() -> ::Float

**Returns**

  * (::Float) — The likelihood that this column contains free-form text. A value close to 1 may indicate the column is likely to contain free-form or natural language text. Range in 0-1. 



### #free_text_score=
    
    
    def free_text_score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The likelihood that this column contains free-form text. A value close to 1 may indicate the column is likely to contain free-form or natural language text. Range in 0-1. 



**Returns**

  * (::Float) — The likelihood that this column contains free-form text. A value close to 1 may indicate the column is likely to contain free-form or natural language text. Range in 0-1. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of the profile. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the profile. 



**Returns**

  * (::String) — The name of the profile. 



### #other_matches
    
    
    def other_matches() -> ::Array<::Google::Cloud::Dlp::V2::OtherInfoTypeSummary>

**Returns**

  * (::Array<[::Google::Cloud::Dlp::V2::OtherInfoTypeSummary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-OtherInfoTypeSummary)>) — Other types found within this column. List will be unordered. 



### #other_matches=
    
    
    def other_matches=(value) -> ::Array<::Google::Cloud::Dlp::V2::OtherInfoTypeSummary>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dlp::V2::OtherInfoTypeSummary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-OtherInfoTypeSummary)>) — Other types found within this column. List will be unordered. 



**Returns**

  * (::Array<[::Google::Cloud::Dlp::V2::OtherInfoTypeSummary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-OtherInfoTypeSummary)>) — Other types found within this column. List will be unordered. 



### #policy_state
    
    
    def policy_state() -> ::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnPolicyState

**Returns**

  * ([::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnPolicyState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile-ColumnPolicyState)) — Indicates if a policy tag has been applied to the column. 



### #policy_state=
    
    
    def policy_state=(value) -> ::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnPolicyState

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnPolicyState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile-ColumnPolicyState)) — Indicates if a policy tag has been applied to the column. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::ColumnDataProfile::ColumnPolicyState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile-ColumnPolicyState)) — Indicates if a policy tag has been applied to the column. 



### #profile_last_generated
    
    
    def profile_last_generated() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Protobuf-Timestamp)) — The last time the profile was generated. 



### #profile_last_generated=
    
    
    def profile_last_generated=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Protobuf-Timestamp)) — The last time the profile was generated. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Protobuf-Timestamp)) — The last time the profile was generated. 



### #profile_status
    
    
    def profile_status() -> ::Google::Cloud::Dlp::V2::ProfileStatus

**Returns**

  * ([::Google::Cloud::Dlp::V2::ProfileStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ProfileStatus)) — Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated. 



### #profile_status=
    
    
    def profile_status=(value) -> ::Google::Cloud::Dlp::V2::ProfileStatus

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::ProfileStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ProfileStatus)) — Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::ProfileStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ProfileStatus)) — Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated. 



### #sensitivity_score
    
    
    def sensitivity_score() -> ::Google::Cloud::Dlp::V2::SensitivityScore

**Returns**

  * ([::Google::Cloud::Dlp::V2::SensitivityScore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-SensitivityScore)) — The sensitivity of this column. 



### #sensitivity_score=
    
    
    def sensitivity_score=(value) -> ::Google::Cloud::Dlp::V2::SensitivityScore

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::SensitivityScore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-SensitivityScore)) — The sensitivity of this column. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::SensitivityScore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-SensitivityScore)) — The sensitivity of this column. 



### #state
    
    
    def state() -> ::Google::Cloud::Dlp::V2::ColumnDataProfile::State

**Returns**

  * ([::Google::Cloud::Dlp::V2::ColumnDataProfile::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile-State)) — State of a profile. 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::Dlp::V2::ColumnDataProfile::State

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::ColumnDataProfile::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile-State)) — State of a profile. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::ColumnDataProfile::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-ColumnDataProfile-State)) — State of a profile. 



### #table_data_profile
    
    
    def table_data_profile() -> ::String

**Returns**

  * (::String) — The resource name of the table data profile. 



### #table_data_profile=
    
    
    def table_data_profile=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource name of the table data profile. 



**Returns**

  * (::String) — The resource name of the table data profile. 



### #table_full_resource
    
    
    def table_full_resource() -> ::String

**Returns**

  * (::String) — The resource name of the resource this column is within. 



### #table_full_resource=
    
    
    def table_full_resource=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource name of the resource this column is within. 



**Returns**

  * (::String) — The resource name of the resource this column is within. 



### #table_id
    
    
    def table_id() -> ::String

**Returns**

  * (::String) — The table ID. 



### #table_id=
    
    
    def table_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The table ID. 



**Returns**

  * (::String) — The table ID. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
