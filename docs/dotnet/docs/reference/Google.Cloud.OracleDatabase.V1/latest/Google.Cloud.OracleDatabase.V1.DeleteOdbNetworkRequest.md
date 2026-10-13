---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest
title: Oracle Database@Google Cloud v1 API - Class DeleteOdbNetworkRequest (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:06.170626+00:00
---

# Oracle Database@Google Cloud v1 API - Class DeleteOdbNetworkRequest (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class DeleteOdbNetworkRequest (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class DeleteOdbNetworkRequest : IMessage<DeleteOdbNetworkRequest>, IEquatable<DeleteOdbNetworkRequest>, IDeepCloneable<DeleteOdbNetworkRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class DeleteOdbNetworkRequest.

The request for `OdbNetwork.Delete`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteOdbNetworkRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### DeleteOdbNetworkRequest()
    
    
    public DeleteOdbNetworkRequest()

### DeleteOdbNetworkRequest(DeleteOdbNetworkRequest)
    
    
    public DeleteOdbNetworkRequest(DeleteOdbNetworkRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteOdbNetworkRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The name of the resource in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OdbNetworkName
    
    
    public OdbNetworkName OdbNetworkName { get; set; }

[OdbNetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbNetworkName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.DeleteOdbNetworkRequest#Google_Cloud_OracleDatabase_V1_DeleteOdbNetworkRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OdbNetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.OdbNetworkName)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional ID to identify the request. This value is used to identify duplicate requests. If you make a request with the same request ID and the original request is still in progress or completed, the server ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
