---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest
title: Cloud Domains v1beta1 API - Class ConfigureContactSettingsRequest (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:52.013448+00:00
---

# Cloud Domains v1beta1 API - Class ConfigureContactSettingsRequest (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Domains v1beta1 API - Class ConfigureContactSettingsRequest (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/2.0.0-beta05/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/1.0.0-beta04/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest)


    
    
    public sealed class ConfigureContactSettingsRequest : IMessage<ConfigureContactSettingsRequest>, IEquatable<ConfigureContactSettingsRequest>, IDeepCloneable<ConfigureContactSettingsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Domains v1beta1 API class ConfigureContactSettingsRequest.

Request for the `ConfigureContactSettings` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConfigureContactSettingsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ConfigureContactSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ConfigureContactSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ConfigureContactSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Domains.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1)

## Assembly

Google.Cloud.Domains.V1Beta1.dll

## Constructors 

### ConfigureContactSettingsRequest()
    
    
    public ConfigureContactSettingsRequest()

### ConfigureContactSettingsRequest(ConfigureContactSettingsRequest)
    
    
    public ConfigureContactSettingsRequest(ConfigureContactSettingsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ConfigureContactSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest)`  
  
  
## Properties 

### ContactNotices
    
    
    public RepeatedField<ContactNotice> ContactNotices { get; }

The list of contact notices that the caller acknowledges. The notices needed here depend on the values specified in `contact_settings`.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ContactNotice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ContactNotice)` |   
  
### ContactSettings
    
    
    public ContactSettings ContactSettings { get; set; }

Fields of the `ContactSettings` to update.

**Property Value**  
---  
**Type** | **Description**  
`[ContactSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ContactSettings)` |   
  
### Registration
    
    
    public string Registration { get; set; }

Required. The name of the `Registration` whose contact settings are being updated, in the format `projects/*/locations/*/registrations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RegistrationAsRegistrationName
    
    
    public RegistrationName RegistrationAsRegistrationName { get; set; }

[RegistrationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.RegistrationName)-typed view over the [Registration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.ConfigureContactSettingsRequest#Google_Cloud_Domains_V1Beta1_ConfigureContactSettingsRequest_Registration) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RegistrationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.RegistrationName)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. The field mask describing which fields to update as a comma-separated list. For example, if only the registrant contact is being updated, the `update_mask` is `"registrant_contact"`.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Validate the request without actually updating the contact settings.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
