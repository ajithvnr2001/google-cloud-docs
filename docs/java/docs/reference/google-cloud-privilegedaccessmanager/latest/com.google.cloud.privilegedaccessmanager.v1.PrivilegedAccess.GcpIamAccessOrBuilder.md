---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-privilegedaccessmanager/latest/com.google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccessOrBuilder
title: Interface PrivilegedAccess.GcpIamAccessOrBuilder (0.53.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:48.094301+00:00
---

# Interface PrivilegedAccess.GcpIamAccessOrBuilder (0.53.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-privilegedaccessmanager/latest/com.google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccessOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PrivilegedAccess.GcpIamAccessOrBuilder (0.53.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.53.0 (latest)  0.49.0  0.48.0  0.47.0  0.45.0  0.42.0  0.41.0  0.39.0  0.37.0  0.36.0  0.34.0  0.32.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.24.0  0.22.0  0.21.0  0.18.0  0.17.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface PrivilegedAccess.GcpIamAccessOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getResource()
    
    
    public abstract String getResource()

Required. Name of the resource.

`string resource = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resource.  
  
### getResourceBytes()
    
    
    public abstract ByteString getResourceBytes()

Required. Name of the resource.

`string resource = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resource.  
  
### getResourceType()
    
    
    public abstract String getResourceType()

Required. The type of this resource.

`string resource_type = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceType.  
  
### getResourceTypeBytes()
    
    
    public abstract ByteString getResourceTypeBytes()

Required. The type of this resource.

`string resource_type = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceType.  
  
### getRoleBindings(int index)
    
    
    public abstract PrivilegedAccess.GcpIamAccess.RoleBinding getRoleBindings(int index)

Required. Role bindings that are created on successful grant.

` repeated .google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccess.RoleBinding role_bindings = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PrivilegedAccess.GcpIamAccess.RoleBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-privilegedaccessmanager/latest/com.google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccess.RoleBinding)` |   
  
### getRoleBindingsCount()
    
    
    public abstract int getRoleBindingsCount()

Required. Role bindings that are created on successful grant.

` repeated .google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccess.RoleBinding role_bindings = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRoleBindingsList()
    
    
    public abstract List<PrivilegedAccess.GcpIamAccess.RoleBinding> getRoleBindingsList()

Required. Role bindings that are created on successful grant.

` repeated .google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccess.RoleBinding role_bindings = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RoleBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-privilegedaccessmanager/latest/com.google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccess.RoleBinding)>` |   
  
### getRoleBindingsOrBuilder(int index)
    
    
    public abstract PrivilegedAccess.GcpIamAccess.RoleBindingOrBuilder getRoleBindingsOrBuilder(int index)

Required. Role bindings that are created on successful grant.

` repeated .google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccess.RoleBinding role_bindings = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PrivilegedAccess.GcpIamAccess.RoleBindingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-privilegedaccessmanager/latest/com.google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccess.RoleBindingOrBuilder)` |   
  
### getRoleBindingsOrBuilderList()
    
    
    public abstract List<? extends PrivilegedAccess.GcpIamAccess.RoleBindingOrBuilder> getRoleBindingsOrBuilderList()

Required. Role bindings that are created on successful grant.

` repeated .google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccess.RoleBinding role_bindings = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.privilegedaccessmanager.v1.PrivilegedAccess.GcpIamAccess.RoleBindingOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
