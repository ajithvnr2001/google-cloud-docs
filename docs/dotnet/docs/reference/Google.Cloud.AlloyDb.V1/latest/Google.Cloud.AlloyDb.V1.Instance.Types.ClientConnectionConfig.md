---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types.ClientConnectionConfig
title: AlloyDB v1 API - Class Instance.Types.ClientConnectionConfig (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:18.287939+00:00
---

# AlloyDB v1 API - Class Instance.Types.ClientConnectionConfig (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types.ClientConnectionConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1 API - Class Instance.Types.ClientConnectionConfig (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class Instance.Types.ClientConnectionConfig : IMessage<Instance.Types.ClientConnectionConfig>, IEquatable<Instance.Types.ClientConnectionConfig>, IDeepCloneable<Instance.Types.ClientConnectionConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1 API class Instance.Types.ClientConnectionConfig.

Client connection configuration

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Instance.Types.ClientConnectionConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types)[ClientConnectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types.ClientConnectionConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types)[ClientConnectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types.ClientConnectionConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types)[ClientConnectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types.ClientConnectionConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1)

## Assembly

Google.Cloud.AlloyDb.V1.dll

## Constructors 

### ClientConnectionConfig()
    
    
    public ClientConnectionConfig()

### ClientConnectionConfig(ClientConnectionConfig)
    
    
    public ClientConnectionConfig(Instance.Types.ClientConnectionConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types)[ClientConnectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.Types.ClientConnectionConfig)`  
  
  
## Properties 

### RequireConnectors
    
    
    public bool RequireConnectors { get; set; }

Optional. Configuration to enforce connectors only (ex: AuthProxy) connections to the database.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SslConfig
    
    
    public SslConfig SslConfig { get; set; }

Optional. SSL configuration option for this instance.

**Property Value**  
---  
**Type** | **Description**  
`[SslConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SslConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
