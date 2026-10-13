---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceRequest
title: Google Cloud Spanner Instance Administration v1 API - Class GetInstanceRequest (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:32.759879+00:00
---

# Google Cloud Spanner Instance Administration v1 API - Class GetInstanceRequest (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner Instance Administration v1 API - Class GetInstanceRequest (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class GetInstanceRequest : IMessage<GetInstanceRequest>, IEquatable<GetInstanceRequest>, IDeepCloneable<GetInstanceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner Instance Administration v1 API class GetInstanceRequest.

The request for [GetInstance][google.spanner.admin.instance.v1.InstanceAdmin.GetInstance].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetInstanceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.Admin.Instance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1)

## Assembly

Google.Cloud.Spanner.Admin.Instance.V1.dll

## Constructors 

### GetInstanceRequest()
    
    
    public GetInstanceRequest()

### GetInstanceRequest(GetInstanceRequest)
    
    
    public GetInstanceRequest(GetInstanceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceRequest)`  
  
  
## Properties 

### FieldMask
    
    
    public FieldMask FieldMask { get; set; }

If field_mask is present, specifies the subset of [Instance][google.spanner.admin.instance.v1.Instance] fields that should be returned. If absent, all [Instance][google.spanner.admin.instance.v1.Instance] fields are returned.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### InstanceName
    
    
    public InstanceName InstanceName { get; set; }

Google.Cloud.Spanner.Common.V1.InstanceName-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.GetInstanceRequest#Google_Cloud_Spanner_Admin_Instance_V1_GetInstanceRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`Google.Cloud.Spanner.Common.V1.InstanceName` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the requested instance. Values are of the form `projects/<project>/instances/<instance>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
