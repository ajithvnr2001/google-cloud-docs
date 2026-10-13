---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest
title: Identity and Access Management (IAM) v1 API - Class ListServiceAccountKeysRequest (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:12.016153+00:00
---

# Identity and Access Management (IAM) v1 API - Class ListServiceAccountKeysRequest (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v1 API - Class ListServiceAccountKeysRequest (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/2.4.0/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/2.3.0/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/2.2.0/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/2.1.0/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/2.0.0/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/1.2.0/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/1.1.0/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/1.0.0/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)


    
    
    public sealed class ListServiceAccountKeysRequest : IMessage<ListServiceAccountKeysRequest>, IEquatable<ListServiceAccountKeysRequest>, IDeepCloneable<ListServiceAccountKeysRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity and Access Management (IAM) v1 API class ListServiceAccountKeysRequest.

The service account keys list request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListServiceAccountKeysRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListServiceAccountKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListServiceAccountKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListServiceAccountKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.Admin.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1)

## Assembly

Google.Cloud.Iam.Admin.V1.dll

## Constructors 

### ListServiceAccountKeysRequest()
    
    
    public ListServiceAccountKeysRequest()

### ListServiceAccountKeysRequest(ListServiceAccountKeysRequest)
    
    
    public ListServiceAccountKeysRequest(ListServiceAccountKeysRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListServiceAccountKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)`  
  
  
## Properties 

### KeyTypes
    
    
    public RepeatedField<ListServiceAccountKeysRequest.Types.KeyType> KeyTypes { get; }

Filters the types of keys the user wants to include in the list response. Duplicate key types are not allowed. If no key type is provided, all keys are returned.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ListServiceAccountKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest.Types)[KeyType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest.Types.KeyType)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name of the service account in the following format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`.

Using `-` as a wildcard for the `PROJECT_ID`, will infer the project from the account. The `ACCOUNT` value can be the `email` address or the `unique_id` of the service account.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAccountName
    
    
    public ServiceAccountName ServiceAccountName { get; set; }

[ServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ServiceAccountName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ListServiceAccountKeysRequest#Google_Cloud_Iam_Admin_V1_ListServiceAccountKeysRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.Admin.V1/latest/Google.Cloud.Iam.Admin.V1.ServiceAccountName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
