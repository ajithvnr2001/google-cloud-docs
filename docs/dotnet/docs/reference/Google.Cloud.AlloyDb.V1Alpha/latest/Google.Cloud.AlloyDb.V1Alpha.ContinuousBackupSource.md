---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.ContinuousBackupSource
title: AlloyDB v1alpha API - Class ContinuousBackupSource (1.0.0-alpha19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:21.960564+00:00
---

# AlloyDB v1alpha API - Class ContinuousBackupSource (1.0.0-alpha19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.ContinuousBackupSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1alpha API - Class ContinuousBackupSource (1.0.0-alpha19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-alpha19 (latest)  1.0.0-alpha18 
    
    
    public sealed class ContinuousBackupSource : IMessage<ContinuousBackupSource>, IEquatable<ContinuousBackupSource>, IDeepCloneable<ContinuousBackupSource>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1alpha API class ContinuousBackupSource.

Message describing a ContinuousBackupSource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ContinuousBackupSource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ContinuousBackupSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.ContinuousBackupSource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ContinuousBackupSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.ContinuousBackupSource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ContinuousBackupSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.ContinuousBackupSource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha)

## Assembly

Google.Cloud.AlloyDb.V1Alpha.dll

## Constructors 

### ContinuousBackupSource()
    
    
    public ContinuousBackupSource()

### ContinuousBackupSource(ContinuousBackupSource)
    
    
    public ContinuousBackupSource(ContinuousBackupSource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ContinuousBackupSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.ContinuousBackupSource)`  
  
  
## Properties 

### Cluster
    
    
    public string Cluster { get; set; }

Required. The source cluster from which to restore. This cluster must have continuous backup enabled for this operation to succeed. For the required format, see the comment on the Cluster.name field.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PointInTime
    
    
    public Timestamp PointInTime { get; set; }

Required. The point in time to restore to.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
