---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Asset.SecurityCenterPropertiesOrBuilder
title: Interface Asset.SecurityCenterPropertiesOrBuilder (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:17.285385+00:00
---

# Interface Asset.SecurityCenterPropertiesOrBuilder (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1beta1.Asset.SecurityCenterPropertiesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Asset.SecurityCenterPropertiesOrBuilder (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 
    
    
    public static interface Asset.SecurityCenterPropertiesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getResourceName()
    
    
    public abstract String getResourceName()

Immutable. The full resource name of the Google Cloud resource this asset represents. This field is immutable after create time. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>

`string resource_name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceName.  
  
### getResourceNameBytes()
    
    
    public abstract ByteString getResourceNameBytes()

Immutable. The full resource name of the Google Cloud resource this asset represents. This field is immutable after create time. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>

`string resource_name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceName.  
  
### getResourceOwners(int index)
    
    
    public abstract String getResourceOwners(int index)

Owners of the Google Cloud resource.

`repeated string resource_owners = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceOwners at the given index.  
  
### getResourceOwnersBytes(int index)
    
    
    public abstract ByteString getResourceOwnersBytes(int index)

Owners of the Google Cloud resource.

`repeated string resource_owners = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the resourceOwners at the given index.  
  
### getResourceOwnersCount()
    
    
    public abstract int getResourceOwnersCount()

Owners of the Google Cloud resource.

`repeated string resource_owners = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of resourceOwners.  
  
### getResourceOwnersList()
    
    
    public abstract List<String> getResourceOwnersList()

Owners of the Google Cloud resource.

`repeated string resource_owners = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the resourceOwners.  
  
### getResourceParent()
    
    
    public abstract String getResourceParent()

The full resource name of the immediate parent of the resource. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>

`string resource_parent = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceParent.  
  
### getResourceParentBytes()
    
    
    public abstract ByteString getResourceParentBytes()

The full resource name of the immediate parent of the resource. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>

`string resource_parent = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceParent.  
  
### getResourceProject()
    
    
    public abstract String getResourceProject()

The full resource name of the project the resource belongs to. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>

`string resource_project = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceProject.  
  
### getResourceProjectBytes()
    
    
    public abstract ByteString getResourceProjectBytes()

The full resource name of the project the resource belongs to. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>

`string resource_project = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceProject.  
  
### getResourceType()
    
    
    public abstract String getResourceType()

The type of the Google Cloud resource. Examples include: APPLICATION, PROJECT, and ORGANIZATION. This is a case insensitive field defined by Security Command Center and/or the producer of the resource and is immutable after create time.

`string resource_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceType.  
  
### getResourceTypeBytes()
    
    
    public abstract ByteString getResourceTypeBytes()

The type of the Google Cloud resource. Examples include: APPLICATION, PROJECT, and ORGANIZATION. This is a case insensitive field defined by Security Command Center and/or the producer of the resource and is immutable after create time.

`string resource_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceType.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
