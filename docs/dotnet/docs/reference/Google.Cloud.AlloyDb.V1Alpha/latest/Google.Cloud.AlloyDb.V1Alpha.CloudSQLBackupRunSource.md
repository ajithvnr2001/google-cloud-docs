---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.CloudSQLBackupRunSource
title: AlloyDB v1alpha API - Class CloudSQLBackupRunSource (1.0.0-alpha19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:38.514886+00:00
---

# AlloyDB v1alpha API - Class CloudSQLBackupRunSource (1.0.0-alpha19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.CloudSQLBackupRunSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1alpha API - Class CloudSQLBackupRunSource (1.0.0-alpha19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-alpha19 (latest)  1.0.0-alpha18 
    
    
    public sealed class CloudSQLBackupRunSource : IMessage<CloudSQLBackupRunSource>, IEquatable<CloudSQLBackupRunSource>, IDeepCloneable<CloudSQLBackupRunSource>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1alpha API class CloudSQLBackupRunSource.

The source CloudSQL backup resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudSQLBackupRunSource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CloudSQLBackupRunSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.CloudSQLBackupRunSource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudSQLBackupRunSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.CloudSQLBackupRunSource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CloudSQLBackupRunSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.CloudSQLBackupRunSource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha)

## Assembly

Google.Cloud.AlloyDb.V1Alpha.dll

## Constructors 

### CloudSQLBackupRunSource()
    
    
    public CloudSQLBackupRunSource()

### CloudSQLBackupRunSource(CloudSQLBackupRunSource)
    
    
    public CloudSQLBackupRunSource(CloudSQLBackupRunSource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CloudSQLBackupRunSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Alpha/latest/Google.Cloud.AlloyDb.V1Alpha.CloudSQLBackupRunSource)`  
  
  
## Properties 

### BackupRunId
    
    
    public long BackupRunId { get; set; }

Required. The CloudSQL backup run ID.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### InstanceId
    
    
    public string InstanceId { get; set; }

Required. The CloudSQL instance ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Project
    
    
    public string Project { get; set; }

The project ID of the source CloudSQL instance. This should be the same as the AlloyDB cluster's project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
