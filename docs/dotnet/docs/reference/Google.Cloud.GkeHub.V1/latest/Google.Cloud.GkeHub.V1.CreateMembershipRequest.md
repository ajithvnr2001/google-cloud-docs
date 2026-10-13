---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.CreateMembershipRequest
title: GKE Hub v1 API - Class CreateMembershipRequest (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:36.846563+00:00
---

# GKE Hub v1 API - Class CreateMembershipRequest (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.CreateMembershipRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GKE Hub v1 API - Class CreateMembershipRequest (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.7.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.6.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.5.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.4.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.3.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.2.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.1.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.0.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.2.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.1.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.0.0/Google.Cloud.GkeHub.V1.CreateMembershipRequest)


    
    
    public sealed class CreateMembershipRequest : IMessage<CreateMembershipRequest>, IEquatable<CreateMembershipRequest>, IDeepCloneable<CreateMembershipRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the GKE Hub v1 API class CreateMembershipRequest.

Request message for the `GkeHub.CreateMembership` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateMembershipRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateMembershipRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.CreateMembershipRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateMembershipRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.CreateMembershipRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateMembershipRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.CreateMembershipRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1)

## Assembly

Google.Cloud.GkeHub.V1.dll

## Constructors 

### CreateMembershipRequest()
    
    
    public CreateMembershipRequest()

### CreateMembershipRequest(CreateMembershipRequest)
    
    
    public CreateMembershipRequest(CreateMembershipRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateMembershipRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.CreateMembershipRequest)`  
  
  
## Properties 

### MembershipId
    
    
    public string MembershipId { get; set; }

Required. Client chosen ID for the membership. `membership_id` must be a valid RFC 1123 compliant DNS label:

  1. At most 63 characters in length
  2. It must consist of lower case alphanumeric characters or `-`
  3. It must start and end with an alphanumeric character



Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`, with a maximum length of 63 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent (project and location) where the Memberships will be created. Specified in the format `projects/*/locations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.CreateMembershipRequest#Google_Cloud_GkeHub_V1_CreateMembershipRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Resource
    
    
    public Membership Resource { get; set; }

Required. The membership to create.

**Property Value**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.Membership)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
