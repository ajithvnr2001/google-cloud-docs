---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest
title: Discovery Engine v1 API - Class BatchUpdateUserLicensesRequest (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:57.012889+00:00
---

# Discovery Engine v1 API - Class BatchUpdateUserLicensesRequest (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class BatchUpdateUserLicensesRequest (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    public sealed class BatchUpdateUserLicensesRequest : IMessage<BatchUpdateUserLicensesRequest>, IEquatable<BatchUpdateUserLicensesRequest>, IDeepCloneable<BatchUpdateUserLicensesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1 API class BatchUpdateUserLicensesRequest.

Request message for [UserLicenseService.BatchUpdateUserLicenses][google.cloud.discoveryengine.v1.UserLicenseService.BatchUpdateUserLicenses] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchUpdateUserLicensesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Constructors 

### BatchUpdateUserLicensesRequest()
    
    
    public BatchUpdateUserLicensesRequest()

### BatchUpdateUserLicensesRequest(BatchUpdateUserLicensesRequest)
    
    
    public BatchUpdateUserLicensesRequest(BatchUpdateUserLicensesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest)`  
  
  
## Properties 

### DeleteUnassignedUserLicenses
    
    
    public bool DeleteUnassignedUserLicenses { get; set; }

Optional. If true, if user licenses removed associated license config, the user license will be deleted. By default which is false, the user license will be updated to unassigned state.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InlineSource
    
    
    public BatchUpdateUserLicensesRequest.Types.InlineSource InlineSource { get; set; }

The inline source for the input content for document embeddings.

**Property Value**  
---  
**Type** | **Description**  
`[BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest.Types)[InlineSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest.Types.InlineSource)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent [UserStore][] resource name, format: `projects/{project}/locations/{location}/userStores/{user_store_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsUserStoreName
    
    
    public UserStoreName ParentAsUserStoreName { get; set; }

[UserStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UserStoreName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest#Google_Cloud_DiscoveryEngine_V1_BatchUpdateUserLicensesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[UserStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UserStoreName)` |   
  
### SourceCase
    
    
    public BatchUpdateUserLicensesRequest.SourceOneofCase SourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest)[SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BatchUpdateUserLicensesRequest.SourceOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
