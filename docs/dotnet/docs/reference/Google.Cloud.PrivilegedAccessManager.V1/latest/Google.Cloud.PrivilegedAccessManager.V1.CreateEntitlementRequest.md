---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest
title: Privileged Access Manager v1 API - Class CreateEntitlementRequest (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:43.104233+00:00
---

# Privileged Access Manager v1 API - Class CreateEntitlementRequest (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Privileged Access Manager v1 API - Class CreateEntitlementRequest (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/1.1.0/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/1.0.0/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest)


    
    
    public sealed class CreateEntitlementRequest : IMessage<CreateEntitlementRequest>, IEquatable<CreateEntitlementRequest>, IDeepCloneable<CreateEntitlementRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Privileged Access Manager v1 API class CreateEntitlementRequest.

Message for creating an entitlement.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateEntitlementRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateEntitlementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateEntitlementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateEntitlementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PrivilegedAccessManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1)

## Assembly

Google.Cloud.PrivilegedAccessManager.V1.dll

## Constructors 

### CreateEntitlementRequest()
    
    
    public CreateEntitlementRequest()

### CreateEntitlementRequest(CreateEntitlementRequest)
    
    
    public CreateEntitlementRequest(CreateEntitlementRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateEntitlementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest)`  
  
  
## Properties 

### Entitlement
    
    
    public Entitlement Entitlement { get; set; }

Required. The resource being created

**Property Value**  
---  
**Type** | **Description**  
`[Entitlement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.Entitlement)` |   
  
### EntitlementId
    
    
    public string EntitlementId { get; set; }

Required. The ID to use for this entitlement. This becomes the last part of the resource name.

This value should be 4-63 characters in length, and valid characters are "[a-z]", "[0-9]", and "-". The first character should be from [a-z].

This value should be unique among all other entitlements under the specified `parent`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Name of the parent resource for the entitlement. Possible formats:

  * `organizations/{organization-number}/locations/{region}`
  * `folders/{folder-number}/locations/{region}`
  * `projects/{project-id|project-number}/locations/{region}`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsFolderLocationName
    
    
    public FolderLocationName ParentAsFolderLocationName { get; set; }

[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.FolderLocationName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest#Google_Cloud_PrivilegedAccessManager_V1_CreateEntitlementRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.FolderLocationName)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest#Google_Cloud_PrivilegedAccessManager_V1_CreateEntitlementRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### ParentAsOrganizationLocationName
    
    
    public OrganizationLocationName ParentAsOrganizationLocationName { get; set; }

[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.OrganizationLocationName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest#Google_Cloud_PrivilegedAccessManager_V1_CreateEntitlementRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.OrganizationLocationName)` |   
  
### ParentAsResourceName
    
    
    public IResourceName ParentAsResourceName { get; set; }

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivilegedAccessManager.V1/latest/Google.Cloud.PrivilegedAccessManager.V1.CreateEntitlementRequest#Google_Cloud_PrivilegedAccessManager_V1_CreateEntitlementRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees this for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, ignores the second request and returns the previous operation's response. This prevents clients from accidentally creating duplicate entitlements.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
