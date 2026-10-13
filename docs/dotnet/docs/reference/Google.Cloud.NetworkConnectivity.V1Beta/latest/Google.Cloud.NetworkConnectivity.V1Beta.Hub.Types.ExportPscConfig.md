---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types.ExportPscConfig
title: Network Connectivity v1beta API - Class Hub.Types.ExportPscConfig (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:43.392521+00:00
---

# Network Connectivity v1beta API - Class Hub.Types.ExportPscConfig (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types.ExportPscConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1beta API - Class Hub.Types.ExportPscConfig (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta02 (latest)  1.0.0-beta01 
    
    
    public sealed class Hub.Types.ExportPscConfig : IMessage<Hub.Types.ExportPscConfig>, IEquatable<Hub.Types.ExportPscConfig>, IDeepCloneable<Hub.Types.ExportPscConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Connectivity v1beta API class Hub.Types.ExportPscConfig.

Configuration for more granular control of Private Service Connect connection propagation. This allows enabling or disabling connection propagation for specific types of Private Service Connect endpoints.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Hub.Types.ExportPscConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types)[ExportPscConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types.ExportPscConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types)[ExportPscConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types.ExportPscConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types)[ExportPscConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types.ExportPscConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkConnectivity.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta)

## Assembly

Google.Cloud.NetworkConnectivity.V1Beta.dll

## Constructors 

### ExportPscConfig()
    
    
    public ExportPscConfig()

### ExportPscConfig(ExportPscConfig)
    
    
    public ExportPscConfig(Hub.Types.ExportPscConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Hub](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types)[ExportPscConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Hub.Types.ExportPscConfig)`  
  
  
## Properties 

### GlobalGoogleApis
    
    
    public bool GlobalGoogleApis { get; set; }

Optional. Controls whether Private Service Connect endpoints for global Google APIs should be propagated. The default value is false.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasGlobalGoogleApis
    
    
    public bool HasGlobalGoogleApis { get; }

Gets whether the "global_google_apis" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPublishedServicesAndRegionalGoogleApis
    
    
    public bool HasPublishedServicesAndRegionalGoogleApis { get; }

Gets whether the "published_services_and_regional_google_apis" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### PublishedServicesAndRegionalGoogleApis
    
    
    public bool PublishedServicesAndRegionalGoogleApis { get; set; }

Optional. Controls whether Private Service Connect endpoints for regional ILBs and regional Google APIs should be propagated. Default value is true if export_psc is true. Otherwise, the default value is false.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
