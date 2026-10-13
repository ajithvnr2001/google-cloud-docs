---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest
title: Cloud Memorystore for Memcached v1 API - Class CreateInstanceRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:13.080221+00:00
---

# Cloud Memorystore for Memcached v1 API - Class CreateInstanceRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Memorystore for Memcached v1 API - Class CreateInstanceRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.5.0/Google.Cloud.Memcache.V1.CreateInstanceRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.4.0/Google.Cloud.Memcache.V1.CreateInstanceRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.3.0/Google.Cloud.Memcache.V1.CreateInstanceRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.2.0/Google.Cloud.Memcache.V1.CreateInstanceRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.1.0/Google.Cloud.Memcache.V1.CreateInstanceRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/2.0.0/Google.Cloud.Memcache.V1.CreateInstanceRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/1.2.0/Google.Cloud.Memcache.V1.CreateInstanceRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/1.1.0/Google.Cloud.Memcache.V1.CreateInstanceRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/1.0.0/Google.Cloud.Memcache.V1.CreateInstanceRequest)


    
    
    public sealed class CreateInstanceRequest : IMessage<CreateInstanceRequest>, IEquatable<CreateInstanceRequest>, IDeepCloneable<CreateInstanceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Memorystore for Memcached v1 API class CreateInstanceRequest.

Request for [CreateInstance][google.cloud.memcache.v1.CloudMemcache.CreateInstance].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateInstanceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memcache.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1)

## Assembly

Google.Cloud.Memcache.V1.dll

## Constructors 

### CreateInstanceRequest()
    
    
    public CreateInstanceRequest()

### CreateInstanceRequest(CreateInstanceRequest)
    
    
    public CreateInstanceRequest(CreateInstanceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest)`  
  
  
## Properties 

### Instance
    
    
    public Instance Instance { get; set; }

Required. A Memcached Instance

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.Instance)` |   
  
### InstanceId
    
    
    public string InstanceId { get; set; }

Required. The logical name of the Memcached instance in the user project with the following restrictions:

  * Must contain only lowercase letters, numbers, and hyphens.
  * Must start with a letter.
  * Must be between 1-40 characters.
  * Must end with a number or a letter.
  * Must be unique within the user project / location.



If any of the above are not met, the API raises an invalid argument error.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1/latest/Google.Cloud.Memcache.V1.CreateInstanceRequest#Google_Cloud_Memcache_V1_CreateInstanceRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
