---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types.DataplexConfig
title: AlloyDB v1alpha API - Class Cluster.Types.DataplexConfig (1.0.0-alpha19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:41.578795+00:00
---

# AlloyDB v1alpha API - Class Cluster.Types.DataplexConfig (1.0.0-alpha19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types.DataplexConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1alpha API - Class Cluster.Types.DataplexConfig (1.0.0-alpha19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-alpha19 (latest)  1.0.0-alpha18 
    
    
    public sealed class Cluster.Types.DataplexConfig : IMessage<Cluster.Types.DataplexConfig>, IEquatable<Cluster.Types.DataplexConfig>, IDeepCloneable<Cluster.Types.DataplexConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1alpha API class Cluster.Types.DataplexConfig.

Configuration for Dataplex integration.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Cluster.Types.DataplexConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types)[DataplexConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types.DataplexConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types)[DataplexConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types.DataplexConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types)[DataplexConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types.DataplexConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha)

## Assembly

Google.Cloud.AlloyDb.V1Alpha.dll

## Constructors 

### DataplexConfig()
    
    
    public DataplexConfig()

### DataplexConfig(DataplexConfig)
    
    
    public DataplexConfig(Cluster.Types.DataplexConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types)[DataplexConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.Cluster.Types.DataplexConfig)`  
  
  
## Properties 

### Enabled
    
    
    public bool Enabled { get; set; }

Dataplex is enabled by default for resources such as clusters and instances. This flag controls the integration of AlloyDB PG resources (like databases, schemas, and tables) with Dataplex."

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
