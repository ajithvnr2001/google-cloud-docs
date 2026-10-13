---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.Product
title: Service Health v1 API - Class Product (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:33.486647+00:00
---

# Service Health v1 API - Class Product (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.Product

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Health v1 API - Class Product (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.Product)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/1.3.0/Google.Cloud.ServiceHealth.V1.Product)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/1.2.0/Google.Cloud.ServiceHealth.V1.Product)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/1.1.0/Google.Cloud.ServiceHealth.V1.Product)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/1.0.0/Google.Cloud.ServiceHealth.V1.Product)


    
    
    public sealed class Product : IMessage<Product>, IEquatable<Product>, IDeepCloneable<Product>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Health v1 API class Product.

Represents the Google Cloud product impacted by the event.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Product

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.Product), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.Product), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.Product), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceHealth.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1)

## Assembly

Google.Cloud.ServiceHealth.V1.dll

## Constructors 

### Product()
    
    
    public Product()

### Product(Product)
    
    
    public Product(Product other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceHealth.V1/latest/Google.Cloud.ServiceHealth.V1.Product)`  
  
  
## Properties 

### Id
    
    
    public string Id { get; set; }

Unique identifier for the product.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProductName
    
    
    public string ProductName { get; set; }

Google Cloud product impacted by the event. Example: `"Google Cloud SQL"`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
