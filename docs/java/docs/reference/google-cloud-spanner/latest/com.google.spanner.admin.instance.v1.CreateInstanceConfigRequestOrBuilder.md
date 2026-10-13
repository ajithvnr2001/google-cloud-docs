---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceConfigRequestOrBuilder
title: Interface CreateInstanceConfigRequestOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:27.050554+00:00
---

# Interface CreateInstanceConfigRequestOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceConfigRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateInstanceConfigRequestOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface CreateInstanceConfigRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getInstanceConfig()
    
    
    public abstract InstanceConfig getInstanceConfig()

Required. The `InstanceConfig` proto of the configuration to create. `instance_config.name` must be `<parent>/instanceConfigs/<instance_config_id>`. `instance_config.base_config` must be a Google-managed configuration name, e.g. <parent>/instanceConfigs/us-east1, <parent>/instanceConfigs/nam3.

` .google.spanner.admin.instance.v1.InstanceConfig instance_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[InstanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfig)` | The instanceConfig.  
  
### getInstanceConfigId()
    
    
    public abstract String getInstanceConfigId()

Required. The ID of the instance configuration to create. Valid identifiers are of the form `custom-[-a-z0-9]*[a-z0-9]` and must be between 2 and 64 characters in length. The `custom-` prefix is required to avoid name conflicts with Google-managed configurations.

`string instance_config_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instanceConfigId.  
  
### getInstanceConfigIdBytes()
    
    
    public abstract ByteString getInstanceConfigIdBytes()

Required. The ID of the instance configuration to create. Valid identifiers are of the form `custom-[-a-z0-9]*[a-z0-9]` and must be between 2 and 64 characters in length. The `custom-` prefix is required to avoid name conflicts with Google-managed configurations.

`string instance_config_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instanceConfigId.  
  
### getInstanceConfigOrBuilder()
    
    
    public abstract InstanceConfigOrBuilder getInstanceConfigOrBuilder()

Required. The `InstanceConfig` proto of the configuration to create. `instance_config.name` must be `<parent>/instanceConfigs/<instance_config_id>`. `instance_config.base_config` must be a Google-managed configuration name, e.g. <parent>/instanceConfigs/us-east1, <parent>/instanceConfigs/nam3.

` .google.spanner.admin.instance.v1.InstanceConfig instance_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[InstanceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The name of the project in which to create the instance configuration. Values are of the form `projects/<project>`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The name of the project in which to create the instance configuration. Values are of the form `projects/<project>`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getValidateOnly()
    
    
    public abstract boolean getValidateOnly()

An option to validate, but not actually execute, a request, and provide the same response.

`bool validate_only = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The validateOnly.  
  
### hasInstanceConfig()
    
    
    public abstract boolean hasInstanceConfig()

Required. The `InstanceConfig` proto of the configuration to create. `instance_config.name` must be `<parent>/instanceConfigs/<instance_config_id>`. `instance_config.base_config` must be a Google-managed configuration name, e.g. <parent>/instanceConfigs/us-east1, <parent>/instanceConfigs/nam3.

` .google.spanner.admin.instance.v1.InstanceConfig instance_config = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the instanceConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
