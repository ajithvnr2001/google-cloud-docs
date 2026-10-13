---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlInstancesPatchRequestOrBuilder
title: Interface SqlInstancesPatchRequestOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:53.168121+00:00
---

# Interface SqlInstancesPatchRequestOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlInstancesPatchRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SqlInstancesPatchRequestOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface SqlInstancesPatchRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBody()
    
    
    public abstract DatabaseInstance getBody()

`.google.cloud.sql.v1beta4.DatabaseInstance body = 100;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.DatabaseInstance)` | The body.  
  
### getBodyOrBuilder()
    
    
    public abstract DatabaseInstanceOrBuilder getBodyOrBuilder()

`.google.cloud.sql.v1beta4.DatabaseInstance body = 100;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseInstanceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.DatabaseInstanceOrBuilder)` |   
  
### getInstance()
    
    
    public abstract String getInstance()

Cloud SQL instance ID. This does not include the project ID.

`string instance = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instance.  
  
### getInstanceBytes()
    
    
    public abstract ByteString getInstanceBytes()

Cloud SQL instance ID. This does not include the project ID.

`string instance = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instance.  
  
### getProject()
    
    
    public abstract String getProject()

Project ID of the project that contains the instance.

`string project = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The project.  
  
### getProjectBytes()
    
    
    public abstract ByteString getProjectBytes()

Project ID of the project that contains the instance.

`string project = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for project.  
  
### getReconcilePscNetworking()
    
    
    public abstract boolean getReconcilePscNetworking()

Optional. Set PSC config to the same value as the existing config to reconcile the PSC networking.

`optional bool reconcile_psc_networking = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reconcilePscNetworking.  
  
### getReconcilePscNetworkingForce()
    
    
    public abstract boolean getReconcilePscNetworkingForce()

Optional. Set PSC config to the same value as the existing config and force reconcile the PSC networking.

` optional bool reconcile_psc_networking_force = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reconcilePscNetworkingForce.  
  
### hasBody()
    
    
    public abstract boolean hasBody()

`.google.cloud.sql.v1beta4.DatabaseInstance body = 100;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the body field is set.  
  
### hasReconcilePscNetworking()
    
    
    public abstract boolean hasReconcilePscNetworking()

Optional. Set PSC config to the same value as the existing config to reconcile the PSC networking.

`optional bool reconcile_psc_networking = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reconcilePscNetworking field is set.  
  
### hasReconcilePscNetworkingForce()
    
    
    public abstract boolean hasReconcilePscNetworkingForce()

Optional. Set PSC config to the same value as the existing config and force reconcile the PSC networking.

` optional bool reconcile_psc_networking_force = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reconcilePscNetworkingForce field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
