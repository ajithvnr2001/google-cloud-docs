---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-ResourceValueConfig/
title: Cloud Security Command Center V1 API - Class Google::Cloud::SecurityCenter::V1::ResourceValueConfig (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:03.492564+00:00
---

# Cloud Security Command Center V1 API - Class Google::Cloud::SecurityCenter::V1::ResourceValueConfig (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-ResourceValueConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Command Center V1 API - Class Google::Cloud::SecurityCenter::V1::ResourceValueConfig (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.1  1.8.0  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.2  0.33.0  0.32.0  0.31.1  0.30.0  0.29.1  0.28.0  0.27.0  0.26.0  0.25.1  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.1 

Reference documentation and code samples for the Cloud Security Command Center V1 API class Google::Cloud::SecurityCenter::V1::ResourceValueConfig.

A resource value configuration (RVC) is a mapping configuration of user's resources to resource values. Used in Attack path simulations.

## Inherits

  * [Object](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-Kubernetes-Object)



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cloud_provider
    
    
    def cloud_provider() -> ::Google::Cloud::SecurityCenter::V1::CloudProvider

**Returns**

  * ([::Google::Cloud::SecurityCenter::V1::CloudProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-CloudProvider)) — Cloud provider this configuration applies to 



### #cloud_provider=
    
    
    def cloud_provider=(value) -> ::Google::Cloud::SecurityCenter::V1::CloudProvider

**Parameter**

  * **value** ([::Google::Cloud::SecurityCenter::V1::CloudProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-CloudProvider)) — Cloud provider this configuration applies to 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V1::CloudProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-CloudProvider)) — Cloud provider this configuration applies to 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp this resource value configuration was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Description of the resource value configuration. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Description of the resource value configuration. 



**Returns**

  * (::String) — Description of the resource value configuration. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Name for the resource value configuration 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name for the resource value configuration 



**Returns**

  * (::String) — Name for the resource value configuration 



### #resource_labels_selector
    
    
    def resource_labels_selector() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — List of resource labels to search for, evaluated with `AND`. For example, `"resource_labels_selector": {"key": "value", "env": "prod"}` will match resources with labels "key": "value" `AND` "env": "prod" https://cloud.google.com/resource-manager/docs/creating-managing-labels 



### #resource_labels_selector=
    
    
    def resource_labels_selector=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — List of resource labels to search for, evaluated with `AND`. For example, `"resource_labels_selector": {"key": "value", "env": "prod"}` will match resources with labels "key": "value" `AND` "env": "prod" https://cloud.google.com/resource-manager/docs/creating-managing-labels 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — List of resource labels to search for, evaluated with `AND`. For example, `"resource_labels_selector": {"key": "value", "env": "prod"}` will match resources with labels "key": "value" `AND` "env": "prod" https://cloud.google.com/resource-manager/docs/creating-managing-labels 



### #resource_type
    
    
    def resource_type() -> ::String

**Returns**

  * (::String) — Apply resource_value only to resources that match resource_type. resource_type will be checked with `AND` of other resources. For example, "storage.googleapis.com/Bucket" with resource_value "HIGH" will apply "HIGH" value only to "storage.googleapis.com/Bucket" resources. 



### #resource_type=
    
    
    def resource_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Apply resource_value only to resources that match resource_type. resource_type will be checked with `AND` of other resources. For example, "storage.googleapis.com/Bucket" with resource_value "HIGH" will apply "HIGH" value only to "storage.googleapis.com/Bucket" resources. 



**Returns**

  * (::String) — Apply resource_value only to resources that match resource_type. resource_type will be checked with `AND` of other resources. For example, "storage.googleapis.com/Bucket" with resource_value "HIGH" will apply "HIGH" value only to "storage.googleapis.com/Bucket" resources. 



### #resource_value
    
    
    def resource_value() -> ::Google::Cloud::SecurityCenter::V1::ResourceValue

**Returns**

  * ([::Google::Cloud::SecurityCenter::V1::ResourceValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-ResourceValue)) — Required. Resource value level this expression represents 



### #resource_value=
    
    
    def resource_value=(value) -> ::Google::Cloud::SecurityCenter::V1::ResourceValue

**Parameter**

  * **value** ([::Google::Cloud::SecurityCenter::V1::ResourceValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-ResourceValue)) — Required. Resource value level this expression represents 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V1::ResourceValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-ResourceValue)) — Required. Resource value level this expression represents 



### #scope
    
    
    def scope() -> ::String

**Returns**

  * (::String) — Project or folder to scope this configuration to. For example, "project/456" would apply this configuration only to resources in "project/456" scope will be checked with `AND` of other resources. 



### #scope=
    
    
    def scope=(value) -> ::String

**Parameter**

  * **value** (::String) — Project or folder to scope this configuration to. For example, "project/456" would apply this configuration only to resources in "project/456" scope will be checked with `AND` of other resources. 



**Returns**

  * (::String) — Project or folder to scope this configuration to. For example, "project/456" would apply this configuration only to resources in "project/456" scope will be checked with `AND` of other resources. 



### #sensitive_data_protection_mapping
    
    
    def sensitive_data_protection_mapping() -> ::Google::Cloud::SecurityCenter::V1::ResourceValueConfig::SensitiveDataProtectionMapping

**Returns**

  * ([::Google::Cloud::SecurityCenter::V1::ResourceValueConfig::SensitiveDataProtectionMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-ResourceValueConfig-SensitiveDataProtectionMapping)) — A mapping of the sensitivity on Sensitive Data Protection finding to resource values. This mapping can only be used in combination with a resource_type that is related to BigQuery, e.g. "bigquery.googleapis.com/Dataset". 



### #sensitive_data_protection_mapping=
    
    
    def sensitive_data_protection_mapping=(value) -> ::Google::Cloud::SecurityCenter::V1::ResourceValueConfig::SensitiveDataProtectionMapping

**Parameter**

  * **value** ([::Google::Cloud::SecurityCenter::V1::ResourceValueConfig::SensitiveDataProtectionMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-ResourceValueConfig-SensitiveDataProtectionMapping)) — A mapping of the sensitivity on Sensitive Data Protection finding to resource values. This mapping can only be used in combination with a resource_type that is related to BigQuery, e.g. "bigquery.googleapis.com/Dataset". 



**Returns**

  * ([::Google::Cloud::SecurityCenter::V1::ResourceValueConfig::SensitiveDataProtectionMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Cloud-SecurityCenter-V1-ResourceValueConfig-SensitiveDataProtectionMapping)) — A mapping of the sensitivity on Sensitive Data Protection finding to resource values. This mapping can only be used in combination with a resource_type that is related to BigQuery, e.g. "bigquery.googleapis.com/Dataset". 



### #tag_values
    
    
    def tag_values() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Required. Tag values combined with `AND` to check against. Values in the form "tagValues/123" Example: `[ "tagValues/123", "tagValues/456", "tagValues/789" ]` https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing 



### #tag_values=
    
    
    def tag_values=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Required. Tag values combined with `AND` to check against. Values in the form "tagValues/123" Example: `[ "tagValues/123", "tagValues/456", "tagValues/789" ]` https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing 



**Returns**

  * (::Array<::String>) — Required. Tag values combined with `AND` to check against. Values in the form "tagValues/123" Example: `[ "tagValues/123", "tagValues/456", "tagValues/789" ]` https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp this resource value configuration was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
