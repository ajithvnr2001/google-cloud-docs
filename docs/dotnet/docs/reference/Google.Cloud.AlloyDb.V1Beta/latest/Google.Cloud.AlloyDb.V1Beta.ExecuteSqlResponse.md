---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse
title: AlloyDB v1beta API - Class ExecuteSqlResponse (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:47.422156+00:00
---

# AlloyDB v1beta API - Class ExecuteSqlResponse (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class ExecuteSqlResponse (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class ExecuteSqlResponse : IMessage<ExecuteSqlResponse>, IEquatable<ExecuteSqlResponse>, IDeepCloneable<ExecuteSqlResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class ExecuteSqlResponse.

Execute a SQL statement response.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExecuteSqlResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### ExecuteSqlResponse()
    
    
    public ExecuteSqlResponse()

### ExecuteSqlResponse(ExecuteSqlResponse)
    
    
    public ExecuteSqlResponse(ExecuteSqlResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ExecuteSqlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlResponse)`  
  
  
## Properties 

### Metadata
    
    
    public ExecuteSqlMetadata Metadata { get; set; }

Any additional metadata information regarding the execution of the sql statement.

**Property Value**  
---  
**Type** | **Description**  
`[ExecuteSqlMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ExecuteSqlMetadata)` |   
  
### SqlResults
    
    
    public RepeatedField<SqlResult> SqlResults { get; }

SqlResult represents the results for the execution of sql statements.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SqlResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SqlResult)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
