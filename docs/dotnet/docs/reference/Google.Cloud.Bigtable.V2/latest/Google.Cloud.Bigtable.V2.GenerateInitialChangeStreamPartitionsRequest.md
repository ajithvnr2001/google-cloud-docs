---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest
title: Google Bigtable v2 API - Class GenerateInitialChangeStreamPartitionsRequest (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:47.278526+00:00
---

# Google Bigtable v2 API - Class GenerateInitialChangeStreamPartitionsRequest (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class GenerateInitialChangeStreamPartitionsRequest (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class GenerateInitialChangeStreamPartitionsRequest : IMessage<GenerateInitialChangeStreamPartitionsRequest>, IEquatable<GenerateInitialChangeStreamPartitionsRequest>, IDeepCloneable<GenerateInitialChangeStreamPartitionsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class GenerateInitialChangeStreamPartitionsRequest.

NOTE: This API is intended to be used by Apache Beam BigtableIO. Request message for Bigtable.GenerateInitialChangeStreamPartitions.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GenerateInitialChangeStreamPartitionsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GenerateInitialChangeStreamPartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GenerateInitialChangeStreamPartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GenerateInitialChangeStreamPartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### GenerateInitialChangeStreamPartitionsRequest()
    
    
    public GenerateInitialChangeStreamPartitionsRequest()

### GenerateInitialChangeStreamPartitionsRequest(GenerateInitialChangeStreamPartitionsRequest)
    
    
    public GenerateInitialChangeStreamPartitionsRequest(GenerateInitialChangeStreamPartitionsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GenerateInitialChangeStreamPartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest)`  
  
  
## Properties 

### AppProfileId
    
    
    public string AppProfileId { get; set; }

This value specifies routing for replication. If not specified, the "default" application profile will be used. Single cluster routing must be configured on the profile.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TableName
    
    
    public string TableName { get; set; }

Required. The unique name of the table from which to get change stream partitions. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`. Change streaming must be enabled on the table.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TableNameAsTableName
    
    
    public TableName TableNameAsTableName { get; set; }

[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)-typed view over the [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest#Google_Cloud_Bigtable_V2_GenerateInitialChangeStreamPartitionsRequest_TableName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
