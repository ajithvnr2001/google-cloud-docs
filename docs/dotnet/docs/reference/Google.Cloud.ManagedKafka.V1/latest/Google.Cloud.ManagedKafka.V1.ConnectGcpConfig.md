---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectGcpConfig
title: Managed Service for Apache Kafka API v1 API - Class ConnectGcpConfig (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:40.205054+00:00
---

# Managed Service for Apache Kafka API v1 API - Class ConnectGcpConfig (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectGcpConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class ConnectGcpConfig (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectGcpConfig)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.ConnectGcpConfig)


    
    
    public sealed class ConnectGcpConfig : IMessage<ConnectGcpConfig>, IEquatable<ConnectGcpConfig>, IDeepCloneable<ConnectGcpConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class ConnectGcpConfig.

Configuration properties for a Kafka Connect cluster deployed to Google Cloud Platform.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConnectGcpConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ConnectGcpConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectGcpConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ConnectGcpConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectGcpConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ConnectGcpConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectGcpConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Constructors 

### ConnectGcpConfig()
    
    
    public ConnectGcpConfig()

### ConnectGcpConfig(ConnectGcpConfig)
    
    
    public ConnectGcpConfig(ConnectGcpConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ConnectGcpConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectGcpConfig)`  
  
  
## Properties 

### AccessConfig
    
    
    public ConnectAccessConfig AccessConfig { get; set; }

Required. Access configuration for the Kafka Connect cluster.

**Property Value**  
---  
**Type** | **Description**  
`[ConnectAccessConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectAccessConfig)` |   
  
### SecretPaths
    
    
    public RepeatedField<string> SecretPaths { get; }

Optional. Secrets to load into workers. Exact SecretVersions from Secret Manager must be provided -- aliases are not supported. Up to 32 secrets may be loaded into one cluster. Format: projects/<project-id>/secrets/<secret-name>/versions/<version-id>

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecretPathsAsSecretVersionNames
    
    
    public ResourceNameList<SecretVersionName> SecretPathsAsSecretVersionNames { get; }

[SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.SecretVersionName)-typed view over the [SecretPaths](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectGcpConfig#Google_Cloud_ManagedKafka_V1_ConnectGcpConfig_SecretPaths) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.SecretVersionName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
