---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.GoogleDomainsDns
title: Cloud Domains v1beta1 API - Class DnsSettings.Types.GoogleDomainsDns (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:41.136616+00:00
---

# Cloud Domains v1beta1 API - Class DnsSettings.Types.GoogleDomainsDns (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.GoogleDomainsDns

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Domains v1beta1 API - Class DnsSettings.Types.GoogleDomainsDns (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.GoogleDomainsDns)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/2.0.0-beta05/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.GoogleDomainsDns)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/1.0.0-beta04/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.GoogleDomainsDns)


    
    
    public sealed class DnsSettings.Types.GoogleDomainsDns : IMessage<DnsSettings.Types.GoogleDomainsDns>, IEquatable<DnsSettings.Types.GoogleDomainsDns>, IDeepCloneable<DnsSettings.Types.GoogleDomainsDns>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Domains v1beta1 API class DnsSettings.Types.GoogleDomainsDns.

Configuration for using the free DNS zone provided by Google Domains as a `Registration`'s `dns_provider`. You cannot configure the DNS zone itself using the API. To configure the DNS zone, go to [Google Domains](https://domains.google/).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DnsSettings.Types.GoogleDomainsDns

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DnsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types)[GoogleDomainsDns](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.GoogleDomainsDns), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DnsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types)[GoogleDomainsDns](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.GoogleDomainsDns), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DnsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types)[GoogleDomainsDns](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.GoogleDomainsDns), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Domains.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1)

## Assembly

Google.Cloud.Domains.V1Beta1.dll

## Constructors 

### GoogleDomainsDns()
    
    
    public GoogleDomainsDns()

### GoogleDomainsDns(GoogleDomainsDns)
    
    
    public GoogleDomainsDns(DnsSettings.Types.GoogleDomainsDns other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DnsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types)[GoogleDomainsDns](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.GoogleDomainsDns)`  
  
  
## Properties 

### DsRecords
    
    
    public RepeatedField<DnsSettings.Types.DsRecord> DsRecords { get; }

Output only. The list of DS records published for this domain. The list is automatically populated when `ds_state` is `DS_RECORDS_PUBLISHED`, otherwise it remains empty.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DnsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types)[DsRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.DsRecord)` |   
  
### DsState
    
    
    public DnsSettings.Types.DsState DsState { get; set; }

Required. The state of DS records for this domain. Used to enable or disable automatic DNSSEC.

**Property Value**  
---  
**Type** | **Description**  
`[DnsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types)[DsState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1Beta1/latest/Google.Cloud.Domains.V1Beta1.DnsSettings.Types.DsState)` |   
  
### NameServers
    
    
    public RepeatedField<string> NameServers { get; }

Output only. A list of name servers that store the DNS zone for this domain. Each name server is a domain name, with Unicode domain names expressed in Punycode format. This field is automatically populated with the name servers assigned to the Google Domains DNS zone.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
