---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.StartMigrationRequestOrBuilder
title: Interface StartMigrationRequestOrBuilder (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:12.749932+00:00
---

# Interface StartMigrationRequestOrBuilder (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.StartMigrationRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StartMigrationRequestOrBuilder (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface StartMigrationRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getName()
    
    
    public abstract String getName()

Required. The resource name of the instance to start migration on. Format: projects/{project}/locations/{location}/instances/{instance}

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The resource name of the instance to start migration on. Format: projects/{project}/locations/{location}/instances/{instance}

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSelfManagedSource()
    
    
    public abstract SelfManagedSource getSelfManagedSource()

Required. Configuration for migrating from a self-managed Valkey/Redis instance

` .google.cloud.memorystore.v1beta.SelfManagedSource self_managed_source = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SelfManagedSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.SelfManagedSource)` | The selfManagedSource.  
  
### getSelfManagedSourceOrBuilder()
    
    
    public abstract SelfManagedSourceOrBuilder getSelfManagedSourceOrBuilder()

Required. Configuration for migrating from a self-managed Valkey/Redis instance

` .google.cloud.memorystore.v1beta.SelfManagedSource self_managed_source = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SelfManagedSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.SelfManagedSourceOrBuilder)` |   
  
### getSourceCase()
    
    
    public abstract StartMigrationRequest.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[StartMigrationRequest.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1beta.StartMigrationRequest.SourceCase)` |   
  
### hasSelfManagedSource()
    
    
    public abstract boolean hasSelfManagedSource()

Required. Configuration for migrating from a self-managed Valkey/Redis instance

` .google.cloud.memorystore.v1beta.SelfManagedSource self_managed_source = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfManagedSource field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
