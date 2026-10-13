---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest
title: Cloud Domains v1 API - Class ConfigureDnsSettingsRequest (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:31.405486+00:00
---

# Cloud Domains v1 API - Class ConfigureDnsSettingsRequest (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Domains v1 API - Class ConfigureDnsSettingsRequest (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.4.0/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.3.0/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.2.0/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.1.0/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.0.0/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/1.0.0/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest)


    
    
    public sealed class ConfigureDnsSettingsRequest : IMessage<ConfigureDnsSettingsRequest>, IEquatable<ConfigureDnsSettingsRequest>, IDeepCloneable<ConfigureDnsSettingsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Domains v1 API class ConfigureDnsSettingsRequest.

Request for the `ConfigureDnsSettings` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConfigureDnsSettingsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Domains.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1)

## Assembly

Google.Cloud.Domains.V1.dll

## Constructors 

### ConfigureDnsSettingsRequest()
    
    
    public ConfigureDnsSettingsRequest()

### ConfigureDnsSettingsRequest(ConfigureDnsSettingsRequest)
    
    
    public ConfigureDnsSettingsRequest(ConfigureDnsSettingsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ConfigureDnsSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest)`  
  
  
## Properties 

### DnsSettings
    
    
    public DnsSettings DnsSettings { get; set; }

Fields of the `DnsSettings` to update.

**Property Value**  
---  
**Type** | **Description**  
`[DnsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.DnsSettings)` |   
  
### Registration
    
    
    public string Registration { get; set; }

Required. The name of the `Registration` whose DNS settings are being updated, in the format `projects/*/locations/*/registrations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RegistrationAsRegistrationName
    
    
    public RegistrationName RegistrationAsRegistrationName { get; set; }

[RegistrationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RegistrationName)-typed view over the [Registration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ConfigureDnsSettingsRequest#Google_Cloud_Domains_V1_ConfigureDnsSettingsRequest_Registration) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RegistrationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.RegistrationName)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. The field mask describing which fields to update as a comma-separated list. For example, if only the name servers are being updated for an existing Custom DNS configuration, the `update_mask` is `"custom_dns.name_servers"`.

When changing the DNS provider from one type to another, pass the new provider's field name as part of the field mask. For example, when changing from a Google Domains DNS configuration to a Custom DNS configuration, the `update_mask` is `"custom_dns"`. //

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Validate the request without actually updating the DNS settings.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
