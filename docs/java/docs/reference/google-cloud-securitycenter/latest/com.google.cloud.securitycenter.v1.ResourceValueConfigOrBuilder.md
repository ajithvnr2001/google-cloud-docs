---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ResourceValueConfigOrBuilder
title: Interface ResourceValueConfigOrBuilder (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:03.709225+00:00
---

# Interface ResourceValueConfigOrBuilder (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ResourceValueConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ResourceValueConfigOrBuilder (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 
    
    
    public interface ResourceValueConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsResourceLabelsSelector(String key)
    
    
    public abstract boolean containsResourceLabelsSelector(String key)

List of resource labels to search for, evaluated with `AND`. For example, `"resource_labels_selector": {"key": "value", "env": "prod"}` will match resources with labels "key": "value" `AND` "env": "prod" <https://cloud.google.com/resource-manager/docs/creating-managing-labels>

`map<string, string> resource_labels_selector = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCloudProvider()
    
    
    public abstract CloudProvider getCloudProvider()

Cloud provider this configuration applies to

`.google.cloud.securitycenter.v1.CloudProvider cloud_provider = 10;`

**Returns**  
---  
**Type** | **Description**  
`[CloudProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.CloudProvider)` | The cloudProvider.  
  
### getCloudProviderValue()
    
    
    public abstract int getCloudProviderValue()

Cloud provider this configuration applies to

`.google.cloud.securitycenter.v1.CloudProvider cloud_provider = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for cloudProvider.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Timestamp this resource value configuration was created.

`.google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Timestamp this resource value configuration was created.

`.google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Description of the resource value configuration.

`string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Description of the resource value configuration.

`string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getName()
    
    
    public abstract String getName()

Name for the resource value configuration

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name for the resource value configuration

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getResourceLabelsSelector() (deprecated)
    
    
    public abstract Map<String,String> getResourceLabelsSelector()

Use [#getResourceLabelsSelectorMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ResourceValueConfigOrBuilder#com_google_cloud_securitycenter_v1_ResourceValueConfigOrBuilder_getResourceLabelsSelectorMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getResourceLabelsSelectorCount()
    
    
    public abstract int getResourceLabelsSelectorCount()

List of resource labels to search for, evaluated with `AND`. For example, `"resource_labels_selector": {"key": "value", "env": "prod"}` will match resources with labels "key": "value" `AND` "env": "prod" <https://cloud.google.com/resource-manager/docs/creating-managing-labels>

`map<string, string> resource_labels_selector = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResourceLabelsSelectorMap()
    
    
    public abstract Map<String,String> getResourceLabelsSelectorMap()

List of resource labels to search for, evaluated with `AND`. For example, `"resource_labels_selector": {"key": "value", "env": "prod"}` will match resources with labels "key": "value" `AND` "env": "prod" <https://cloud.google.com/resource-manager/docs/creating-managing-labels>

`map<string, string> resource_labels_selector = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getResourceLabelsSelectorOrDefault(String key, String defaultValue)
    
    
    public abstract String getResourceLabelsSelectorOrDefault(String key, String defaultValue)

List of resource labels to search for, evaluated with `AND`. For example, `"resource_labels_selector": {"key": "value", "env": "prod"}` will match resources with labels "key": "value" `AND` "env": "prod" <https://cloud.google.com/resource-manager/docs/creating-managing-labels>

`map<string, string> resource_labels_selector = 6;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResourceLabelsSelectorOrThrow(String key)
    
    
    public abstract String getResourceLabelsSelectorOrThrow(String key)

List of resource labels to search for, evaluated with `AND`. For example, `"resource_labels_selector": {"key": "value", "env": "prod"}` will match resources with labels "key": "value" `AND` "env": "prod" <https://cloud.google.com/resource-manager/docs/creating-managing-labels>

`map<string, string> resource_labels_selector = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getResourceType()
    
    
    public abstract String getResourceType()

Apply resource_value only to resources that match resource_type. resource_type will be checked with `AND` of other resources. For example, "storage.googleapis.com/Bucket" with resource_value "HIGH" will apply "HIGH" value only to "storage.googleapis.com/Bucket" resources.

`string resource_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceType.  
  
### getResourceTypeBytes()
    
    
    public abstract ByteString getResourceTypeBytes()

Apply resource_value only to resources that match resource_type. resource_type will be checked with `AND` of other resources. For example, "storage.googleapis.com/Bucket" with resource_value "HIGH" will apply "HIGH" value only to "storage.googleapis.com/Bucket" resources.

`string resource_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceType.  
  
### getResourceValue()
    
    
    public abstract ResourceValue getResourceValue()

Required. Resource value level this expression represents

` .google.cloud.securitycenter.v1.ResourceValue resource_value = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ResourceValue)` | The resourceValue.  
  
### getResourceValueValue()
    
    
    public abstract int getResourceValueValue()

Required. Resource value level this expression represents

` .google.cloud.securitycenter.v1.ResourceValue resource_value = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for resourceValue.  
  
### getScope()
    
    
    public abstract String getScope()

Project or folder to scope this configuration to. For example, "project/456" would apply this configuration only to resources in "project/456" scope will be checked with `AND` of other resources.

`string scope = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The scope.  
  
### getScopeBytes()
    
    
    public abstract ByteString getScopeBytes()

Project or folder to scope this configuration to. For example, "project/456" would apply this configuration only to resources in "project/456" scope will be checked with `AND` of other resources.

`string scope = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for scope.  
  
### getSensitiveDataProtectionMapping()
    
    
    public abstract ResourceValueConfig.SensitiveDataProtectionMapping getSensitiveDataProtectionMapping()

A mapping of the sensitivity on Sensitive Data Protection finding to resource values. This mapping can only be used in combination with a resource_type that is related to BigQuery, e.g. "bigquery.googleapis.com/Dataset".

` .google.cloud.securitycenter.v1.ResourceValueConfig.SensitiveDataProtectionMapping sensitive_data_protection_mapping = 11; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceValueConfig.SensitiveDataProtectionMapping](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ResourceValueConfig.SensitiveDataProtectionMapping)` | The sensitiveDataProtectionMapping.  
  
### getSensitiveDataProtectionMappingOrBuilder()
    
    
    public abstract ResourceValueConfig.SensitiveDataProtectionMappingOrBuilder getSensitiveDataProtectionMappingOrBuilder()

A mapping of the sensitivity on Sensitive Data Protection finding to resource values. This mapping can only be used in combination with a resource_type that is related to BigQuery, e.g. "bigquery.googleapis.com/Dataset".

` .google.cloud.securitycenter.v1.ResourceValueConfig.SensitiveDataProtectionMapping sensitive_data_protection_mapping = 11; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceValueConfig.SensitiveDataProtectionMappingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ResourceValueConfig.SensitiveDataProtectionMappingOrBuilder)` |   
  
### getTagValues(int index)
    
    
    public abstract String getTagValues(int index)

Required. Tag values combined with `AND` to check against. Values in the form "tagValues/123" Example: `[ "tagValues/123", "tagValues/456", "tagValues/789" ]` <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing>

`repeated string tag_values = 3 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tagValues at the given index.  
  
### getTagValuesBytes(int index)
    
    
    public abstract ByteString getTagValuesBytes(int index)

Required. Tag values combined with `AND` to check against. Values in the form "tagValues/123" Example: `[ "tagValues/123", "tagValues/456", "tagValues/789" ]` <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing>

`repeated string tag_values = 3 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the tagValues at the given index.  
  
### getTagValuesCount()
    
    
    public abstract int getTagValuesCount()

Required. Tag values combined with `AND` to check against. Values in the form "tagValues/123" Example: `[ "tagValues/123", "tagValues/456", "tagValues/789" ]` <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing>

`repeated string tag_values = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of tagValues.  
  
### getTagValuesList()
    
    
    public abstract List<String> getTagValuesList()

Required. Tag values combined with `AND` to check against. Values in the form "tagValues/123" Example: `[ "tagValues/123", "tagValues/456", "tagValues/789" ]` <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing>

`repeated string tag_values = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the tagValues.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Timestamp this resource value configuration was last updated.

`.google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Timestamp this resource value configuration was last updated.

`.google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Timestamp this resource value configuration was created.

`.google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasSensitiveDataProtectionMapping()
    
    
    public abstract boolean hasSensitiveDataProtectionMapping()

A mapping of the sensitivity on Sensitive Data Protection finding to resource values. This mapping can only be used in combination with a resource_type that is related to BigQuery, e.g. "bigquery.googleapis.com/Dataset".

` .google.cloud.securitycenter.v1.ResourceValueConfig.SensitiveDataProtectionMapping sensitive_data_protection_mapping = 11; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sensitiveDataProtectionMapping field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Timestamp this resource value configuration was last updated.

`.google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
