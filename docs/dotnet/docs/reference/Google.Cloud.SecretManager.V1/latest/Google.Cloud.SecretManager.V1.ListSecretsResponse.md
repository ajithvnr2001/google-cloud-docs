---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.ListSecretsResponse
title: Secret Manager v1 API - Class ListSecretsResponse (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:49.155536+00:00
---

# Secret Manager v1 API - Class ListSecretsResponse (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.ListSecretsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Secret Manager v1 API - Class ListSecretsResponse (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0 
    
    
    public sealed class ListSecretsResponse : IPageResponse<Secret>, IEnumerable<Secret>, IEnumerable, IMessage<ListSecretsResponse>, IEquatable<ListSecretsResponse>, IDeepCloneable<ListSecretsResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Secret Manager v1 API class ListSecretsResponse.

Response message for [SecretManagerService.ListSecrets][google.cloud.secretmanager.v1.SecretManagerService.ListSecrets].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListSecretsResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[Secret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Secret), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Secret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Secret), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.ListSecretsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.ListSecretsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.ListSecretsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1)

## Assembly

Google.Cloud.SecretManager.V1.dll

## Constructors 

### ListSecretsResponse()
    
    
    public ListSecretsResponse()

### ListSecretsResponse(ListSecretsResponse)
    
    
    public ListSecretsResponse(ListSecretsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListSecretsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.ListSecretsResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token to retrieve the next page of results. Pass this value in [ListSecretsRequest.page_token][google.cloud.secretmanager.v1.ListSecretsRequest.page_token] to retrieve the next page.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Secrets
    
    
    public RepeatedField<Secret> Secrets { get; }

The list of [Secrets][google.cloud.secretmanager.v1.Secret] sorted in reverse by create_time (newest first).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Secret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Secret)` |   
  
### TotalSize
    
    
    public int TotalSize { get; set; }

The total number of [Secrets][google.cloud.secretmanager.v1.Secret] but 0 when the [ListSecretsRequest.filter][google.cloud.secretmanager.v1.ListSecretsRequest.filter] field is set.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<Secret> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[Secret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Secret)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
