---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.OrganizationContact
title: GDC Hardware Management v1alpha API - Class OrganizationContact (1.0.0-alpha08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:42.009649+00:00
---

# GDC Hardware Management v1alpha API - Class OrganizationContact (1.0.0-alpha08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.OrganizationContact

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GDC Hardware Management v1alpha API - Class OrganizationContact (1.0.0-alpha08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-alpha08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.OrganizationContact)
  * [ 1.0.0-alpha07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/1.0.0-alpha07/Google.Cloud.GdcHardwareManagement.V1Alpha.OrganizationContact)


    
    
    public sealed class OrganizationContact : IMessage<OrganizationContact>, IEquatable<OrganizationContact>, IDeepCloneable<OrganizationContact>, IBufferMessage, IMessage

Reference documentation and code samples for the GDC Hardware Management v1alpha API class OrganizationContact.

Contact information of the customer organization.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OrganizationContact

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OrganizationContact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.OrganizationContact), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OrganizationContact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.OrganizationContact), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OrganizationContact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.OrganizationContact), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GdcHardwareManagement.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha)

## Assembly

Google.Cloud.GdcHardwareManagement.V1Alpha.dll

## Constructors 

### OrganizationContact()
    
    
    public OrganizationContact()

### OrganizationContact(OrganizationContact)
    
    
    public OrganizationContact(OrganizationContact other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OrganizationContact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.OrganizationContact)`  
  
  
## Properties 

### Address
    
    
    public PostalAddress Address { get; set; }

Required. The organization's address.

**Property Value**  
---  
**Type** | **Description**  
`[PostalAddress](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PostalAddress.html)` |   
  
### Contacts
    
    
    public RepeatedField<Contact> Contacts { get; }

Required. The individual points of contact in the organization at this location.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Contact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.Contact)` |   
  
### Email
    
    
    public string Email { get; set; }

Optional. The organization's email.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Phone
    
    
    public string Phone { get; set; }

Optional. The organization's phone number.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
