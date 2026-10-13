---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddCatalogAttributeRequest
title: Retail v2 API - Class AddCatalogAttributeRequest (2.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:50.210861+00:00
---

# Retail v2 API - Class AddCatalogAttributeRequest (2.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddCatalogAttributeRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Retail v2 API - Class AddCatalogAttributeRequest (2.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.16.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.15.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.14.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.13.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.12.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.11.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.10.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.9.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.8.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.7.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.6.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.5.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.4.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.3.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.2.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.1.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/2.0.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.6.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.5.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.4.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.3.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.2.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.1.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/1.0.0/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)


    
    
    public sealed class AddCatalogAttributeRequest : IMessage<AddCatalogAttributeRequest>, IEquatable<AddCatalogAttributeRequest>, IDeepCloneable<AddCatalogAttributeRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Retail v2 API class AddCatalogAttributeRequest.

Request for [CatalogService.AddCatalogAttribute][google.cloud.retail.v2.CatalogService.AddCatalogAttribute] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AddCatalogAttributeRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AddCatalogAttributeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddCatalogAttributeRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AddCatalogAttributeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddCatalogAttributeRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AddCatalogAttributeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddCatalogAttributeRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Retail.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2)

## Assembly

Google.Cloud.Retail.V2.dll

## Constructors 

### AddCatalogAttributeRequest()
    
    
    public AddCatalogAttributeRequest()

### AddCatalogAttributeRequest(AddCatalogAttributeRequest)
    
    
    public AddCatalogAttributeRequest(AddCatalogAttributeRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AddCatalogAttributeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddCatalogAttributeRequest)`  
  
  
## Properties 

### AttributesConfig
    
    
    public string AttributesConfig { get; set; }

Required. Full AttributesConfig resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/attributesConfig`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AttributesConfigAsAttributesConfigName
    
    
    public AttributesConfigName AttributesConfigAsAttributesConfigName { get; set; }

[AttributesConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AttributesConfigName)-typed view over the [AttributesConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AddCatalogAttributeRequest#Google_Cloud_Retail_V2_AddCatalogAttributeRequest_AttributesConfig) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AttributesConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.AttributesConfigName)` |   
  
### CatalogAttribute
    
    
    public CatalogAttribute CatalogAttribute { get; set; }

Required. The [CatalogAttribute][google.cloud.retail.v2.CatalogAttribute] to add.

**Property Value**  
---  
**Type** | **Description**  
`[CatalogAttribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Retail.V2/latest/Google.Cloud.Retail.V2.CatalogAttribute)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
