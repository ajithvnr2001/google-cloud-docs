---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse
title: Oracle Database@Google Cloud v1 API - Class ListGoldengateDeploymentEnvironmentsResponse (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:15.104689+00:00
---

# Oracle Database@Google Cloud v1 API - Class ListGoldengateDeploymentEnvironmentsResponse (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class ListGoldengateDeploymentEnvironmentsResponse (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ListGoldengateDeploymentEnvironmentsResponse : IMessage<ListGoldengateDeploymentEnvironmentsResponse>, IEquatable<ListGoldengateDeploymentEnvironmentsResponse>, IDeepCloneable<ListGoldengateDeploymentEnvironmentsResponse>, IBufferMessage, IMessage, IPageResponse<GoldengateDeploymentEnvironment>, IEnumerable<GoldengateDeploymentEnvironment>, IEnumerable

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class ListGoldengateDeploymentEnvironmentsResponse.

Message for response to listing GoldengateDeploymentEnvironments

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListGoldengateDeploymentEnvironmentsResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[GoldengateDeploymentEnvironment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeploymentEnvironment), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[GoldengateDeploymentEnvironment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeploymentEnvironment), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### ListGoldengateDeploymentEnvironmentsResponse()
    
    
    public ListGoldengateDeploymentEnvironmentsResponse()

### ListGoldengateDeploymentEnvironmentsResponse(ListGoldengateDeploymentEnvironmentsResponse)
    
    
    public ListGoldengateDeploymentEnvironmentsResponse(ListGoldengateDeploymentEnvironmentsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.ListGoldengateDeploymentEnvironmentsResponse)`  
  
  
## Properties 

### GoldengateDeploymentEnvironments
    
    
    public RepeatedField<GoldengateDeploymentEnvironment> GoldengateDeploymentEnvironments { get; }

The list of GoldengateDeploymentEnvironment

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[GoldengateDeploymentEnvironment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeploymentEnvironment)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token identifying a page of results the server should return. If this field is empty, there are no subsequent pages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Unreachable
    
    
    public RepeatedField<string> Unreachable { get; }

Unordered list. Locations that could not be reached.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<GoldengateDeploymentEnvironment> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[GoldengateDeploymentEnvironment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.GoldengateDeploymentEnvironment)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
