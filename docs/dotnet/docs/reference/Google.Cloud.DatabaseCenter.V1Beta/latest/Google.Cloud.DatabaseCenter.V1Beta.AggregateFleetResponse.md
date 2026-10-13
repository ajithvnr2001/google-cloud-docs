---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse
title: Database Center v1beta API - Class AggregateFleetResponse (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:50.988535+00:00
---

# Database Center v1beta API - Class AggregateFleetResponse (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class AggregateFleetResponse (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class AggregateFleetResponse : IPageResponse<AggregateFleetRow>, IEnumerable<AggregateFleetRow>, IEnumerable, IMessage<AggregateFleetResponse>, IEquatable<AggregateFleetResponse>, IDeepCloneable<AggregateFleetResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class AggregateFleetResponse.

The response message to aggregate a fleet by some group by fields.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AggregateFleetResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### AggregateFleetResponse()
    
    
    public AggregateFleetResponse()

### AggregateFleetResponse(AggregateFleetResponse)
    
    
    public AggregateFleetResponse(AggregateFleetResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AggregateFleetResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceGroupsTotalCount
    
    
    public int ResourceGroupsTotalCount { get; set; }

Count of all resource groups in the fleet. This includes counts from all pages.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ResourceTotalCount
    
    
    public int ResourceTotalCount { get; set; }

Count of all resources in the fleet. This includes counts from all pages.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Rows
    
    
    public RepeatedField<AggregateFleetRow> Rows { get; }

Represents a row grouped by the fields in the input.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow)` |   
  
### Unreachable
    
    
    public RepeatedField<string> Unreachable { get; }

Unordered list. List of unreachable regions from where data could not be retrieved.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<AggregateFleetRow> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[AggregateFleetRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.AggregateFleetRow)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
