---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings
title: Cloud Domains v1 API - Class ContactSettings (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:17.912496+00:00
---

# Cloud Domains v1 API - Class ContactSettings (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Domains v1 API - Class ContactSettings (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.4.0/Google.Cloud.Domains.V1.ContactSettings)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.3.0/Google.Cloud.Domains.V1.ContactSettings)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.2.0/Google.Cloud.Domains.V1.ContactSettings)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.1.0/Google.Cloud.Domains.V1.ContactSettings)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.0.0/Google.Cloud.Domains.V1.ContactSettings)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/1.0.0/Google.Cloud.Domains.V1.ContactSettings)


    
    
    public sealed class ContactSettings : IMessage<ContactSettings>, IEquatable<ContactSettings>, IDeepCloneable<ContactSettings>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Domains v1 API class ContactSettings.

Defines the contact information associated with a `Registration`.

[ICANN](https://icann.org/) requires all domain names to have associated contact information. The `registrant_contact` is considered the domain's legal owner, and often the other contacts are identical.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ContactSettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ContactSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ContactSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ContactSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Domains.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1)

## Assembly

Google.Cloud.Domains.V1.dll

## Constructors 

### ContactSettings()
    
    
    public ContactSettings()

### ContactSettings(ContactSettings)
    
    
    public ContactSettings(ContactSettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ContactSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings)`  
  
  
## Properties 

### AdminContact
    
    
    public ContactSettings.Types.Contact AdminContact { get; set; }

Required. The administrative contact for the `Registration`.

**Property Value**  
---  
**Type** | **Description**  
`[ContactSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings.Types)[Contact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings.Types.Contact)` |   
  
### Privacy
    
    
    public ContactPrivacy Privacy { get; set; }

Required. Privacy setting for the contacts associated with the `Registration`.

**Property Value**  
---  
**Type** | **Description**  
`[ContactPrivacy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactPrivacy)` |   
  
### RegistrantContact
    
    
    public ContactSettings.Types.Contact RegistrantContact { get; set; }

Required. The registrant contact for the `Registration`.

_Caution: Anyone with access to this email address, phone number, and/or postal address can take control of the domain._

_Warning: For new`Registration`s, the registrant receives an email confirmation that they must complete within 15 days to avoid domain suspension._

**Property Value**  
---  
**Type** | **Description**  
`[ContactSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings.Types)[Contact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings.Types.Contact)` |   
  
### TechnicalContact
    
    
    public ContactSettings.Types.Contact TechnicalContact { get; set; }

Required. The technical contact for the `Registration`.

**Property Value**  
---  
**Type** | **Description**  
`[ContactSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings.Types)[Contact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactSettings.Types.Contact)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
