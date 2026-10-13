---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.DeleteContactRequest
title: Essential Contacts v1 API - Class DeleteContactRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:27.966870+00:00
---

# Essential Contacts v1 API - Class DeleteContactRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.DeleteContactRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Essential Contacts v1 API - Class DeleteContactRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/2.5.0/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/2.4.0/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/2.3.0/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/2.2.0/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/2.1.0/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/2.0.0/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/1.1.0/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/1.0.0/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)


    
    
    public sealed class DeleteContactRequest : IMessage<DeleteContactRequest>, IEquatable<DeleteContactRequest>, IDeepCloneable<DeleteContactRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Essential Contacts v1 API class DeleteContactRequest.

Request message for the DeleteContact method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteContactRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteContactRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.DeleteContactRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteContactRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.DeleteContactRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteContactRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.DeleteContactRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.EssentialContacts.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1)

## Assembly

Google.Cloud.EssentialContacts.V1.dll

## Constructors 

### DeleteContactRequest()
    
    
    public DeleteContactRequest()

### DeleteContactRequest(DeleteContactRequest)
    
    
    public DeleteContactRequest(DeleteContactRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteContactRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.DeleteContactRequest)`  
  
  
## Properties 

### ContactName
    
    
    public ContactName ContactName { get; set; }

[ContactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.ContactName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.DeleteContactRequest#Google_Cloud_EssentialContacts_V1_DeleteContactRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ContactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EssentialContacts.V1/latest/Google.Cloud.EssentialContacts.V1.ContactName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the contact to delete. Format: organizations/{organization_id}/contacts/{contact_id}, folders/{folder_id}/contacts/{contact_id} or projects/{project_id}/contacts/{contact_id}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
